<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="/outcast/css/last-project-afcf8d.webflow.css" media="none" onload="if(media!='all')media='all'">
      </head>
      <body>
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
  data(){
    return{
      level: "",
      description: ""
    }
  },
  head() {
    return {
      title: 'Bugs',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  methods: {
    async bugformhandler(){
      const csrfToken = await getCSRF()
      await fetch('/api/bugs/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify({
          "bug": this.description,
          "level": parseInt(this.level)
        }),
      })
    }
  }
}
 
</script>
