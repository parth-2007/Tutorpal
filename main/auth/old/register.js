// DO NOT USE THIS IS OUTDATED
const createUser = ({email, password, is_student, is_tutor, first_name, last_name, profile_pic}) => {
    fetch('http://127.0.0.1:8000/users/', {
        method: "POST",
        headers: {
            'Content-type':'multipart/form-data',
            // 'origin': '*',
            // 'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({email, password, is_student, is_tutor, first_name, last_name, profile_pic})
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

const createTutor = ({access, qualifications, what_you_teach, subjects, birth_date, bio, rates, occupation, linkedIn, prof_exp, teach_exp, education, school, gpa, major, gender, tutor_type, availability, paypal_email}) => {
    fetch('http://127.0.0.1:8000/tutors/', {
        method: "POST",
        headers: {
            'Content-type':'multipart/form-data',
            // 'X-CSRFToken': getCookie('csrftoken'),
            'Authorization': `Bearer ${access}`,
        },
        body: JSON.stringify({qualifications, what_you_teach, subjects, birth_date, bio, rates, occupation, linkedIn, prof_exp, teach_exp, education, school, gpa, major, gender, tutor_type, availability, paypal_email})
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

const createStudent = ({access, parent_email, birth_date}) => {
    fetch('http://127.0.0.1:8000/students/', {
        method: "POST",
        headers: {
            'Content-type':'multipart/form-data',
            // 'X-CSRFToken': getCookie('csrftoken'),
            'Authorization': `Bearer ${access}`,
        },
        body: JSON.stringify({parent_email, birth_date})
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