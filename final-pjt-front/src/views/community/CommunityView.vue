<template>
  <!-- <div>
    <h1>커뮤니티</h1>
    <router-link :to="{name: 'CreateArticle'}">글 작성하기</router-link>
    <div v-for="article in articles" :key="article.id" @click="gotoArticle(article.id)">
      {{ article.title }} : {{ article.content }}
    </div>
  </div> -->
  <div class="board-list">
    <div class="common-buttons">
      <button type="button" class="w3-button w3-round w3-blue-gray" @click="createArticle()">등록</button>
    </div>
    <table class="w3-table-all text-dark">
      <thead>
      <tr class="text-dark">
        <th>No</th>
        <th>제목</th>
        <th>작성자</th>
        <th>등록일자</th>
        <th>댓글 수</th>
      </tr>
      </thead>
      <tbody>
      <tr class="text-dark" v-for="(row, idx) in articles" :key="idx">
        <td>{{ row.id }}</td>
        <td class="zoom" v-on:click="gotoArticle(row.id)">{{ row.title }}</td>
        <td class="zoom" @click="gotoUser(row.user.username)">{{ row.user.username }}</td>
        <td>{{ row.updated_at.slice(0, 10) }}</td>
        <td>{{ row.comment_counts }}</td>
      </tr>
      </tbody>
    </table>
    <div class="pagination w3-bar w3-padding-16 w3-small" v-if="paging.total_list_cnt > 0">
      <span class="pg">
      <a href="javascript:;" @click="fnPage(1)" class="first w3-button w3-border">&lt;&lt;</a>
      <a href="javascript:;" v-if="paging.start_page > 10" @click="fnPage(`${paging.start_page-1}`)"
         class="prev w3-button w3-border">&lt;</a>
      <template v-for=" (n,index) in paginavigation()">
          <template v-if="paging.page==n">
              <strong class="w3-button w3-border w3-green" :key="index">{{ n }}</strong>
          </template>
          <template v-else>
              <a class="w3-button w3-border" href="javascript:;" @click="fnPage(`${n}`)" :key="index">{{ n }}</a>
          </template>
      </template>
      <a href="javascript:;" v-if="paging.total_page_cnt > paging.end_page"
         @click="fnPage(`${paging.end_page+1}`)" class="next w3-button w3-border">&gt;</a>
      <a href="javascript:;" @click="fnPage(`${paging.total_page_cnt}`)" class="last w3-button w3-border">&gt;&gt;</a>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
  created() {
    this.$store.dispatch('getArticles')
    console.log(this.$store.getters.getArticles)
  },
  data() { //변수생성
    return {
      requestBody: {}, //리스트 페이지 데이터전송
      no: '', //게시판 숫자처리
      paging: {
        block: 0,
        end_page: 0,
        next_block: 0,
        page: 0,
        page_size: 0,
        prev_block: 0,
        start_index: 0,
        start_page: 0,
        total_block_cnt: 0,
        total_list_cnt: 0,
        total_page_cnt: 0,
      }, //페이징 데이터
      page: this.$route.query.page ? this.$route.query.page : 1,
      size: this.$route.query.size ? this.$route.query.size : 10,
      keyword: this.$route.query.keyword,
      paginavigation() { //페이징 처리 for문 커스텀
        let pageNumber = [] //;
        let start_page = this.paging.start_page;
        let end_page = this.paging.end_page;
        for (let i = start_page; i <= end_page; i++) pageNumber.push(i);
        return pageNumber;
      }
    }
  },
  methods: {
    createArticle() {
      this.$router.push({name: 'CreateArticle'})
    },
    gotoArticle(articleId) {
      this.$router.push({name: 'communityDetail', params: {'articleId': articleId}})
    },
    fnView(idx) {
      this.requestBody.idx = idx
      this.$router.push({
        path: './detail',
        query: this.requestBody
      })
    },
    fnWrite() {
      this.$router.push({
        path: './write'
      })
    },
    fnPage(n) {
      if (this.page !== n) {
        this.page = n
        this.fnGetList()
      }
    },
    gotoUser(username) {
      this.$router.push({name: 'UserPage', params: {'username': username}})
    },
  },
  computed: {
    articles() {
      return this.$store.getters.getArticles
    }
  }
}
</script>

<style>
  .board-list {
    width: 768px;
    margin: auto;
  }

  .board-detail {
      width: 768px;
      margin: auto;
      text-align: left;
  }

  .board-contents {
      padding: 12px 8px;
      border-bottom: 1px solid #eee;
  }

  .common-buttons {
      padding: 8px;
      text-align: right;
  }

  .zoom:hover {
    transform: scale(1.2);
    transition: 0.7s;
  }

</style>