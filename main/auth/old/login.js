// DO NOT USE THIS IS OUTDATED
const login = async (email, password) => {
    await fetch('http://127.0.0.1:8000/login/', {
        method: 'POST',
        // mode: 'cors',
        // credentials: 'same-origin',
        // credentials: 'include',
        // withCredentials: true,
        headers: {
            'Accept': 'application/json',
            'Content-type':'application/json',
            // 'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            email,
            password,
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
};



const getMyData = async (token) => {

    await fetch("http://127.0.0.1:8000/users/me", {
        method: "GET",
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': `Token ${token}`
            // 'X-CSRFToken': getCookie('csrftoken'),
        },
    }).then((resp) => {
        // console.log(resp)
        resp.json().then((data) => {
            console.log(data);
            // console.log(document.cookie);
        })
    })
}