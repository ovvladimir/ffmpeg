import { createServer } from 'http';
import { readFile } from 'fs';
import path from 'path';
import { exec } from "child_process";
const HOST = '127.0.0.1';
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
// const list = Object.values(mimeTypes);
// const space = list.reduce((i, j) => j.length > i.length ? j : i, list[0]).length;
// console.log(space)
const sp = 30;

export function main() {
  function print(name, rs) {
    console.log(`${name}${" ".repeat(
      (name.length>sp?name.length:sp)-name.length)}\t\x1b[33m${rs}\x1b[39m`);
  }

  function staticFile (response, filePatch, ext) {
    response.setHeader("Content-Type", mimeTypes[ext]);
    readFile(path.join(process.cwd(), `./${filePatch}`), (error, data) => {
      let res = response.statusCode;
      if (error) {
        res = 404;
        print(filePatch, res);
        response.end();
      } else if (ext == '.html') {
        print(filePatch, res);
        const header = "V I D E O"; 
        const message = `код ${res}`;
        const dataText = data.toString().replace(/{header}/g, header).replace(/{message}/g, message);
        response.end(dataText);
      } else {
        print(filePatch, res);
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
    console.log(`\n\x1b[38;2;255;128;0mСервер запущен:  \x1b[34mhttp://${HOST}:${PORT}\x1b[39m\n`)
    exec(`start http://${HOST}:${PORT}`)
  })
}
// node_modules, package-lock.json, package.json - для node-media-server и др. модулей node.
// В package.json добавлено - "type": "module", для import вместо require
// запуск: cd D:\1\PythonProjects\FFMPEG_Audio_Video\server_test -> node server_web.js