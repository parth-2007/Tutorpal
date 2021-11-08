<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="/main/css/homepage-12.webflow.css" media="none" onload="if(media!='all')media='all'">
      </head>
      <body>
          <div class="homediv-block-3">
            <router-link
              style="margin-top: 0px; margin-bottom: -30px"
              to="/"
              class="homelink-block w-inline-block"
              ><img
                src="../static/student/images/logo.jpg"
                width="250"
                alt=""
                class="homeimage"
            /></router-link>
            <div class="homediv-block-4"><router-link to="/login" class="homelink-2-copy">login</router-link></div><router-link to="/register" class="homebutton w-button">register</router-link></div>
          <div data-w-id="f0d0fabc-c4a9-309e-3cfe-1d2993a9c551" class="homediv-block-24">
          <img 
            src="../static/student/images/team_pic.jpg" 
            loading="lazy" 
            width="639" 
            srcset="../static/student/images/team_pic.jpg 500w, ../static/student/images/team_pic.jpg 800w" 
            class="homeimage-13"
          >
          </div>
          <p class="homeparagraph-8">Our members in the team are Parth Saxena, Sarosh Thalappil, and Pratham Saxena.
          <ul>
            <li> Sarosh Thalappil is a co-founder and one of the developers of the TutorPal platform, currently a 10th grader attending Scripps Ranch High School with programming knowledge in Python, HTML, and more languages. </li> 
            <li> Parth Saxena, a 8th grader at Thurgood Marshall Middle School with a background in Python, JavaScript, CSS, HTML, and more, is accompanying Sarosh in the development of the TutorPal platform. </li> 
            <li> Pratham Saxena is the website content manager, designer, the testing lead, and marketing lead for the TutorPal platform. He is currently a senior at SRHS and has a programming background in Java, C#, JavaScript, CSS, and HTML.</li>
          </ul>
          TutorPal’s main purpose is to link students and tutors from any area to receive assistance. To prevent struggle in the search for tutors, TutorPal instantly provides the best tutors.<br></p>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Our team',
      link: [
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
        { rel:"stylesheet", type:"text/css", href: "/student/css/student-main.webflow.css" },
      ]
    }
  },
}
</script>
