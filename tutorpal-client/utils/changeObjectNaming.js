const toCamel = (key) => {
  return key.replace(/([_][a-z])/gi, ($1) => {
    return $1.toUpperCase().replace('_', '')
  })
}

const toSnake = (key) =>
  key.replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`)

const isArray = (a) => {
  return Array.isArray(a)
}

const isObject = (o) => {
  return o === Object(o) && !isArray(o) && typeof o !== 'function'
}

export const keysToCamel = (o) => {
  if (isObject(o)) {
    const n = {}

    Object.keys(o).forEach((k) => {
      n[toCamel(k)] = keysToCamel(o[k])
    })

    return n
  } else if (isArray(o)) {
    return o.map((i) => {
      return keysToCamel(i)
    })
  }

  return o
}

export const keysToSnake = (o) => {
  if (isObject(o)) {
    const n = {}

    Object.keys(o).forEach((k) => {
      n[toSnake(k)] = keysToSnake(o[k])
    })

    return n
  } else if (isArray(o)) {
    return o.map((i) => {
      return keysToSnake(i)
    })
  }

  return o
}
