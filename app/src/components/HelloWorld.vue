<template>
<div class="wrapper">
  <h1 id="header">Hey, I am Pepper, want to chat with me?</h1>
  <div class="content">
  <div v-if="this.textinputs.length === 0">
    <h3>Please start a chat with me :-)</h3>
  </div>
  <div v-else>
  <div v-for="(value, index) in myresult" v-bind:key="index">
    <div v-if="index % 2 == 0" class="left">
      <p class="left_message"><strong>You:</strong> {{value}}</p>
      </div>
    <div v-else class="right">
      <p class="right_message">{{value}}</p>
      <img height="35px" :src="require(`@/assets/robot.jpeg`)">
    </div>
  </div>
  </div>

    <div class="right" id="writing" v-if="visible">
      <div class="loading">
        <span></span>
        <span></span>
        <span></span>
    </div>
    <img height="35px" :src="require(`@/assets/robot.jpeg`)">
  </div>

  <div class="left totop">
    <input id="new_message" type="text" v-model="message" placeholder="Message..." v-on:keyup.enter="onEnter">
    <div id="sendmessage" @click="onSubmit">Send!</div>
  </div>


  </div>
</div>
</template>

<script>

import axios from "axios";

export default {
  name: 'HelloWorld',
  data() {
    return {
      visible: false,
      message: "",  
      textinputs: [],
      textoutputs: []
    }
  },
  methods: {
    onEnter: function(e) {
      if (e.keyCode === 13) {
        this.textinputs.push(this.message)  
        this.visible = true
        
        axios
        .post("http://127.0.0.1:5000/chat", {
          text: this.message,
        })
        .then(res => {
          this.visible = false
          this.textoutputs.push(res.data.message)

        })
        .catch(err => {
          console.log(err);
        });
      }
      this.message = ""
    },
    onSubmit: function() {
        this.textinputs.push(this.message)  
        
        axios
        .post("http://127.0.0.1:5000/chat", {
          text: this.message,
        })
        .then(res => {
          this.visible = false
          this.textoutputs.push(res.data.message)

        })
        .catch(err => {
          console.log(err);
        });
      this.message = ""
    }
  },
  computed: {
    myresult: function() {
      const result = new Array;
          for(var i = 0; i < this.textinputs.length; i++){
          if (i < this.textinputs.length) {
            result.push(this.textinputs[i]);  
          }
          if (i < this.textoutputs.length) {
            result.push(this.textoutputs[i]);  
          }
      }
      return result
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#header {
  color: white;
}

.left_message {
  background: lightgray;
  display: inline;
  padding: 5px 4px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

.right_message {
  background: #25D366;
  display: inline;
  padding: 5px 4px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}

#new_message {
  width: 300px;
  display: inline-block;
  padding: 10px 5px;
  border: none;
  margin-top: 15px;
  border: 3px solid black;
  border-radius: 5px;
}

.totop {
  margin-top: 20px;
}

#sendmessage {
  display: inline;
  border: 1px solid black;
  cursor: pointer;
  padding: 10px 25px;
  background: #25D366;
  color: white;
  font-weight: bold;
}


.wrapper {
  text-align: center;
  padding-top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
    width: 800px;
    border: 1px solid gray;
    background: white;
    padding: 10px 10px;
    border-radius: 10px;
}

.left {
  text-align: left;
  padding: 8px 2px;
}

.right {
  text-align: right;
  padding: 8px 2px;
}

.loading {
  display: inline;
}

.loading span {
  width: 15px;
  height: 15px;
  margin: 0 2px;
  background-color: #25D366;
  border-radius: 50%;
  display: inline-block;
  animation-name: dots;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: ease-in-out;
}

.loading span:nth-child(2) {
  animation-delay: 0.4s
}

.loading span:nth-child(3) {
  animation-delay: 0.8s;
}

@keyframes dots {
  50% {
    opacity: 0;
    transform: scale(0.7) translateY(10px);
  }
}

@media (max-width: 600px) {

  .content {
      width: 90%;
      border: 1px solid gray;
      background: white;
      padding: 10px 10px;
      border-radius: 10px;
  }

  #new_message {
    width: 96%;
    display: block;
    margin-bottom: 20px;
  }
  
  #sendmessage  {
    display: block;
  }
}

</style>

