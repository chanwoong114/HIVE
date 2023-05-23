<template>
  <div class="container">
    <div>
    <h1>{{ user.username }}</h1>
    <p>팔로잉 : {{ user.followings_count }}</p>
    <p>팔로워 : {{ user.follower_count }}</p>

    <div class="container">
      <div class="row row-cols-3 row-cols-md-6 g-2">
        <div class="col" v-for="movie in user.rated_movies" :key="movie.id">
          <MovieDetailItem :movie="movie"/>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue'

export default {
  name: 'UserPage',
  components: {
    MovieDetailItem
  },
  data() {
    return {
      user: null,
    }
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/username/${this.$route.params.username}/`,
        headers: `Token ${this.$store.state.token}`
      })
      .then(res => {
        console.log(res)
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