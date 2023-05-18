<template>
  <div>
    <h1>MovieDetailView</h1>
    {{ movie }}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: null
    }
  },
  methods: {
    loadMovieDetail() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.movieId}/`
      })
      .then(res => {
        this.movie = res.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.loadMovieDetail()
  }
}
</script>

<style>

</style>