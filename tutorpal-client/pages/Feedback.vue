<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
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
        <router-link
          style="margin-top: 0px; margin-bottom: -30px"
          to="/"
          class="outcastlink-block w-inline-block"
          ><img
            src="../static/student/images/logo.jpg"
            width="250"
            alt=""
            class="outcastimage"
        /></router-link>
        <div
          style="
            height: auto;
            font-family: Poppins;
            padding-bottom: 20px;
            border-width: 2px;
            border-color: skyblue;
          "
          class="outcastdiv-block"
        >
          <div>
            Please provide any user feedback you may have so we can continue to
            improve the platform. We will work on these suggestions immediately.
            If you would like to report a bug, please do so
            <router-link to="/bugs">here</router-link>
            <form>
              <div style="margin-top: 20px" class="outcastmb-3">
                <label for="feedback" class="form-label">Feedback</label>
                <textarea
                  v-model="text"
                  style="height: 250px"
                  class="form-control"
                  id="feedback"
                  rows="3"
                ></textarea>
              </div>
              <button
                @submit="feedbackhandler()"
                class="btn btn-primary"
                style="margin-top: 10px"
              >
                Submit
              </button>
            </form>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import getCSRF from '../utils/getCSRF'

export default {
  data() {
    return {
      text: '',
    }
  },
  head() {
    return {
      title: 'Feedback',
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
    async feedbackhandler(e) {
      e.preventDefault()
      await fetch(process.env.API_URL + '/feedback/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': (await getCSRF()).success,
        },
        body: JSON.stringify({ text: this.text }),
      })
    },
  },
}
</script>
