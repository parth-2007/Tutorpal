<template>
  <client-only>
    <html
      data-wf-page="5f59c197d2dc127d5475d1e0"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <div v-if="user.isStudent">
      </div>
      <div v-else-if="user.isTutor">
      </div>
      <body v-else>
        <div class="homediv-block-3">
          <router-link
            style="margin-top: 0px; margin-bottom: -30px"
            to="/"
            class="homelink-block w-inline-block"
            ><img
              src="../static/student/images/logo.jpg"
              width="250"
              alt=""
              class="homeimage"
          /></router-link>
          <div class="homediv-block-4">
            <router-link to="/login" class="homelink-2-copy">login</router-link>
          </div>
          <router-link
            to="/register"
            aria-current="page"
            class="homebutton w-button w--current"
            >register</router-link
          >
        </div>
        
        <div class="homecolumns-3 w-row">
          <div class="homecolumn-13 w-col w-col-6">
            <router-link to="/register-tutor" class="homelink-block-2 w-inline-block"
              ><img
                src="../static/student/images/partners.png"
                loading="lazy"
                width="150"
                srcset="
                  ../static/student/images/partners-p-500.png 500w,
                  ../static/student/images/partners.png       512w
                "
                sizes="150px"
                alt=""
              />
              <h1 class="homeheading-7">Become a Tutor</h1>
              <p style="font-size:14px" class="homeparagraph-7">
                Join the community at TutorPal by registering as a tutor! You can provide
                your knowledge and skills to students struggling and make
                profit at the same time. We do take 5% commission from your hourly rates primarily to maintain the platform's infrastructure. 
                If your tutor agency or service has been shut down due to COVID-19, make
                it online in a couple of minutes.
              </p></router-link
            >
          </div>
          <div class="homecolumn-13 w-col w-col-6">
            <router-link to="/register-student" class="homelink-block-2 w-inline-block"
              ><img
                src="../static/student/images/student-1.png"
                loading="lazy"
                width="150"
                srcset="
                  ../static/student/images/student-1-p-500.png 500w,
                  ../static/student/images/student-1.png       512w
                "
                sizes="150px"
                alt=""
              />
              <h1 class="homeheading-7">Become a student</h1>
              <p style="font-size:14px" class="homeparagraph-7">
                Struggling on your homework? Struggling to understand a concept?
                 Need to prepare for a competition? Need assistance in preparing for an upcoming test?
                 Don't worry! TutorPal provides a variety of services on this online platform. 
                 Register an account as a student in TutorPal and gain access to these
                services in an instant! 
              </p></router-link
            >
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  head() {
    return {
      title: 'Register',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
  computed: mapGetters({ user: 'getUser' }),
  async created() {
    await this.fetchUser()
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser']),
  }
}

</script>
