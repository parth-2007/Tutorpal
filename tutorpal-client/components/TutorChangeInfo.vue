<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" media="print" onload="this.media='all'">
      </head>
      <body>
        <div :style="updateModal" class="tutordiv-block-22">
          <div
            style="
              border-radius: 8px;
              padding-bottom: 20px;
              height: 550px;
              font-family: Poppins;
            "
            class="tutordiv-block-23"
          >
            <div class="tutordiv-block-24">
              <img
                @click="updateModalValue()"
                src="../static/tutor/images/close-1.png"
                width="20"
                alt=""
              />
            </div>
            <h1 style="margin-top: 30px" class="tutorheading-10">Update Profile</h1>
            <div class="tutordiv-block-25">
              <TutorChangeInfoModal @modalSubmit="handleModalSubmit()" />
            </div>
          </div>
        </div>
        <div>
          <div class="tutorsection">
            <router-link to="/" class="tutorlink-block w-inline-block"
              ><img
                src="../static/tutor/images/logo.jpg"
                loading="lazy"
                width="260"
                srcset="
                  ../static/tutor/images/logo.jpg   500w,
                  ../static/tutor/images/logo.jpg   800w,
                  ../static/tutor/images/logo.jpg 1080w,
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
                    <div @click="logoutclick()" class="tutordropdown-toggle-2-copy w-dropdown-toggle">
                      <div id="name" class="tutortext-block-18">{{user.firstName}} {{user.lastName}}</div>
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
                    aria-current="page"
                    class="tutornav-link-4 w-nav-link"
                    >Requests</router-link
                  ><router-link
                    to="/inbox"
                    class="tutornav-link-4 w-nav-link"
                    >Messages
                    <span v-if="user.unread > 0" class="tutorbadge">{{ user.unread }}</span>
                    </router-link
                  ><router-link to="/payments" class="tutornav-link-4 w-nav-link"
                    >Payments</router-link
                  >
                  <router-link
                    to="/volunteering"
                    class="tutornav-link-4 w-nav-link"
                    >Volunteering</router-link>
                  <router-link to="/calendar" class="nav-link-4 w-nav-link"
                    >Calendar</router-link>
                </nav>
                <div class="tutormenu-button-2 w-nav-button">
                  <div class="tutoricon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tutordiv-block-48-copy">
          <div class="tutortext-block-23">Profile</div>
          <p class="tutorparagraph">
            This is your public profile, all of this information can be viewed
            by potential students.
          </p>
        </div>
        <div style="margin-bottom: 20px" class="tutorcolumns-5 w-row">
          <div class="tutorcolumn-16 w-col w-col-4">
            <img
              id="image2"
              loading="lazy"
              width="257"
              height="257"
              sizes="(max-width: 479px) 73vw, (max-width: 767px) 257px, (max-width: 991px) 28vw, 257px"
              alt=""
              :src="user.profilePic"
              class="tutorimage-11"
            />
          </div>
          <div class="tutorw-col w-col-8">
            <div>
              <h1 class="tutorheading-3">Subject: {{ tutor.subjects }}</h1>
              <div class="tutordiv-block-54">
                <div class="tutortext-block-32">
                  <strong class="tutorbold-text-3">
                    {{ user.firstName }} {{ user.lastName }}
                  </strong>
                </div>
              </div>
              <p style="padding-top: 20px overflow: hidden" class="tutorparagraph-7">
                <strong>Birth Date: </strong>{{ tutor.birthDate }}<br /><strong
                    >Qualification Description: </strong>{{tutor.qualifications}}
                <br><strong>Email: </strong>{{ user.email }}<br />
                <strong>Paypal Email: </strong>{{ tutor.paypalEmail }}<br />
                <strong>Education:</strong>
                {{ tutor.education }}<br /><strong
                    >Working/Subject Experience:</strong
                    >
                {{ tutor.profExp }} years<br /><strong>Teaching Experience: </strong>{{ tutor.teachExp }}
                years<br /><strong>Average Review:</strong>
                {{ tutor.averageReviews }}<br />
                <strong>Occupation: </strong>{{ tutor.occupation }}<br />
                <strong>Gender: </strong>{{ tutor.gender }}<br />
                <strong>Price: </strong>${{tutor.rates}} per hour <br />
                <strong>Bio: </strong>{{ tutor.bio}}<br />
                <strong>Availability: </strong>{{ tutor.availability}}<br />
                <strong style="padding-bottom: 10px;">Course Description: </strong>{{ tutor.whatYouTeach }}<br />
                <a
                  style="font-family: Poppins;"
                  :href="'https://www.tutorpal.org/tutors/'+tutor.id"
                  target="_blank"
                  ><strong>View my profile</strong>
                <br>
                </a>
              </p>
              <div style="margin-left: 50%;">
                <a
                  @click="updateModalValue"
                  style="margin-top: 10px;"
                  class="tutorbutton-10-copy-copy w-button"
                  >Update Information
                </a>
                <router-link
                  style="font-family: Poppins; padding-left: 10px;"
                  to="/timezone"
                  ><strong>Set my timezone</strong>
                </router-link>
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
import TutorChangeInfoModal from './TutorChangeInfoModal.vue'
export default {
  components: { TutorChangeInfoModal },
  data() {
    return {
      clicked: false,
      clicked1: false,
    }
  },
  head() {
    return {
      title: 'Account Information',
      link: [
        { rel:"stylesheet", type:"text/css", href: "/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ],
    }
  },
  computed: {
    logout() {
        return {
          display: this.clicked1 ? "flex" : "none"
        }
    },
    updateModal() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    ...mapGetters({ tutor: 'getTutor' }),
    ...mapGetters({ user: 'getUser' }),
  },
  async created() {
    await this.fetchTutor()
    await this.fetchUser()
  },
  methods: {
    logoutclick(){
      this.clicked1 = !this.clicked1
    },
    updateModalValue() {
      this.clicked = !this.clicked
    },
    async handleModalSubmit() {
      this.updateModalValue()
      await this.fetchTutor()
      await this.fetchUser()
    },
    ...mapActions(['fetchTutor', 'fetchUser']),
  },
}
</script>
<style>
.tutordiv-block-22 {
  position: fixed;
  z-index: 21;
  width: 100vw;
  display: none;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.3);
  -o-object-fit: contain;
  object-fit: contain;
}
.tutorbadge {
  position: absolute;
  top: 11px;
  right: 3px;
  padding: 2px 8px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>