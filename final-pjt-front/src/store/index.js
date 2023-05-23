import Vue from 'vue'
import Vuex from 'vuex'
import movie from '@/store/movie/movie'
import community from '@/store/community/community.js'
import comment from '@/store/community/comment.js'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [
    ],
    token: null,
    username:null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log(token)
      router.push({name : 'MovieView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    SAVE_USERNAME(state, username) {
      state.username = username;
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      console.log(payload)
      axios({
        
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
          context.dispatch('loadUserData', res.data.key)

        })
      .catch((err) => console.log(err))
    },
  },
  modules: {
    movie,
    community,
    comment,
  },
})
