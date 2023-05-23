<template>
  <div>
    <h1>{{ user.username }}</h1>
    <p>팔로잉 : {{ user.followings_count }}</p>
    <p>팔로워 : {{ user.follower_count }}</p>

    <div class="container">
      <div class="row row-cols-3 row-cols-md-6 g-2">
        <div class="col" v-for="movie in user.rated_movies" :key="movie.id">
          <div class="card mb-4" @click="gotoDetail(movie.id)">
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title"   
            class="card-img-top">
            <div class="card-body">
              <h5 class="card-title" style="color: black">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      user: null,
    }
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/mypage/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.user = res.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    },
  },
  created() {
    this.getUserInfo()
  }
}
</script>

<style>

</style>