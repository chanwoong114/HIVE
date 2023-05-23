<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 col-12" >
        <h1 style="text-align: start;">{{ movie.title }}</h1>
        <br>
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" width="50%" alt="">
      </div>
  
      <div class="col-md-8 col-12 d-flex-column justify-content-between">
        <h4 class="text-start">감독</h4>
        <div style="width: 10%;">
          <a class="personBox" href="" data-fancybox @click="trigger('crew', movie.crew_ids.id)" style="width: 10%;" data-src="#crew-content">
            <img id="personimg" :src="`https://image.tmdb.org/t/p/original/${movie.crew_ids.profile_path}`" width="100" class="rounded-2" alt="">
            <p id="personP">{{ movie.crew_ids.name }}</p>
          </a>
          <div id="crew-content" style="display:none;width:70%;">
            <h1>{{ movie.crew_ids.name }}</h1>
            <br>
            <br>
            <h3>제작한 영화</h3>
            <div id="cardbox" class="row mx-auto">
              <MovieDetailItem class="col-2" v-for="(crewMovie, index) in personMovie" :key="index" :movie="crewMovie"/>
            </div>
          </div>
        </div>

        <h4>출연진</h4>
        <div class="row">
          <div class="col" v-for="cast in movie.cast_ids" :key="cast.id">
            <a class="personBox" href="" data-fancybox @click="trigger('cast', cast.id)" :data-src="`#${cast.id}`">
              <img id="personimg" :src="`https://image.tmdb.org/t/p/original/${cast.profile_path}`" width="100" class="rounded-2" alt="">
              <p id="personP">{{ cast.name }}</p>
            </a>
            <div :id="cast.id" style="display:none;width:70%;">
              <h1>{{ cast.name }}</h1>
              <br>
              <br>
              <h3>참여</h3>
              <div class="row">
                <MovieDetailItem class="col-2" v-for="(castMovie, index) in personMovie" :key="index" :movie="castMovie" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br>
    <h1 style="text-align: start;">연관 추천 영화</h1>
    <br>
    <div class="row row-cols-3 row-cols-md-6 g-2 mx-auto ">
      <div class="col container"  v-for="(recommendMovie, index) in movie.recommend_movies" :key="index"
      @click="gotoDetail(recommendMovie.id), reload()">
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
      API_URL: 'http://127.0.0.1:8000',
      liked: null, 

      URL: 'yJIl-hpPVDA',
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
    },
    loadUrl() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.movieId}/videos?language=ko-KR/`,
        params: {
          api_key: 'c0277ff053c36cf743bb896821c5f0f1'
        }
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created() {
    this.loadMovieDetail()
    this.loadUrl()
  },
}
</script>

<style scoped>
  /* #posterimg {
    position: absolute;
    left: 0%;
    z-index: 1;
    opacity: 0.2;
  }

  div {
    z-index: 2;
  }

  a {
    z-index: 2;
  } */

  .personBox {
    position: relative;
  }

  .personBox:hover #personimg {
    opacity: 0.5;
    border: 2px solid;
    border-color:white;
    margin-bottom: 2px;
  }

  .personBox:hover #cardbox {
    opacity: 1;
  }

  #personP {
    display: none;
    color: white;
  }

  .personBox:hover #personP {
    position: absolute;
    left: 8%;
    top: 0%;
    display: inline;
  }

</style>