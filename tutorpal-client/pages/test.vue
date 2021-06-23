<template>
  <div>
    <!-- <button @click="logSessions">log sessions</button> -->
    <button @click="addSessionHandler">add session</button>
    <button @click="removeSessionHandler">remove session</button>
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
    ...mapActions(['fetchSessions', 'addSession', 'removeSession']),
    ...mapGetters(['getStartedSessions']),
    addSessionHandler() {
      this.addSession([
        { hi: Math.floor(Math.random() * 5) },
        'startedSessions',
      ])
    },
    removeSessionHandler() {
      const startedSessions = this.getStartedSessions()
      this.removeSession([startedSessions[0], 'startedSessions'])
    },
  },
}
</script>