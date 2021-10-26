// import loggedInFetch from '../../utils/loggedInFetch'
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
      const student = await fetch(process.env.API_URL + '/students/me/', {
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
      commit('setStudent', keysToCamel(student))
    }
  },
  async refreshStudent({ commit }) {
    const student = await fetch(process.env.API_URL + '/students/me/', {
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
