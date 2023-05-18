<template>
  <div class="container">
    <div class="row cols-4">
      <div class="col" v-for="movie in movies" :key="movie.id">
        <div class="card mb-4">
          <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title" 
          
          class="card-img-top">
          <div class="card-body">
            <h5 class="card-title" style="color: black">{{ movie.title }}</h5>
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
      API_URL: 'http://localhost:8000',
      movies: []
    }
  },
  methods: {
    movieList(){
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.movies = res.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.movieList()
  }
}
</script>

<style>

</style>
