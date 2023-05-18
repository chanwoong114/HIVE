<template>
  <div>
    <h1>home</h1>

    <video width="100%" height="auto" autoplay loop playsinline muted>
      <source src="../assets/movie.mp4"  type="video/mp4">
    </video>
    <div class="inss">
      <div>
        <!-- <h1>HIVE</h1> -->
      </div>
      <div class="image-container">
        <img src="../assets/bighive.png" class="shaking-image" />
        
      </div>
      <div class="inss-box">
        <LogInView/>
      </div>
    </div>
    
    
    <router-link to="/signup">
      <button>signup</button>
    </router-link>

  </div>
</template>

<script>
import LogInView from '@/views/LogInView.vue'

export default {
  components: {
    LogInView
  }
}
</script>

<style scoped>
video {
  -o-object-fit: cover;
  object-fit: cover;
  position: absolute;
  height: 100%;
  width: 100%;
  overflow: hidden;
  top: 0;
  left: 0;
  z-index: 0;
}

.inss {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1;
}

.image-container {
  position: absolute;
  top: -200px; /* 조정 가능한 값 */
}

.shaking-image {
  width: 250px;
  height: 200px;
  animation: shake 1.5s infinite;
}

@keyframes shake {
  0% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(5px);
  }
  100% {
    transform: translateX(-5px);
  }
}

.inss-box {
  background-color: rgba(255, 255, 255, 0.384);
  padding: 30px;
  border-radius: 30px;
}
</style>
