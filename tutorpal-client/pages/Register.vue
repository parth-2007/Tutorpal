<template>
  <client-only>
    <html
      data-wf-page="5f59c197d2dc127d5475d1e0"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body>
        <div class="div-block-3">
          <router-link to="/" class="w-inline-block"
            ><img
              src="../static/main/images/logo.jpg"
              loading="lazy"
              width="307"
              srcset="
                ../static/main/images/logo-p-500.jpeg   500w,
                ../static/main/images/logo-p-800.jpeg   800w,
                ../static/main/images/logo-p-1080.jpeg 1080w,
                ../static/main/images/logo.jpg         1432w
              "
              sizes="(max-width: 479px) 100vw, (max-width: 767px) 27vw, (max-width: 991px) 24vw, (max-width: 1439px) 21vw, (max-width: 1919px) 16vw, 13vw"
              alt=""
              class="image-14"
          /></router-link>
          <div class="div-block-4">
            <router-link to="/login" class="link-2-copy">login</router-link>
          </div>
          <router-link
            to="/register"
            aria-current="page"
            class="button w-button w--current"
            >register</router-link
          >
        </div>
        
        <div class="columns-3 w-row">
          <div class="column-13 w-col w-col-6">
            <router-link to="/register-tutor" class="link-block-2 w-inline-block"
              ><img
                src="../static/main/images/partners.png"
                loading="lazy"
                width="150"
                srcset="
                  ../static/main/images/partners-p-500.png 500w,
                  ../static/main/images/partners.png       512w
                "
                sizes="150px"
                alt=""
              />
              <h1 class="heading-7">Become a tutor</h1>
              <p class="paragraph-7">
                Join our community at TutorPal by becoming a tutor to spread
                your passion and knowledge with many other students while making
                a profit at the same time. We do not take any commission, so
                what you list as your price is how much you get paid. If your
                tutor agency or program has been shut down due to COVID-19, make
                it online and global in a couple of minutes.
              </p></router-link
            >
          </div>
          <div class="column-13 w-col w-col-6">
            <router-link to="/register-student" class="link-block-2 w-inline-block"
              ><img
                src="../static/main/images/student-1.png"
                loading="lazy"
                width="150"
                srcset="
                  ../static/main/images/student-1-p-500.png 500w,
                  ../static/main/images/student-1.png       512w
                "
                sizes="150px"
                alt=""
              />
              <h1 class="heading-7">Become a student</h1>
              <p class="paragraph-7">
                School education is not as strong as before? Have loads of
                homework coming in? Need to prepare for a competition? We
                provide a variety of services here at TutorPal. It does NOT cost
                to register an account as a student. Gain access to these
                services in the click of a button.
              </p></router-link
            >
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Register',
      link: [
        { rel:"stylesheet", type:"text/css", href:"./main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'./main/css/homepage-12.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"./main/css/normalize.css" },
      ]
    }
  },
}

</script>