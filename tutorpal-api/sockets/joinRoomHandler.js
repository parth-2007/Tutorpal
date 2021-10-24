function joinRoom(socket){
    socket.on('joinRoom', ({ username, room }) => {
        socket.join(room);
    });
}

module.exports = {
    joinRoom,
};