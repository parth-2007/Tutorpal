// DO NOT USE THIS IS OUTDATED
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