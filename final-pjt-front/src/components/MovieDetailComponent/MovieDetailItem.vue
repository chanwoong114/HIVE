<template>
  <div>
    <h3>Item</h3>
    <div>
        <p>{{ movie.title }}</p>
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