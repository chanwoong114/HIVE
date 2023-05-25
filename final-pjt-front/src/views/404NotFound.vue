<template>
  <div class="bg-gray">
    <div class="container">
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
    </div>
  </div>
</template>

<script>
import TwoZeroView from '@/components/game/TwoZeroView.vue'

export default {
  name:"404NotFound",
  components: {
    TwoZeroView
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