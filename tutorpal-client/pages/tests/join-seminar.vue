<template>
  <div>
    <button @click="sendRequest">get meeting url</button>
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
      const data = await loggedInFetch('/seminars/21/join_seminar')
      this.data = data
    },
  },
}
</script>