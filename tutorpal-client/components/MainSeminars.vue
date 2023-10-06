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
      <body>
        <div id="main">
          <div class="div-block-55">
            <div class="section">
              <router-link
                style="margin-top: 0px; margin-bottom: -30px"
                to="/"
                class="link-block w-inline-block"
                ><img
                  src="../static/student/images/logo.jpg"
                  width="250"
                  alt=""
                  class="image"
              /></router-link>
              <div style="margin-top: 15px" class="div-block-4">
                <div class="stuff w-form">
                  <img
                    src="../static/student/images/search-1.png"
                    loading="lazy"
                    width="25"
                    height="25"
                    srcset="
                      ../static/student/images/search-1.png 500w,
                      ../static/student/images/search-1.png 512w
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
                  />
                </div>
              </div>
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
  methods: {
    convertTime,
    submitSearch() {
      this.$router.push("/search/"+this.q);
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