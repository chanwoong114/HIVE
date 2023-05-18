import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import HomeView from '../views/HomeView.vue'
import GenreView from '../views/GenreView.vue'
import FavoritesView from '../views/FavoritesView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import PersonView from '@/views/PersonView'
import NotFound from '@/views/404NotFound'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/',
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
    name: 'FavoritesView',
    component: FavoritesView
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetailView',
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
    path: '/:job/:personId',
    name: 'PersonView',
    component: PersonView
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

router.beforeEach((to, from, next) => {
  const isLoggedIn =  store.getters.isLogin
  const authPage = ['HomeView', 'SignUpView']
  const isAuth = !authPage.includes(to.name)
  // 로그인이 필요한 페이지에 접근하려고 할 때
  if (isAuth && !isLoggedIn) {
    alert('로그인하세요')
    next({ name: 'HomeView' }); // HomeView로 리디렉션합니다.
    
  } else {
    next(); // 정상적으로 다음 단계로 진행합니다.
  }
});

