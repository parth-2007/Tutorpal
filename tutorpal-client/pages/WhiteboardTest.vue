<template>
  <client-only>
    <html
      data-wf-page="5f3c2694b3e9866a68ad2a10"
      data-wf-site="5f3c2694b3e98672caad2a0f"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body>
        <div style="width: 98vw; height: 550px;" id="wt-container"></div>
      </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'White Board Test',
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
  mounted(){
    const script = document.createElement('script')

    script.src = "https://www.whiteboard.team/dist/api.js"
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },
  methods: {
    setLoaded() {
      const wt = new api.WhiteboardTeam('#wt-container', {
          clientId: '322f4ec635688d506ad1bae2f1b21cb9',
          boardCode: 'humptydumptycacacccacacaccacac',
      });
      console.log(wt)
    }
  },
}
</script>
