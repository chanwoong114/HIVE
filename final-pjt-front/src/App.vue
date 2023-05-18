<template>
  <div id="app" class="bg-dark">
    
    <div v-if="isLogin">
      <nav id="navbar-example2" class="navbar bg-secondary px-3 mb-3 d-flex justify-content-between align-items-center">
        <a class="navbar-brand" href=""><img class="hive" src="./assets/hive.png" alt="nike"></a>
        <ul class="nav nav-pills">
          <!-- <li class="nav-item">
            <a class="nav-link"><router-link to="/home">home</router-link></a>
          </li> -->
          <li class="nav-item">
            <a class="nav-link" ><router-link to="/movies">movies</router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link"><router-link to="/genre">genre</router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link"><router-link to="/favorites">favorites</router-link></a>
          </li>
          <li class="nav-item">
            <span class="nav-link">{{ $store.state.username }}</span>
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
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  min-height: 100vh;
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
#video-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1; /* Ensure the video is behind the content */
}
</style>
