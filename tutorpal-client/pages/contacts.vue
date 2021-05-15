<template>
  <div>
    <!-- <button @click="logSessions">log sessions</button> -->
    <button @click="addContact">add contact</button>
    <br />
    {{ contacts }}
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: mapGetters({ contacts: 'getContacts' }),
  async created() {
    await this.fetchContacts()
  },
  methods: {
    ...mapActions(['fetchContacts', 'updateContacts']),
    ...mapGetters(['getContacts']),
    addContact() {
      this.updateContacts({ hi: 'hi' })
    },
  },
}
</script>
