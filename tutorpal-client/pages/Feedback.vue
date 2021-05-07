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
        <div style="height: auto; font-family: Poppins; padding-bottom: 20px; border-width: 2px; border-color: skyblue;" class="div-block">
          <div>
            Please let us know what user feedback you have so we can continue to improve our product. We will work on these immediately, if you would like to report a bug, please do so <router-link to="/bugs">here</router-link> 
            <form>
              <div style="margin-top: 20px;" class="mb-3">
                <label for="feedback" class="form-label">Feedback</label>
                <textarea style="height:250px;" class="form-control" id="feedback" rows="3"></textarea>
                <button class="btn btn-primary" style="margin-top: 10px;">Submit</button>
              </div>
            </form>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Feedback',
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
}
</script>
