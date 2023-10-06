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
      <body v-if="this.showButton === true"
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
          <div id="carouselExampleCaptions" class="carousel carousel-dark slide" data-bs-ride="false">
            <div style="padding-top: 50px;" class="carousel-inner">
              <div class="carousel-item active">
                <div style="height: 100vh;" id="jaas-container"></div>
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
      <div v-if="this.showButton === false">
        <Loader></Loader>
      </div>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import loggedInFetch from '~/utils/loggedInFetch'

export default {
  data() {
    return {
      seminar: [],
      url: "",
      showButton: false,
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
  async fetch() {
    const id = parseInt(this.$route.params.id)
    this.seminar = await fetch(process.env.API_URL + '/seminars/' + id + '/', {
      credentials: 'include',
    })
    await this.fetchUser()
    const data = await loggedInFetch('/seminars/'+id+'/join_seminar')
    if(data.unauthenticated === true){
      this.showButton = false;
      console.log("Invalid User")
    }
    else{
      const script = document.createElement('script')
      script.src = "https://www.whiteboard.team/dist/api.js"
      const script2 = document.createElement('script')
      script2.src = "https://8x8.vc/vpaas-magic-cookie-e1cf7aa7d58942b78fdf25a47d3490ca/external_api.js"
      document.body.appendChild(script)
      document.body.appendChild(script2)
      script2.addEventListener('load', this.setLoaded)
      await this.fetchUser()
      this.showButton = true;
      this.url = data.url;
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
    }),
  },
  methods: {
    logoutclick() {
      this.clicked = !this.clicked
    },
    /* eslint-disable */
    async setLoaded() {
      const api = new JitsiMeetExternalAPI("8x8.vc", {
        roomName: this.url,
        parentNode: document.querySelector('#jaas-container'),
        // Make sure to include a JWT if you intend to record,
        // make outbound calls or use any other premium features!
        // jwt: "eyJraWQiOiJ2cGFhcy1tYWdpYy1jb29raWUtZTFjZjdhYTdkNTg5NDJiNzhmZGYyNWE0N2QzNDkwY2EvMGRhMTE3LVNBTVBMRV9BUFAiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJqaXRzaSIsImlzcyI6ImNoYXQiLCJpYXQiOjE2OTY2MzEzMDksImV4cCI6MTY5NjYzODUwOSwibmJmIjoxNjk2NjMxMzA0LCJzdWIiOiJ2cGFhcy1tYWdpYy1jb29raWUtZTFjZjdhYTdkNTg5NDJiNzhmZGYyNWE0N2QzNDkwY2EiLCJjb250ZXh0Ijp7ImZlYXR1cmVzIjp7ImxpdmVzdHJlYW1pbmciOmZhbHNlLCJvdXRib3VuZC1jYWxsIjpmYWxzZSwic2lwLW91dGJvdW5kLWNhbGwiOmZhbHNlLCJ0cmFuc2NyaXB0aW9uIjpmYWxzZSwicmVjb3JkaW5nIjpmYWxzZX0sInVzZXIiOnsiaGlkZGVuLWZyb20tcmVjb3JkZXIiOmZhbHNlLCJtb2RlcmF0b3IiOnRydWUsIm5hbWUiOiJUZXN0IFVzZXIiLCJpZCI6Imdvb2dsZS1vYXV0aDJ8MTA5NjYxMTI2NTYxNTY1NTEwMzI2IiwiYXZhdGFyIjoiIiwiZW1haWwiOiJ0ZXN0LnVzZXJAY29tcGFueS5jb20ifX0sInJvb20iOiIqIn0.e6xefyb_Xn1DqS1ulFF37u4cA-_uonMelo1tbuEZ4E2BIA0qnmXoAyM6lclPrt-INwAl152fq44kqtjXhgpSH7XA3A0qcEWPRPvnBs8huJdG0tFcLKgOhnS1SW_5N2nYy-8cefHgBgc2E5YkWmtC9ouuRppFy-hCU7AUwZZWaovHqHwRJQpTHtioxik7Tvux8sZJ3DnXMcbas2mq8cAzK_St4gE6Dmg4CfmOueIcY-gkiQnRDzPm92jwbJLxRoQXUC7GgzIpXRqQ518hcca1Nm-NxcFt-Fx4vZE0HUtRWe5atB1dou3-MnI7N6XgQ6eJFLTH3-PPsm3AsCo5aYxQqA"
      });
     
      await new Promise(resolve => setTimeout(resolve, 2000));
      const wt = new api.WhiteboardTeam(this.$refs.container, {
          clientId: '322f4ec635688d506ad1bae2f1b21cb9',
          boardCode: this.url,
      });
      setInterval(function myTimer(){
        wt.resetZoom()
      }, 1000);

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
 