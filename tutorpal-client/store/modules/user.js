import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

const state = () => ({
  user: { unfetched: true },
})

const getters = {
  getUser: (state) => state.user,
}

const actions = {
  async fetchUser({ commit, state }) {
    if (state.user.unfetched) {
      const user = await loggedInFetch('/api/users/me/')
      commit('setUser', keysToCamel(user))
    }
  },
  async refreshUser({ commit }) {
    const user = await loggedInFetch('/api/users/me/')
    commit('setUser', keysToCamel(user))
  },
  async logoutUser({ commit }) {
    await fetch('/api/auth/logout/', {
      credentials: 'include',
    })
      .then((res) => {
        if (res.status >= 400 && res.status < 600) {
          return { error: 'server error' }
        }
        return res.json()
      })
      .catch(() => {
        return { error: 'client error' }
      })
    commit('setUser', { unauthenticated: true })
  },
  updateUser({ commit }, user) {
    commit('setUser', user)
  },
}

const mutations = {
  setUser(state, user) {
    state.user = user
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
