import { createServer } from 'http';
import { readFile } from 'fs';
import path from 'path';
const HOSR = '127.0.0.1';
const PORT = 1234;
const mimeTypes = {
  '.html': 'text/html; charset=UTF-8',
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
  readFile(path.join(process.cwd(), `./public${filePatch}`), (error, data) => {
    let res = response.statusCode;
    if (error) {
      res = 404;
      console.log(`${filePatch}\t\t\t \x1b[33m${res}\x1b[39m`);
      response.end();
    } else if (ext == '.html') {
      console.log(`${filePatch}\t\t\t \x1b[33m${res}\x1b[39m`);
      const header = "V I D E O"; 
      const message = `код ${res}`;
      const dataText = data.toString().replace(/{header}/g, header).replace(/{message}/g, message);
      response.end(dataText);
    } else {
      console.log(`${filePatch}\t\t\t \x1b[33m${res}\x1b[39m`);
      response.end(data);
    }
  })
}

createServer(function (request, response) {
  const url = request.url;
  //console.table([url]);
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
}).listen(PORT, () => {
  console.log(`\n\x1b[38;2;255;128;0mСервер запущен:  \x1b[34mhttp://${HOSR}:${PORT}\x1b[39m\n`)
})

// node_modules, package-lock.json, package.json - для ffmpeg и др. модулей node.
// В package.json добавлено - "type": "module" для import вместо require
// npm list - список модулей
// запуск: cd D:\1\PythonProjects\FFMPEG_Audio_Video\server_test -> node server.js