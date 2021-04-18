<template>
  <ul id="users">
    <li v-for="key in Object.keys(user)" :key="key">
      {{ key }} : {{ user[key] }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      user: {}
    }
  },
  methods: {
    async fetchUser() {
      const res = await fetch('api/users/me')
      const data = await res.json()
      return data
    },
  },
  async created() {
    const data = await this.fetchUser()
    this.user = data
  },
}
</script>