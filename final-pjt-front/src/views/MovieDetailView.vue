<template>
  <div>
    <h1>MovieDetailView</h1>
    {{ movie.title }}
    <p>{{ movie.crew_ids }}</p>
    
    <div v-for="cast in movie.cast_ids" :key="cast.id">
      {{ cast.name }}, {{ cast.id }}
    </div>


    <div class="row row-cols-1 row-cols-md-3 g-2">
      <div class="col"  v-for="(recommendMovie, index) in movie.recommend_movies" :key="index"
      @click="gotoDetail(recommendMovie.id), loadMovieDetail()">
        <MovieDetailItem  :movie="recommendMovie"/>
      </div>
    </div>

  </div>
</template>

<script>
import MovieDetailItem from '@/components/MovieDetailItem.vue';
import axios from 'axios';

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailItem,
  },
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
        console.log(res.data)
        this.movie = res.data
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
    this.loadMovieDetail()
  }
}
</script>

<style>

</style>