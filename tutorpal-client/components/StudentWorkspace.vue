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
      <div
        v-if="session.student_paid === true && session.started === false"
      ></div>
      <div
        v-else-if="session.student_paid === false || session.finished === true"
      ></div>
      <div v-else-if="session.student_pk !== user.studentPk"></div>
      <body
        v-else
        id="body"
        style="margin-bottom: 0px; background-color: rgba(65, 168, 211, 0.2)"
        class="body-5"
      >
        <div id="main">
          <div class="div-block-55">
            <div class="section">
              <router-link to="/" class="link-block-3 w-inline-block"
                ><img
                  src="../static/student/images/logo.jpg"
                  loading="lazy"
                  width="200"
                  srcset="
                    ../static/student/images/logo.jpg  500w,
                    ../static/student/images/logo.jpg  800w,
                    ../static/student/images/logo.jpg 1080w,
                    ../static/student/images/logo.jpg 1432w
                  "
                  sizes="200px"
                  alt=""
              /></router-link>
              <div class="div-block-4">
                <div style="margin-left: 0px; padding-left: 0px" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                      class="search-3 w-input"
                      placeholder="Search by subject"
                      id="search"
                      v-model="q"
                      @keyup.enter="submitSearch()"
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
              </div>
                <div class="div-block-43">
                  <div class="name_profile_pic">
                    <img
                      :src="user.profilePic"
                      id="image"
                      width="60"
                      height="60"
                      sizes="60px"
                      alt=""
                      class="image-7"
                    />
                    <div
                      data-hover=""
                      data-delay="0"
                      class="dropdown-3 w-dropdown"
                    >
                      <div
                        @click="logoutclick()"
                        class="dropdown-toggle-2-copy w-dropdown-toggle"
                      >
                        <div id="name" class="text-block-18">
                          {{ user.firstName }} {{ user.lastName }}
                        </div>
                        <div class="text-block-20">Student</div>
                      </div>
                      <nav :style="logout" class="navigation-dropdown-2">
                        <div class="dropdown-pointer-2">
                          <div class="dropdown-wrapper-2">
                            <router-link
                              to="/logout"
                              id="logout"
                              class="dropdown-link-2 w-inline-block"
                            >
                              <div class="nav-content-wrap-2">
                                <div class="dropdown-title-2">Logout</div>
                              </div>
                            </router-link>
                            <router-link
                              to="/account"
                              class="dropdown-link-2 w-inline-block"
                            >
                              <div class="nav-content-wrap-2">
                                <div class="dropdown-title-2">Account</div>
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
        </h1>
        <div id="carouselExampleCaptions" class="carousel carousel-dark slide" data-bs-ride="false">
            <div class="carousel-inner">
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
      </body>
    </html>
  </client-only>
</template>
-
<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'
import convertTime from '../utils/convertTime'

export default {
  data() {
    return {
      clicked: false,
      session: [],
      q: '',
    }
  },
  head() {
    return {
      title: 'Student Workspace',
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
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ user: 'getUser' }),
  },
  beforeDestroy() {
    Array.prototype.slice.call(document.getElementsByTagName('iframe')).forEach(
      function(item) {
        item.remove();
    });
  },
  async mounted() {
    const script = document.createElement('script')
    script.src = "https://www.whiteboard.team/dist/api.js"
    const script2 = document.createElement('script')
    script2.src = "https://8x8.vc/vpaas-magic-cookie-e1cf7aa7d58942b78fdf25a47d3490ca/external_api.js"
    document.body.appendChild(script)
    document.body.appendChild(script2)
    script2.addEventListener('load', this.setLoaded)
    await fetch(
      process.env.API_URL + '/sessions/' + this.$route.params.id + '/',
      {
        method: 'PATCH',
        credentials: 'include',
        headers: {
          'X-CSRFToken': (await getCSRF()).success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student_joined: true,
        }),
      }
    )
    await this.fetchUser()
  },
  methods: {
    logoutclick() {
      this.clicked = !this.clicked
    },
    submitSearch() {
      this.$router.push("/search/"+this.q);
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
      console.log("Successfully loaded scripts")
      new JitsiMeetExternalAPI("8x8.vc", {
        roomName: this.session.call_url,
        parentNode: this.$refs.meeting,
        height: window.innerHeight
        // Make sure to include a JWT if you intend to record,
        // make outbound calls or use any other premium features!
        // jwt: "eyJraWQiOiJ2cGFhcy1tYWdpYy1jb29raWUtZTFjZjdhYTdkNTg5NDJiNzhmZGYyNWE0N2QzNDkwY2EvMGRhMTE3LVNBTVBMRV9BUFAiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJqaXRzaSIsImlzcyI6ImNoYXQiLCJpYXQiOjE2OTY2MzEzMDksImV4cCI6MTY5NjYzODUwOSwibmJmIjoxNjk2NjMxMzA0LCJzdWIiOiJ2cGFhcy1tYWdpYy1jb29raWUtZTFjZjdhYTdkNTg5NDJiNzhmZGYyNWE0N2QzNDkwY2EiLCJjb250ZXh0Ijp7ImZlYXR1cmVzIjp7ImxpdmVzdHJlYW1pbmciOmZhbHNlLCJvdXRib3VuZC1jYWxsIjpmYWxzZSwic2lwLW91dGJvdW5kLWNhbGwiOmZhbHNlLCJ0cmFuc2NyaXB0aW9uIjpmYWxzZSwicmVjb3JkaW5nIjpmYWxzZX0sInVzZXIiOnsiaGlkZGVuLWZyb20tcmVjb3JkZXIiOmZhbHNlLCJtb2RlcmF0b3IiOnRydWUsIm5hbWUiOiJUZXN0IFVzZXIiLCJpZCI6Imdvb2dsZS1vYXV0aDJ8MTA5NjYxMTI2NTYxNTY1NTEwMzI2IiwiYXZhdGFyIjoiIiwiZW1haWwiOiJ0ZXN0LnVzZXJAY29tcGFueS5jb20ifX0sInJvb20iOiIqIn0.e6xefyb_Xn1DqS1ulFF37u4cA-_uonMelo1tbuEZ4E2BIA0qnmXoAyM6lclPrt-INwAl152fq44kqtjXhgpSH7XA3A0qcEWPRPvnBs8huJdG0tFcLKgOhnS1SW_5N2nYy-8cefHgBgc2E5YkWmtC9ouuRppFy-hCU7AUwZZWaovHqHwRJQpTHtioxik7Tvux8sZJ3DnXMcbas2mq8cAzK_St4gE6Dmg4CfmOueIcY-gkiQnRDzPm92jwbJLxRoQXUC7GgzIpXRqQ518hcca1Nm-NxcFt-Fx4vZE0HUtRWe5atB1dou3-MnI7N6XgQ6eJFLTH3-PPsm3AsCo5aYxQqA"
      });
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
    ...mapActions(['fetchUser']),
    convertTime,
  },
}
</script>
<style>
.div-block-80 {
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