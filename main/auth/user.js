// User Actions (Register, Password Reset)

// const createUser = ({email, password, is_student, is_tutor, first_name, last_name, profile_pic}) => {
//     fetch('http://127.0.0.1:8000/users/', {
//         method: "POST",
//         headers: {
//             'Content-type':'multipart/form-data',
//             // 'origin': '*',
//             // 'X-CSRFToken': getCookie('csrftoken'),
//         },
//         body: JSON.stringify({email, password, is_student, is_tutor, first_name, last_name, profile_pic})
//     }).then((resp)=> {
//         try {
//             resp.json().then((data) => {
//                 console.log(data);
//             })
//         } catch (e) {
//             console.log(e);
//         }
//     });
// }

const createTutor = (user, tutor) => {
  fetch("http://127.0.0.1:8080/api/api-auth/register-tutor/", {
    method: "POST",
    headers: {
      "Content-type": "multipart/form-data",
    },
    body: JSON.stringify({
      user: user,
      tutor: tutor,
    }),
  }).then((resp) => {
    try {
      resp.json().then((data) => {
        console.log(data);
      });
    } catch (e) {
      console.log(e);
    }
  });
};

const createStudent = (user, student) => {
  // fetch('http://127.0.0.1:8000/api/register-student/', {
  //     method: "POST",
  //     headers: {
  //         'Accept': 'application/json',
  //         'Content-type':'multipart/form-data',
  //     },
  //     body: JSON.stringify({
  //         user,
  //         student
  //     })
  // })
  fetch("http://127.0.0.1:8080/api/api-auth/register-student/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-type": "application/json", // Change to 'multipart/form-data' for images
    },
    body: JSON.stringify({
      user,
      student,
    }),
  }).then((resp) => {
    try {
      resp.json().then((data) => {
        console.log(data);
      });
    } catch (e) {
      console.log(e);
    }
  });
};

const activateAccount = (apiEndpoint) => {
  fetch(apiEndpoint).then((resp) => {
    try {
      resp.json().then((data) => {
        console.log(data);
      });
    } catch (e) {
      console.log(e);
    }
  });
};

// Takes a user's email and sends an email to them
const resetPassword = (email) => {
  fetch("http://127.0.0.1:8080/api/api-auth/reset-password/", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      email: email,
    }),
  }).then((resp) => {
    try {
      resp.json().then((data) => {
        console.log(data);
      });
    } catch (e) {
      console.log(e);
    }
  });
};

const passwordReset = (password, apiEndpoint) => {
  fetch(apiEndpoint, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      password: password,
    }),
  }).then((resp) => {
    try {
      resp.json().then((data) => {
        console.log(data);
      });
    } catch (e) {
      console.log(e);
    }
  });
};
