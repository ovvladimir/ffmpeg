// https://github.com/websockets/ws
import { createServer } from 'http';
import { readFile, readFileSync } from 'fs';
import WebSocket,  { WebSocketServer } from 'ws';
import * as path from 'path';
const host = '127.0.0.1';
const port = 1234;

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.ico': 'image/x-icon',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.json': 'application/json',
  '.woff': 'font/woff',
  '.wav': 'audio/wav',
  '.ogg': 'video/ogg',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.ffm': 'video/webm'
};

function staticFile (response, filePatch, ext) {
  response.setHeader("Content-Type", mimeTypes[ext]);
  readFile('./public'+filePatch, (error, data) => {
    if (error) {
      response.statusCode = 404;
      console.log(response.statusCode);
      response.end();
    }
    response.end(data)
  })
}

const server = createServer(function (request, response) {
  const url = request.url;
  console.log(url);
  switch(url) {
    case '/':
      staticFile(response, '/index.html', '.html');
      break;
    default:
      const extname = String(path.extname(url)).toLocaleLowerCase();
      if (extname in mimeTypes) {
        staticFile(response, url, extname);
      }
      else {
        response.statusCode = 404;
        response.end();
      }
  }
})

const wss = new WebSocketServer({ port: port });
//const ws = new WebSocket('wss://websocket-echo.com/');
wss.on('connection', (ws) => {
  console.log('Новый клиент подключился!');

  ws.on('message', (message) => {
    console.log(`Получено сообщение: ${message}`);
    ws.send('Сообщение получено!');
  });
  ws.on('close', () => {
    console.log('Клиент отключился');
  });
});

server.listen(port, host, () => {
    console.log(`Сервер запущен:  http://${host}:${port}`);
});