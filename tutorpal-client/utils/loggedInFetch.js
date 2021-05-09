const loggedInFetch = async (url) => {
  const data = await fetch(url)
    .then((res) => {
      if (res.status === 404) {
        return { unauthenticated: true }
      } else if (res.status >= 400 && res.status < 600) {
        return { error: 'server error' }
      }
      return res.json()
    })
    .catch(() => {
      return { error: 'server error' }
    })

  return data
}

export default loggedInFetch
