import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import { Carousel } from "@fancyapps/ui/dist/carousel/carousel.esm.js";
import "@fancyapps/ui/dist/carousel/carousel.css";

// Main carousel
const mainContainer = document.getElementById("myCarousel");
const mainOptions = {};

const mainCarousel = new Carousel(mainContainer, mainOptions);

// Carousel for navigation
const navContainer = document.getElementById("myNavigation");
const navOptions = {
  Sync: {
    target: mainCarousel,
  },
};

new Carousel(navContainer, navOptions)