<template>
  <div id="app" :style="{ backgroundImage: 'url(' + require('@/assets/background.jpg') + ')' }">
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  height: 100%;
}

</style>
