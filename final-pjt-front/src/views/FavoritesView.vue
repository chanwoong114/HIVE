<template>
  <div>
    <div class="container d-flex align-items-center ">
      <h1>{{ user.username }}</h1> &nbsp;
      <p>팔로잉 : {{ user.followings_count }} / </p> &nbsp;
      <p> 팔로워 : {{ user.follower_count }}</p>
    </div>

    <h2 class="container" style="text-align: left;">관심있는 영화</h2>
    <div class="container">
      <div class="row row-cols-3 row-cols-md-6 g-2">
        <div class="col" v-for="movie in user.rated_movies" :key="movie.id">
          <div id="zoom" class="bg-dark card mb-4 border-dark" @click="gotoDetail(movie.id)">
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title"   
            class="card-img-top backgroundimg rounded">
            <img class="mainimg" :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title">
            <div v-if="movie.comments_rating > 0" id="movieInfo">
              <p>평점</p>
              <p>{{ movie.comments_rating }}</p>
            </div>
            <div v-else id="movieInfo">
              <p>리뷰가 없습니다.</p>
            </div>
            <div id="title">
              {{ movie.title }}
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