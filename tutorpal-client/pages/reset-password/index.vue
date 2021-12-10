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
          media="print"
          onload="this.media='all'"
        />
      </head>
      <body>
        <router-link
          style="margin-top: 0px; margin-bottom: -30px; margin-left: 10px;"
          to="/"
          class="outcastlink-block w-inline-block"
          ><img
            src="https://www.tutorpal.org/_nuxt/img/logo.729d859.jpg"
            width="250"
            alt=""
            class="outcastimage"
        /></router-link>
         <form
            style="font-family: Poppins; margin-top: 25px; margin-left: 25px"
            @submit="handleSubmit"
         >
            <div style="width: 1000px" class="input-group mb-3">
               <input
               placeholder="Enter your account email here"
               class="form-control"
               type="email"
               v-model="email"
               required
               />
               <button class="btn btn-primary" @click="handleSubmit">Submit</button>
            </div>
        </form>
      </body>
    </html>
  </client-only>
</template>
<script>
import getCSRF from './../../utils/getCSRF'

export default {
   data() {
    return {
      email: '',
    }
  },
  head() {
    return {
      title: 'Reset your password here',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/student-main.webflow.css" },
      ]
    }
  },
  methods: {
   async handleSubmit(e) {
      e.preventDefault()
      await fetch(process.env.API_URL +'/auth/reset-password/', {
        credentials: 'include',
        method: 'POST',
        headers: {
          'X-CSRFToken': (await getCSRF()).success,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "email": this.email,
        }),
      }).then((res) => {
         console.log(res.status)
      })
    },
  }
}
</script>
