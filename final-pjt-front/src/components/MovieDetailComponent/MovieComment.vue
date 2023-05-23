<template>
  <div>
    <h1>movie Comment</h1>
      <div v-for="comment in comments" :key="comment.id">
        <p>작성자 : {{ comment.user.username }}</p>
        <p>내용 : {{ comment.content }}</p>
        <star-rating :star-size="25" :border-width="2" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" 
        :rating="comment.rating" :read-only="true" :increment="0.5"></star-rating>
        <hr>
      </div>
      <form @submit.prevent="createComment()">
        <div class="input-group mb-3 ">
          <input type="text" class="form-control" v-model="content"
          aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
          <star-rating :border-width="3" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
            :inline="true" :increment="0.5" :star-size="30" :show-rating="false" v-model="rating"></star-rating>
          <button type="submit" class="input-group-text btn bg-primary text-white" id="inputGroup-sizing-default">
            &nbsp;&nbsp;작성&nbsp;&nbsp;</button>
        </div>
      </form>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieComment',
  props: {
    movieComments: Array,
    movieId: Number
  },
  components: {
    StarRating
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
      if (!this.content || !this.rating) {
        return alert('평점과 내용을 입력하세요!')
      }
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