// import loggedInFetch from '../../utils/loggedInFetch'
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
      const contacts = await fetch(process.env.API_URL + '/rooms/', {
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
      commit('setContacts', keysToCamel(contacts.results))
    }
  },
  async refreshContacts({ commit }) {
    const contacts = await fetch(process.env.API_URL + '/rooms/', {
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
    commit('setContacts', keysToCamel(contacts.results))
  },
  updateContacts({ commit, state }, contact) {
    commit('setContacts', [contact, ...state.contacts])
  },
  markContactAsRead({ commit, state }, id) {
    const contacts = [...state.contacts]
    const contact = {
      ...contacts.find((contact) => contact.id === id),
      unread: 0,
    }
    const contactIndex = contacts.findIndex((x) => x.id === id)
    console.log('contact: ', contact)
    console.log('contacts: ', contacts)
    contacts[contactIndex] = contact
    commit('setContacts', contacts)
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
