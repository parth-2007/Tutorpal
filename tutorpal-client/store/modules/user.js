import getUserData from '../../utils/getUserData'

const state = () => ({
  user: { unfetched: true },
})

const getters = {
  getUser: (state) => state.user,
}

const actions = {
  async fetchUser({ commit, state }) {
    if (state.user.unfetched) {
      const user = await getUserData()
      commit('setUser', user)
    }
  },
}

const mutations = {
  setUser(state, user) {
    state.user = user
  },
  logout(state) {
    state.user = { unauthenticated: true }
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
