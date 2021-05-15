import user from './modules/user'
import tutor from './modules/tutor'
import student from './modules/student'
import session from './modules/session'
import chat from './modules/chat'
import trending from './modules/trending'

const store = {
  modules: {
    user,
    tutor,
    student,
    session,
    chat,
    trending,
  },
}

export default store
