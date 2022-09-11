<template>
  <div>
    <button @click="sendRequest">create seminar</button>
    <pre>{{ data }}</pre>
  </div>
</template>
<script>
import getCSRF from '~/utils/getCSRF'
export default {
  data() {
    return {
      data: '',
    }
  },
  methods: {
    async sendRequest() {
      const csrfToken = await getCSRF()
      const data = await fetch(process.env.API_URL + '/seminars/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken.success,
        },
        body: JSON.stringify({
          times: [
            '2022-09-16T20:05:00-07:00', // yyyy-mm-ddThh:mm:ss-psttoutc
            '2022-09-23T20:05:00-07:00',
            '2022-09-30T20:05:00-07:00',
          ],
          duration: '01:00:00',
          description: 'test',
          subjects: 'sdfsd',
          free: true,
        }),
      }).then((res) => res.json())
      this.data = data
    },
  },
}
</script>