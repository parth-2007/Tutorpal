
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body
        style="background-color: rgba(65, 168, 211, 0.2); min-height: 100vh"
        id="body"
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
                      sizes="(max-width: 479px) 15vw, (max-width: 767px) 8vw, 60px"
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
            <div class="div-block-6">
              <div
                data-collapse="none"
                data-animation="default"
                data-duration="400"
                role="banner"
                class="navbar-2 w-nav"
              >
                <div class="container-2 w-container">
                  <nav role="navigation" class="nav-menu-3 w-nav-menu">
                    <router-link
                      to="/"
                      aria-current="page"
                      class="nav-link-4 w-nav-link"
                      >Explore</router-link
                      ><router-link
                    to="/seminars"
                    class="tutornav-link-4 w-nav-link w--current"
                    >Seminars
                  </router-link
                    ><router-link
                      to="/inbox"
                      class="nav-link-4 w-nav-link"
                      >Messages</router-link
                    ><router-link to="/requests" class="nav-link-4 w-nav-link"
                      >Requests</router-link
                    ><router-link to="/payments" class="nav-link-4 w-nav-link"
                      >Payments</router-link
                    ><router-link to="/calendar" class="nav-link-4 w-nav-link"
                    >Calendar</router-link>
                    <router-link to="/donations" class="nav-link-4 w-nav-link"
                      >Donate</router-link>
                  </nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="div-block-66">
            <div class="div-block-45">
              <img
                src="../static/student/images/question.png"
                loading="lazy"
                width="30"
                alt=""
              /><a
                href="mailto:info@tutorpal.org?subject=Website%20Email"
                class="link-2"
                >Need help? Send us an email</a
              >
            </div>
            <div class="div-block-65">
              <div class="text-block-23">My Seminars</div>
              <p class="paragraph">
                View all of the seminars that you have already enrolled for, you will be joining all your seminars here:
              </p>
            </div>
            <div v-if="myseminars.unfetched === undefined">
              <div v-for="seminar in myseminars.results" :key="seminar.id" class="loop">
                <div class="i">
                  <div class="div-block-51-copy">
                    <img
                      :src="
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.profile_pic
                          : ''
                      "
                      loading="lazy"
                      width="75"
                      height="75"
                      sizes="100px"
                      alt=""
                      class="image-15"
                    />
                    <p class="paragraph-2">
                      <strong class="bold-text">Schedule <br /></strong>First
                      Seminar: {{ seminar.times[0].substring(0, 10) }}<br />Tutor:
                      {{
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.first_name
                          : ''
                      }}
                      {{
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.last_name
                          : ''
                      }}<br />Duration: {{seminar.duration}} 
                      <br />Start Time: {{convertTime(seminar.times[0].substring(11, 18))}}
                    </p>
                  </div>
                  <p class="paragraph-2-copy">
                    <strong class="bold-text">Class Information</strong>
                    <br />Topic: {{ seminar.subjects }}
                    <br />Description: {{ seminar.description }}
                    <br />Amount: ${{seminar.price}}
                    <br />Unpaid Class: {{ seminar.free }}
                    <br>
                    <router-link :to="'/seminarjoin/'+seminar.id"  style="margin-top: 15px;" class="btn btn-info">Join Class</router-link>
                  </p>
                </div>
              </div>
            </div>
            <div class="div-block-65">
              <div class="text-block-23">Discover Seminars</div>
              <p class="paragraph">
                View all of the seminars that our platform has to offer.
              </p>
            </div>
            <div v-if="seminars.unfetched === undefined">
              <div v-for="seminar in seminars.results" :key="seminar.id" class="loop">
                <div class="i">
                  <div class="div-block-51-copy">
                    <img
                      :src="
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.profile_pic
                          : ''
                      "
                      loading="lazy"
                      width="75"
                      height="75"
                      sizes="100px"
                      alt=""
                      class="image-15"
                    />
                    <p class="paragraph-2">
                      <strong class="bold-text">Schedule <br /></strong>First
                      Seminar: {{ seminar.times[0].substring(0, 10) }}<br />Tutor:
                      {{
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.first_name
                          : ''
                      }}
                      {{
                        seminar.tutor !== undefined
                          ? seminar.tutor.user.last_name
                          : ''
                      }}<br />Duration: {{seminar.duration}} 
                      <br />Start Time: {{convertTime(seminar.times[0].substring(11, 18))}}
                    </p>
                  </div>
                  <p class="paragraph-2-copy">
                    <strong class="bold-text">Class Information</strong>
                    <br />Topic: {{ seminar.subjects }}
                    <br />Description: {{ seminar.description }}
                    <br />Amount: ${{seminar.price}}
                    <br />Unpaid Class: {{ seminar.free }}
                    <br>
                    <button v-if="seminar.free === true" @click="registerClass(seminar.free, seminar.id)" style="margin-top: 15px;" class="btn btn-warning">Enroll</button>
                    <router-link v-if="seminar.free === false" :to="'/seminarpay/' + seminar.id" style="margin-top: 15px;" class="btn btn-warning">Enroll</router-link>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import convertTime from '../utils/convertTime'
import getCSRF from '~/utils/getCSRF'

export default {
  data() {
    return {
      clicked: false,
      q:"",
      seminars: [],
      myseminars: [],
      data: '',
    }
  },
  async fetch() {
    await this.fetchUser();
    this.seminars = await fetch(
      process.env.API_URL + '/seminars/discover_seminars',
      {
        credentials: 'include',
      }
    ).then((res) => res.json(this.response = res.status))
    this.myseminars = await fetch(
      process.env.API_URL + '/seminars/my_seminars',
      {
        credentials: 'include',
      }
    ).then((res) => res.json(this.response = res.status))
  },
  head() {
    return {
      title: 'Inbox',
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
    ...mapGetters({ user: 'getUser'}),
  },
  methods: {
    ...mapActions([
      'fetchUser',
      'setUser',
    ]),
    ...mapGetters(['getUser']),
    ...mapMutations(['setUser']),
    convertTime,
    logoutclick() {
      this.clicked = !this.clicked
    },
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
    async registerClass(free, id){
      const csrfToken = await getCSRF()
      if(free===true){
        const data = await fetch(process.env.API_URL + '/seminars/'+id+'/register/', {
          method: 'POST',
          credentials: 'include',
          headers: {
            'X-CSRFToken': csrfToken.success,
          },
        }).then((res) => res.json())
        this.data = data
        alert("You have successfully enrolled yourself into this seminar!")
      }
    },

  }
    
}
</script>
<style scoped>
.tutorbadge {
  margin-top: 5px;
  float: right;
  padding: 2px 8px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
  margin-right: 15px;
}
</style>