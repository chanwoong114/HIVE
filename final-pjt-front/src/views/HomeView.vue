<template>
  <div>
    <!-- Page wrapper-->
    <div class="page-wrapper">
      <div class="dark-mode">
        <!-- 네브바-->
        <header class="navbar navbar-expand-lg fixed-top bg-dark ">
          <div class="container"><a class="navbar-brand pe-sm-3" href="index.html">
            <img src="../assets/bighive.png" alt="Logo" width="35" height="32">
            HIVE
            </a>
            <div>
            <div class="form-check form-switch mode-switch order-lg-2 me-3 me-lg-4 ms-auto" data-bs-toggle="mode">
              <input class="form-check-input" type="checkbox" id="theme-mode" v-model="darkMode" @click="toggleDarkMode()">
              <label class="form-check-label" for="theme-mode"><i class="ai-sun fs-lg"></i></label>
              <label class="form-check-label" for="theme-mode"><i class="ai-moon fs-lg"></i></label>
              <div class="btn btn-primary btn-sm fs-sm order-lg-3 d-none d-sm-inline-flex" @click="gotoLogin()" target="_blank" rel="noopener">
              <i class="ai-login fs-xl me-2 ms-n1"></i>로그인
              </div>
            </div>
            
            
          </div>
            
          </div>
        </header>
      </div>
      <!-- 젤처름 꿀벌 3마리 랑 스크롤-->
      
      <div class="bg-dark dark-mode position-relative min-vh-100 overflow-hidden pt-5">
        <svg class="position-absolute top-0" width="262" height="160" viewBox="0 0 262 160" fill="none" xmlns="http://www.w3.org/2000/svg" style="left: 6%;">
          <ellipse cx="131" cy="30.5" rx="131" ry="129.5" fill="white" fill-opacity=".03"></ellipse>
        </svg>
        <div class="container position-relative zindex-5 text-center pt-5 mt-lg-4 mt-xl-5">
          <h1 class="display-1 pt-4 mt-sm-3"><span class="text-white fw-normal"><h3> 영화추천은 </h3></span><span class="d-inline-flex align-items-center"><span class="text-white">HIVE!</span></span></h1>
          <p class="fs-xl mb-5">페이지를 스크롤해주세요</p><a class="scroll-down-btn" href="#landings" data-scroll data-scroll-offset="20">
            <div class="mouse"></div>
            <p>Landings</p></a>
        </div>
        <div class="d-none d-lg-block" style="margin-top: -80px;"></div>
        <div class="d-none d-sm-block d-lg-none" style="margin-top: -40px;"></div>
        <div class="parallax mx-auto mb-n5" style="max-width: 800px;">
          <div class="parallax-layer zindex-2" data-depth="0.9" style="margin-top: -3cm;"><img src="../assets/A.png" alt="Foreground shape"></div>
          <div class="parallax-layer zindex-2" data-depth="0.9" style="margin-top: -3cm;"><img src="../assets/B.png" alt="Foreground shape"></div>
          <div class="parallax-layer zindex-2" data-depth="0.9" style="margin-top: -3cm;"><img src="../assets/C.png" alt="Foreground shape"></div>
          <div class="parallax-layer" data-depth="-0.1"><img src="assets/img/landing/intro/hero/01.png" alt="Background shapes"></div>
        </div>
      </div>
      <!-- HIVE란?-->
      <div class="bg-gray py-2 py-lg-3 py-xl-4 py-xxl-5" id="landings">
        <div class="container py-5 mt-1 mb-2 mt-sm-2 mb-sm-3 mt-md-3 mb-md-4 my-lg-4 my-xl-5">
          <h2 class="display-5 text-center pt-xxl-2">HIVE란?</h2>
          <h3 class="fs-lg text-center pb-3 pb-lg-0 mb-lg-5">"당신을 위해 최고의 영화를 선택해봤어요! 영화 속 세계로 여행을 떠나보세요. 잠깐의 시간을 잊고 즐거운 시간을 보내실 수 있을 거예요. 여러분을 감동시키고 웃음을 안겨줄 영화를 선별했습니다. 편안한 자리에 앉아서 최고의 영화와 함께 특별한 순간을 즐겨보세요!"</h3>
          <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 gy-5 pb-xl-3">
            <!-- 사진들어가는곳-->
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/hh.png"><img class="d-none d-dark-mode-block" src="../assets/hh.png"></div>
                <h3 class="h5 text-center mb-0"><a class="stretched-link" href="landing-mobile-app-showcase.html">영화추천</a></h3>
              </div>
            </div>
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/hh.png" ><img class="d-none d-dark-mode-block" src="../assets/hh.png"></div>
                <h2 class="h5 text-center mb-0"><a class="stretched-link" href="landing-product.html">즐겨찾기</a></h2>
              </div>
            </div>
            <div class="col">
              <div class="card-hover card-lifted mx-auto" style="max-width: 416px;">
                <div class="card-lifted overflow-hidden rounded-3 mb-3"><img class="d-dark-mode-none" src="../assets/hh.png" ><img class="d-none d-dark-mode-block" src="../assets/hh.png"></div>
                <h3 class="h5 text-center mb-0"><a class="stretched-link" href="#">장르별</a></h3>
              </div>
            </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 사이트 목업 보여주는곳-->

      <section class="overflow-hidden pt-2 pt-sm-3 pt-md-4 pt-lg-3 pb-1 pb-sm-3 pb-md-4 pb-lg-5">
        <div class="container position-relative py-5 my-lg-3 my-xl-4 my-xxl-5">
          <div class="position-absolute" style="margin-left: -9.7%;" data-aos="zoom-in" data-aos-duration="500" data-aos-offset="300" data-disable-parallax-down="lg">
            <svg class="text-warning d-none d-lg-block" width="744" height="744" viewBox="0 0 744 744" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <circle cx="372" cy="372" r="372"></circle>
            </svg>
          </div>
          <div class="d-none d-xxl-block" style="height: 190px;"></div>
          <div class="d-none d-lg-block d-xxl-none" style="height: 150px;"></div>
          <div class="row justify-content-center justify-content-lg-start position-relative zindex-2">
            <div class="col-sm-10 col-md-8 col-lg-5 col-xl-4 text-center text-lg-start" data-aos="fade-up" data-aos-duration="850" data-aos-offset="120" data-disable-parallax-down="lg">
              <div class="ignore-dark-mode d-none d-lg-block">
                <h2 class="display-5 mb-4">영화 추천의 새로운시작 HIVE</h2>
                <p class="fs-lg text-dark pb-3 pb-sm-4 mb-lg-0">"하루의 피로를 한 번의 클릭으로 날려버리세요!  이제 한 번의 클릭으로 최고의 영화를 경험할 수 있습니다!"</p>
              </div>
              <div class="d-lg-none">
                <h2 class="display-5 mb-4">영화 추천의 새로운시작 HIVE</h2>
                <p class="fs-lg text-dark pb-3 pb-sm-4 mb-lg-0">"하루의 피로를 한 번의 클릭으로 날려버리세요!  이제 한 번의 클릭으로 최고의 영화를 경험할 수 있습니다!"</p>
              </div>
            </div>
          </div>
          <div class="d-none d-xl-block" style="margin-top: -240px;"></div>
          <div class="d-none d-lg-block d-xl-none" style="margin-top: -160px;"></div>
          <div class="d-flex position-relative zindex-2 mb-3">
            <div class="flex-xxl-shrink-0 position-relative zindex-2" style="max-width: 700px; margin-top: 26%; margin-right: 5.6%;" data-aos="fade-up" data-aos-duration="500" data-aos-delay="400" data-disable-parallax-down="lg">
              <img class="rounded-3 mt-n5 mt-lg-0 d-block d-dark-mode-none" src="assets/Group3.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="border rounded-3 mt-n5 mt-lg-0 d-none d-dark-mode-block" src="assets/Group3.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
            <div class="flex-xxl-shrink-0 position-relative zindex-1" style="max-width: 600px; margin-top: 17.6%; margin-right: 5.5%;" data-aos="fade-up" data-aos-duration="500" data-aos-delay="200" data-disable-parallax-down="lg">
              <img class="rounded-3 mt-n5 mt-lg-0 d-block d-dark-mode-none" src="assets/Group5.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="border rounded-3 mt-n5 mt-lg-0 d-none d-dark-mode-block" src="assets/Group5.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
            <div class="flex-xxl-shrink-0" style="max-width: 600px;" data-aos="fade-up" data-aos-duration="500" data-aos-offset="250" data-disable-parallax-down="lg">
              <img class="rounded-3 d-block d-dark-mode-none" src="assets/Group6.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(65,81,98, .2);">
              <img class="border rounded-3 d-none d-dark-mode-block" src="assets/Group6.png" alt="Page" style="box-shadow: 1.875rem .625rem 5rem rgba(0,0,0, .2);"></div>
          </div>
        </div>
      </section>
      
      <!-- 출연진별-->
      <section class="container pt-5 mt-lg-3 mt-xl-4 mt-xxl-5">
        <h2 class="display-5 text-center pt-2 pt-sm-3 pt-md-4 pt-lg-5 pb-lg-3 mt-xxl-2 mb-0">출연진별 모아보기</h2>
        
        <div class="row align-items-center py-4 mt-2 mt-sm-3 mt-md-4 mb-2 mb-md-3 mb-lg-4" data-aos="fade-up" data-aos-duration="600" data-aos-offset="300" data-disable-parallax-down="md">
          <div class="col-md-6 col-lg-7 order-md-2 d-flex justify-content-end"><img class="d-dark-mode-none" src="assets/Group5.png" width="593" alt="Colors"><img class="d-none d-dark-mode-block" src="assets/Group5.png" width="593" alt="Colors"></div>
          <div class="col-md-6 col-lg-5 order-md-1 mt-md-n5" data-aos="fade-up" data-aos-duration="850" data-aos-offset="200" data-disable-parallax-down="md"><span class="badge fs-sm bg-faded-primary text-primary mb-4">콘텐츠 정보</span>
            <h2 class="mb-4">감독/출연진</h2>
            <p class="fs-lg mb-0 mb-lg-4">선택한 감독/배우 별로 영화를 저희가 정성을 다해 선택해드려요!</p>
          </div>
        </div>
        
      </section>
    
      <!-- 메일 -->
      <div class="container">
        <div class="bg-dark position-relative rounded-5 overflow-hidden px-4 pt-1 pb-2 py-sm-4 py-lg-5">
          <div class="d-none d-dark-mode-block position-absolute top-0 start-0 w-100 h-100" style="background-color: rgba(255,255,255, .02);"></div>
          <div class="position-absolute top-0 end-0 pe-5 zindex-2">
            <svg class="me-5" width="514" height="254" viewBox="0 0 514 254" fill="white" fill-opacity=".03" xmlns="http://www.w3.org/2000/svg">
              <ellipse cx="257" cy="0.5" rx="257" ry="253.5"></ellipse>
            </svg>
          </div>
          <div class="d-none d-lg-flex position-absolute start-0 bottom-0 ms-n4">
            <div data-aos="fade-left" data-aos-duration="700" data-aos-anchor-placement="bottom-bottom">  
              <svg class="text-primary" width="117" height="117" viewBox="0 0 117 117" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <circle cx="58.5" cy="58.5" r="58.5"></circle>
              </svg>
            </div>
            <div data-aos="fade-right" data-aos-duration="700" data-aos-anchor-placement="bottom-bottom">
              <svg class="text-warning" width="117" height="117" viewBox="0 0 117 117" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M-2.51516e-06 58.5C-3.52666e-06 70.0702 3.43096 81.3806 9.85902 91.0008C16.2871 100.621 25.4235 108.119 36.113 112.547C46.8025 116.975 58.5649 118.133 69.9128 115.876C81.2607 113.619 91.6844 108.047 99.8657 99.8657C108.047 91.6844 113.619 81.2607 115.876 69.9128C118.133 58.5649 116.975 46.8025 112.547 36.113C108.119 25.4235 100.621 16.2871 91.0009 9.85903C81.3806 3.43096 70.0702 -4.24071e-06 58.5 -5.11423e-06L58.5 58.5L-2.51516e-06 58.5Z"></path>
              </svg>
            </div>
          </div>
          <div class="dark-mode position-relative zindex-3 text-center py-5 my-xl-3 mx-auto" style="max-width: 565px;">
            <h2 class="display-5">메일 ㄱㄱ</h2>
            <p class="fs-lg pb-3 mb-3 mb-lg-4">구독할라믄 메일 ㄱㄱ</p>
            <form class="subscription-form validate mx-auto" action="https://studio.us12.list-manage.com/subscribe/post?u=c7103e2c981361a6639545bd5&amp;amp;id=29ca296126" method="post" name="mc-embedded-subscribe-form" target="_blank" novalidate style="max-width: 500px;">
              <div class="input-group"><span class="input-group-text"><i class="ai-mail"></i></span>
                <input class="form-control" type="email" name="EMAIL" placeholder="Enter your email" required id="subscr-email">
                <button class="btn btn-primary" type="submit" name="subscribe">제출</button>
              </div>
              <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
              <div style="position: absolute; left: -5000px;" aria-hidden="true">
                <input class="subscription-form-antispam" type="text" name="b_c7103e2c981361a6639545bd5_29ca296126" tabindex="-1">
              </div>
              <div class="subscription-status mx-auto"></div>
            </form>
          </div>
        </div>
      
    
      <footer class="footer py-4">
        <div class="container text-center py-3"><span class="text-muted">&copy; <span class='text-danger'>❤명인❤찬웅❤</span> by </span><a class="nav-link d-inline fw-normal p-0" href="https://createx.studio/" target="_blank" rel="noopener">Team HIVE</a></div>
      </footer>
    <!-- Back to top button-->
    <a class="btn-scroll-top" href="#top" data-scroll>
      <svg viewBox="0 0 40 40" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <circle cx="20" cy="20" r="19" fill="none" stroke="currentColor" stroke-width="1.5" stroke-miterlimit="10"></circle>
      </svg><i class="ai-arrow-up"></i>
    </a>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      darkMode: false
    };
  },
  components: {
    // 컴포넌트의 내용
  },
  mounted() {
   
  },
  methods: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      if (this.darkMode) {
        // 다크 모드 클래스를 추가
        document.body.classList.add('dark-mode');
      } else {
        // 다크 모드 클래스를 제거
        document.body.classList.remove('dark-mode');
      }
    },
    gotoLogin() {
      this.$router.push({name: 'LogInView'})
    }
  }
};
</script>

<style scoped>
.scroll-down-btn {
        display: inline-block;
        text-decoration: none;
      }
      .scroll-down-btn p {
        margin-top: 1.25rem;
        color: white;
        font-size: .875rem;
        font-weight: 500;
        letter-spacing: .375rem;
        text-indent: .375rem;
        animation: colorText 5s ease-out infinite, nudgeText 5s ease-out infinite;
      }
      .mouse {
        background: #2c333e linear-gradient(transparent 0%, transparent 50%, white 50%, white 100%);
        position: relative;
        width: 38px;
        height: 65px;
        margin: 0 auto;
        border-radius: 6rem;
        background-size: 100% 200%;
        animation: colorSlide 5s linear infinite, nudgeMouse 5s ease-out infinite;
      }
      .mouse:before, .mouse:after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        margin: auto;
      }
      .mouse:before {
        width: 34px;
        height: 61px;
        background-color: #121519;
        border-radius: 6rem;
      }
      .mouse:after {
        background-color: white;
        width: .375rem;
        height: .375rem;
        border-radius: 100%;
        animation: trackBallSlide 5s linear infinite;
      }
      @keyframes colorSlide {
        0% { background-position: 0% 100%; }
        20% { background-position: 0% 0%; }
        21% { background-color: #2c333e; }
        29.99% {
          background-color: white;
          background-position: 0% 0%;
        }
        30% {
          background-color: #2c333e;
          background-position: 0% 100%;
        }
        50% { background-position: 0% 0%; }
        51% { background-color: #2c333e; }
        59% {
          background-color: white;
          background-position: 0% 0%;
        }
        60% {
          background-color: #2c333e;
          background-position: 0% 100%;
        }
        80% { background-position: 0% 0%; }
        81% { background-color: #2c333e; }
        90%, 100% {
          background-color: white;
        }
      }
      @keyframes trackBallSlide {
        0% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        6% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        14% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        15%, 19% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        28%, 29.99% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        30% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        36% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        44% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        45%, 49% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        58%, 59.99% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        60% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
        66% {
          opacity: 1;
          transform: scale(0.9) translateY(5px);
        }
        74% {
          opacity: 0;
          transform: scale(0.4) translateY(40px);
        }
        75%, 79% {
          opacity: 0;
          transform: scale(0.4) translateY(-20px);
        }
        88%, 100% {
          opacity: 1;
          transform: scale(1) translateY(-20px);
        }
      }
      @keyframes nudgeMouse {
        0%, 30%, 60%, 90% { transform: translateY(0); }
        20%, 50%, 80% { transform: translateY(8px); }
      }
      @keyframes nudgeText {
        0%, 30%, 60%, 90% { transform: translateY(0); }
        20%, 50%, 80% { transform: translateY(2px); }
      }
      @keyframes colorText {
        21%, 51%, 81% { color: #2c333e; }
        30%, 60%, 90% { color: white; }
      }

</style>
