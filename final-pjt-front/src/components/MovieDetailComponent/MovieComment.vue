<template>
  <div>
    <h1>movie Comment</h1>
      <div v-for="comment in comments" :key="comment.id">
        <p>{{ comment.content }}</p>
        <p>{{ comment.rating }}</p>
        <hr>
      </div>
      <form @submit.prevent="createComment()">
        <label for="content">내용 : </label>
        <input type="text" v-model="content"><br>
        <label for="rating">별점 : </label>
        <b-input-group style="min-width: 10em;">
          <b-input-group-prepend>
            <b-button @click="rating = null">Clear</b-button>
          </b-input-group-prepend>
          <b-form-rating v-model="rating" color="#ff8800"></b-form-rating>
        </b-input-group>    
        <input type="submit">
      </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieComment',
  props: {
    movieComments: Array,
    movieId: Number
  },
  data() {
    return {
      comments: [],
      content: null,
      rating: null,
    }
  },
  methods: {
    getstart() {
      this.comments = this.movieComments
    },
    createComment() {
      console.log(this.content, this.rating)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/comments/`,
        data: {
          content: this.content,
          rating: this.rating
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        }
      })
      .then(res => {
        this.comments.push(res.data)
        this.content = null
        this.rating = null
      })
      .catch(error => {
        console.log(error)
      })
    },
    getComment() {
      axios
    }
  },
  created() {
    this.getstart()
  }
}
</script>

<style >

</style>