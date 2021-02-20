<template>
<div class="wrapper">
  <h1 id="header">Hey, I am Pepper, want to hang out me with?</h1>
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

  <div class="left totop">
    <input id="new_message" type="text" v-model="message" placeholder="Message..." v-on:keyup.enter="onEnter">
    <div id="sendmessage" @click="onSubmit">Senden!</div>
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
      message: "",  
      textinputs: [],
      textoutputs: []
    }
  },
  methods: {
    onEnter: function(e) {
      if (e.keyCode === 13) {
        this.textinputs.push(this.message)  
        this.textoutputs.push("heyhey")
        this.message = ""

        axios
        .post("http://127.0.0.1:5000/chat", {
          text: this.textinputs,
        })
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
      }
    },
    onSubmit: function() {
        this.textinputs.push(this.message)
        this.textoutputs.push("heyhey")
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
  padding: 10px 5px;
  background: red;
  color: white;
  font-weight: bold;
}

#new_message:active {
  border: none;
}

.wrapper {
  padding-top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
    width: 500px;
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
</style>
