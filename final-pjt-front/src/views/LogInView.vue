<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username"></label><br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> </label><br>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
    <button @click="gotoSignup()">Sign Up</button>
    
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
      .then((res) => {
          console.log(1)
          // 로그인 성공 시 사용자 이름을 스토어에 저장
          this.$store.commit('SAVE_TOKEN', res.data.key)
          this.$store.commit('SET_USERNAME', username);
          // this.$router.push({ name: 'MovieView' });
        })
        .catch((error) => {
          // 로그인 실패 처리
          console.error(error);
        });
    },
    gotoSignup() {
      this.$router.push({name: 'SignUpView'})
    }
  },
  
}
</script>
