<template>
  <client-only>
    <html
      data-wf-page="5f322f74eb6b4d4ac650a23f"
      data-wf-site="5f322f74eb6b4d7e4650a23e"
    >
      <head>
        <meta charset="utf-8" />
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous"
        />
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
          crossorigin="anonymous"
        />
      </head>
      <body>
        <div class="div-block">
          <a
            href="/"
            aria-current="page"
            class="link-block w-inline-block w--current"
            ><img
              src="../components/student/images/logo.jpg"
              width="200"
              alt=""
          /></a>
          <div class="columns w-row">
            <div class="column-2 w-col w-col-6">
              <div class="div-block-10">
                <h1 class="heading-2">
                  <strong class="bold-text-3"
                    >Ready to start teaching on TutorPal? Here&#x27;s the
                    breakdown:</strong
                  >
                </h1>
                <div class="div-block-5">
                  <img
                    src="../components/registration/images/profile.png"
                    width="38"
                    alt=""
                  />
                  <div class="div-block-6">
                    <h1 class="heading-3">
                      <strong class="bold-text-2">Create a profile</strong>
                    </h1>
                    <p class="paragraph">
                      Fill out all the forms and be as detailed as possible.
                    </p>
                  </div>
                </div>
                <div class="div-block-5-copy">
                  <img
                    src="../components/registration/images/gear-1.png"
                    width="38"
                    alt=""
                  />
                  <div class="div-block-6">
                    <h1 class="heading-3">
                      <strong class="bold-text-2">Do your best work</strong>
                    </h1>
                    <p class="paragraph">
                      Accept a student request, join the call, and tutor!
                    </p>
                  </div>
                </div>
                <div class="div-block-5-copy">
                  <img
                    src="../components/registration/images/payment.png"
                    width="38"
                    srcset="
                      ../components/registration/images/payment-p-500.png 500w,
                      ../components/registration/images/payment.png       512w
                    "
                    sizes="38px"
                    alt=""
                  />
                  <div class="div-block-6">
                    <h1 class="heading-3">
                      <strong class="bold-text-2">Get paid</strong>
                    </h1>
                    <p class="paragraph">
                      12 hours after you have conducted your class, a Paypal
                      payment will be sent to your email.
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <div style="margin-top: 20px" class="w-col w-col-6">
              <img
                src="../components/main/images/AdobeStock_352057232.jpeg"
                width="620"
                srcset="
                  ../components/main/images/AdobeStock_352057232.jpeg  500w,
                  ../components/main/images/AdobeStock_352057232.jpeg  800w,
                  ../components/main/images/AdobeStock_352057232.jpeg 1080w,
                  ../components/main/images/AdobeStock_352057232.jpeg 1600w,
                  ../components/main/images/AdobeStock_352057232.jpeg 1805w
                "
                sizes="(max-width: 479px) 71vw, (max-width: 767px) 73vw, 42vw"
                alt=""
                class="image"
              />
            </div>
          </div>
        </div>
        <RegisterTutorForm />
      </body>
    </html>
  </client-only>
</template>
<script>
import RegisterTutorForm from '../components/RegisterTutorForm'

export default {
  name: 'RegisterTutor',
  components: { RegisterTutorForm },
}

require('../components/registration/css/webflow.css')
require('../components/registration/css/new-registration.webflow.css')
require('../components/registration/css/normalize.css')
</script>
<style>
.columns-3-copy {
  position: static;
  left: 0%;
  top: auto;
  right: 0%;
  bottom: 0%;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  padding: 20px 140px;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  background-color: transparent;
}
.columns-3-copy {
  position: static;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
}
.columns-3-copy {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
}
.columns-3-copy {
  position: static;
  left: 0%;
  top: auto;
  right: 0%;
  bottom: 0%;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  padding: 20px 140px;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  background-color: transparent;
}

.link {
  color: grey;
  font-size: 15px;
  text-decoration: none;
}

.link-2 {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  color: grey;
  text-decoration: none;
}

.link-3 {
  color: grey;
  text-decoration: none;
}

.link-4 {
  color: grey;
  text-decoration: none;
}
</style>