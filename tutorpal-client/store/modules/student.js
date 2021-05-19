import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

const state = () => ({
  student: { unfetched: true },
})

const getters = {
  getStudent: (state) => state.student,
}

const actions = {
  async fetchStudent({ commit, state }) {
    if (state.student.unfetched) {
      const student = await loggedInFetch('api/students/me/')
      commit('setStudent', keysToCamel(student))
    }
  },
  async refreshStudent({ commit }) {
    const student = await loggedInFetch('api/students/me/')
    commit('setStudent', keysToCamel(student))
  },
  logoutStudent({ commit }) {
    commit('setStudent', { unauthenticated: true })
  },
  updateStudent({ commit }, student) {
    commit('setStudent', student)
  },
}

const mutations = {
  setStudent(state, student) {
    state.student = student
  },
  logout(state) {
    state.student = { unauthenticated: true }
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
