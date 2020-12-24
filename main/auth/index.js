const url = 'http://127.0.0.1:8000/api/login/';

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
const csrftoken = getCookie('csrftoken');

console.log('csrf token: ' + csrftoken);

fetch(url, {
    method: "POST",
    headers: {
        // 'x-csrftoken': csrftoken,
        'Content-type':'application/json',
        'X-CSRFToken': csrftoken,
        // 'HTTP_X_CSRFTOKEN': csrftoken,
    },
    body: JSON.stringify({
        email: 'email',
        password: 'password',
        csrfmiddlewaretoken: csrftoken,
    })
}).then((resp) => {
    console.log(resp)
    resp.json().then((data) => {
        console.log(data)
    })
})
