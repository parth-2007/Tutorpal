<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
      </head>
      <div style="font-family: Poppins; padding-top: 8px; " :style="updatemodal">
        <h3 style="text-align: center; font-size: 14px; width: 100%;">{{message}}<span style="margin-left:10px; font-size: 14px;" class="badge bg-secondary">New</span>
        <img
          style="float:right;  cursor: pointer;"
          @click="updatemodalvalue()"
          src="../static/student/images/close-1.png"
          width="16"
          alt=""
        />
        </h3>
      </div>
      <div style="font-family: Poppins;" class="d-grid gap-2">
        <router-link to="/seminars" class="btn btn-primary" type="button">Join Ongoing Seminar</router-link>
      </div>
      <body id="body" style="min-height: 100vh" class="body">
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
                      <div class="text-block-18" id="name">
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
                    class="nav-link-4 w-nav-link w--current"
                    >Explore</router-link
                  ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                    >Messages
                    <span v-if="user.unread > 0" class="badge">{{
                      user.unread
                    }}</span> </router-link
                  ><router-link to="/requests" class="nav-link-4 w-nav-link"
                    >Requests</router-link
                  ><router-link to="/payments" class="nav-link-4 w-nav-link"
                    >Payments</router-link>
                  <router-link to="/calendar" class="nav-link-4 w-nav-link"
                    >Calendar</router-link>
                </nav>
                <div class="menu-button-2 w-nav-button">
                  <div class="icon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="columns-4 w-row">
          <div class="column-18 w-col w-col-8">
            <div class="div-block-44">
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
              <div class="div-block-48">
                <div class="text-block-23">Trending</div>
                <p class="paragraph">
                  Find the highest-ranked tutors and the ones everybody is
                  learning from.
                </p>
              </div>
              <div v-if="trending.unfetched === undefined" class="trending">
                <div v-for="tutor of trending" :key="tutor.id" style="min-width: 50vw; max-width: 100vw" id="trending">
                  <router-link
                    :to="'/tutors/' + tutor.id"
                    class="link-block-2 w-inline-block"
                  >
                    <div style="line-height: 14px" class="div-block-54-copy">
                      <img
                        :src="
                          tutor.user !== undefined ? tutor.user.profilePic : ''
                        "
                        loading="lazy"
                        width="38"
                        height="38"
                        sizes="38px"
                        alt=""
                        class="image-5"
                      />
                      <div class="text-block-21">
                        <strong class="bold-text-3"
                          >{{
                            tutor.user !== undefined ? restrictChar(17, tutor.user.firstName) : ''
                          }}
                          {{
                            tutor.user !== undefined ? restrictChar(17, tutor.user.lastName) : ''
                          }}</strong
                        >
                      </div>
                      <div class="text-block-21-copy">
                        Subject: {{ restrictChar(20, tutor.subjects) }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Price: ${{ tutor.rates }} hourly
                      </div>
                      <div class="text-block-21-copy-2">
                        Degree: {{ tutor.education }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Education: {{ restrictChar(20, `${tutor.school}`) }}
                      </div>
                      <div class="text-block-21-copy-2">
                        Reviews: <div style="width: 90px; margin-top: 10%;" :id="tutor.id"></div>
                      </div>
                      <div style="margin-left: 15px;" class="text-block-21-copy-2">
                        Occupation: {{ restrictChar(15, tutor.occupation) }}
                      </div>
                    </div>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
          <div class="column-15 w-col w-col-4">
            <div style="margin-bottom: 20px" class="div-block-53">
              <h1 class="heading-2">Starting:</h1>
              <div v-if="started.unfetched === undefined" class="upcoming_loop">
                <div
                  style="margin-bottom: 50px"
                  v-for="session in started"
                  :key="session.id"
                  id="started"
                >
                  <div class="upcoming_item">
                    <p class="paragraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Tutor:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.firstName
                          : ''
                      }}
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.lastName
                          : ''
                      }}<br />Subject:
                      {{
                        session.tutor !== undefined
                          ? session.subjects
                          : ''
                      }}<br />Class Description:
                      {{ session.description }}‍<br />
                    </p>
                    <a
                      @click="joinSession(session.id)"
                      class="button-4 w-button"
                      >Join Meeting</a
                    ><br />
                    <strong
                      style="
                        margin-top: 10px;
                        font-size: 14px;
                        margin-top: 10px;
                      "
                      class="bold-text-2"
                      >We suggest using Google Chrome as that is most compatible
                      with our calling system</strong
                    >
                  </div>
                </div>
              </div>
            </div>
            <div
              style="height: 300px; margin-bottom: 20px"
              class="div-block-53"
            >
              <h1 class="heading-2">Upcoming Classes:</h1>
              <div
                v-if="upcoming.unfetched === undefined"
                class="upcoming_loop"
              >
                <div
                  style="margin-bottom: 50px"
                  v-for="session in upcoming"
                  :key="session.id"
                  id="upcoming"
                >
                  <img
                    @click="canceledHandler(session.id, session)"
                    style="cursor: pointer"
                    src="../static/student/images/close-1.png"
                    align="right"
                    width="10"
                    alt=""
                  />
                  <div class="upcoming_item">
                    <p class="paragraph-3">
                      Date: {{ session.date }}<br />Time:
                      {{ convertTime(session.timeStart) }} -
                      {{ convertTime(session.timeEnd) }}<br />Tutor:
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.firstName
                          : ''
                      }}
                      {{
                        session.tutor !== undefined
                          ? session.tutor.user.lastName
                          : ''
                      }}<br />Subject:
                      {{
                        session.tutor !== undefined
                          ? session.subjects
                          : ''
                      }}<br />‍Class Description:
                      {{ session.description }}‍<br /><strong
                        style="margin-top: 10px"
                        class="bold-text-2"
                        >Don&#x27;t worry if you can&#x27;t keep track of your
                        classes, we send an email 10 minutes prior to the
                        beginning of the class.</strong
                      >
                    </p>
                  </div>
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
import { mapGetters, mapActions } from 'vuex'
import convertTime from '../utils/convertTime'
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      clicked1: false,
      clicked: false,
      reviewHtml: [],
      message: '',
      showButton: false,
      q: '',
    }
  },
  async fetch() {
    await this.fetchTrending()
    await this.fetchSessions('startedSessions')
  },
  mounted(){
    this.getStars()
  },
  head() {
    return {
      title: 'Home',
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
        {
          rel: 'stylesheet',
          type: 'text/css',
          href: 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
        },
      ],
    }
  },
  computed: {
    logout() {
      return {
        display: this.clicked1 ? 'flex' : 'none',
      }
    },
    updatemodal() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({
      user: 'getUser',
      started: 'getStartedSessions',
      trending: 'getTrending',
      upcoming: 'getUpcoming',
    }),
  },
  async created() {
    await this.fetchSessions('upcoming')
    await this.fetchUser()
    const range = ["2:00", "3:00"];
    const value = (new Date().toLocaleTimeString()).substring(0, 4)
    const dayOfWeekName = new Date().toLocaleString(
      'default', {weekday: 'long'}
    );

    /* eslint-disable */
    if(dayOfWeekName === "Sunday"){
      this.message = "Stay tuned in tommorow, because we will be hosting a free Physics seminar, only on Mondays!"
    } 

    if(dayOfWeekName === "Tuesday"){
      this.message = "Stay tuned in tommorow, because we will be hosting a free Competitive Math seminar, only on Wednesdays!"
    } 

    if(dayOfWeekName === "Monday"){
      this.message = "Today on TutorPal, our tutors will be hosting a free Physics (beginner to intermediate) seminar to prepare you for future courses. Register as a student to join!"
    } 

    if(dayOfWeekName === "Wednesday"){
      this.message = "Today on TutorPal, our tutors will be hosting a free Competition Math (intermediate to advanced) seminar to prepare you for future contests. Register as a student to join!"
    } 

    if (value >= range[0] && value <= range[1] && dayOfWeekName === "Monday"){
      this.message = "A free Physics seminar is IN PROGRESS from 2 - 3 pm, register as a student to join!";
      this.showButton = true;
    }
    else if(value >= range[0] && value <= range[1] && dayOfWeekName === "Wednesday"){
      this.message = "A free Competition Math seminar is IN PROGRESS from 2 - 3 pm, register as a student to join!";
      this.showButton = true;
    }

    /* eslint-enable */
    console.log(this.message, this.showButton)
  },
  methods: {
    ...mapActions([
      'fetchUser',
      'fetchSessions',
      'fetchTrending',
      'removeSession',
    ]),
    ...mapGetters(['getStartedSessions', 'getUser', 'getUpcoming']),
    convertTime,
    logoutclick() {
      this.clicked1 = !this.clicked1
    },
    restrictChar(charNum, input){
      if(parseInt(input.length) > parseInt(charNum)){
        input = input.substr(0, charNum)
        return input + "..."
      }
      else{
        return input
      }
    },
    updatemodalvalue() {
      this.clicked = !this.clicked
    },
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
    async getStars() {
      await new Promise(resolve => setTimeout(resolve, 1000));
      this.trending.forEach((value,index ) => {
        const rating = value.averageReviews;
        let output = '';
        let i = ""
        for (i = rating; i >= 1; i--){
          output+=('<i class="fa fa-star" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        }
        /* eslint-disable */
        if (i == 0.5){
          output+=('<i class="fa fa-star-half-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        } 
        /* eslint-enable */
        for (i = (5 - rating); i >= 1; i--){
          output+=('<i class="fa fa-star-o" aria-hidden="true" style="color: gold; font-size: 16px;"></i>&nbsp;');
        }
        document.getElementById(value.id).innerHTML = output;
      });

    },
    async joinSession(id) {
      const csrfToken = await getCSRF()
      await fetch(process.env.API_URL + '/sessions/' + id + '/', {
        credentials: 'include',
        method: 'PATCH',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student_joined: true,
        }),
      })
      const url = '/sessions/' + id + '/'
      this.$router.push(url)
    },
    async canceledHandler(id, session) {
      const x = confirm('Please confirm that you wish to cancel this session.')
      if (x === true) {
        const csrfToken = await getCSRF()
        await fetch(process.env.API_URL + '/sessions/' + id + '/', {
          method: 'PATCH',
          credentials: 'include',
          headers: {
            'X-CSRFToken': csrfToken.success,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            canceled: true,
          }),
        })
        this.removeSession([session, 'upcoming'])
      }
    },
  }
}
</script>
<style scoped>
.badge {
  position: absolute;
  top: 11px;
  right: 3px;
  padding: 4px 7px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>
