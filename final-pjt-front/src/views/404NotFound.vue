<template>
  <div class="bg-gray">
    <main class="page-wrapper">
      <!-- Page content-->
      <div class="container overflow-hidden pb-5">
        <!-- Dangling lamp-->
        <div class="d-flex justify-content-center px-5 mt-n1"><img class="d-dark-mode-none" src="assets/img/404/lamp-light.png" width="348" alt="Lamp" style="transform-origin: 50% 0; animation: swinging 3.5s ease-in-out forwards infinite;"><img class="d-none d-dark-mode-block" src="assets/img/404/lamp-dark.png" width="348" alt="Lamp" style="transform-origin: 50% 0; animation: swinging 3.5s ease-in-out forwards infinite;"></div>
        <!-- Text + search bar-->
        <div class="d-flex justify-content-center pb-5 mb-md-2 mb-lg-3 mb-xl-4 mb-xxl-5">
          <div style="max-width: 420px;">
            <div class="d-none d-sm-block" style="margin-top: -127px;"></div>
            <div class="d-sm-none" style="margin-top: -25%;"></div>
            <div class="d-flex align-items-center mb-4">
              <h1 class="display-1 mb-0">404</h1>
              <p class="text-dark lead ps-4 mb-0">Whoops! That page is missing...</p>
            </div>
            
          </div>
        </div>
        <!-- Categories-->
        <h2 class="h4 text-center pb-lg-2 mb-4">Let's GAME!</h2>
        <div class="row g-4 pb-3 pb-lg-4 pb-xl-5">
          <div class="col-md-4">
            <!-- Card-->
            <div class="card zoom-effect h-100 border-0 rounded-1 overflow-hidden" style="min-height: 320px;"><span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
              <div class="zoom-effect-wrapper rounded-1 position-absolute top-0 start-0 w-100 h-100">
                <div class="zoom-effect-img bg-size-cover bg-position-bottom-center position-absolute top-0 start-0 w-100 h-100" style="background-image: url(assets/img/shop/categories/01.jpg);"></div>
              </div><a class="card-body d-flex flex-column justify-content-end align-items-start position-absolute top-0 start-0 w-100 h-100 text-decoration-none zindex-3" href="shop-catalog.html"><span class="bg-light text-dark rounded-pill fs-sm fw-semibold lh-1 py-3 px-4">For the living room</span></a>
            </div>
          </div>
          <div class="col-md-8">
            <!-- Card-->
            <div class="card zoom-effect border-0 rounded-1 overflow-hidden"><span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
              <div class="zoom-effect-wrapper rounded-1"><img class="zoom-effect-img" src="assets/img/shop/categories/02.jpg" alt="Category image"></div><a class="card-body d-flex flex-column justify-content-end align-items-start position-absolute top-0 start-0 w-100 h-100 text-decoration-none zindex-3" href="shop-catalog.html"><span class="bg-light text-dark rounded-pill fs-sm fw-semibold lh-1 py-3 px-4">For the kitchen</span></a>
            </div>
            <div class="row g-4 pt-4">
              <div class="col-sm-6">
                <!-- Card-->
                <div class="card zoom-effect border-0 rounded-1 overflow-hidden"><span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
                  <div class="zoom-effect-wrapper rounded-1"><img class="zoom-effect-img" src="assets/img/shop/categories/03.jpg" alt="Category image"></div><a class="card-body d-flex flex-column justify-content-end align-items-start position-absolute top-0 start-0 w-100 h-100 text-decoration-none zindex-3" href="shop-catalog.html"><span class="bg-light text-dark rounded-pill fs-sm fw-semibold lh-1 py-3 px-4">For the bathroom</span></a>
                </div>
              </div>
              <div class="col-sm-6">
                <!-- Card-->
                <div class="card zoom-effect border-0 rounded-1 overflow-hidden"><span class="position-absolute top-0 start-0 w-100 h-100 bg-dark opacity-10 zindex-2"></span>
                  <div class="zoom-effect-wrapper rounded-1"><img class="zoom-effect-img" src="assets/img/shop/categories/04.jpg" alt="Category image"></div><a class="card-body d-flex flex-column justify-content-end align-items-start position-absolute top-0 start-0 w-100 h-100 text-decoration-none zindex-3" href="shop-catalog.html"><span class="bg-light text-dark rounded-pill fs-sm fw-semibold lh-1 py-3 px-4">For the bedroom</span></a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    <!-- <div class="container">
      <h1>404</h1>
      <a class="personBox" href="" data-fancybox  data-src="#brick">
        아랑랑
      </a>
      <div id="brick" style="display:none;width:70%; height: 80%;">
        <canvas class="pt-5" id="myCanvas" width="480" height="320"></canvas>
        <br>
        <div class="d-flex justify-content-between" style="width: 30%;">
          <button class="btn btn-success" style="width: 30%;"  @click="brickgamestart">게임 시작</button>
          <button class="btn btn-danger" style="width: 30%;" @click="brickgameEnd" >게임 끝!</button>

        </div>
      </div>
      <TwoZeroView />
    </div> -->
  </div>
</template>

<script>
// import TwoZeroView from '@/components/game/TwoZeroView.vue'

export default {
  name:"404NotFound",
  components: {
    // TwoZeroView
  },
  methods: {
    brickgamestart() {
      var canvas = document.getElementById("myCanvas");
      var ctx = canvas.getContext("2d");
      var ballRadius = 10;
      var x = canvas.width/2;
      var y = canvas.height-30;
      var dx = 2;
      var dy = -2;
      var paddleHeight = 10;
      var paddleWidth = 75;
      var paddleX = (canvas.width-paddleWidth)/2;
      var rightPressed = false;
      var leftPressed = false;
      var brickRowCount = 5;
      var brickColumnCount = 3;
      var brickWidth = 75;
      var brickHeight = 20;
      var brickPadding = 10;
      var brickOffsetTop = 30;
      var brickOffsetLeft = 30;
      var score = 0;
      var lives = 3;

      var bricks = [];
      for(var c=0; c<brickColumnCount; c++) {
        bricks[c] = [];
        for(var r=0; r<brickRowCount; r++) {
          bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
      }

      document.addEventListener("keydown", keyDownHandler, false);
      document.addEventListener("keyup", keyUpHandler, false);
      document.addEventListener("mousemove", mouseMoveHandler, false);

      function keyDownHandler(e) {
          if(e.key == "Right" || e.key == "ArrowRight") {
              rightPressed = true;
          }
          else if(e.key == "Left" || e.key == "ArrowLeft") {
              leftPressed = true;
          }
      }

      function keyUpHandler(e) {
          if(e.key == "Right" || e.key == "ArrowRight") {
              rightPressed = false;
          }
          else if(e.key == "Left" || e.key == "ArrowLeft") {
              leftPressed = false;
          }
      }

      function mouseMoveHandler(e) {
        var relativeX = e.clientX - canvas.offsetLeft;
        if(relativeX > 0 && relativeX < canvas.width) {
          paddleX = relativeX - paddleWidth/2;
        }
      }
      function collisionDetection() {
        for(var c=0; c<brickColumnCount; c++) {
          for(var r=0; r<brickRowCount; r++) {
            var b = bricks[c][r];
            if(b.status == 1) {
              if(x > b.x && x < b.x+brickWidth && y > b.y && y < b.y+brickHeight) {
                dy = -dy;
                b.status = 0;
                score++;
                if(score == brickRowCount*brickColumnCount) {
                  alert("YOU WIN, CONGRATS!");
                  document.location.reload();
                }
              }
            }
          }
        }
      }

      function drawBall() {
        ctx.beginPath();
        ctx.arc(x, y, ballRadius, 0, Math.PI*2);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
      }
      function drawPaddle() {
        ctx.beginPath();
        ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);
        ctx.fillStyle = "#0095DD";
        ctx.fill();
        ctx.closePath();
      }
      function drawBricks() {
        for(var c=0; c<brickColumnCount; c++) {
          for(var r=0; r<brickRowCount; r++) {
            if(bricks[c][r].status == 1) {
              var brickX = (r*(brickWidth+brickPadding))+brickOffsetLeft;
              var brickY = (c*(brickHeight+brickPadding))+brickOffsetTop;
              bricks[c][r].x = brickX;
              bricks[c][r].y = brickY;
              ctx.beginPath();
              ctx.rect(brickX, brickY, brickWidth, brickHeight);
              ctx.fillStyle = "#0095DD";
              ctx.fill();
              ctx.closePath();
            }
          }
        }
      }
      function drawScore() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Score: "+score, 8, 20);
      }
      function drawLives() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#0095DD";
        ctx.fillText("Lives: "+lives, canvas.width-65, 20);
      }

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawBricks();
        drawBall();
        drawPaddle();
        drawScore();
        drawLives();
        collisionDetection();

        if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
          dx = -dx;
        }
        if(y + dy < ballRadius) {
          dy = -dy;
        }
        else if(y + dy > canvas.height-ballRadius) {
          if(x > paddleX && x < paddleX + paddleWidth) {
            dy = -dy;
          }
          else {
            lives--;
            if(!lives) {
              alert("GAME OVER");
              document.location.reload();
            }
            else {
              x = canvas.width/2;
              y = canvas.height-30;
              dx = 3;
              dy = -3;
              paddleX = (canvas.width-paddleWidth)/2;
            }
          }
        }

        if(rightPressed && paddleX < canvas.width-paddleWidth) {
          paddleX += 7;
        }
        else if(leftPressed && paddleX > 0) {
          paddleX -= 7;
        }

        x += dx;
        y += dy;
        requestAnimationFrame(draw);
      }

      draw();
    },
    brickgameEnd() {
      this.$router.go(this.$router.currentRoute)
    }
  },
}
</script>

<style scoped>
  * { padding: 0; margin: 0; }
  canvas { background: #eee; display: block; margin: 0 auto; }

  #brick {
    display: flex;
    flex-direction: column; /* arrage items on top of the other */
    justify-content: center;
    align-items: center;
  }
</style>