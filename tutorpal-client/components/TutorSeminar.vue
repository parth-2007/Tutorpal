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
        <div class="tutordiv-block-6">
            <div
              data-collapse="none"
              data-animation="default"
              data-duration="400"
              role="banner"
              class="tutornavbar-2 w-nav"
            >
              <div class="tutorcontainer-2 w-container">
                <nav role="navigation" class="tutornav-menu-3 w-nav-menu">
                  <router-link
                    to="/"
                    class="tutornav-link-4 w-nav-link"
                    >Requests
                  </router-link>
                  <router-link
                    to="/seminars"
                    class="tutornav-link-4 w-nav-link w--current"
                    >Seminars
                  </router-link
                  ><router-link to="/inbox" class="tutornav-link-4 w-nav-link"
                    >Messages
                    <span v-if="user.unread > 0" class="tutorbadge">{{
                      user.unread
                    }}</span> </router-link
                  ><router-link
                    to="/payments"
                    class="tutornav-link-4 w-nav-link"
                    >Payments</router-link>
                  <router-link
                    to="/volunteering"
                    class="tutornav-link-4 w-nav-link"
                    >Volunteering</router-link>
                  <router-link to="/calendar" class="nav-link-4 w-nav-link"
                    >Calendar</router-link>
                  <router-link to="/donations" class="nav-link-4 w-nav-link"
                    >Donate</router-link>
                </nav>
                <div class="tutormenu-button-2 w-nav-button">
                  <div class="tutoricon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
          <div style="height: 100%; font-family: Poppins;">
            <div style="padding: 15px; margin:20px; background-color: white; height: 100%; border-radius: 8px;">
              <p style="color: #008000; font-size: 16px; margin-top: 10px;">{{ message }}</p>
              <h1>Class Schedule</h1>
              <div class="row">
                <div class="col">
                  <label for="date-time" class="col-2 col-form-label">Start Date</label>
                  <div class="col-10">
                    <input
                      class="form-control"
                      type="date"
                      required
                      v-model="seminar.startDate"
                    />
                  </div>
                </div>
                <div style="padding-left: 0px" class="col">
                  <label for="date-time" class="col-2 col-form-label">End Date</label>
                  <div class="col-10">
                    <input
                      class="form-control"
                      type="date"
                      required
                      v-model="seminar.endDate"
                    />
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col">
                  <label for="date-time" class="col-2 col-form-label">Start Time</label>
                  <div class="col-10">
                    <input
                      v-model="seminar.startTime"
                      class="form-control"
                      type="time"
                      required
                    />
                  </div>
                </div>
                <div style="padding-left: 0px" class="col">
                  <label for="date-time" class="col-2 col-form-label">Duration (min)</label>
                  <div class="col-10">
                    <input
                      v-model="seminar.duration"
                      class="form-control"
                      type="number"
                      required
                    />
                  </div>
                </div>
              </div>
              <h1 style="margin-top: 20px" >Class Description</h1>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Subjects</label>
                <input v-model="seminar.subjects" type="text" class="form-control" id="exampleFormControlInput1" placeholder="Physics">
              </div>
              <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Description</label>
                <textarea v-model="seminar.description" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
              </div>
              <h1 style="margin-top: 20px" >Class Payments</h1>
                <div class="col-10">
                  <input
                    v-model="seminar.price"
                    class="form-control"
                    placeholder="Pricing per seminar"
                    type="number"
                    required
                  />
                </div>
                <input style="margin-top: 25px;" v-model="seminar.free" class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                <label style="margin-top: 20px;" class="form-check-label" for="flexCheckDefault">
                  Free Seminar($0), No payments will be sent
                </label>
                <br>
              <button class="btn btn-primary" @click="seminarRequest" style="margin-top: 10px;" >Submit</button>
              </div>

          </div>
      </body>
    </html>
  </client-only>
</template>
-
<script>
import { mapGetters, mapActions } from 'vuex'
import getCSRF from '~/utils/getCSRF'

export default {
  data() {
    return {
      message: '',
      clicked: false,
      seminar: {
        startTime: "",
        startDate: "",
        endDate: "",
        duration: "",
        price: "",
        description: "",
        free: false,
      }
      
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
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ tutor: 'getTutor' }),
    ...mapGetters({ user: 'getUser' }),
  },
  methods: {
    logoutclick() {
      this.clicked = !this.clicked
    },
    addDays(date, days) {
        const newDate = new Date(date);
        newDate.setDate(date.getDate() + days);
        return newDate
    },

    recurringDates(startDate, endDate, interval) {
        let date = startDate;
        const dates = [];

        while ((date = this.addDays(date, interval)) < endDate) {
            dates.push(date);
        }

        return dates;
    },
    timeCalculations(){
      const startDate = new Date(this.seminar.startDate);
      startDate.setDate(startDate.getDate() - 7);
      const endDate = new Date(this.seminar.endDate);
      endDate.setDate(endDate.getDate() + 7);
      const interval = 7;
      const dates = this.recurringDates(startDate, endDate, interval);
      const startTime = this.seminar.startTime
      const timings = [];
      dates.forEach(function(date) {
          const todayDate = new Date(date).toISOString().slice(0, 10);
          const newDate = date.toString()
          const timeOffset = newDate.substring(30, 31)
          const time = todayDate + "T" + startTime + ":00-0" + timeOffset+":00";
          timings.push(time);
      });
      return timings
    },
    async seminarRequest(){
      const timings = this.timeCalculations();
      const sessionMinutes = this.seminar.duration;
      let minutes = sessionMinutes % 60;
      let hours = (sessionMinutes-minutes)/60;
      if(hours < 10){
        hours = "0" + hours.toString()
      }

      if(minutes < 10){
        minutes = "0" + minutes.toString()
      }
      const sessionDuration = hours + ':' + minutes + ":00";
      let totalPrice = this.seminar.price;
      totalPrice = totalPrice*timings.length;
      const csrfToken = await getCSRF()
      await fetch(process.env.API_URL + '/seminars/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify({
          times: timings,
          duration: sessionDuration,
          description: this.seminar.description,
          subjects: this.seminar.subjects,
          free: this.seminar.free,
          price: totalPrice,
        }),
      }).then((res) => {
        if(res.status===200 || res.status===201){
          this.message="Thank you for successfully creating a seminar with us!"
        }
        else if(res.status===400 || res.status===500){
          this.message="Oops! We believe there has been an error, please double-check all your fields"
        }
      })
    },
    ...mapActions(['fetchTutor', 'fetchUser']),

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
 
