<template>
  <div>
    <!-- <button @click="logSessions">log sessions</button> -->
    <button @click="addSessionHandler">add session</button>
    <br />
    {{ startedSessions }}
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: mapGetters({ startedSessions: 'getStartedSessions' }),
  async created() {
    await this.fetchSessions('startedSessions')
  },
  methods: {
    ...mapActions(['fetchSessions', 'addSession']),
    ...mapGetters(['getStartedSessions']),
    addSessionHandler() {
      this.addSession([{ hi: 'hi' }, 'startedSessions'])
    },
  },
}
</script>
