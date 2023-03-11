<template>

  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>
  
  <div class="about">
    <div class="container my-5 p-3 border rounded shadow bg-white">
      <h3 class="text-center"> درباره ما </h3>
      <hr class="col-6 mx-auto">
      <div class="row p-5" dir="rtl">
        <div class="col-12 col-xl-6">
          <img src="@/assets/Travel_plans_Outline.svg" class="w-100" alt="حمل و نقل آنلاین زیبار">
        </div>
        <div class="col-12 col-xl-6 pt-4">
          <p class="fs-4">
            <strong>وب سایت زیبار</strong> از سال 1400 توسط <strong>کارگزاری حمل و نقل ضیائی</strong> ایجاد گردید تا شاید بتواند کمک کوچکی در زمینه <em>اتصال رانندگان به متصدیان بار</em> به عمل آورد. این سامانه، مشکلاتی که در مسیر این مهم بود را تسهیل کرده و <strong>سریع، امن و مطمئن</strong> است. امروزه خوشحال هستیم که میتوانیم به صد ها راننده خدمات ارائه دهیم و مسیر <strong>حمل و نقل</strong> را برایشان آسان سازیم.
          </p>
        </div>
      </div>
      <div class="row">
            
        <div class="col-md-4 text-center">
          <h3 class="text-success">کارگزاری حمل و نقل ضیائی</h3>
          <p> شرکت حمل و نقل ضیائی در سال 1380 به مدیریت <strong>حمیدرضا ضیائی</strong> ایجاد گردید. در این مدت ما مفتخریم که بیش از هزاران بار را به اقصی و نقاط جهان ارسال کرده ایم. اگر میخواهید بارهای خود را منتقل کنید، میتوانید به ما <strong>اعتماد</strong> کنید.. <a class="fw-bold text-primary" href="https://ziatc.ir" target="_blank" title="کارگزاری حمل و نقل ضیائی">ارسال بار توسط ما</a></p>
        </div>
        <div class="col-md-4"></div>
        <div class="col-md-4 text-center">
          <h3 class="text-success">گروه تلگرامی زیبار</h3>
          <p>خدمات زیبار تنها به این سایت ختم نمیشود. <strong>گروه تلگرامی</strong> ما به صورت شبانه روزی شما رانندگان محترم را در جریان بارهای جدید قرار میدهد. همچنین متصدیان عزیز نیز میتوانند با مراجعه به گروه تلگرامی زیبار <em>آگهی های بار</em> خود را درج نمایند. <a class="fw-bold text-primary" href="https://telegram.me/zibar_ir" target="_blank" title="شبکه های اجتماعی">گروه تلگرام زیبار</a> </p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { useMeta } from 'vue-meta'

export default {
  setup () {
    useMeta({
      title: "درباره ما | زیبار",
      description: "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      robots: "index, follow",
      keywords: "حمل و نقل آنلاین, حمل و نقل, زیبار, سامانه حمل و نقل",
      googlebot: "index, follow",
      author: "مهدی حدادزاده",
      owner: "امیرحسام ضیایی",
      canonical: "https://zibar.ir/about",
      'og:type': "about-zibar",
      'og:title': "zibar",
      'og:description': "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      'og:site_name': "زیبار",
      'og:url': "https://zibar.ir/about",
      // 'og:image': "https://zibar.ir/media/image.jpg",
      'twitter:title': "زیبار",
      'twitter:description': "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      // 'twitter:image': "https://zibar.ir/media/image.jpg",
    });
  }
}
</script>