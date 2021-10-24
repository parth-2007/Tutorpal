
const socket = io('ws://localhost:8080');

const { username, room } = Qs.parse(location.search, {
    ignoreQueryPrefix: true,
});

socket.emit('joinRoom', { username, room });

socket.on('message', message => {
    console.log(message)
    const el = document.createElement('li');
    el.innerHTML = `${message[1]} says ${message[0]}`;
    document.querySelector('ul').appendChild(el)

});

document.querySelector('button').onclick = () => {

    const text = document.querySelector('input').value;
    if(text !== ""){
        socket.emit('message', {text, username, room})
    }
    
}