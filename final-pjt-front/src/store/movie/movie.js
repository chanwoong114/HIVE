import axios from "axios"
import index from "../index.js"

const movie = {
  state: {
    liked: {}
  },
  getters: {
    checklike(state, movieId) {
      return state.liked[movieId]
    }
  },
  mutations: {
    IS_LIKE(state, data) {
      state.liked[data[0]] = data[1]
    }
  },
  actions: {
    movieLike(context, movieId) {
      console.log(context)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movieId}/like/`,
        headers: {
          Authorization: `Token ${index.state.token}`
        }
      })
      .then(res => {
        console.log(res)
      })
      .catch(error => {
        error
      })
    },
    isLike(context, movieId) {
      console.log(index.state.token)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movieId}/like/`,
        headers: {
          Authorization: `Token ${index.state.token}`
        }
      })
      .then(res => {
        context.commit('IS_LIKE', [movieId, res.data.state])
      })
      .catch(error => {
        error
      })
    }
  },
}

export default movie
