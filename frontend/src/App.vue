<template>
  <div>
    <NavBar/>
    <router-view class="w-75 mx-auto"/>
  </div>
</template>

<script>
  import NavBar from './components/NavBar.vue'

  export default {
    name: 'App',
    components: {
      NavBar
    }
  }
</script>
