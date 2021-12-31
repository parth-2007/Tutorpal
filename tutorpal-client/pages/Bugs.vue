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
            padding-bottom: 0x;
            border-color: skyblue;
            border-width: 2.5px;
          "
          class="outcastdiv-block"
        >
          <div>
            <h1 style="font-size: 30px"><strong>Bug Reports</strong></h1>
            Please let us know what bugs you are facing so we can fix them
            immediately. We use this information to immediately fix issues we
            have not yet come across. If you have any feedback, please do so
            <router-link to="/feedback">here</router-link>
            <form id="form-wrapper" @submit="bugformhandler">
              <div style="margin-top: 20px" class="outcastmb-3">
                <label for="bugs" class="form-label">Bug Description</label>
                <textarea
                  v-model="description"
                  style="height: 250px"
                  class="form-control"
                  id="bugs"
                  rows="3"
                  name="bugs"
                  placeholder="Bug description"
                ></textarea>
                <p style="color: hsla(0, 100%, 64%, 1)">
                  {{ errors.description }}
                </p>
                <label for="buglevel" class="form-label"
                  >Bug Severity (1=low, 10=high)</label
                >
                <select
                  v-model="level"
                  style="margin-top: 15px"
                  class="form-select"
                  id="buglevel"
                  name="buglevel"
                  aria-label="Default select example"
                  aria-placeholder="Severity of bug (1 = low, 10 = high)"
                >
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                  <option value="6">6</option>
                  <option value="7">7</option>
                  <option value="8">8</option>
                  <option value="9">9</option>
                  <option value="10">10</option>
                </select>
                <p style="color: hsla(0, 100%, 64%, 1)">
                  {{ errors.level }}
                </p>
              </div>
              <button
                type="submit"
                class="btn btn-primary"
                style="margin-top: 10px"
              >
                Submit
              </button>
            </form>
            <br />
            <p style="color: chartreuse" id="form-response">
              {{ response }}
            </p>
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
      level: null,
      description: null,
      errors: {
        level: null,
        description: null,
      },
      response: null,
    }
  },
  head() {
    return {
      title: 'Bugs',
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
    async bugformhandler(e) {
      if (!this.level > 0) {
        this.errors.level = 'Please select a value greater than 0'
        return
      }
      if (!this.description.length > 0) {
        this.errors.level = 'Please put a description here'
        return
      }
      if (this.description.length > 1024) {
        this.errors.level = 'Description length too long'
        return
      }
      this.errors.level = null
      this.errors.description = null
      e.preventDefault()
      const csrfToken = await getCSRF()
      await fetch(process.env.API_URL + '/bugs/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify({
          bug: this.description,
          level: parseInt(this.level),
        }),
      })
      this.level = ''
      this.description = ''
      this.response = 'Successfully submitted a bug report'
    },
  },
}
</script>