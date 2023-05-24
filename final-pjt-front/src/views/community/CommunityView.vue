<template>
  
  <div class="board-list">
    <!-- 게시글생성 버튼 -->
    <div class="common-buttons">
      <button type="button" class="w3-button w3-round w3-blue-gray" @click="createArticle()">글쓰기</button>
    </div>
    
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

    <div class="container pt-5 pb-lg-5 pb-md-4 pb-2 my-5">
        <!-- 게시글 네브바 -->
        <div class="row align-items-center gy-2 mb-4 pb-1 pb-sm-2 pb-lg-3">
          <div class="col-lg-5">
            <h1 class="mb-lg-0">게시판</h1>
          </div>
          <div class="col-xl-2 offset-xl-1 col-lg-3 col-sm-5">
            <select class="form-select">
              <option>All categories</option>
              <option>뭐별</option>
              <option>뭐별</option>
            </select>
          </div>
          <div class="col-lg-4 col-sm-7">
            <div class="position-relative"><i class="ai-search position-absolute top-50 start-0 translate-middle-y ms-3"></i>
              <input class="form-control ps-5" type="search" placeholder="Enter keyword">
            </div>
          </div>
        </div>
        <!-- 게시글들 -->
        <article class="row g-0 border-0 mb-4" v-for="(row, idx) in articles" :key="idx">
          <a class="col-sm-5 col-lg-4 bg-repeat-0 bg-size-cover bg-position-center rounded-5" href="#" style="background-color: blueviolet; min-height: 16rem"></a>
          <div class="col-sm-7 col-lg-8">
            <div class="pt-4 pb-sm-4 ps-sm-4 pe-lg-4">
              <h3>No.{{ row.id }}</h3>
              <h3 class="zoom" v-on:click="gotoArticle(row.id)"><a :href="row.url">제목 {{ row.title }}</a></h3>
              <p class="zoom d-sm-none d-md-block" @click="gotoUser(row.user.username)">작성자 {{ row.user.username }}</p>
              <p>등록일자 {{ row.updated_at.slice(0, 10) }}</p>
              <p>댓글 {{ row.comment_counts }}</p>
            </div>
          </div>
        </article>
  
        <div class="row gy-3 align-items-center mt-lg-5 pt-2 pt-md-3 pt-lg-0 mb-md-2 mb-xl-4">
          <div class="col col-md-4 col-6 order-md-1 order-1">
            
          </div>
       
          <div class="col col-md-4 col-6 order-md-3 order-2">
            <nav aria-label="Page navigation">
              <ul class="pagination pagination-sm justify-content-end">
                <li class="page-item active" aria-current="page"><span class="page-link">1<span class="visually-hidden">(current)</span></span></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">4</a></li>
                <li class="page-item"><a class="page-link" href="#">5</a></li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
   
    <!-- Subscription-->
    
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