<template>
  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>

  <div class="contact-us">
    <div class="container">
      <div class="row">
        <div class="col-md-8 mx-auto">
          <p class="fs-5 mt-3">شما میتوانید از طریق فرم زیر با ما در ارتباط. لطفا انتقادات و پیشنهاد های خود را به ما منتقل کرده و زمینه پیشرفت ما را فراهم سازید. همچنین میتوانید از طریق ایمیل و شماره همراه زیر نیز با ما ارتباط برقرار کنید.</p>
        </div>
      </div>
      <section class="my-4 border p-5 shadow">

        <div class="row">

          <div class="col-md-9 mb-md-0 mb-5">
            <form id="contact-form">

              <div class="row" >


                <div class="col-md-6">
                  <div class="form-floating mb-3">
                    <input v-model="fullName" type="name" class="form-control" id="nameInput" placeholder="example">
                    <label for="nameInput">نام و نام خانوادگی</label>
                  </div>
                </div>

                <div class="col-md-6">
                    <div class="form-floating mb-3">
                        <input v-model="email" type="email" class="form-control" id="emailInput" placeholder="name@example.com">
                        <label for="emailInput">ایمیل / شماره تلفن</label>
                    </div>
                </div>

              </div>

              <div class="row">
                <div class="col-md-12">
                  <div class="form-floating mb-3">
                    <input v-model="subject" type="text" class="form-control" id="subjectInput" placeholder="example">
                    <label for="subjectInput">موضوع</label>
                  </div>
                </div>
              </div>

              <div class="row">

                <div class="col-md-12">

                  <div class="form-floating mb-3">
                    <textarea v-model="content" class="form-control" placeholder="Leave a message here" id="textareaInput" style="height: 100px"></textarea>
                    <label for="textareaInput">پیام</label>
                  </div>

                </div>
              </div>

            </form>

            <div class="text-center text-md-left">
                <a @click="sendMessage()" class="btn btn-primary">ارسال</a>
            </div>
            <div class="status"></div>
          </div>

          <div class="col-md-3 text-center">
            <ul class="list-unstyled mb-0">
              <li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
                <p>خراسان رضوی، مشهد، پایانه بار مشهد، سالن ۱، غرفه ۲۰۹، کارگزاری حمل و نقل ضیائی</p>
              </li>

              <li dir="ltr"><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-telephone-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/></svg>
                <a class="d-block my-1" href="tel:+989151113523" title="تماس با زیبار">+ 98 915 111 3523</a>
              </li>

              <li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor" class="bi bi-envelope-fill" viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/></svg>
                <a class="d-block my-1" href="mailto:info@zibar.ir" title="تماس با زیبار">info@zibar.ir</a>
              </li>
            </ul>
          </div>

        </div>
      </section>
    </div>
  </div>
</template>


<script>
import Swal from 'sweetalert2'
import { ref } from "vue";
import axios from 'axios'
import { useMeta } from 'vue-meta'

export default {
  setup () {
    useMeta({
      title: "تماس با ما | زیبار",
      description: "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      robots: "index, follow",
      keywords: "حمل و نقل آنلاین, حمل و نقل, زیبار, سامانه حمل و نقل",
      googlebot: "index, follow",
      author: "مهدی حدادزاده",
      owner: "امیرحسام ضیایی",
      canonical: "https://zibar.ir/contact-us",
      'og:type': "contact-zibar",
      'og:title': "zibar",
      'og:description': "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      'og:site_name': "زیبار",
      'og:url': "https://zibar.ir/contact-us",
      // 'og:image': "https://zibar.ir/media/image.jpg",
      'twitter:title': "زیبار",
      'twitter:description': "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      // 'twitter:image': "https://zibar.ir/media/image.jpg",
    });
    let fullName = ref('')
    let email = ref('')
    let subject = ref('')
    let content = ref('')


    function sendMessage() {
      if(document.getElementById('nameInput').value.length != 0 && document.getElementById('emailInput').value.length != 0 && document.getElementById('subjectInput').value.length != 0 && document.getElementById('textareaInput').value.length != 0){
        axios
          .post('ContactUs/', {
            'full_name': fullName.value,
            'email': email.value,
            'subject': subject.value,
            'content': content.value,
          })
          .then(response => {
            console.log(fullName.value);
            console.log(email.value);
            console.log(subject.value);
            console.log(content.value);
            Swal.fire({
              title: 'هورا!',
              text:   "پیام شما با موفقیت ارسال شد.",
              icon: 'success',
            });

            fullName.value = '';
            email.value = '';
            subject.value = '';
            content.value = '';
          })
          .catch(error => {
            console.log(error);
            console.log(fullName.value);
            console.log(email.value);
            console.log(subject.value);
            console.log(content.value);
          })

      }else {
        Swal.fire({
          title: '',
          text:   "لطفا تمام فیلد های مورد نیاز را به درستی تکمیل فرمایید.",
          icon: 'warning',
        });
      }
        
    }


    return{
      sendMessage,
      fullName,
      email,
      subject,
      content
    }
  }
}
</script>
