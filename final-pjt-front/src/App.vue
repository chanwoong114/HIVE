<template>
  
  <div id="app" class="">
    <div>
    <!-- <div v-if="isLogin"> -->
      <!-- <nav id="navbar-example2" class="navbar bg-dark px-3 mb-3 d-flex justify-content-between align-items-center">
        <span class="d-flex align-items-center">
          <a class="navbar-brand" :href="`http://localhost:8080/movies`"><img class="hive" src="./assets/hive.png" alt="nike"></a>
  
          <ul class="nav nav-pills">
            <li class="nav-item">
              <a class="nav-link" ><router-link to="/movies">movies</router-link></a>
            </li>
            <li class="nav-item">
              <a class="nav-link"><router-link to="/genre">genre</router-link></a>
            </li>
            <li class="nav-item">
              <a class="nav-link"><router-link :to="{name: 'community'}">community</router-link></a>
            </li>
          </ul>
        </span>
        <ul class="nav nav-pills">
          <li class="nav-item">
            <a class="nav-link"><router-link to="/favorites">mypage</router-link></a>
          </li>
          
          <li class="nav-item ml-auto">
            <input type="text" placeholder="Search" class="form-control">
          </li>
        </ul>
      </nav> -->
      <div class="dark-mode">
        <!-- 네브바-->
        <header class="navbar bg-white navbar-expand-lg fixed-top" >
          
          <div class="container"><a class="navbar-brand pe-sm-3" :href="`http://localhost:8080/movies`">
            <img src="./assets/bighive.png"  alt="Logo" width="35" height="32">
            HIVE
            </a>
            
            <div class="form-check form-switch mode-switch order-lg-2 me-3 me-lg-4 ms-auto" data-bs-toggle="mode">
              <input class="form-check-input" type="checkbox" id="theme-mode" v-model="darkMode" @click="toggleDarkMode()">
              <label class="form-check-label" for="theme-mode"><i class="ai-sun fs-lg"></i></label>
              <label class="form-check-label" for="theme-mode"><i class="ai-moon fs-lg"></i></label>
            </div>
            <!-- 로그인버튼 -->
            <!-- 로그인이면 마이페이지 아니면 로그인 -->
            <div v-if="!isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex" target="_blank" rel="noopener" >
            <i class="ai-login fs-xl me-2 ms-n1"></i><router-link class="nav-link" to="/login">로그인</router-link>
            </div>
            <div v-if="isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex"  target="_blank" rel="noopener" >
            <i class="ai-login fs-xl me-2 ms-n1"></i><router-link class="nav-link" to="/favorites">마이페이지</router-link>
            </div>
            
         
            <!-- 영화추천 -->
            <nav class="collapse navbar-collapse" id="navbarNav" >
              <ul class="navbar-nav navbar-nav-scroll me-auto " style="--ar-scroll-height: 520px;">
                <li class="nav-item dropdown "><a class="nav-link dropdown-toggle active" href="#" data-bs-toggle="dropdown" aria-expanded="false">영화</a>
                  <div class="dropdown-menu overflow-hidden p-0 ">
                    <div class="d-lg-flex bg-white">
                      <div class="mega-dropdown-column pt-1 pt-lg-3 pb-lg-4">
                        <ul class="list-unstyled mb-0">
                          <li><router-link class="dropdown-item" to="/movies">영화추천</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h- bg-size-cover bg-repeat-0 rounded-3 rounded-start-0" style="background-image: url(assets/img/megamenu/bee.png)"></span></li>
                          <li><router-link class="dropdown-item" to="/genre">장르별 영화</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h-100 bg-size-cover bg-repeat-0 zindex-2 opacity-0" style="background-image: url(assets/img/megamenu/C.png)"></span></li>  
                        </ul>
                      </div>
                      <div class="mega-dropdown-column position-relative border-start zindex-3"></div>
                    </div>
                  </div>
                </li>
                <!-- 게시판,마이페이지 -->
                <li class="nav-item"><router-link class="nav-link" to="/community">게시판</router-link></li>
                <!-- <li class="nav-item"><a class="nav-link" href="docs/getting-started.html">마이페이지</a></li> -->
              </ul>
              <div class="d-sm-none p-3 mt-n3"><a class="btn btn-primary w-100  mb-1" href="https://themes.getbootstrap.com/product/around-multipurpose-template-ui-kit/" target="_blank" rel="noopener"><i class="ai-cart fs-xl me-2 ms-n1"></i>Buy now</a></div>
            </nav>
          </div>
        </header>
        <header class="position-relative navbar bg-white navbar-expand-lg" >
          
          <div class="container"><a class="navbar-brand pe-sm-3" :href="`http://localhost:8080/movies`">
            <img src="./assets/bighive.png"  alt="Logo" width="35" height="32">
            HIVE
            </a>
            <div class="form-check form-switch mode-switch order-lg-2 me-3 me-lg-4 ms-auto" data-bs-toggle="mode">
              <input class="form-check-input" type="checkbox" id="theme-mode" v-model="darkMode" @click="toggleDarkMode()">
              <label class="form-check-label" for="theme-mode"><i class="ai-sun fs-lg"></i></label>
              <label class="form-check-label" for="theme-mode"><i class="ai-moon fs-lg"></i></label>
            </div>
            <!-- 로그인버튼 -->
            <!-- 로그인이면 마이페이지 아니면 로그인 -->
            <div v-if="!isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex" target="_blank" rel="noopener" >
            <i class="ai-login fs-xl me-2 ms-n1"></i><router-link class="nav-link" to="/login">로그인</router-link>
            </div>
            <div v-if="isLogin" class="btn btn-success btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex"  target="_blank" rel="noopener" >
            <router-link class="nav-link" :to="{name: 'FavoritesView'}">
            <i class="ai-login fs-xl me-2 ms-n1"></i>마이페이지</router-link>
            </div>
         
         
            <!-- 영화추천 -->
            <nav class="collapse navbar-collapse" id="navbarNav" >
              <ul class="navbar-nav navbar-nav-scroll me-auto " style="--ar-scroll-height: 520px;">
                <li class="nav-item dropdown "><a class="nav-link dropdown-toggle active" href="#" data-bs-toggle="dropdown" aria-expanded="false">영화</a>
                  <div class="dropdown-menu overflow-hidden p-0 ">
                    <div class="d-lg-flex bg-white">
                      <div class="mega-dropdown-column pt-1 pt-lg-3 pb-lg-4">
                        <ul class="list-unstyled mb-0">
                          <li><router-link class="dropdown-item" to="/movies">영화추천</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h- bg-size-cover bg-repeat-0 rounded-3 rounded-start-0" style="background-image: url(assets/img/megamenu/bee.png)"></span></li>
                          <li><router-link class="dropdown-item" to="/genre">장르별 영화</router-link>
                            <span class="mega-dropdown-column position-absolute top-0 end-0 h-100 bg-size-cover bg-repeat-0 zindex-2 opacity-0" style="background-image: url(assets/img/megamenu/C.png)"></span></li>  
                        </ul>
                      </div>
                      <div class="mega-dropdown-column position-relative border-start zindex-3"></div>
                    </div>
                  </div>
                </li>
                <!-- 게시판,마이페이지 -->
                <li class="nav-item"><router-link class="nav-link" to="/community">게시판</router-link></li>
                <!-- <li class="nav-item"><a class="nav-link" href="docs/getting-started.html">마이페이지</a></li> -->
              </ul>
              <div class="d-sm-none p-3 mt-n3"><a class="btn btn-primary w-100  mb-1" href="https://themes.getbootstrap.com/product/around-multipurpose-template-ui-kit/" target="_blank" rel="noopener"><i class="ai-cart fs-xl me-2 ms-n1"></i>Buy now</a></div>
            </nav>
          </div>
        </header>
      </div>
    </div>
    
    <router-view class="pt-2"/>
    <footer class="footer py-4 bg-dark">
      <div class="container text-center py-3">
        <span class="text-muted">&copy; <span class='text-danger'></span></span>
        <a class="nav-link d-inline fw-normal p-0" href="https://www.instagram.com/non_inss/" target="_blank" rel="noopener">Team HIVE</a></div>
    </footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      darkMode: false
    };
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods:{
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      if (this.darkMode) {
        // 다크 모드 클래스를 추가
        document.body.classList.add('dark-mode');
      } else {
        // 다크 모드 클래스를 제거
        document.body.classList.remove('dark-mode');
      }
    },
   
    gotoLogin() {
      this.$router.push({name: 'LogInView'})
    }
  
  },
  // watch: {
  //   $route() {
  //     window.scrollTo(0, 0);
  //   },
  // },
}
</script>
<style>


nav {
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: black;
}

.hive {
  width: 130px;
  height: 90px;
}
h1 {
  color: #FFD963;
}

h3 {
  color: #FFD963;
}

#video-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1; /* Ensure the video is behind the content */
}
  #zoom {
    position: relative;
    border-radius: 5%;
  }

  #zoom:hover {
    transform: scale(2);
    transition: 0.5s;
    z-index: 1;
    border-radius: 5%;
  }

  #zoom:hover > .backgroundimg {
    opacity: 0.3;
  }

  .mainimg {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #movieInfo {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #title {
    position: absolute;
    opacity: 0;
    display: none;
  }

  #zoom:hover > .mainimg {
    display: inline;
    opacity: 1;
    width: 40%;
    top: 15%;
    left: 10%
  }

  #zoom:hover > #movieInfo {
    display: inline;
    opacity: 1;
    top: 15%;
    left: 60%;
    font-size: 4px;
    color: #fff;
  }

  #zoom:hover > #title {
    display: inline;
    opacity: 1;
    top: 90%;
    text-align: center;
    width: 60%;
    font-size: 8px;
    left: 20%;
    color: #FFD963;
    font-weight: bold;
  }

  #liked {
    display: none;
    position: absolute;
    opacity: 0;
  }

  #zoom:hover > #liked {
    display: inline;
    opacity: 1;
    top: 70%;
    text-align: center;
    width: 60%;
    font-size: 8px;
    left: 20%;
  }

  #zoom:hover > #liked:active {
    transform: scale(1.2);
    transition: 0.3s;
  }
</style>
