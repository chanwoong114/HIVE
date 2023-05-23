<template>
  <div>
    <div id="zoom" class="bg-dark card mb-4" @click="gotoDetail(movie?.id)">
      <img id="firstimg" :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title"   
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
</template>

<script>
export default {
    name: 'MovieDetailItem',
    props: {
        movie: Object,
    },
    method: {
    }
}
</script>
 
<style>
  .firstimg {
    height: 100%;
  }
</style>