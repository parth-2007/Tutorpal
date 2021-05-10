import loggedInFetch from '../../utils/loggedInFetch'
import keysToCamel from '../../utils/keysToCamel'

const state = () => ({
  user: { unfetched: true },
})

const getters = {
  getUser: (state) => state.user,
}

const actions = {
  async fetchUser({ commit, state }) {
    if (state.user.unfetched) {
      const user = await loggedInFetch('api/users/me/')
      commit('setUser', keysToCamel(user))
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
