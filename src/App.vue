<template>
  <div>
    <h3 class="p-3 text-center">Api Tester</h3>
    <http-request/>
  </div>
</template>

<script>
import HttpRequest from './components/HttpRequest.vue'

export default {
  name: "app",
  components: {
    HttpRequest,
  }
};
</script>
