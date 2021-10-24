// import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

const state = () => ({
  tutor: { unfetched: true },
})

const getters = {
  getTutor: (state) => state.tutor,
}

const actions = {
  async fetchTutor({ commit, state }) {
    if (state.tutor.unfetched) {
      const tutor = await fetch(process.env.API_URL + 'tutors/me/', {
        credentials: 'include',
      })
        .then((res) => {
          if (res.status === 403 || res.status === 404) {
            return { unauthenticated: true }
          } else if (res.status >= 400 && res.status < 600) {
            return { error: 'server error', status: res.status }
          }
          return res.json()
        })
        .catch(() => {
          // console.warn(e)
          return { error: 'client error' }
        })
      commit('setTutor', keysToCamel(tutor))
    }
  },
  async refreshTutor({ commit }) {
    const tutor = await fetch(process.env.API_URL + 'tutors/me/', {
      credentials: 'include',
    })
      .then((res) => {
        if (res.status === 403 || res.status === 404) {
          return { unauthenticated: true }
        } else if (res.status >= 400 && res.status < 600) {
          return { error: 'server error', status: res.status }
        }
        return res.json()
      })
      .catch(() => {
        // console.warn(e)
        return { error: 'client error' }
      })
    commit('setTutor', keysToCamel(tutor))
  },
  logoutTutor({ commit }) {
    commit('setTutor', { unauthenticated: true })
  },
  updateTutor({ commit }, tutor) {
    commit('setTutor', tutor)
  },
}

const mutations = {
  setTutor(state, tutor) {
    state.tutor = tutor
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
