# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:11:39 2021

@author: User
"""

from transformers import pipeline, Conversation
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

texts = ["Hi how are you?", "Want to go to Dinner with me?"]

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
    print(
        "DialoGPT: {}".format(
            tokenizer.decode(
                chat_history_ids[:, bot_input_ids.shape[-1] :][0],
                skip_special_tokens=True,
            )
        )
    )


import numpy as np

tensor1 = torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))
tensor2 = torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))

torch.cat([tensor1, tensor2])
