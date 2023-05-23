<template>
  <div>

    <!-- <form @submit.prevent="login">
      <label for="username"></label><br>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> </label><br>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
    <button @click="gotoSignup()">Sign Up</button> -->
    <main class="page-wrapper">
      <!-- Page content-->
      <div class="d-lg-flex position-relative">
        <!-- Sign in form-->
        
        <div class="d-flex flex-column align-items-center mx-auto w-lg-50 h-100 px-3 px-lg-5 pt-5">
          <img src="../assets/bighive.png" alt="Logo" width="200" height="200">
          <div class="w-100 mt-auto" style="max-width: 526px;">
            <h1>HIVE</h1>
            <h1>로그인</h1>
            <form class="needs-validation" novalidate>
              <div class="pb-3 mb-3">
                <div class="position-relative"><i class="ai-mail fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <input class="form-control form-control-lg ps-5" type="email" placeholder="아이디" required>
                </div>
              </div>
              <div class="mb-4">
                <div class="position-relative"><i class="ai-lock-closed fs-lg position-absolute top-50 start-0 translate-middle-y ms-3"></i>
                  <div class="password-toggle">
                    <input class="form-control form-control-lg ps-5" type="password" placeholder="비밀번호" required>
                    <label class="password-toggle-btn" aria-label="Show/hide password">
                      <input class="password-toggle-check" type="checkbox"><span class="password-toggle-indicator"></span>
                    </label>
                  </div>
                </div>
              </div>
              <div class="d-flex flex-wrap align-items-center justify-content-between pb-4">
                <form-check class="my-1">
                  <input class="form-check-input" type="checkbox" id="keep-signedin">
                  <label class="form-check-label ms-1" for="keep-signedin">로그인 상태유지</label>
                </form-check><a class="fs-sm fw-semibold text-decoration-none my-1" href="#">비밀번호찾기</a>
              </div>
              <button class="btn btn-lg btn-success  w-100 mb-4" type="submit">로그인</button>
              <button class="btn btn-lg btn-success w-100 mb-4" type="submit" @click="gotoSignup()">회원가입</button>
              <h2 class="h6 text-center pt-3 pt-lg-4 mb-4">다른방법 로그인</h2>
              <div class="row row-cols-1 row-cols-sm-2 gy-3">
                <div class="col"><a class="btn btn-icon btn-outline-secondary btn-google btn-lg w-100" href="#"><i class="ai-google fs-xl me-2"></i>Google</a></div>
                <div class="col"><a class="btn btn-icon btn-outline-secondary btn-facebook btn-lg w-100" href="#"><i class="ai-facebook fs-xl me-2"></i>Facebook</a></div>
              </div>
            </form>
          </div>
          <!-- Copyright-->
          <p class="w-100 fs-sm pt-5 mt-auto mb-5" style="max-width: 526px;"><span class="text-muted">&copy; Made by</span><a class="nav-link d-inline-block p-0 ms-1" href="https://createx.studio/" target="_blank" rel="noopener">TEAM HIVE</a></p>
        </div>
        <!-- Cover image-->
        <!-- <div class="w-50 bg-size-cover bg-repeat-0 bg-position-center" style="background-image: url(assets/hive.png);"></div> -->
      </div>
    </main>
     
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
<style scoped>
img {
    position: relative;
    z-index: -1;
}
</style>