//Constants
var SESSION_STATUS = Flashphoner.constants.SESSION_STATUS;
var STREAM_STATUS = Flashphoner.constants.STREAM_STATUS;
var session;
var stream;

//Init Flashphoner API on page load
function init_api() {
    Flashphoner.init({});
    publishBtn.onclick = connect;
    playBtn.onclick = playStream;
    stopBtn.onclick = stopPublish;
    startPlayBtn.onclick = start; // добавлено
}

// Запуск playStream() без publishStream() - добавлено
function start() {
    session = Flashphoner.createSession({
        urlServer: "wss://demo.flashphoner.com"
    }).on(SESSION_STATUS.ESTABLISHED, function(session) {
        playStream(session);
    });
}

//Connect to WCS server over websockets
function connect() {
    session = Flashphoner.createSession({
        urlServer: "wss://demo.flashphoner.com"
    }).on(SESSION_STATUS.ESTABLISHED, function(session) {
        publishStream(session);
    });
}

//Publish stream
function publishStream(session) {
    stream = session.createStream({
        name: "ovStream1967",
        display: document.getElementById("publish"),
    });
    stream.publish();
}

//Playing stream
function playStream() {
    session.createStream({
        name: "ovStream1967",
        display: document.getElementById("play"),
    }).play();
}

//Stopping stream
function stopPublish() {
    stream.stop();
}