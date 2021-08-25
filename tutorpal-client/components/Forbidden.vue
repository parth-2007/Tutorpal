<template>
  <client-only>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body>
        <router-link to="/" class="outcastlink-block-4 w-inline-block"
          ><img src="../static/student/images/logo.jpg" loading="lazy" width="200" alt=""
        /></router-link>
        <div class="outcastcolumns-6 w-row">
          <div class="outcastcolumn-6 w-col w-col-6">
            <div class="outcastdiv-block-41">
              <h1 class="outcastheading-3">Oops!</h1>
              <p class="outcastparagraph-8">
                You don't have the permission to view this page. Access Denied.
              </p>
              <div class="outcasttext-block-19">Error Code: 403 Forbidden</div>
            </div>
          </div>
          <div class="w-col w-col-6">
            <img style="margin-left: 60px" src="../static/outcast/images/no-entry.png" width="490" />
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
      title: '404 Forbidden',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
}
</script>
<style>
</style>
