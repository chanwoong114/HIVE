<template>
  <div>
    <div class="card mb-4" @click="gotoDetail(movie?.id)">
      <img :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" :alt="movie.title"   
      class="card-img-top">
      <div class="card-body">
        <h5 class="card-title" style="color: black">{{ movie?.title }}</h5>
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

</style>