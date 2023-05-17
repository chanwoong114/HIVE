<template>
  <div>
    <div class="box">
    <h1>회원 가입</h1>
    <form @submit.prevent="signUp">
      <label for="username" style="text-align: left;">아이디</label>
      <br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> 비밀번호</label>
      <br>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> 비밀번호 확인 </label>
      <br>
      <input type="password" id="password2" v-model="password2">
      <br>
      <input type="submit" value="SignUp">
      
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
<style>

.box {
  border: solid 0px;
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.5);
  padding-bottom:50px
  /* pddding-top:50px */
}


</style>