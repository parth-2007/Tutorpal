export const unpackTutor = ({
  qualifications,
  whatYouTeach,
  subjects,
  birthDate,
  bio,
  rates,
  occupation,
  linkedIn,
  verified,
  profExp,
  teachExp,
  education,
  school,
  gpa,
  major,
  gender,
  tutorType,
  availability,
  paypalEmail,
}) => {
  return {
    qualifications,
    whatYouTeach,
    subjects,
    birthDate,
    bio,
    rates,
    occupation,
    linkedIn,
    verified,
    profExp,
    teachExp,
    education,
    school,
    gpa,
    major,
    gender,
    tutorType,
    availability,
    paypalEmail,
  }
}

export const unpackUser = ({ email, firstName, lastName }) => {
  return { email, firstName, lastName }
}

export const unpackStudent = ({ parentEmail, birthDate }) => {
  return { parentEmail, birthDate }
}
