-
<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
      </head>
      <div v-if="session.student_paid === true && session.started === false">
        <p style="font-size: 18px; font-family: Poppins; margin: 15px">
          This class has not been started yet, your job as a tutor is to start
          meetings when the proper times and date occur.
        </p>
      </div>
      <div
        v-else-if="session.student_paid === false || session.finished === true"
      ></div>
      <div v-else-if="session.tutor_pk !== user.tutorPk"></div>
      <body
        v-else
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
            <div
              v-if="session.student_joined === true"
              class="tutordiv-block-25"
            >
              Clicking "confirm" will confirm to us that this class has
              been finished. You will be paid shortly after. Thank you for
              tutoring with TutorPal!
              <br>
              <button
                @click="endclass()"
                style="
                  background-color: green;
                  font-size: 14px;
                  margin-top: 10px;
                  float: left
                "
                class="tutorbutton-10-copy-copy w-button"
              >
                Confirm
              </button>
            </div>
            <div
              v-else-if="session.student_joined === false"
              style="margin-left: 10px; margin-top: 10px; margin-right: 10px"
            >
              Your student has not joined this class, therefore, we are not
              allowing you to end it. If there are any issues, please contact us
              at info@tutorpal.org. We are very sorry for the inconvienence.
            </div>
            <button
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
            <p style="color: hsla(0, 100%, 64%, 1); margin-top: 10px; margin-left: 20px;">{{message}}</p>
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
                    :src="user.profilePic"
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
                        {{ user.firstName }} {{ user.lastName }}
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
        <h1
          style="
            font-family: Poppins;
            margin-top: 10px;
            margin-bottom: 10px;
            margin-left: 10px;
            font-size: 20px;
            color: black;
            float: right;
          "
        >
          <strong>Duration: {{ convertTime(session.time_start) }} - {{ convertTime(session.time_end) }}</strong>
          <button
            @click="updateModalValue()"
            class="tutorbutton-10-copy-copy w-button"
            style="
              background-color: #bb0a1e;
              margin-left: 30px;
              font-size: 16px;
            "
          >
            End this Class
          </button>
        </h1>
        <div id="carouselExampleCaptions" class="carousel carousel-dark slide" data-bs-ride="false">
          <div class="carousel-inner">
            <div style="padding: 0px; margin: 0px;" class="carousel-item active">
              <div style="margin-top: -15px;" ref="meeting"></div>
            </div>
            <div class="carousel-item">
              <div style="height: 100vh;" ref="container" id="wt-container"></div>
            </div>
          </div>
          <button style="height:20px; margin-top: 15px; color: black; float:left;" class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
              <span class="btn btn-outline-primary" style="border-radius: 20px; margin: 15px; padding-bottom: 10px;">Whiteboard</span>
          </button>
        </div>
      </body>
    </html>
  </client-only>
</template>
-
<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'
import dateToString from '../utils/dateToString'
import convertTime from '../utils/convertTime'

export default {
  data() {
    return {
      clicked: false,
      clicked1: false,
      session: [],
      timerCount: '',
      timerDisplay: '',
      message: ''
    }
  },
  head() {
    return {
      title: 'Tutor Workspace',
      link: [
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/webflow.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/normalize.css',
        },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: '/student/css/student-main.webflow.css',
        },
      ],
    }
  },
  beforeDestroy() {
    Array.prototype.slice.call(document.getElementsByTagName('iframe')).forEach(
      function(item) {
        item.remove();
    });
  },
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    updateModal() {
      return {
        display: this.clicked1 ? 'flex' : 'none',
      }
    },
    ...mapGetters({
      user: 'getUser',
      pastSessions: 'getPastSessions',
      startedSessions: 'getStartedSessions',
    }),
  },
  async mounted() {
    const script = document.createElement('script')
    script.src = "https://www.whiteboard.team/dist/api.js"
    const script2 = document.createElement('script')
    script2.src = "https://meet.jit.si/external_api.js"
    document.body.appendChild(script)
    document.body.appendChild(script2)
    script2.addEventListener('load', this.setLoaded)
    await this.fetchUser()
    await this.fetchSessions('pastSessions')
    await this.fetchSessions('startedSessions')
  },
  methods: {
    dateToString,
    logoutclick() {
      this.clicked = !this.clicked
    },
    /* eslint-disable */
    async setLoaded() {
      this.session = await fetch(
        process.env.API_URL + '/sessions/' + this.$route.params.id + '/',
        {
          credentials: 'include',
        }
      ).then((res) => {
        if (res.status === 500) {
          this.$router.push('/')
        }
        return res.json()
      })
      const domain = 'meet.jit.si';
      const options = {
        roomName: this.session.call_url,
        parentNode: this.$refs.meeting,
        height: window.innerHeight,
      };
      new JitsiMeetExternalAPI(domain, options);
     
      await new Promise(resolve => setTimeout(resolve, 2000));
      const wt = new api.WhiteboardTeam(this.$refs.container, {
          clientId: '322f4ec635688d506ad1bae2f1b21cb9',
          boardCode: this.session.call_url,
      });
      setInterval(function myTimer(){
        wt.resetZoom()
      }, 1000);
    },
    /* eslint-enable */
    async updateModalValue() {
      this.session = await fetch(
        process.env.API_URL + '/sessions/' + this.$route.params.id + '/',
        {
          credentials: 'include',
        }
      ).then((res) => {
        if (res.status === 500) {
          this.$router.push('/')
        }
        return res.json()
      })
      this.clicked1 = !this.clicked1
    },
    async endclass() {
      await fetch(
        process.env.API_URL + '/finish_session/' + this.$route.params.id + '/',
        {
          method: 'POST',
          credentials: 'include',
          headers: {
            'X-CSRFToken': (await getCSRF()).success,
            'Content-Type': 'application/json',
          },
        }
      ).then((res) => {
        if (res.status === 500) {
          this.message="There seems to be an issue with ending the class, we believe it is because you are attempting to end this class too early. You are only allowed to end classes in the last 5 minutes, not any earlier."
        }
        else if(res.status === 200 || res.status === 201){
          this.removeSession([this.session, 'startedSessions'])
          this.addSession([this.session, 'pastSessions'])
          this.$router.push('/')
        }
        console.log(res.status)
      })
    },
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'removeSession',
      'addSession',
    ]),
    ...mapGetters(['getPastSessions', 'getStartedSessions']),
    convertTime,
  },
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
 
