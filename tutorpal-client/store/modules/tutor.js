import loggedInFetch from '../../utils/loggedInFetch'
import keysToCamel from '../../utils/keysToCamel'

const state = () => ({
  tutor: { unfetched: true },
})

const getters = {
  getTutor: (state) => state.tutor,
}

const actions = {
  async fetchTutor({ commit, state }) {
    if (state.tutor.unfetched) {
      const tutor = await loggedInFetch('api/tutors/me')
      commit('setTutor', keysToCamel(tutor))
    }
  },
  async refreshTutor({ commit, state }) {
    const tutor = await loggedInFetch('api/tutors/me')
    commit('setTutor', keysToCamel(tutor))
  },
}

const mutations = {
  setTutor(state, tutor) {
    state.tutor = tutor
  },
  logout(state) {
    state.tutor = { unauthenticated: true }
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
