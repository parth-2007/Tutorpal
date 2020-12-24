const createToken = (email, password) => {
    fetch('http://127.0.0.1:8000/api-auth/token/', {
        method: "POST",
        headers: {
            'Content-type':'application/json',
            // 'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            email: email,
            password: password,
        })
    }).then((resp)=> {
        try {
            resp.json().then((data) => {
                console.log(data);
                localStorage.setItem("refresh", data.refresh);
                localStorage.setItem("access", data.access);
            })
        } catch (e) {
            console.log(e);
        }
    });
};

const refreshToken = () => {
    fetch('http://127.0.0.1:8000/api-auth/token/refresh/', {
        method: "POST",
        headers: {
            'Content-type':'application/json',
            // 'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            refresh: localStorage.getItem("refresh")
        })
    }
    ).then((resp)=> {
        try {
            resp.json().then((data) => {
                console.log(data);
                localStorage.setItem("access", data.access);
            })
        } catch (e) {
            console.log(e)
        }
    });
};