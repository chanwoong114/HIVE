<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
    <!-- <div class="ss-container">
    <img class="hive" src="../assets/bighive.png">
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    }
  }
}
</script>
<style scoped>
.ss-container {
  position: relative;
  height: 100px; 
  overflow: hidden;
}

.hive {
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  height: 80%;
  animation: moveUpDown 3s infinite alternate;
}

@keyframes moveUpDown {
  0% {
    transform: translateY(40px);
  }
  50% {
    transform: translateY(-40px); /* 이미지가 위로 이동하는 양 조정 */
  }
  100% {
    transform: translateY(0);
  }
}
</style>