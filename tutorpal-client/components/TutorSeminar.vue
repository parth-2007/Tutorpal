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
      <body
        id="body"
        style="background-color: rgba(65, 168, 211, 0.2)"
        class="tutorbody-5"
      >
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
                      <div class="tutortext-block-20">User</div>
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
          <span style="font-family: Poppins; text-align:center; font-size: 30px; color: black; margin-top: 8px; z-index: 0; margin-left: 23vw;"><strong>{{message}}</strong></span>
          <div v-if="showBody == true" id="carouselExampleCaptions" class="carousel carousel-dark slide" data-bs-ride="false">
            <div style="padding-top: 50px;" class="carousel-inner">
              <div class="carousel-item active">
                <div style="height: 100vh;" ref="meeting"></div>
              </div>
              <div class="carousel-item">
                <div style="height: 100vh;" ref="container" id="wt-container"></div>
              </div>
            </div>
            <button style="height:20px; margin-top: 15px; width: 100%; color: black; float:left;" class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                <span class="btn btn-outline-primary" style="border-radius: 20px; margin: 10px;">Whiteboard</span>
            </button>
          </div>
          <div v-else style="height: 87.8vh; font-family: Poppins; padding: 15px;">
            <h1 style="font-size: 200px; color:black;"><strong>OOPS!</strong></h1>
              It seems you are trying to join a seminar that either hasn't started or has already ended. Please be patient and thank you for using TutorPal!
              <br><br><p style="font-size: 20px;" >Our seminar timings are:</p> <p style="font-size: 16px;"> <strong>Veer's Physics Seminar </strong> - 2 to 3 pm PT Mondays <br> <strong>Anirudh's Competition Math Seminar</strong> - 2 to 3 pm PT Wednesdays</p>
          </div>
      </body>
    </html>
  </client-only>
</template>
-
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data() {
    return {
      showBody: false,
      message: '',
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
  created(){
    const range = ["1:45", "3:15"];
    const value = (new Date().toLocaleTimeString()).substring(0, 4)
    const dayOfWeekName = new Date().toLocaleString(
      'default', {weekday: 'long'}
    );
    console.log(dayOfWeekName); 

    /* eslint-disable */
    if (value >= range[0] && value <= range[1] && dayOfWeekName === "Monday"){
      this.showBody = true;
      this.message = "Welcome to Veer's Physics Seminar!";
    }
    else if(value >= range[0] && value <= range[1] && dayOfWeekName === "Wednesday"){
      this.showBody = true;
      this.message = "Welcome to Anirudh's Competition Math Seminar!";
    }
    /* eslint-enable */

    
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
    if(this.showBody === true){
      const script = document.createElement('script')
      script.src = "https://www.whiteboard.team/dist/api.js"
      const script2 = document.createElement('script')
      script2.src = "https://meet.jit.si/external_api.js"
      document.body.appendChild(script)
      document.body.appendChild(script2)
      script2.addEventListener('load', this.setLoaded)
      await this.fetchUser()
    }
  },
  methods: {
    logoutclick() {
      this.clicked = !this.clicked
    },
    /* eslint-disable */
    async setLoaded() {
      const domain = 'meet.jit.si';
      const options = {
        roomName: "uihesiutfhiujhiwujheriujqio13784o1-098iy",
        parentNode: this.$refs.meeting,
      };
      new JitsiMeetExternalAPI(domain, options);
     
      await new Promise(resolve => setTimeout(resolve, 2000));
      const wt = new api.WhiteboardTeam(this.$refs.container, {
          clientId: '322f4ec635688d506ad1bae2f1b21cb9',
          boardCode: "uihesiutfhiujhiwujheriujqio13784o1-098iy",
      });
    },
    /* eslint-enable */
    ...mapActions([
      'fetchUser',
    ]),
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
 
