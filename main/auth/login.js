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

const getCSRF = () => {
    fetch('http://127.0.0.1:8000/api/set-csrf', {method: "GET"}) // .then((resp) => {document.cookie = resp.headers.setCookie});
    csrfToken = getCookie('csrftoken');
    return csrfToken;
}


const login = (email, password) => {
    fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        // mode: 'cors',
        credentials: 'same-origin', // in prod
        // credentials: 'include',
        withCredentials: true,
        headers: {
            'Accept': 'application/json',
            'Content-type':'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            email,
            password,
        })
    }).then((resp)=> {
        console.log(resp)
        try {
            resp.json().then((data) => {
                console.log(data);
            })
        } catch (e) {
            console.log(e);
        }
    });
};

const getMyData = () => {
    const csrftoken = getCookie('csrftoken');

    fetch("http://127.0.0.1:8000/users/me", {
        method: "GET",
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    }).then((resp) => {
        console.log(resp)
        resp.json().then((data) => {
            console.log(data);
            console.log(document.cookie);
        })
    })
}