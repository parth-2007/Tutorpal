<template>
  <client-only>
    <html
      data-wf-page="5f5844923df4f0c1c6587323"
      data-wf-site="5f5844923df4f032aa587322"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <div style="margin-left: 40px; margin-top: 20px">
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
        <div class="search">
          <form
            style="margin-left: 0px; margin-bottom: 40px"
            action="/search"
            class="stuff w-form"
          >
            <img
              src="../static/student/images/search-1.png"
              loading="lazy"
              width="25"
              height="25"
              srcset="
                ../static/student/images/search-1-p-500.png 500w,
                ../static/student/images/search-1.png       512w
              "
              sizes="(max-width: 767px) 25px, (max-width: 991px) 3vw, (max-width: 1919px) 25px, 1vw"
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
          <div
            v-for="tutor in tutordata.results"
            :key="tutor.id"
            style="margin-bottom: 20px"
            id="posts"
          >
            <router-link
              :to="'/tutors/' + tutor.id"
              class="link-block-2 w-inline-block"
            >
              <div style="line-height: 14px" class="div-block-54">
                <img
                  :src="tutor.user !== undefined ? tutor.user.profile_pic : ''"
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
                      tutor.user !== undefined ? tutor.user.first_name : ''
                    }}
                    {{
                      tutor.user !== undefined ? tutor.user.last_name : ''
                    }}</strong
                  >
                </div>
                <div class="text-block-21-copy">
                  Subject: {{ tutor.subjects }}
                </div>
                <div class="text-block-21-copy-2">
                  Price: ${{ tutor.rates }} hourly
                </div>
                <div class="text-block-21-copy-2">
                  Degree: {{ tutor.education }}
                </div>
                <div class="text-block-21-copy-2">
                  Education: {{ tutor.major }} at {{ tutor.school }}, GPA of
                  {{ tutor.gpa }}
                </div>
                <div class="text-block-21-copy-2">
                  Reviews: {{ tutor.average_reviews }} Stars
                </div>
                <div class="text-block-21-copy-2">
                  Occupation: {{ tutor.occupation }}
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </html>
  </client-only>
</template>
<script>
export default {
  data() {
    return {
      tutordata: [],
    }
  },
  head() {
    return {
      title: 'Find a Tutor',
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
  async created() {
    const tutorData = await fetch(
      process.env.API_URL + '/tutors/search/?q=' + this.$route.query.q + '/',
      {
        credentials: 'include',
      }
    )
      .then((res) => res.json())
      .catch(() => ({ error: 'client error' }))
    this.tutordata = tutorData
  },
}
</script>
