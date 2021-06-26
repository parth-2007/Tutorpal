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
  pastSessions: { unfetched: true },
})

const getters = {
  getPendingOnTutor: (state) => state.pendingOnTutor,
  getPendingOnStudentPayment: (state) => state.pendingOnStudentPayment,
  getUpcoming: (state) => state.upcoming,
  getTutorNotPaid: (state) => state.tutorNotPaid,
  getFinishedSessions: (state) => state.finishedSessions,
  getCanceledSessions: (state) => state.canceledSessions,
  getStartedSessions: (state) => state.startedSessions,
  getPastSessions: (state) => state.pastClasses,
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
  addSession({ commit, state }, [newSession, sessionName]) {
    commit('setSessions', [[newSession, ...state[sessionName]], sessionName])
  },
  removeSession({ commit, state }, [session, sessionName]) {
    const index = state[sessionName].indexOf(session)
    if (index > -1) {
      const newArr = [...state[sessionName]]
      newArr.splice(index, 1)
      commit('setSessions', [newArr, sessionName])
    }
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
