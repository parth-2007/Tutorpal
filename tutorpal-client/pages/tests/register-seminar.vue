<template>
  <div>
    <button @click="sendRequest">register for a seminar</button>
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
      const data = await fetch(process.env.API_URL + '/seminars/15/register/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'X-CSRFToken': csrfToken.success,
        },
      }).then((res) => res.json())
      this.data = data
    },
  },
}
</script>