<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body id="body" style="min-height: 100vh" class="body-3">
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
                    ><router-link to="/inbox" class="nav-link-4 w-nav-link"
                      >Messages<span v-if="user.unread > 0" class="tutorbadge">{{
                        user.unread
                      }}</span></router-link
                    ><router-link to="/requests" class="nav-link-4 w-nav-link"
                      >Requests</router-link
                    ><router-link
                      to="/payments"
                      class="nav-link-4 w-nav-link"
                      >Payments</router-link
                    ><router-link to="/calendar" class="nav-link-4 w-nav-link w--current"
                    >Calendar</router-link>
                  </nav>
                  <div class="menu-button-2 w-nav-button">
                    <div class="icon-2 w-icon-nav-menu"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div style="display: flex; justify-content: center; padding: 20px;">
          <div id="container" ref="container">
            <div id="header">
              <div id="monthDisplay">{{monthDisplay}}</div>
            </div>

            <div id="weekdays">
              <div>Sunday</div>
              <div>Monday</div>
              <div>Tuesday</div>
              <div>Wednesday</div>
              <div>Thursday</div>
              <div>Friday</div>
              <div>Saturday</div>
            </div>
              <div id="calendar" ref="calendar">    
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
// import getCSRF from '../utils/getCSRF'

export default {
  data(){
    return {
      monthDisplay:'',
      calendarData: [],
      q: '',
      clicked: false,
    }
  },
  head() {
    return {
      title: 'My Calendar',
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
          href: '/student/css/calendar.css',
        },
      ],
    }
  },
  async mounted(){
    await this.fetchStudent()
    await this.fetchUser()
    const url =
      process.env.API_URL + '/sessions/my_sessions'
    const data = await fetch(url, {
      credentials: 'include',
    }).then((res) => res.json())
    this.calendarData = data.results;
    this.calendar()
  },
  computed: {
    logout() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ student: 'getStudent' }),
    ...mapGetters({ user: 'getUser' }),
  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['fetchUser', 'fetchStudent']),
    convertTime,
    logoutclick() {
      this.clicked = !this.clicked
    },
    submitSearch() {
      this.$router.push("/search/"+this.q);
    },
    calendar(){
      const events = []
      const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      const calendar = this.$refs.calendar
      const dt = new Date();

      const day = dt.getDate();
      const month = dt.getMonth();
      const year = dt.getFullYear();

      const firstDayOfMonth = new Date(year, month, 1);
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      this.monthDisplay = `${dt.toLocaleDateString('en-us', { month: 'long' })} ${year}`;
      const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
      });

      calendar.innerHTML = '';

      const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);
      this.calendarData.forEach(function(x){
        if(x.accepted === true){
          const splitDate = x.date.split('-');
          if(splitDate.count === 0){
              return null;
          }

          const year = splitDate[0];
          const month = splitDate[1];
          const day = splitDate[2]; 
          const date = Number(month) + "/" + Number(day) + "/" + year
          const title = "Class with " + x.tutor.user.first_name + ": " + convertTime(x.time_start) + " - " + convertTime(x.time_end)
          /* eslint-disable */
          events.push({
            date: date,
            title: title
          })
          /* eslint-enable */
        }
        
      })
      for(let i = 1; i <= paddingDays + daysInMonth; i++) {
        const daySquare = document.createElement('div');
        daySquare.classList.add('day');
        const dayString = `${month + 1}/${i - paddingDays}/${year}`;
        if (i > paddingDays) {
          daySquare.innerText = i - paddingDays;
          const eventForDay = events.filter(e => e.date === dayString);
          if (i - paddingDays === day) {
            daySquare.id = 'currentDay';
          }

          if (eventForDay.length!==0) {
            const eventDiv = document.createElement('div');
            eventForDay.forEach(function(x){
              console.log(x)
              eventDiv.innerHTML +=`<div style="margin-top: 10px;">${x.title}</div>`
            })
            eventDiv.classList.add('event');
            daySquare.appendChild(eventDiv);
            console.log(eventDiv)
          }
        } else {
          daySquare.classList.add('padding');
        }
        calendar.appendChild(daySquare); 
        this.$refs.container.style.display = "block";
      }
    }
  },
}
</script>
<style scoped>
.tutorbadge {
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