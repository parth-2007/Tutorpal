<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
    <head>
      <meta charset="utf-8" />
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" media="none" onload="if(media!='all')media='all'">
    </head>
      <body
        id="body"
        style="background-color: rgba(65, 168, 211, 0.2)"
        class="tutorbody-5"
      >
        <div
          :style="updateModal"
          style="padding-bottom: 0px"
          class="tutordiv-block-22"
        >
          <div
            style="
              border-radius: 8px;
              padding-bottom: 20px;
              height: 240px;
              width: 375px;
              font-family: Poppins;
            "
            class="tutordiv-block-23"
          >
            <div class="tutordiv-block-25">
              <strong
                >You have 00:00:00 left in this class,
                are you sure you want to end it?</strong
              >
              <br />Clicking "confirm" will confirm to us that this class has
              been finished. You will be paid shortly after. Thank you for
              tutoring with TutorPal!
            </div>
            <div
              style="margin-left: 10px; margin-top: 10px; margin-right: 10px"
            >
              Your student has not joined this class, therefore, we are not
              allowing you to end this class. If there are any issues, please
              contact us at support@tutorpal.org. We are very sorry for the
              inconvienence and hope you will continue to tutor on this
              platform.
            </div>
            <button
              @click="endclass()"
              style="
                background-color: green;
                margin-left: 10px;
                margin-top: 10px;
                font-size: 14px;
              "
              class="tutorbutton-10-copy-copy w-button"
            >
              Confirm</button
            ><button
              @click="updateModalValue()"
              style="
                background-color: #bb0a1e;
                margin-left: 10px;
                margin-top: 10px;
                font-size: 14px;
              "
              class="tutorbutton-10-copy-copy w-button"
            >
              Cancel
            </button>
          </div>
        </div>
        <div id="main">
          <div class="tutorsection">
            <router-link to="/" class="tutorlink-block w-inline-block"
              ><img
                src="../static/tutor/images/logo.jpg"
                loading="lazy"
                width="260"
                srcset="
                  ../static/tutor/images/logo-p-500.jpeg   500w,
                  ../static/tutor/images/logo-p-800.jpeg   800w,
                  ../static/tutor/images/logo-p-1080.jpeg 1080w,
                  ../static/tutor/images/logo.jpg         1432w
                "
                sizes="(max-width: 479px) 100vw, (max-width: 767px) 34vw, (max-width: 991px) 25vw, (max-width: 1439px) 21vw, (max-width: 1919px) 15vw, 12vw"
                alt=""
            /></router-link>
            <div class="tutordiv-block-4">
              <div class="tutordiv-block-43">
                <div class="tutorname_profile_pic">
                  <img
                    id="image"
                    width="60"
                    height="60"
                    sizes="60px"
                    alt=""
                    class="tutorimage-7"
                  />
                  <div
                    data-hover=""
                    data-delay="0"
                    class="tutordropdown-3 w-dropdown"
                  >
                    <div
                      @click="logoutclick()"
                      class="tutordropdown-toggle-2-copy w-dropdown-toggle"
                    >
                      <div id="name" class="tutortext-block-18">
                        Amit Prakash
                      </div>
                      <div class="tutortext-block-20">Tutor</div>
                    </div>
                    <nav :style="logout" class="tutornavigation-dropdown-2">
                      <div class="tutordropdown-pointer-2">
                        <div class="tutordropdown-wrapper-2">
                          <router-link
                            to="/logout"
                            id="logout"
                            class="tutordropdown-link-2 w-inline-block"
                          >
                            <div class="tutornav-content-wrap-2">
                              <div class="tutordropdown-title-2">Logout</div>
                            </div>
                          </router-link>
                          <router-link
                            to="/account"
                            class="tutordropdown-link-2 w-inline-block"
                          >
                            <div class="tutornav-content-wrap-2">
                              <div class="tutordropdown-title-2">Account</div>
                            </div>
                          </router-link>
                        </div>
                      </div>
                    </nav>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div style="float: right; font-family: Poppins; background-color:white; height:100%; width:23vw; margin-top:25px; margin-bottom:25px; margin-right:8px; border-radius:8px; padding:10px">
          <div>
            <p style="font-size:16px;">Here are some tools you can use to help:</p>
            <a target="_blank" href="https://www.google.com/docs/about/">Google Docs, Sheets, Forms, Slides</a>
            <br>
            <a target="_blank" href="https://jamboard.google.com/">Google Jamboard</a>
            <br>
            <a target="_blank" href="https://colab.research.google.com/notebooks/intro.ipynb">Google Colab</a>
            <br>
            <a target="_blank" href="https://docs.google.com/drawings/">Google Drawings</a>
            <br>
            <a target="_blank" href="https://kahoot.com/">Kahoot</a>
            <br>
            <a target="_blank" href="https://www.hackerrank.com/">Hackerrank</a>
            <p style="margin-top:10px">Tips: 1) Leaving the call will NOT end this class as it is not directly connected to our platform. Remember to end the class by clicking the red button below. 2) Please do not need to share the meeting link with anybody, including the student. 3) The video calling system is most compatible with Google Chrome</p>
            <h1
              style="
                font-family: Poppins;
                margin-top: 10px;
                margin-bottom: 10px;
                font-size: 20px;
                color: black;
              "
            >
              <strong>Countdown Timer: 00:00:00</strong>
            </h1>
             <button
              @click="updateModalValue()"
              class="tutorbutton-10-copy-copy w-button"
              style="
                margin-top: 10px;
                margin-bottom: 10px;
                background-color: #bb0a1e;
              "
            >
              End this Class
            </button>
          </div>
        </div>
        <iframe
          style="width: 75vw; height: 100vh"
          allow="camera;microphone"
          :src="'https://meet.jit.si/TutorpalSession'+'efhieuf'"
        ></iframe>
      </body>
    </html>
  </client-only>
</template>
<script>

export default {
  data() {
    return {
      clicked: false,
    }
  },
  head() {
    return {
      title: 'Tutor Workspace',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
  },
  methods:{
    logoutclick() {
      this.clicked = !this.clicked
    },
  }
}
</script>
<style>
.tutordiv-block-80 {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  margin: 10px 5%;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
}
</style>
 

