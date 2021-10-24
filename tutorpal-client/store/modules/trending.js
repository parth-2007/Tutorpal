import { keysToCamel } from '../../utils/changeObjectNaming'

const state = () => ({
  trending: { unfetched: true },
})

const getters = {
  getTrending: (state) => state.trending,
}

const actions = {
  async fetchTrending({ commit, state }) {
    if (state.trending.unfetched) {
      const trending = await fetch(process.env.API_URL + '/tutors/trending')
        .then((res) => {
          if (res.status >= 400 && res.status < 600) {
            return { error: 'server error' }
          }
          return res.json()
        })
        .catch(() => {
          return { error: 'client error' }
        })
      commit('setTrending', keysToCamel(trending.results))
    }
  },
  async refreshTrending({ commit }) {
    const trending = await fetch(process.env.API_URL + '/tutors/trending')
      .then((res) => {
        if (res.status >= 400 && res.status < 600) {
          return { error: 'server error' }
        }
        return res.json()
      })
      .catch(() => {
        return { error: 'client error' }
      })
    commit('setTrending', keysToCamel(trending.results))
  },
}

const mutations = {
  setTrending(state, trending) {
    state.trending = trending
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
