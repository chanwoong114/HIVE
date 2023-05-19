<template>
  <div>
    <h1>MovieDetailView</h1>
    {{ movie.title }}
    <div>
      <br>
      <h4>감독</h4>
      <a href="" data-fancybox @click="trigger('crew', movie.crew_ids.id)" data-src="#crew-content">
        <div class="btn btn-light my-2 ">
          <p>{{ movie.crew_ids.name }}</p>
          <p>{{ movie.crew_ids.id }}</p>
        </div>
      </a>
      <div id="crew-content" style="display:none;width:1000px;">
        <h1>{{ movie.crew_ids.name }}</h1>
        <img :src="`https://image.tmdb.org/t/p/original/${movie.crew_ids.profile_path}`" width="50px" height="70px" alt="">
        <div v-for="(crewMovie, index) in personMovie" :key="index">
          <div @click="gotoDetail(crewMovie.id), loadMovieDetail(), reload()">
            {{ crewMovie.title }}  
          </div>
        </div>
      </div>
      <h4>출연진</h4>
      <div class="row">
        <div class="col btn btn-light mx-3" v-for="cast in movie.cast_ids" :key="cast.id">
          <a href="" data-fancybox @click="trigger('cast', cast.id)" :data-src="`#${cast.id}`">
            <div class="btn btn-light my-2 ">
              <p>{{ cast.name }}</p>
              <p>{{ cast.id }}</p>
              <p>{{ cast.character }}</p>
            </div>
          </a>
          <div :id="cast.id" style="display:none;width:1000px;">
            <h1>{{ cast.name }}</h1>
            {{ cast }}
            <img :src="`https://image.tmdb.org/t/p/original/${cast.profile_path}`" width="50px" height="70px" alt="">
            <div v-for="(crewMovie, index) in personMovie" :key="index">
              <div @click="gotoDetail(crewMovie.id), loadMovieDetail(), reload()">
                {{ crewMovie.title }}  
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row row-cols-1 row-cols-md-3 g-2">
      <div class="col"  v-for="(recommendMovie, index) in movie.recommend_movies" :key="index"
      @click="gotoDetail(recommendMovie.id), loadMovieDetail()">
        <MovieDetailItem  :movie="recommendMovie"/>
      </div>
    </div>

    <div>
      <MovieComment :movieComments="movie.comments" :movieId="movie.id"/>
    </div>
  </div>
</template>

<script>
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue';
import axios from 'axios';
import MovieComment from '../components/MovieDetailComponent/MovieComment.vue';


export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailItem,
    MovieComment,
  },
  data() {
    return {
      movie: null,
      personMovie: null,
      API_URL: 'http://127.0.0.1:8000'
    }
  },
  methods: {
    loadMovieDetail() {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${this.$route.params.movieId}/`
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
    trigger(job, id) {
      axios({
        method: 'get',
        url: `${this.API_URL}/movies/${job}/${id}/`,
      })
      .then(res => {
        this.personMovie = res.data
        console.log(this.personMovie)
      })
      .catch(error => {
        console.log(error)
      })
    },
    reload() {
      this.$router.go(this.$router.currentRoute)
    }
  },
  created() {
    this.loadMovieDetail()
  },
}
</script>

<style>

</style>