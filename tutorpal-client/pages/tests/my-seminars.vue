<template>
  <div>
    <button @click="sendRequest">list my seminars</button>
    <pre>{{ data }}</pre>
  </div>
</template>
<script>
import loggedInFetch from '~/utils/loggedInFetch'
export default {
  data() {
    return {
      data: '',
    }
  },
  methods: {
    async sendRequest() {
      const data = await loggedInFetch('/seminars/my_seminars')
      this.data = data
    },
  },
}
</script>