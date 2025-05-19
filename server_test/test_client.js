//import WebSocket, { WebSocketServer } from 'ws';
const wsConnection = new WebSocket("ws://127.0.0.1:1234");
wsConnection.onopen = function() {
    console.log("Соединение установлено.");
};

wsConnection.onclose = function(event) {
    if (event.wasClean) {
        console.log('Соединение закрыто чисто');
    } else {
        console.log('Обрыв соединения'); // например, "убит" процесс сервера
    }
    console.log('Код: ' + event.code + ' причина: ' + event.reason);
};

wsConnection.onerror = function(error) {
    console.log("Ошибка " + error.message);
};

const wsSend = function(data) {
// readyState - true, если есть подключение
    if(!wsConnection.readyState){
        setTimeout(function (){
            wsSend(data);
        },100);
    } else {
        wsConnection.send(data);
    }
};