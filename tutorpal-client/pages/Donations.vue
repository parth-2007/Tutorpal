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
          media="none"
          onload="if(media!='all')media='all'"
        />
      </head>
      <body>
        <router-link
          style="margin-top: 0px; margin-bottom: -30px"
          to="/"
          class="outcastlink-block w-inline-block"
          ><img
            src="../static/student/images/logo.jpg"
            width="250"
            alt=""
            class="outcastimage"
        /></router-link>
        <div
          style="
            height: auto;
            font-family: Poppins;
            padding-bottom: 20px;
            border-width: 2px;
            border-color: skyblue;
          "
          class="outcastdiv-block"
        >
          <div>
            <strong style="font-size:36px;">Donate Now</strong>
            <br>
            Please donate for our external services and efforts to setting up, supporting, and making sure your classes/seminars go smoothly. We are proud of our low prices and people like you support us by providing donations that we can use to uphold the platform's infrastructure. We rely largely on donations to carry out our services and to support our backend. The TutorPal team would appreciate it if you could donate today, thank you!
                <p style="color: hsla(0, 100%, 64%, 1); margin-top:25px;">{{ message }}</p>
                <div style="max-width: 750px; min-width:150px; margin-bottom:25px;" class="form-floating">
                  <input v-model="amount" v-on:input="onEnter" type="text" class="form-control" id="floatingPassword" placeholder="Amount">
                  <label for="floatingPassword">Amount (ex. $5.00)</label>
                </div>
            
            <div ref="paypal"></div>
          </div>
        </div>
      </body>
    </html>
  </client-only>
</template>
<script>

export default {
  data() {
    return {
      amount: '',
      message: '',
    }
  },

  mounted() {
    const script = document.createElement('script')
    script.src = 'https://www.paypal.com/sdk/js?client-id=Ae0zJYc6uq0r19vdNLW2TedQ86i7_FTrS7s_3pwgU5ePOXriAibXuXssw_Nbc5jOg7JOUvU4e7q_LkaT&enable-funding=venmo&currency=USD'
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },

  head() {
    return {
      title: 'Donations',
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
  methods: {
    onEnter() {
      if(parseFloat(this.amount) < 1.00){
        this.message = "Sorry, the amount must be at least $1 as transactions and payment fees will take away from the final donation."
       }
       else if(isNaN(parseFloat(this.amount)) || parseFloat(this.amount) <= 0){
        this.message = "The amount you have entered must be a positive number."
       }
       else{
        this.message = "Click the below buttons to proceed with paying your donation."
       }
    },

    setLoaded() {
      window.paypal
        .Buttons({
          style: {
            color: 'blue',
            shape: 'pill',
            label: 'pay',
            height: 40,
          },
          createOrder: function(data, actions) {
              console.log(parseFloat(this.amount))
              return actions.order.create({
                purchase_units: [{"amount":{"currency_code":"USD","value":1}}]
              });
          },

        onApprove: function(data, actions) {
          return actions.order.capture().then(function(orderData) {
            
            // Full available details
            console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));

            // Show a success message within this page, e.g.
            this.message = "Thank you for your donation!"
            console.log("success")
            // Or go to another URL:  actions.redirect('thank_you.html');
            
          });
        },
          onError: () => {
            this.$router.push('/donations')
          },
        })
        .render(this.$refs.paypal)
      }
  },
}
</script>
