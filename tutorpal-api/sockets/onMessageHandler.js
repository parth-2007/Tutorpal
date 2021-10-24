function onMessage(io, socket){
    socket.on('message', ({text, username, room}) =>     {
        const message = [text, username, room]
        console.log(message)
        io.to(room).emit('message', message);   
    });
}

module.exports = {
    onMessage,
};