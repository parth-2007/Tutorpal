function disconnect(socket){
    socket.on('disconnect', () => {
        console.log("a user has disconnected " + socket.id)
    });
}

module.exports = {
    disconnect,
};