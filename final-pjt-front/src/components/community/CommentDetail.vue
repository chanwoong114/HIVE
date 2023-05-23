<template>
  <div>
    <div v-if="updateCheck" class="input-group mb-3 ">
      <input type="text" class="form-control" v-model="content"
      aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
      <span @click="updateComment" class="input-group-text btn bg-success text-white" 
      id="inputGroup-sizing-default">&nbsp;&nbsp;수정&nbsp;&nbsp;</span>
      <span @click="updateToggle" class="input-group-text btn bg-secondary text-white" 
      id="inputGroup-sizing-default">&nbsp;&nbsp;취소&nbsp;&nbsp;</span>
    </div>
    <span v-if="!updateCheck" class="underbar d-flex justify-content-between" >
      <span>
        내용 : {{ comment.content }}
      </span>
      <span>
        작성자 : {{ comment.user.username }}
        <span v-if="comment.user.username === $store.state.username">
          <span class="btn btn-success" @click="updateToggle()">수정</span>
          <span class="btn btn-danger" @click="deleteComment()">삭제</span>
        </span>
      </span>
    </span>
  </div>
</template>

<script>

export default {
  name: 'CommentDetail',
  props: {
    comment: Object,
  },
  data() {
    return {
      updateCheck: false,
      content: '',
    }
  },
  methods: {
    deleteComment() {
      this.$store.dispatch('deleteComment', this.comment.id)
    },
    updateComment() {
      this.$store.dispatch('updateComment', [this.comment.id, this.content])
      this.content = ''
      this.updateCheck = !this.updateCheck
    },
    updateToggle() {
      this.updateCheck = !this.updateCheck
    }
  }
}
</script>

<style>

</style>