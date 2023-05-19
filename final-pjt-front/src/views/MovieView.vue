<template>
  <div class="container">
    <!-- <div class="f-carousel" id="myCarousel">
      <div class="f-carousel__slide">1</div>
      <div class="f-carousel__slide">2</div>
      <div class="f-carousel__slide">3</div>
      <div class="f-carousel__slide">421321</div>
      <div class="f-carousel__slide">5</div>
      <div class="f-carousel__slide">6</div>
      <div class="f-carousel__slide">7</div>
      <div class="f-carousel__slide">8</div>
      <div class="f-carousel__slide">9</div>
      <div class="f-carousel__slide">10</div>
    </div>
    
    <div class="f-carousel" id="myNavigation">
      <div class="f-carousel__slide">1</div>
      <div class="f-carousel__slide">2</div>
      <div class="f-carousel__slide">3</div>
      <div class="f-carousel__slide">423214</div>
      <div class="f-carousel__slide">5</div>
      <div class="f-carousel__slide">6</div>
      <div class="f-carousel__slide">7</div>
      <div class="f-carousel__slide">8</div>
      <div class="f-carousel__slide">9</div>
      <div class="f-carousel__slide">10</div>
    </div> -->
    <div>{{ movies.length }}</div>
    <div v-if="movies.length != 0" class="f-carousel" id="myCarousel">
      <div :class="'f-carousel__slide'" v-for="(movie, index) in movies" :key="index">
        <!-- <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" 
        width="100px" height="140" :alt="movie.title"> -->
        {{ movie.id }}
      </div>
    </div>
    <!-- <div v-if="movies.length != 0" class="f-carousel" id="myNavigation">
      <div :class="'f-carousel__slide'" v-for="(movie, index) in movies" :key="index">
        <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" 
        width="100px" height="140" :alt="movie.title">
        {{ movie?.id }}
      </div>
    </div> -->
    <div class="row">
      <div class="col-2" v-for="movie in movies" :key="movie.id">
        <div class="card mb-4" @click="gotoDetail(movie?.id)">
          <img :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" :alt="movie.title"   
          class="card-img-top">
          <div class="card-body">
            <h5 class="card-title" style="color: black">{{ movie?.title }}</h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import { Carousel } from "@fancyapps/ui/dist/carousel/carousel.esm.js";
import "@fancyapps/ui/dist/carousel/carousel.css";

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
        this.movies = res.data.slice(0, 10)
        const container = document.getElementById("myCarousel");
        const options = { infinite: false };

        new Carousel(container, options);
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    }
  },
  created() {
    this.movieList()
  }
}
</script>

<style>
  .f-carousel__slide {
    display: flex;
    align-items: center;
    justify-content: center;

    min-height: 100px;
    text-align: center;
    color: #ff3520;
    background: #f3f3f3;
    font-size: 1.25rem;
  }

  .f-carousel__slide.is-nav-selected {
    color: #fff;
    background: #ff3520;
  }

  #myCarousel {
    --f-carousel-slide-width: 100%;
    --f-carousel-spacing: 10px;

    margin-bottom: 1rem;
  }

  #myNavigation {
    --f-carousel-slide-width: 100px;
    --f-carousel-spacing: 5px;
  }
</style>
