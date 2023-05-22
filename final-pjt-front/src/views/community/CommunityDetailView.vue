<template>
  <div class="board-detail">
    <div class="common-buttons">
      <button type="button" class="w3-button w3-round w3-blue-gray" @click="articleUpdate">수정</button>&nbsp;
      <button type="button" class="w3-button w3-round w3-red" @click="articleDelete">삭제</button>&nbsp;
      <button type="button" class="w3-button w3-round w3-gray" @click="articleList">목록</button>
    </div>
    <div class="board-contents">
      <h3>{{ title }}</h3>
      <div>
        <strong class="w3-large">{{ author }}</strong>
        <br>
        <span>{{ updated_at.slice(0, 10) }}</span>
      </div>
    </div>
    <div class="board-contents">
      <span>{{ contents }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityDetailView',
  data() { //변수생성
    return {
      requestBody: this.$route.query,
      idx: this.$route.query.idx,

      title: '',
      author: '',
      contents: '',
      updated_at: ''
    }
  },
  mounted() {
    this.getArticle()
  },
  methods: {
    getArticle() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/${this.$route.params.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.title = res.data.title
        this.author = res.data.user.username
        this.contents = res.data.content
        this.updated_at = res.data.updated_at
      })
      .catch((err) => {
        if (err.message.indexOf('Network Error') > -1) {
          alert('네트워크가 원활하지 않습니다.\n잠시 후 다시 시도해주세요.')
        }
      })
    },
    articleList() {
      delete this.requestBody.idx
      this.$router.push({name: 'community'})
    },
    articleUpdate() {
      this.$router.push({name: 'UpdateArticle', params: {articleId: this.$route.params.articleId}})
    },
    articleDelete() {
      if (!confirm("삭제하시겠습니까?")) return

      this.$store.dispatch('deleteArticle', this.$route.params.articleId)
    }
  }
  }
</script>


<style>

</style>