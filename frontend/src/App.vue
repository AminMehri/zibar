<template>
  <Navbar/>
  <router-view/>
  <Footer/>
</template>


<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'HomeView',
  components: {
    Navbar,
    Footer
  }
}
</script>



<style>	
@font-face {
  font-family: 'Vazir';
  src: url('@/assets/fonts/Vazir.woff2') format('woff2'),
         url('@/assets/fonts/Vazir.woff') format('woff'),
         url('@/assets/fonts/Vazir.ttf') format('truetype');
}

#app {
  font-family: Vazir;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #e2ffce;
}

a{
  text-decoration: none !important;
}

.bi-telegram:hover{
  color:#00f;transition-duration:.3s
}
.bi-instagram:hover{
  color:red;transition-duration:.3s
}
.bi-linkedin:hover{
  color:#00f;transition-duration:.3s
}
</style>
