import loggedInFetch from '../../utils/loggedInFetch'
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
      const tutor = await loggedInFetch('https://api.tutorpal.org/tutors/me')
      commit('setTutor', keysToCamel(tutor))
    }
  },
  async refreshTutor({ commit }) {
    const tutor = await loggedInFetch('https://api.tutorpal.org/tutors/me')
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
