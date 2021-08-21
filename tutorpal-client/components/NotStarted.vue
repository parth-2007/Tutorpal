<template>
  <no-ssr>
    <html
      data-wf-page="5f405fbdac064904ad639864"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <body style="background-color: rgba(65, 168, 211, 0.2); height: 100vh; padding-top: 60px;">
        <div style="width: 80vw; height: 80vh; background-color:white;border-width:0px; margin-top: 0px;" class="div-block-80">
          <h1 style="font-family: Poppins;">We are very sorry but your class has not started yet.</h1>
        </div>
      </body>
    </html>
  </no-ssr>
</template>
<script>
export default {
  head() {
    return {
      title: 'Class Not Started',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/main/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/main/css/normalize.css" },
      ]
    }
  },
  beforeMount() {
    const link = document.createElement('link');
    link.rel = 'stylesheet';       
    link.type = 'text/css';
    link.href = 'https://www.tutorpal.org/main/css/homepage-12.webflow.css';
    document.getElementsByTagName('HEAD')[0].appendChild(link);
  },
}
</script>
<style>
</style>
