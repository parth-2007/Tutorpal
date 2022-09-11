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
          times: ['2022-09-16', '2022-09-23', '2022-09-30'],
          time_start: '20:05',
          time_end: '21:05',
          description: 'test',
          subjects: 'sdfsd',
          call_url: 'sdfsf',
          free: true,
        }),
      }).then((res) => res.json())
      this.data = data
    },
  },
}
</script>