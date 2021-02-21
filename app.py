from flask import Flask, request
from flask_cors import CORS
import numpy as np
from flask_restx import Resource, Api
from transformers import pipeline, Conversation
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

texts = []

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)
app.secret_key = "markus"
CORS(app)
api = Api(app, version="1.0", title="TodoMVC API", description="A simple TodoMVC API")


@api.route("/chat")
class Predict(Resource):
    def post(self):
        text = request.get_json()["text"]
        texts.append(text)

        print(texts)

        for idx, text in enumerate(texts):
            # encodethe new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = tokenizer.encode(
                text + tokenizer.eos_token, return_tensors="pt"
            )

            # append the new user input tokens to the chat history
            bot_input_ids = (
                torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
                if idx > 0
                else new_user_input_ids
            )

            # generated a response while limiting the total chat history to 1000 tokens,
            chat_history_ids = model.generate(
                bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
            )

            # pretty print last ouput tokens from bot
            new_output = tokenizer.decode(
                chat_history_ids[:, bot_input_ids.shape[-1] :][0],
                skip_special_tokens=True,
            )
        return {"message": new_output}


if __name__ == "__main__":
    app.run(debug=True)
