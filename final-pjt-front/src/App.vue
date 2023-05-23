<template>
  
  <div id="app" class="">
    <div v-if="isLogin">
      <nav id="navbar-example2" class="navbar bg-dark px-3 mb-3 d-flex justify-content-between align-items-center">
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
          <!-- <li class="nav-item">
            <a class="nav-link"><router-link to="/home">home</router-link></a>
          </li> -->
          
          <li class="nav-item">
            <a class="nav-link"><router-link to="/favorites">mypage</router-link></a>
          </li>
          
          <li class="nav-item ml-auto">
            <input type="text" placeholder="Search" class="form-control">
          </li>
        
        </ul>
      </nav>
    </div>
  
    <router-view/>
  </div>
</template>
<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  watch: {
    $route() {
      window.scrollTo(0, 0);
    },
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

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
.page-loading {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        -webkit-transition: all .4s .2s ease-in-out;
        transition: all .4s .2s ease-in-out;
        background-color: #fff;
        opacity: 0;
        visibility: hidden;
        z-index: 9999;
      }
      .dark-mode .page-loading {
        background-color: #121519;
      }
      .page-loading.active {
        opacity: 1;
        visibility: visible;
      }
      .page-loading-inner {
        position: absolute;
        top: 50%;
        left: 0;
        width: 100%;
        text-align: center;
        -webkit-transform: translateY(-50%);
        transform: translateY(-50%);
        -webkit-transition: opacity .2s ease-in-out;
        transition: opacity .2s ease-in-out;
        opacity: 0;
      }
      .page-loading.active > .page-loading-inner {
        opacity: 1;
      }
      .page-loading-inner > span {
        display: block;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: normal;
        color: #6f788b;
      }
      .dark-mode .page-loading-inner > span {
        color: #fff;
        opacity: .6;
      }
      .page-spinner {
        display: inline-block;
        width: 2.75rem;
        height: 2.75rem;
        margin-bottom: .75rem;
        vertical-align: text-bottom;
        background-color: #d7dde2; 
        border-radius: 50%;
        opacity: 0;
        -webkit-animation: spinner .75s linear infinite;
        animation: spinner .75s linear infinite;
      }
      .dark-mode .page-spinner {
        background-color: rgba(255,255,255,.25);
      }
      @-webkit-keyframes spinner {
        0% {
          -webkit-transform: scale(0);
          transform: scale(0);
        }
        50% {
          opacity: 1;
          -webkit-transform: none;
          transform: none;
        }
      }
      @keyframes spinner {
        0% {
          -webkit-transform: scale(0);
          transform: scale(0);
        }
        50% {
          opacity: 1;
          -webkit-transform: none;
          transform: none;
        }
      }
      #zoom {
    position: relative;
  }

  #zoom:hover {
    transform: scale(2);
    transition: 0.5s;
    z-index: 1;
  }

  #zoom:hover > .backgroundimg {
    opacity: 0.3;
  }

  .mainimg {
    position: absolute;
    opacity: 0;
  }

  #movieInfo {
    position: absolute;
    opacity: 0;
  }

  #title {
    position: absolute;
    opacity: 0;
  }

  #zoom:hover > .mainimg {
    opacity: 1;
    width: 40%;
    top: 15%;
    left: 10%
  }

  #zoom:hover > #movieInfo {
    opacity: 1;
    top: 15%;
    left: 60%;
    font-size: 4px;
  }

  #zoom:hover > #title {
    opacity: 1;
    top: 70%;
    text-align: center;
    width: 60%;
    font-size: 8px;
    left: 20%;
    color: #FFD963;
    font-weight: bold;
  }
</style>
