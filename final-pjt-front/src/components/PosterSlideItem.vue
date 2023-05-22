<template>
  <div id="buttons">
    <div>
      <p v-if="movie.comments_rating">평점 : {{ movie.comments_rating.toFixed(1) }}</p>
      <p v-if="!movie.comments_rating">아직 댓글이 없습니다...</p>
    </div>
    <button class="btn btn-success" v-if="liked" @click="movieLike">
      좋아요 취소
    </button>
    <button class="btn btn-primary" v-if="!liked" @click="movieLike">
      좋아요
    </button>
    <button class="btn btn-light border-light" @click="gotoDetail(movie.id)">상세 정보 보기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PosterSlideItem',
  props: {
    movie: Object
  },
  data() {
    return {
      liked: null
    }
  },
  methods: {
    movieLike() {
      this.$store.dispatch('movieLike', this.movie.id)
      this.liked = !this.liked
    },
    isLike() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        this.liked = res.data.state
      })
      .catch(error => {
        error
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    }
  },
  created() {
    this.isLike()
  }

}
</script>

<style>
</style>