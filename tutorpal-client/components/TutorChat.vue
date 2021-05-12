
<template>
  <client-only>
    <html
      data-wf-page="5f600218af481481a99ffa6a"
      data-wf-site="5f600218af4814e3759ffa69"
    >
      <head>
        <meta charset="utf-8" />
      </head>
      <body style="height: 100vh;" class="body">
        <router-link to="/inbox" aria-current="page" style="font-family: Poppins; margin-left: 5%; padding-top: 20px;" class="link-block w-inline-block w--current">Go back to contacts</router-link>
        <div style="border-radius: 8px;" class="div-block-80">
          <div class="div-block-71"><img src="../static/student/images/user-2.png" loading="lazy" width="130" height="130" srcset="../static/student/images/user-2.png 500w, ../static/student/images/user-2.png 512w" sizes="74px" alt="">
              <div class="div-block-72">
                <h1 class="heading-3" id="fullname" style="font-size: 30px;">Johnny Lawrence</h1>
              </div>
            </div>
        </div>
        <!-- display chat messages -->
        <div class="wrapper" id="chat-items">
          <div>
            <div class="chat_item_away">
              <div class="div-block-61">
                <p class="paragraph-6">{message.message} </p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_here">
              <div class="div-block-61-copy">
                <p class="paragraph-6">{message.message}</p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_away">
              <div class="div-block-61">
                <p class="paragraph-6">{message.message} </p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_here">
              <div class="div-block-61-copy">
                <p class="paragraph-6">{message.message}</p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_away">
              <div class="div-block-61">
                <p class="paragraph-6">{message.message} </p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_here">
              <div class="div-block-61-copy">
                <p class="paragraph-6">{message.message}</p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_away">
              <div class="div-block-61">
                <p class="paragraph-6">{message.message} </p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
            <div class="chat_item_here">
              <div class="div-block-61-copy">
                <p class="paragraph-6">{message.message}</p>
                <div class="text-block-40"><em class="italic-text">{message.timestamp}</em></div>
              </div>
            </div>
          </div>
        </div>
        <input style="width: 80%; margin-right: 10%; margin-left: 10%; font-family: Poppins; margin-top: 20px;"
            class="form-control"
            placeholder="Send a message"
          />
     </body>
    </html>
  </client-only>
</template>
<script>
export default {
  head() {
    return {
      title: 'Chat with John',
      link: [
        { rel:"stylesheet", type:"text/css", href:"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" },
        { rel:"stylesheet", type:"text/css", href:"/student/css/webflow.css" },
        { rel:"stylesheet", type:"text/css", href:'/student/css/student-main.webflow.css' },
        { rel:"stylesheet", type:"text/css", href:"/student/css/normalize.css" },
      ]
    }
  },
}
</script>
<style scoped>
.wrapper {
  overflow-y:auto;
  margin-top: 20px;
  margin-right: 10%;
  margin-left: 10%;
  padding-top: 20px;
  padding-bottom: 20px;
  background-color: #fff;
  padding-left: 20%;
  padding-right: 20%;
  border-radius: 8px;
  height: 58%;
}
</style>