// Updated register funcs
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
    fetch('http://127.0.0.1:8000/register-tutor/', {
        method: "POST",
        headers: {
            'Content-type':'multipart/form-data',
        },
        body: JSON.stringify({
            "user": user,
            "tutor": tutor
        })
    }).then((resp)=> {
        try {
            resp.json().then((data) => {
                console.log(data);
            })
        } catch (e) {
            console.log(e);
        }
    });
}

const createStudent = (user, student) => {
    fetch('http://127.0.0.1:8000/register-student/', {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-type':'multipart/form-data',
        },
        body: JSON.stringify({
            "user": user,
            "student": student
        })
    })
    .then((resp)=> {
        try {
            resp.json().then((data) => {
                console.log(data);
            })
        } catch (e) {
            console.log(e);
        }
    });
}