<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <button class="navbar-toggler bg-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <ul class="collapse navbar-collapse navbar-nav ms-auto mb-2 mb-lg-0" id="navbarTogglerDemo03">
        <li class="nav-item">
          <router-link class="nav-link" to="/">صفحه اصلی</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/about">درباره ما</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/contact-us">تماس با ما</router-link>
        </li>
      </ul>
      <router-link to="/">
        <img src="@/assets/zibar-logo.webp" id="logo-img" alt="زیبار">
      </router-link>
    </div>
  </nav>
</template>

<style scoped>
nav {
  padding: 5px;
  background-color: #000000;
}

nav a {
  font-weight: bold;
  color: #ccc;
}

nav a:hover {
  color: #72c209;
}
nav a.router-link-exact-active {
  color: #42b983;
}
#logo-img{
  width: 50px;
}
</style>
