<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          media="none"
          onload="if(media!='all')media='all'"
        />
      </head>
      <body>
        <div :style="updatemodal" class="div-block-22">
          <div
            style="border-radius: 8px; padding-bottom: 20px; height: 550px"
            class="div-block-23"
          >
            <div class="div-block-24">
              <img
                @click="updateModalValue()"
                src="../static/student/images/close-1.png"
                width="20"
                alt=""
              />
            </div>
            <h1 style="margin-top: 30px" class="heading-10">Update Profile</h1>
            <div class="div-block-25">
              <StudentChangeInfoForm @modalSubmit="updateModalValue()" />
            </div>
          </div>
        </div>
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
                      @click="logoutClick()"
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
                    >Messages
                    <span class="tutorbadge">{{
                      user.unread
                    }}</span> </router-link
                  ><router-link to="/requests" class="nav-link-4 w-nav-link"
                    >Requests</router-link
                  ><router-link to="/payments" class="nav-link-4 w-nav-link"
                    >Payments</router-link
                  >
                </nav>
                <div class="menu-button-2 w-nav-button">
                  <div class="icon-2 w-icon-nav-menu"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="div-block-67">
          <div class="columns-5 w-row">
            <div
              class="
                column-16
                w-col w-col-4 w-col-small-small-stack w-col-tiny-tiny-stack
              "
            >
              <img
                :src="user.profilePic"
                id="profile"
                loading="lazy"
                width="257"
                height="257"
                sizes="(max-width: 479px) 100vw, (max-width: 767px) 33vw, (max-width: 991px) 21vw, (max-width: 1439px) 19vw, 250px"
                alt=""
                class="image-11"
              />
            </div>
            <div
              class="
                column-17
                w-col w-col-8 w-col-small-small-stack w-col-tiny-tiny-stack
              "
            >
              <div class="div-block-69">
                <h1 class="heading-3">
                  {{ user.firstName }} {{ user.lastName }}
                </h1>
                <p class="paragraph-7">
                  <strong>Birth Date: {{ student.birthDate }}</strong
                  ><small id="bday" style="font-size: 14px"></small
                  ><br /><strong>Parent Email: {{ student.parentEmail }}</strong
                  ><small style="font-size: 14px" id="email"></small
                  ><br /><strong>Student Email: {{ user.email }}</strong
                  ><small style="font-size: 14px" id="parent"></small>
                </p>
                <a @click="updateModalValue()" class="b10 w-button"
                  >Update Information</a
                >
              </div>
            </div>
          </div>
        </div>
        <div
          style="padding-top: 40px; padding-bottom: 40px; height: 100%"
          class="body-3"
        >
          <h1
            style="text-align: center; margin-bottom: 15px; font-size: 36px"
            class="heading-14"
          >
            Completed Classes
          </h1>
          <div
            v-for="completed in pastSessions"
            :key="completed.id"
            style="background-color: #fff; margin-right: 10%; margin-left: 10%"
            class="i"
          >
            <div class="div-block-51-copy">
              <img
                src="student/images/user-2.png"
                loading="lazy"
                width="75"
                height="75"
                srcset="
                  student/images/user-2.png 500w,
                  student/images/user-2.png 512w
                "
                sizes="100px"
                alt=""
                class="image-15"
              />
              <div class="text-block-26">
                Tutor: {{ completed.tutor.user.firstName }}
                {{ completed.tutor.user.lastName }}
              </div>
              <p class="paragraph-2">
                <strong class="bold-text">Schedule <br /></strong>First Session:
                {{ completed.date }}<br />Tutor:
                {{ completed.tutor.user.firstName }}
                {{ completed.tutor.user.lastName }}<br />Duration:
                {{ completed.duration }}<br />Amount: ${{ completed.price
                }}<br />Trial: {{ completed.free }}
              </p>
            </div>
            <p class="paragraph-2-copy">
              <strong class="bold-text">Student Information</strong
              ><br />Description: <strong class="bold-text"> </strong
              >{{ completed.description }}
            </p>
            <div class="text-block-27-copy">
              Congratulations! You have finished this class, let us know how it
              went in your reviews.
            </div>
            <div
              style="font-family: Poppins; margin-left: 10px; margin-top: 15px"
            >
              <div style="margin-left: 0px" class="columns-2-copy w-row">
                <div class="w-col w-col-6">
                  <div>
                    <select
                      ref="select"
                      v-model="stars"
                      style="margin-top: 0px"
                      class="form-select"
                      id="stars"
                      aria-label="Default select example"
                      required
                    >
                      <option value="1">1 Star</option>
                      <option value="2">2 Stars</option>
                      <option value="3">3 Stars</option>
                      <option value="4">4 Stars</option>
                      <option selected value="5">5 Stars</option>
                    </select>
                    <textarea
                      ref="description"
                      v-model="description"
                      style="
                        height: 150px;
                        margin-top: 20px;
                        margin-bottom: 20px;
                      "
                      class="form-control"
                      id="description"
                      placeholder="Enter Description"
                      rows="3"
                      required
                    ></textarea>
                    <button
                      @click="createReview(completed.tutor.id)"
                      class="btn btn-primary"
                      name="review"
                    >
                      Post Review
                    </button>
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
import { mapActions, mapGetters } from 'vuex'
import getCSRF from '../utils/getCSRF'
import StudentChangeInfoForm from './StudentChangeInfoForm.vue'

export default {
  components: { StudentChangeInfoForm },
  data() {
    return {
      clicked: false,
      clicked1: false,
      stars: 5,
      description: '',
    }
  },
  head() {
    return {
      show: false,
      title: 'Account Information',
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
    updatemodal() {
      return {
        display: this.clicked ? 'flex' : 'none',
      }
    },
    logout() {
      return {
        display: this.clicked1 ? 'flex' : 'none',
      }
    },
    ...mapGetters({
      student: 'getStudent',
      user: 'getUser',
      pastSessions: 'getPastSessions',
    }),
  },
  async created() {
    await this.fetchUser()
    await this.fetchSessions('pastSessions')
  },
  methods: {
    updateModalValue() {
      this.clicked = !this.clicked
    },
    logoutClick() {
      this.clicked1 = !this.clicked1
    },
    async createReview(tutorId) {
      const csrfToken = await getCSRF()
      await fetch('/api/reviews/', {
        credentials: 'include',
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken.success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student: this.user.studentPk,
          stars: parseInt(this.stars),
          description: this.description,
          tutor: tutorId,
        }),
      }).then((res) => {
        let error = null
        if (res.status === 403) {
          error = 'You have already posted a review for this tutor.'
        } else if (res.status === 500) {
          error = 'Please check your inputs and make sure they are not empty.'
        } else if (res.status === 404) {
          error =
            'We are dealing with some issues, please try again at a later time. Sorry for the inconvenience.'
        }
        if (error) {
          alert(error)
        }
        this.description = ''
        this.stars = undefined
      })
    },
    ...mapActions(['fetchUser', 'fetchStudent', 'fetchSessions']),
    ...mapGetters(['getPastSessions']),
  },
}
</script>
<style>
.div-block-22 {
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
