import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

const camelToSnakeCase = (str) =>
  str.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`)

const state = () => ({
  pendingOnTutor: { unfetched: true },
  pendingOnStudentPayment: { unfetched: true },
  upcoming: { unfetched: true },
  tutorNotPaid: { unfetched: true },
  finishedSessions: { unfetched: true },
  canceledSessions: { unfetched: true },
  startedSessions: { unfetched: true },
})

const getters = {
  getPendingOnTutor: (state) => state.pendingOnTutor,
  getPendingOnStudentPayment: (state) => state.pendingOnStudentPayment,
  getUpcoming: (state) => state.upcoming,
  getTutorNotPaid: (state) => state.tutorNotPaid,
  getFinishedSessions: (state) => state.finishedSessions,
  getCanceledSessions: (state) => state.canceledSessions,
  getStartedSessions: (state) => state.startedSessions,
}

const actions = {
  async fetchSessions({ commit, state }, sessionName) {
    if (state[sessionName].unfetched) {
      const sessions = await loggedInFetch(
        `api/sessions/${camelToSnakeCase(sessionName)}/`
      )
      commit('setSessions', [keysToCamel(sessions.results), sessionName])
    }
  },
  async refreshSessions({ commit }, sessionName) {
    const sessions = await loggedInFetch(
      `api/sessions/${camelToSnakeCase(sessionName)}/`
    )
    commit('setSessions', [keysToCamel(sessions.results), sessionName])
  },
  updateSessions({ commit, state }, [newSession, sessionName]) {
    commit('setSessions', [[newSession, ...state[sessionName]], sessionName])
  },
}

const mutations = {
  setSessions(state, [sessions, sessionName]) {
    state[sessionName] = sessions
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
