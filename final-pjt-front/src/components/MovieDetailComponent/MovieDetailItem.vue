<template>
  <div>
    <div id="zoom" class="bg-dark card mb-4 border-dark" @click="gotoDetail(movie.id)">
      <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title"   
      class="card-img-top backgroundimg">
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
      <i class="bi bi-suit-heart-fill"></i>
      <i class="bi bi-suit-heart"></i>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieDetailItem',
    props: {
        movie: Object,
    },
    methods: {
      gotoDetail(movieId) {
        if (!this.$route.params.movieId) {
          this.$router.push({name: 'MovieDetailView', params: {movieId: movieId}})
          return
        }

        if (movieId != this.$route.params.movieId) {
          this.$router.push({name: 'MovieDetailView', params: {movieId: movieId}})
          this.$router.go(this.$router.currentRoute)
        } else {
          this.$router.go(this.$router.currentRoute)
        }
      }
    }
}
</script>

<style>

</style>