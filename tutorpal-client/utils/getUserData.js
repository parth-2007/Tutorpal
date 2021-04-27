const getUserData = async () => {
  const data = await fetch('http://localhost:5000/api/users/me/')
    .then((res) => {
      if (res.status === 404) {
        return { unauthenticated: true }
      } else if (res.status >= 400 && res.status < 600) {
        return { error: 'server error' }
      }
      return res.json()
    })
    .catch((err) => {
      // eslint-disable-next-line
      console.warn(err)
      return { error: 'server error' }
    })

  return data
}

export default getUserData
