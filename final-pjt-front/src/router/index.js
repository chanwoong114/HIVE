import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'
import FavoritesView from '../views/FavoritesView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import NotFound from '@/views/404NotFound'


Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Movie',
    component: MovieView
  },
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/genre',
    name: 'GenreView',
    component: GenreView
  },
  {
    path: '/favorites',
    component: FavoritesView
  },
  {
    path: '/detail',
    component: MovieDetailView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  
  {
    path: '/404',
    name: '404NotFound',
    component: NotFound
  },

  {
    path: '*',
    redirect: '/404'
  },
  
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

