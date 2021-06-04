<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body><router-link to="/" aria-current="page" class="link-block w-inline-block w--current"><img src="../static/main/images/logo.jpg" loading="lazy" width="250" srcset="../static/main/images/logo-p-500.jpeg 500w, ../static/main/images/logo-p-800.jpeg 800w, ../static/main/images/logo-p-1080.jpeg 1080w, ../static/main/images/logo.jpg 1432w" sizes="(max-width: 479px) 100vw, 250px" alt="" class="image"></router-link>
        <div style="height: auto; font-family: Poppins; padding-bottom: 0x; border-color: skyblue; border-width: 2.5px;" class="div-block">
          <div>
            <h1 style="font-size: 30px;"><strong>Bug Reports</strong></h1>
            Please let us know what bugs you are facing so we can fix them immediately. We use this information to immediately fix issues we have not yet come across. If you have any feedback, please do so <router-link to="/feedback">here</router-link>
            <form id="form-wrapper">
              <div style="margin-top: 20px;" class="mb-3">
                <label for="bugs" class="form-label">Bugs</label>
                <textarea v-model="description" style="height:250px;" class="form-control" id="bugs" rows="3"></textarea>
                <select v-model="level" style="margin-top: 15px;" class="form-select" id="buglevel" aria-label="Default select example">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option selected value="5">5</option>
                  <option value="6">6</option>
                  <option value="7">7</option>
                  <option value="8">8</option>
                  <option value="9">9</option>
                  <option value="10">10</option>
                </select>
              </div>
            </form>
            <button @click="bugformhandler()" class="btn btn-primary" style="margin-top: 10px;">Submit</button>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
import getCSRF from '../utils/getCSRF'

export default {
  head() {
    return {
      title: 'Bugs',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/outcast/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/outcast/css/last-project-afcf8d.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/outcast/css/normalize.css" },
        {
          rel: 'stylesheet',
          type: 'text/css',
          href:
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
        },
        {
          type: 'text/js',
          href:
            'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js',
        },
      ]
    }
  },
  data(){
    return{
      level: "",
      description: ""
    }
  },
  methods: {
    async bugformhandler(){
      const bugform = {
        "bug": this.description,
        "level": parseInt(this.level)
      }
      const csrfToken = await getCSRF()
      await fetch('/api/bugs/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify(bugform),
      })
    }
  }
}
 
</script>
