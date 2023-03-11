<template>

  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>
  
  <div class="home">
    <header class="header p-md-5">
      <div class="container-md" id="header">
        <div class="row g-0" dir="ltr">

          <div class="col-lg-7">
            <img class="img-fluid justify-content-center w-75" src="@/assets/Travel_plans_Monochromatic.svg" alt="حمل و نقل زیبار">
          </div>

          <div class="col-lg-5" dir="rtl">
            <h1 class="header-h1">حمل و نقل بار با زیبار</h1>
            <p class="header-text">زیبار این افتخار را دارد که هر روزه خدمات خود را به رانندگان و شرکت های حمل و نقل ارائه دهد و با صرفه جویی در زمان، نقطه اتصال بین شرکت ها و رانندگان باشد. زیبار همواره تلاش کرده است که تکیه گاه محکمی برای شما باشد و کمی از دردسر های گرفتن بار بکاهد. سامانه اعلام بار زیبار تلاش میکند در عین سادگی، ظرافت و بدون فوت وقت، بستری محکم و قابل اطمینان برای تمامی کاربران خود باشد. .</p>
            <div class="d-md-flex justify-content-between">
              <a href="https://app.zibar.ir" title="وب اپلیکیشن زیبار"><button class="btn btn-outline-dark my-1">ورود به اپلیکیشن اعلام بار زیبار</button></a>
              <a href="https://ziatc.ir" title="ارسال بار با زیبار"><button class="btn btn-outline-dark my-1">ارسال بار به سراسر کشور با زیبار</button></a>
            </div>

            <div class="row mt-3">
                <div class="d-flex justify-content-center">
                  <a class="social-media-insta text-white" target="_blank" title="صفحه اینستاگرام زیبار" href="https://instagram.com/ziatc.ir">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                      width="40" 
                      height="40" 
                      fill="currentColor" 
                      class="bi bi-instagram" 
                      viewBox="0 0 16 16">
                      <path d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"/>
                    </svg>
                  </a>

                  <a class="social-media-tele text-white" target="_blank" title="گروه تلگرام زیبار" href="https://telegram.me/zibar_ir">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                        width="40" 
                        height="40" 
                        fill="currentColor" 
                        class="bi bi-telegram mx-2" 
                        viewBox="0 0 16 16">
                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
                    </svg>
                  </a>

                  <a class="social-media-lined text-white" target="_blank" title="صفحه لینکدین زیبار" href="https://www.linkedin.com/company/ziaeitc/mycompany/">
                    <svg xmlns="http://www.w3.org/2000/svg"
                        width="40" 
                        height="40" 
                        fill="currentColor" 
                        class="bi bi-linkedin" 
                        viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>
                  </a>
                </div>
              </div>
              <p class="d-flex justify-content-center my-3">
                  زیبار را در <strong>شبکه های اجتماعی</strong> دنبال کنید.
              </p>
            
          </div>
        </div>
      </div>
    </header>

    <section class="container my-5">
      <div class="row">
          
        <div class="col-md-4 text-center">
          <h2 class="text-success">برای رانندگان</h2>
          <p>رانندگان محترم: شما میتوانید به راحتی بین صدها باری که در <strong>وب سایت اعلام بار زیبار</strong> قرار گرفته است، <strong>مقایسه کنید،</strong> <strong>مقصد مورد نظر خود را انتخاب کنید</strong> و بار مورد نظر خود را برگزینید. </p>
        </div>

        <div class="col-md-4"></div>

        <div class="col-md-4 text-center">
          <h3 class="text-success">برای متصدیان</h3>
          <p><strong>تعداد کاربران بالای زیبار</strong> و همچنین اعلام بار شما در <strong>بزرگترین گروه های حمل و نقل شبکه های اجتماعی،</strong> باعث میشود که تعداد زیادی از رانندگان آگهی شما را ببینند و در <strong>سریع ترین زمان ممکن</strong> هدف شما را محقق سازند.</p>
        </div>

      </div>
    </section>


    <section class="container">
      <div class="row text-center">

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">ساده</h3>
            <p class="card-body">زیبار با <strong>طراحی ظریف و ساده</strong> خود، شما را از وجود هرگونه سردرگمی به دور میدارد و امکان استفاده از تمام ابزارهای موجود را به شما میدهد.</p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">مطمئن</h3>
            <p class="card-body">زیبار از تمام کاربران خود میخواهد که <strong>احراز هویت</strong> کنند. این کار ضمن اینکه به <strong>سرعت</strong> انجام میگیرد، باعث <strong>کوتاه شدن دست سودجویان</strong> میشود.  </p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">اختصاصی</h3>
            <p class="card-body">زیبار به جای ارائه خدمات کم کیفیت از سراسر کشور، تمرکز خود را بر <strong>مبدا خراسان بزرگ</strong> گذاشته و سعی میکند <strong>بهترین عملکرد</strong> را در این استان ارائه دهد.</p>
          </div>
        </div>

      </div>

      <div class="row text-center mt-4">

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">سریع</h3>
            <p class="card-body">زیبار این امکان را به شما میدهد که بتوانید در <strong>حداقل زمان</strong> ممکن، <strong>بهترین نتیجه</strong> را دریافت کنید.</p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">شفاف</h3>
            <p class="card-body">زیبار اطلاعات بارها را به صورت <strong>شفاف</strong> به شما نشان میدهد و در را بر روی هرگونه <strong>ابهام</strong> میبندد.</p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card p-3 shadow" id="benifits">
            <h3 class="card-title">متنوع</h3>
            <p class="card-body">زیبار شما را با <strong>دنیایی از فرصت ها</strong> روبرو میسازد که میتوانید از بین آنها، <strong>بهترین</strong> را برای خود برگزینید.</p>
          </div>
        </div>

      </div>
    </section>
    
    <section>
      <div class="container-fluid mt-5">
        <hr class="w-75 mx-auto">
        <h3 class="text-center">چگونگی استفاده از زیبار</h3>
        <div class="row align-items-center gx-0 p-3">

          <div class="col-12 col-xl-6 d-flex align-items-center fs-5">
            <div class="col-12 col-md-8 mx-auto me-xl-auto">
              <h1>
                پروفایل:
              </h1>
              <p>
                با رفتن به بخش پروفایل وب اپلیکیشن زیبار میتوانید اطلاعات خود را مشاهده نمایید. قبل هر کاری شما میبایست <strong>احراز هویت</strong> کنید. پس از ثبت اطلاعات خود، همکاران ما در سریع ترین زمان ممکن اطلاعات شما را بررسی خواهند کرد و از <strong>صحت آنها اطمینان پیدا خواهند کرد.</strong> دقت کنید که این کار با <strong>سامانه های رسمی سازمان حمل و نقل</strong> انجام خواهد شد. پس قبل از تایید اطلاعات از <strong>درستی</strong> آنها اطمینان حاصل فرمایید. <br> <strong>قوانین استفاده از سامانه:</strong> حتما قوانین را با دقت مطالعه فرمایید تا از بروز هرگونه سوء تفاهم جلوگیری شود.
              </p>
            </div>
          </div>

          <div class="col-12 col-xl-6 row">
            <div class="col-10 col-sm-8 col-md-6 col-xl-10 col-xxl-8 mx-auto">
              <img class="w-100" src="@/assets/profile.png" alt="پروفایل زیبار">
            </div>
          </div>

        </div>

        <div class="row align-items-center gx-0 p-3">

          <div class="col-12 col-xl-6 row">
            <div class="col-10 col-sm-8 col-md-6 col-xl-10 col-xxl-8 mx-auto">
              <img class="w-100" src="@/assets/show_bar.png" alt="سالن اعلام بار زیبار">
            </div>
          </div>

          <div class="col-12 col-xl-6 d-flex align-items-center fs-5">
            <div class="col-12 col-md-8 mx-auto me-xl-auto">
              <h1>
                سالن اعلام بار:
              </h1>
              <p> در این بخش شما میتوانید بار های موجود را مشاهده نمایید و بر اساس نیاز های خود، <strong>فیلتر</strong> کنید. شما همچنین میتوانید <strong>بار های پیشنهادی ما</strong> را در قالب <strong>بار های ویژه</strong> مشاهده نمایید. دقت کنید اگر <strong>احراز هویت نکرده باشید،</strong> نخواهید توانست <strong>جزئیات</strong> بیشتری از بارها را مشاهده کنید.</p>
            </div>
          </div>

          <div class="col-12 col-xl-6 d-flex align-items-center fs-5">
            <div class="col-12 col-md-8 mx-auto me-xl-auto">
              <h1>
                ثبت بار:
              </h1>
              <p>این بخش مخصوص <strong>متصدیان بار</strong> است و <strong>رانندگان نمیتوانند</strong> این قسمت را مشاهده نمایند. متصدیان عزیز نیز قادر خواهند بود که <strong>بدون محدودیت</strong> بار های خود را ثبت کنند. دقت کنید که پرکردن تمام قسمت هایی که دارای ستاره (*) هستند <strong>الزامی</strong> میباشند.</p>
            </div>
          </div>

          <div class="col-12 col-xl-6 row">
            <div class="col-10 col-sm-8 col-md-6 col-xl-10 col-xxl-8 mx-auto">
              <img class="w-100" src="@/assets/add_bar.png" alt="ثبت بار در زیبار">
            </div>
          </div>

        </div>

        <div class="row align-items-center gx-0 p-3">

          <div class="col-12 col-xl-6 row">
            <div class="col-10 col-sm-8 col-md-6 col-xl-10 col-xxl-8 mx-auto">
              <img class="w-100" src="@/assets/history.png" alt="تاریخچه بار ها در زیبار">
            </div>
          </div>

          <div class="col-12 col-xl-6 d-flex align-items-center fs-5">
            <div class="col-12 col-md-8 mx-auto me-xl-auto">
              <h1>
                تاریخچه بارها:
              </h1>
              <p>در این بخش <strong>رانندگان</strong> میتوانند بارهایی که تابحال قبول کرده اند را مشاهده کنند. همچنین <strong>متصدیان</strong> هم قادرند علاوه بر <strong>تاریخچه بار های ارسال شده،</strong> <strong>بار های در انتظار پذیرش راننده</strong> و <strong>پذیرفته شده توسط راننده</strong> را مشاهده کنند. بار هایی که هنوز پذیرش نشده باشند، <strong>قابلیت ویرایش و لغو خواهند داشت.</strong> در صورت پذیرش بار توسط راننده با بردن <strong>نمایشگر ماوس کامپیوتر</strong> خود بر روی آن، قادر خواهید بود <strong>اطلاعات راننده</strong> را مشاهده کنید.</p>
            </div>
          </div>

        </div>

      </div>
    </section>

    <section class="container">
      <div class="container bootstrap snippets bootdeys">
        <div class="row d-flex">
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="blue" data-radius="none">
                <div class="content">
                  <h6 class="category">گروه تلگرامی  زیبار</h6>
                  <p class="description">رانندگان عزیز میتوانند در این گروه تعداد بسیار زیادی از اگهی های اعلام بار که از تمامی گروه های اعلام بار موجود در تلگرام جمع آوری میشود را مشاهده کنند.</p>
                  <h4 class="title"><a href="http://telegram.me/zibar_group">ورود به گروه اعلام بار تلگرام زیبار</a></h4>
                </div>
              </div> <!-- end card -->
            </div>
          </div>
            
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="green" data-radius="none">
                <div class="content">
                  <h6 class="category">کانال تلگرام زیبار</h6>
                  <p class="description">شرکت ها و متصدیان گرامی میتوانند در این کانال اعلام بار کنند. تفاوت این کانال با کانال های مشابه در این است که اعلام بار شما در این کانال در ده ها گروه اعلام بار سراسری و استانی منتشر خواهد شد و بازده بسیار بالایی را به همراه خواهد داشت.</p>
                  <h4 class="title"><a href="https://telegram.me/zibar_ir">ورود به کانال تلگرام زیبار</a></h4>
                </div>
              </div> <!-- end card -->
            </div>
          </div>
            
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="yellow" data-radius="none">
                <div class="content">
                  <h6 class="category">ربات زیبار</h6>
                  <p class="description">ربات همه کاره زیبار به شما این امکان را میدهد که جدید ترین بارهای ثبت شده در وب اپلیکیشن زیبار را مشاهده کنید. وهمچنین میتوانید اعلام بار خود را نیز به وسیله این ربات در سایت زیبار به انجام برسانید. </p>
                  <h4 class="title"><a href="https://telegram.me/barbary_bot">ورود به ربات تلگرام زیبار</a></h4>
                </div>
              </div> <!-- end card -->
            </div>
          </div>
            
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="brown" data-radius="none">
                <div class="content">
                  <h6 class="category">وب اپلیکیشن زیبار</h6>
                  <p class="description">رانندگان و متصدیان بزرگوار, شما میتوانید با عضویت کاملا رایگان در وب اپلیکیشن زیبار به راحتی اعلام بار کنید و جدید ترین بارهای ثبت شده را مشاهده نمایید.</p>
                  <h4 class="title"><a href="https://app.zibar.ir/">ورود به وب اپلیکیشن زیبار</a></h4>
                </div>
              </div> <!-- end card -->
            </div>
          </div>
            
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="purple" data-radius="none">
                <div class="content">
                  <h6 class="category">اپلیکیشن اندروید زیبار برای  متصدیان</h6>
                  <p class="description">متصدیان محترم با نصب اپلیکیشن زیبار برای متصدیان میتوانند به خدماتی از قبیل اعلام بار به صورت رایگان دسترسی پیدا کنند.</p>
                  <h4 class="title"><a href="https://myket.ir/app/ir.zibar.app"><img src="@/assets/myket.png" alt="دانلود نرم افزار زیبار از مایکت" width="150" height="50"></a></h4>
                  <h4 class="title"><a href="https://cafebazaar.ir/app/ir.zibar.app"><img src="@/assets/bazar.png" alt="دانلود نرم افزار زیبار از بازار" width="150" height="50"></a></h4>
                  <h4 class="title"><a href="https://myket.ir/get/app?packageName=ir.zibar.app">دانلود مستقیم</a></h4>
                </div>
              </div> <!-- end card -->
            </div>
          </div>
            
          <div class="col-lg-4 col-md-6 col-sm-6 col-12m content-card">
            <div class="card-big-shadow">
              <div class="card card-just-text p-md-4 p-sm-2 p-1" data-background="color" data-color="orange" data-radius="none">
                <div class="content">
                  <h6 class="category">گروه واتساپ زیبار</h6>
                  <h4 class="title"><a href="#">به زودی</a></h4>
                  <p class="description"></p>
                </div>
              </div> <!-- end card -->

            </div>
          </div>
        </div>
      </div>
    </section>
    
  </div>
</template>

<script>
import { useMeta } from 'vue-meta'

export default {
  setup () {
    useMeta({
      title: "اعلام بار هوشمند رانندگان و متصدیان | زیبار",
      description: "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      robots: "index, follow",
      keywords: "حمل و نقل آنلاین, حمل و نقل, زیبار, سامانه حمل و نقل",
      googlebot: "index, follow",
      author: "مهدی حدادزاده",
      owner: "امیرحسام ضیایی",
      canonical: "https://zibar.ir/",
      'og:type': "zibar",
      'og:title': "zibar",
      'og:description': "پلتفرم نوپا زیبار با امکانات فراوان برای تسهیل اعلام و دریافت بار توسط شرکت های حمل و نقل و رانندگان عزیز پا به عرصه وجود گذاشته است.",
      'og:site_name': "زیبار",
      'og:url': "https://zibar.ir/",
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

<style scoped>
.header{
  background-color: rgb(114, 180, 15);
}
.header-h1{
  font-size: 48px;
  font-weight: 700;
}
.header-text{
  text-align: justify;
  text-justify: inter-word;
}

#benifits{
  background-color: #b5ff86;
}

/* cards */
.card .description {
    font-size: 16px;
    color: #66615b;
}
.content-card{
    margin-top:30px;    
}
a:hover, a:focus {
    text-decoration: none;
}

/*======== COLORS ===========*/
.card[data-color="blue"] {
    background: #b8d8d8;
}
.card[data-color="blue"] .description {
    color: #506568;
}

.card[data-color="green"] {
    background: #d5e5a3;
}
.card[data-color="green"] .description {
    color: #60773d;
}
.card[data-color="green"] .category {
    color: #92ac56;
}

.card[data-color="yellow"] {
    background: #ffe28c;
}
.card[data-color="yellow"] .description {
    color: #b25825;
}
.card[data-color="yellow"] .category {
    color: #d88715;
}

.card[data-color="brown"] {
    background: #d6c1ab;
}
.card[data-color="brown"] .description {
    color: #75442e;
}
.card[data-color="brown"] .category {
    color: #a47e65;
}

.card[data-color="purple"] {
    background: #baa9ba;
}
.card[data-color="purple"] .description {
    color: #3a283d;
}
.card[data-color="purple"] .category {
    color: #5a283d;
}

.card[data-color="orange"] {
    background: #ff8f5e;
}
.card[data-color="orange"] .description {
    color: #772510;
}
.card[data-color="orange"] .category {
    color: #e95e37;
}
.card-big-shadow {
    max-width: 320px;
    position: relative;
}

.coloured-cards .card {
    margin-top: 30px;
}

.card[data-radius="none"] {
    border-radius: 0px;
}
.card {
    border-radius: 8px;
    box-shadow: 0 2px 2px rgba(204, 197, 185, 0.5);
    background-color: #FFFFFF;
    color: #252422;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
}

.card.card-just-text .content {
    /* padding: 50px 65px; */
    text-align: center;
}
.card .content {
    padding: 20px 20px 10px 20px;
}
.card[data-color="blue"] .category {
    color: #7a9e9f;
}

.card .category, .card .label {
    font-size: 14px;
    margin-bottom: 0px;
}
.card-big-shadow:before {
  background-image: url("http://static.tumblr.com/i21wc39/coTmrkw40/shadow.png");
  background-position: center bottom;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  bottom: -12%;
  content: "";
  display: block;
  left: -12%;
  position: absolute;
  right: 0;
  top: 0;
  z-index: 0;
}
/* end cards */
</style>