const url = 'http://127.0.0.1:8000/users/me';

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

const getMyData = (acessToken) => {
    const csrftoken = getCookie('csrftoken');

    fetch(url, {
        method: "GET",
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken,
            'Authorization': 'Bearer ' + acessToken,
        },
    }).then((resp) => {
        console.log(resp)
        resp.json().then((data) => {
            console.log(data)
        })
    })
}


// fetch(url).then((resp) => console.log(resp));