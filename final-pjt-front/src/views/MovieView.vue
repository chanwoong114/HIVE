<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4" v-for="movie in movies" :key="movie.id">
        <div class="card mb-4">
          <img :src="'../assetx/hive.png/' + movie.poster_path" :alt="movie.title" class="card-img-top">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieView',
  data() {
    return {
      movies: []
    }
  },
  created() {
    axios.get('https://api.themoviedb.org/3/movie/top_rated?language=ko-KR', {
      params: {
        api_key: '6e4f60ea88e44702b1782875498a4af2'
      }
    })
      .then(response => {
        this.movies = response.data.results
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>
