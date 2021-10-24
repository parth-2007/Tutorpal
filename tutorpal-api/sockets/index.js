
const http = require('http').createServer();
const {
    joinRoom,
} = require('./joinRoomHandler');
const {
    onMessage,
} = require('././onMessageHandler');
const {
    disconnect,
} = require('./disconnectHandler');

const io = require('socket.io')(http, {
    cors: { origin: "*" }
});

io.on('connection', (socket) => {
    console.log('a user connected');
    onMessage(io, socket)
    joinRoom(socket)
    disconnect(socket)
});

http.listen(8080, () => console.log('listening on http://localhost:8080') );