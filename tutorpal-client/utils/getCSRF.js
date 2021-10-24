const getCookie = (name) => {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

const getCSRF = async () => {
  let csrfToken = getCookie('csrftoken')
  if (csrfToken !== null && csrfToken !== undefined) {
    return { success: csrfToken }
  } else {
    const resp = await fetch('api/auth/ensure-csrf/', {
      credentials: 'include',
    })
      .then((res) => {
        if (res.status >= 400 && res.status < 600) {
          return { error: 'server error' }
        }
        return res.json()
      })
      .catch(() => {
        return { error: 'server error' }
      })
    if (resp.success === 'CSRF Ensured!') {
      csrfToken = getCookie('csrftoken')
      return { success: csrfToken }
    } else {
      return { error: 'error in getting csrf token' }
    }
  }
}

export default getCSRF
