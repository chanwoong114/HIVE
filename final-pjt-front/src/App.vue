<template>
  <div id="app" class="bg-dark">
    <nav id="navbar-example2" class="navbar bg-secondary px-3 mb-3 d-flex justify-content-between align-items-center">
      <a class="navbar-brand" href=""><img class="hive" src="./assets/hive.png" alt="nike"></a>
      <ul class="nav nav-pills">
        <li class="nav-item">
          <a class="nav-link"><router-link to="/home">home</router-link></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" ><router-link to="/movies">movies</router-link></a>
        </li>
        <li class="nav-item">
          <a class="nav-link"><router-link to="/genre">genre</router-link></a>
        </li>
        <li class="nav-item">
          <a class="nav-link"><router-link to="/favorites">favorites</router-link></a>
        </li>
        <li class="nav-item ml-auto">
          <input type="text" placeholder="Search" class="form-control">
        </li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

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
</style>
