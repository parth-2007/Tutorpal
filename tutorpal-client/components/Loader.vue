<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <center>
        <div style="height: 90vh; display: table-cell; vertical-align: middle;">
          <img
            src="../static/student/images/logo.jpg"
            width="400"
            alt=""
          />
          <div class="load-bar">
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
          </div>
        </div>
      </center>>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'TutorPal',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/student-main.webflow.css" },
      ]
    }
  },
}
 
</script>
<style scoped>
.load-bar {
  position: relative;
  margin-top: 20px;
  width: 380px;
  height: 6px;
  background-color: #fdba2c;
}
.bar {
  content: "";
  display: inline;
  position: absolute;
  width: 0;
  height: 100%;
  left: 50%;
  text-align: center;
}
.bar:nth-child(1) {
  background-color: #da4733;
  -webkit-animation: loading 3s linear infinite;
          animation: loading 3s linear infinite;
}
.bar:nth-child(2) {
  background-color: #41a8d3;
  -webkit-animation: loading 3s linear 1s infinite;
          animation: loading 3s linear 1s infinite;
}
.bar:nth-child(3) {
  background-color: #fdba2c;
  -webkit-animation: loading 3s linear 2s infinite;
          animation: loading 3s linear 2s infinite;
}
@-webkit-keyframes loading {
    from {left: 50%; width: 0;z-index:100;}
    33.3333% {left: 0; width: 100%;z-index: 10;}
    to {left: 0; width: 100%;}
}
@keyframes loading {
    from {left: 50%; width: 0;z-index:100;}
    33.3333% {left: 0; width: 100%;z-index: 10;}
    to {left: 0; width: 100%;}
}
</style>