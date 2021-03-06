// Authentication Actions
const createToken = (email, password) => {
    fetch('http://127.0.0.1:8000/api-auth/token/', {
        method: "POST",
        headers: {
            'Content-type':'application/json',
            'Access-Control-Allow-Origin': '*'
            // 'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            email,
            password,
        })
    }).then((resp)=> {
        try {
            resp.json().then((data) => {
                console.log(data);
                return data
            })
        } catch (e) {
            console.warn(e);
            return e
        }
    });
};

const refreshToken = () => {
    fetch('http://127.0.0.1:8000/api-auth/token/refresh/').then((resp)=> 
    {
        try {
            resp.json().then((data) => {
                console.log(data);
                return data
            })
        } catch (e) {
            console.warn(e)
            return e
        }
    });
};

const logout = () => {
    fetch('http://127.0.0.1:8000/api-auth/token/logout/').then((resp)=> 
    {
        try {
            resp.json().then((data) => {
                console.log(data);
                return data
            })
        } catch (e) {
            console.log(e)
            return e
        }
    });
};


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// const getCSRF = () => {
//     let csrfToken = getCookie('csrftoken');
//     if (csrfToken != null) {
//         return csrfToken
//     } else {
//         fetch('http://127.0.0.1:8000/api/set-csrf', {method: "GET"});
//         csrfToken = getCookie('csrftoken');
//         return csrfToken;
//     }
// }


// OLD REGISTER FUNCS DONT USE

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

// const createTutor = ({access, qualifications, what_you_teach, subjects, birth_date, bio, rates, occupation, linkedIn, prof_exp, teach_exp, education, school, gpa, major, gender, tutor_type, availability, paypal_email}) => {
//     fetch('http://127.0.0.1:8000/tutors/', {
//         method: "POST",
//         headers: {
//             'Content-type':'multipart/form-data',
//             // 'X-CSRFToken': getCookie('csrftoken'),
//             'Authorization': `Bearer ${access}`,
//         },
//         body: JSON.stringify({qualifications, what_you_teach, subjects, birth_date, bio, rates, occupation, linkedIn, prof_exp, teach_exp, education, school, gpa, major, gender, tutor_type, availability, paypal_email})
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

// const createStudent = ({access, parent_email, birth_date}) => {
//     fetch('http://127.0.0.1:8000/students/', {
//         method: "POST",
//         headers: {
//             'Content-type':'multipart/form-data',
//             // 'X-CSRFToken': getCookie('csrftoken'),
//             'Authorization': `Bearer ${access}`,
//         },
//         body: JSON.stringify({parent_email, birth_date})
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