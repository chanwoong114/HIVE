<template>
  <div>
    <!-- <div class="container d-flex align-items-center ">
      <h1>{{ user.username }}</h1> &nbsp;
      <p>팔로잉 : {{ user.followings_count }} / </p> &nbsp;
      <p> 팔로워 : {{ user.follower_count }}</p>
    </div>

    <h2 class="container" style="text-align: left;">관심있는 영화</h2>
    <div class="container">
      <div class="row row-cols-3 row-cols-md-6 g-2">
        <div class="col" v-for="movie in user.rated_movies" :key="movie.id">
          <div id="zoom" class="bg-dark card mb-4 border-dark" @click="gotoDetail(movie.id)">
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" :alt="movie.title"   
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
      </div>
    </div> -->
    <div class="container py-5 mt-4 mt-lg-5 mb-lg-4 my-xl-5">
        <div class="row pt-sm-2 pt-lg-0">
          <!-- 프로필 바 사진은 992px)-->
          <aside class="col-lg-3 pe-lg-4 pe-xl-5 mt-n3">
            <div class="position-lg-sticky top-0">
              <div class="d-none d-lg-block" style="padding-top: 105px;"></div>
              <div class="offcanvas-lg offcanvas-start" id="sidebarAccount">
                <button class="btn-close position-absolute top-0 end-0 mt-3 me-3 d-lg-none" type="button" data-bs-dismiss="offcanvas" data-bs-target="#sidebarAccount"></button>
                <div class="offcanvas-body">
                  <div class="pb-2 pb-lg-0 mb-4 mb-lg-5"><img class="d-block rounded-circle mb-2" src="assets/img/avatar/23.jpg" width="80">
                    <h3 class="h5 mb-1">{{ user.username }}</h3>
                    <p class="fs-sm text-muted mb-0">팔로잉 : {{ user.followings_count }}</p>
                    <p class="fs-sm text-muted mb-0"> 팔로워 : {{ user.follower_count }}</p>
                    <p class="fs-sm text-muted mb-0">자기소개</p>
                  </div>
                  <nav class="nav flex-column pb-2 pb-lg-4 mb-3">
                    <h4 class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2">Account</h4><a class="nav-link fw-semibold py-2 px-0" href="account-overview.html"><i class="ai-user-check fs-5 opacity-60 me-2"></i>Overview</a><a class="nav-link fw-semibold py-2 px-0" href="account-settings.html"><i class="ai-settings fs-5 opacity-60 me-2"></i>Settings</a><a class="nav-link fw-semibold py-2 px-0" href="account-billing.html"><i class="ai-wallet fs-5 opacity-60 me-2"></i>Billing</a>
                  </nav>
                  <nav class="nav flex-column pb-2 pb-lg-4 mb-1">
                    <h4 class="fs-xs fw-medium text-muted text-uppercase pb-1 mb-2">Dashboard</h4><a class="nav-link fw-semibold py-2 px-0" href="account-orders.html"><i class="ai-cart fs-5 opacity-60 me-2"></i>Orders</a><a class="nav-link fw-semibold py-2 px-0" href="account-earnings.html"><i class="ai-activity fs-5 opacity-60 me-2"></i>Earnings</a><a class="nav-link fw-semibold py-2 px-0" href="account-chat.html"><i class="ai-messages fs-5 opacity-60 me-2"></i>Chat<span class="badge bg-danger ms-auto">4</span></a><a class="nav-link fw-semibold py-2 px-0 active" href="account-favorites.html"><i class="ai-heart fs-5 opacity-60 me-2"></i>Favorites</a>
                  </nav>
                  <nav class="nav flex-column"><a class="nav-link fw-semibold py-2 px-0" href="account-signin.html"><i class="ai-logout fs-5 opacity-60 me-2"></i>Sign out</a></nav>
                </div>
              </div>
            </div>
          </aside>
          <!-- Page content-->
          <div class="col-lg-9 pt-4 pb-2 pb-sm-4">
            <div class="d-flex align-items-center mb-4">
              <h1 class="h2 mb-0">관심있는 영화 <span class='fs-base fw-normal text-muted'>{{ likeMovies.length }}개잇듬</span></h1>
              <button class="btn btn-sm btn-outline-danger ms-auto" type="button"><i class="ai-trash ms-n1 me-2"></i>Clear all</button>
            </div>
            <div class="card border-0 py-1 p-md-2 p-xl-3 p-xxl-4">
              <div class="card-body pb-4">
                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                  <!-- Item-->
                  <div class="col pb-2 pb-sm-3" v-for="movie in likeMovies" :key="movie.id">
                    <MovieDetailItem :movie="movie" />
                    <div class="d-flex mb-1">
                      <h3 class="h6 mb-0"><a href="#">{{ movie.title }}</a></h3>
                      <div class="d-flex ps-2 mt-n1 ms-auto">
                      </div>
                    </div>
                  </div>

        
                  <!-- Item-->
                  <div class="col pb-2 pb-sm-3">
                    <div class="card-hover position-relative bg-secondary rounded-1 p-3 mb-4"><span class="badge bg-faded-primary text-primary position-absolute top-0 start-0 mt-3 ms-3">New</span>
                      <button class="btn btn-icon btn-sm btn-light bg-light border-0 rounded-circle position-absolute top-0 end-0 mt-3 me-3 zindex-5 opacity-0" type="button"><i class="ai-trash fs-xl text-danger"></i></button>
                      <div class="swiper swiper-nav-onhover" data-swiper-options="{&quot;loop&quot;: true, &quot;navigation&quot;: {&quot;prevEl&quot;: &quot;.btn-prev&quot;, &quot;nextEl&quot;: &quot;.btn-next&quot;}}"><a class="swiper-wrapper" href="shop-single.html">
                          <div class="swiper-slide p-2 p-xl-4"><img class="d-block mx-auto" src="assets/img/shop/products/05.png" width="226" alt="Product"></div></a>
                        <button class="btn btn-prev btn-icon btn-sm btn-light bg-light border-0 rounded-circle start-0" type="button"><i class="ai-chevron-left fs-xl d-dark-mode-none"></i><i class="ai-chevron-left text-nav fs-xl d-none d-dark-mode-block"></i></button>
                        <button class="btn btn-next btn-icon btn-sm btn-light bg-light border-0 rounded-circle end-0" type="button"><i class="ai-chevron-right fs-xl d-dark-mode-none"></i><i class="ai-chevron-right text-nav fs-xl d-none d-dark-mode-block"></i></button>
                      </div>
                    </div>
                    <div class="d-flex mb-1">
                      <h3 class="h6 mb-0"><a href="shop-single.html">Pendant lamp</a></h3>
                      <div class="d-flex ps-2 mt-n1 ms-auto">
                        <div class="ms-1">
                          <input class="btn-check" type="radio" name="color4" value="Gray" checked id="color4-1">
                          <label class="btn btn-icon btn-xs btn-outline-secondary rounded-circle" for="color4-1"><span class="d-block rounded-circle" style="width: .625rem; height: .625rem; background-color: #bab8b7;"></span></label>
                        </div>
                        <div class="ms-1">
                          <input class="btn-check" type="radio" name="color4" value="Woody brown" id="color4-2">
                          <label class="btn btn-icon btn-xs btn-outline-secondary rounded-circle" for="color4-2"><span class="d-block bg-size-cover bg-position-center rounded-circle" style="width: .625rem; height: .625rem; background-color: #c0c0c0; background-image: url(assets/img/shop/pattern/wood.jpg);"></span></label>
                        </div>
                        <div class="ms-1">
                          <input class="btn-check" type="radio" name="color4" value="Gray marble" id="color4-3">
                          <label class="btn btn-icon btn-xs btn-outline-secondary rounded-circle" for="color4-3"><span class="d-block bg-size-cover bg-position-center rounded-circle" style="width: .625rem; height: .625rem; background-color: #c0c0c0; background-image: url(assets/img/shop/pattern/marble.jpg);"></span></label>
                        </div>
                      </div>
                    </div>
                    <div class="d-flex align-items-center"><span class="me-2">$22.00</span>
                      <div class="nav ms-auto" data-bs-toggle="tooltip" data-bs-template="&lt;div class=&quot;tooltip fs-xs&quot; role=&quot;tooltip&quot;&gt;&lt;div class=&quot;tooltip-inner bg-light text-muted p-0&quot;&gt;&lt;/div&gt;&lt;/div&gt;" data-bs-placement="left" title="Add to cart"><a class="nav-link fs-lg py-2 px-1" href="#"><i class="ai-cart"></i></a></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailItem from '@/components/MovieDetailComponent/MovieDetailItem.vue'

export default {
  data() {
    return {
      user: null,
    }
  },
  components: {
    MovieDetailItem
  },
  methods: {
    getUserInfo() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/mypage/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.user = res.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    gotoDetail(movieId) {
      this.$router.push({name: 'MovieDetailView', params: {movieId: `${movieId}`}})
    },
  },
  created() {
    this.getUserInfo()
  },
  computed: {
    likeMovies() {
      return this.user.rated_movies.filter(movie => {
        return this.$store.getters.likeMovies.includes(movie.id)
      })
    }
  }
}
</script>

<style>

</style>