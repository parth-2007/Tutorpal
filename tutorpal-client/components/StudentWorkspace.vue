<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://www.tutorpal.org/student/css/student-main.webflow.css" media="print" onload="this.media='all'">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" media="print" onload="this.media='all'">
      </head>
      <div v-if="session.student_paid === true && session.started === false">
      </div>
      <div
        v-else-if="session.student_paid === false || session.finished === true"
      >
      </div>
      <div v-else-if="session.student_pk !== user.studentPk">
      </div>
      <body
        v-else
        id="body"
        style="margin-bottom: 0px; background-color: rgba(65, 168, 211, 0.2)"
        class="body-5"
      >
        <div id="main">
          <div class="div-block-55">
            <div class="section">
              <router-link
                to="/"
                aria-current="page"
                class="link-block w-inline-block w--current"
                ><img
                  src="../static/student/images/logo.jpg"
                  loading="lazy"
                  width="200"
                  srcset="
                    ../static/student/images/logo-p-500.jpeg   500w,
                    ../static/student/images/logo-p-800.jpeg   800w,
                    ../static/student/images/logo-p-1080.jpeg 1080w,
                    ../static/student/images/logo.jpg         1432w
                  "
                  sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 25vw, (max-width: 1439px) 20vw, (max-width: 1919px) 15vw, 12vw"
                  alt=""
              /></router-link>
              <div class="div-block-4">
                <form action="/search" class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1-p-500.png 500w,
                      ../static/student/images/search-1.png       512w
                    "
                    sizes="(max-width: 767px) 20px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
                    alt=""
                    class="image-2"
                  /><input
                    type="search"
                    class="search-3 w-input"
                    maxlength="256"
                    name="q"
                    placeholder="Search by subject"
                    id="search"
                    required=""
                  /><input
                    type="submit"
                    value="Search"
                    class="button-8 _100 _5px-left w-button"
                  />
                </form>
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
        <iframe
          style="width: 100vw; height: 87vh"
          allow="camera;microphone"
          :src="'https://meet.jit.si/TutorpalSession' + session.call_url"
        ></iframe>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      clicked: false,
      session: [],
    }
  },
  head() {
    return {
      title: 'Student Workspace',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
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
  async created() {
    const url =
      'https://api.tutorpal.org/sessions/' + this.$route.params.id + '/'
    this.session = await fetch(url, {
      credentials: 'include',
    }).then((res) => {
      if (res.status === 500) {
        this.$router.push('/')
      }
      return res.json()
    })
    await fetch(url, {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'X-CSRFToken': (await getCSRF()).success,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        student_joined: true,
      }),
    })
    await this.fetchUser()
  },
  methods: {
    logoutclick() {
      this.clicked = !this.clicked
    },
    ...mapActions(['fetchUser']),
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
 

