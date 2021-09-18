import loggedInFetch from '../../utils/loggedInFetch'
import { keysToCamel } from '../../utils/changeObjectNaming'

const state = () => ({
  contacts: { unfetched: true },
})

const getters = {
  getContacts: (state) => state.contacts,
}

const actions = {
  async fetchContacts({ commit, state }) {
    if (state.contacts.unfetched) {
      const contacts = await loggedInFetch('https://api.tutorpal.org/rooms/')
      commit('setContacts', keysToCamel(contacts.results))
    }
  },
  async refreshContacts({ commit }) {
    const contacts = await loggedInFetch('https://api.tutorpal.org/rooms/')
    commit('setContacts', keysToCamel(contacts.results))
  },
  updateContacts({ commit, state }, contact) {
    commit('setContacts', [contact, ...state.contacts])
  },
}

const mutations = {
  setContacts(state, contacts) {
    state.contacts = contacts
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
