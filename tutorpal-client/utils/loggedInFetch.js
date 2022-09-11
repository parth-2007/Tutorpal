const loggedInFetch = async (url) => {
  console.warn('loggedInFetch doesnt work lol')
  const data = await fetch(process.env.API_URL + url, {
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
    .catch((e) => {
      return { error: 'client error' }
    })
  return data
}

export default loggedInFetch
