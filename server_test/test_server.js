// https://habr.com/ru/articles/516334/
import { createServer } from 'http';
import express from "express";
import { WebSocketServer } from 'ws';
const host = '127.0.0.1';
const port = 1234;

const app = express();
const server = createServer(app);
const webSocketServer = new WebSocketServer({ server });
/*
const dispatchEvent = (message, ws) => {
    const json = JSON.parse(message);
    switch (json.event) {
        case "chat-message": webSocketServer.clients.forEach(client => client.send(message));
        default: ws.send((new Error("Wrong query")).message);
    }
}
*/
webSocketServer.on('connection', ws => {
   ws.on('message', m => {
    webSocketServer.clients.forEach(client => client.send(m));
   });
   ws.on("error", e => ws.send(e));
   ws.send('Привет, я сервер WebSocket.');
});

server.listen(port, host, () => {
    console.log(`Сервер запущен:  http://${host}:${port}`);
});