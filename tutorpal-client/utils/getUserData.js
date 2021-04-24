const getUserData = async () => {
  const data = await fetch('api/users/me/')
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

export default getUserData
