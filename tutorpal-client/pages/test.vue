<template>
  <div>
    <button @click="logSessions">log sessions</button>
    <button @click="addSession">add session</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  // computed: mapGetters({startedSessions: this.getStartedSessions()}),
  async created() {
    await this.fetchSessions('startedSessions')
  },
  methods: {
    ...mapActions(['fetchSessions', 'updateSessions']),
    ...mapGetters(['getStartedSessions']),
    logSessions() {
      const startedSessions = this.getStartedSessions()
      console.log(startedSessions)
    },
    addSession() {
      this.updateSessions([{ hi: 'hi' }, 'startedSessions'])
    },
  },
}
</script>
