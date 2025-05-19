import { createReadStream, promises } from "fs";
import { createServer } from "http";
import { join, extname } from "path";
import { exec } from "child_process";
// const Transform = require('node:stream').Transform
import { Transform } from "stream";

const HOST = '127.0.0.1';
const PORT = 1234;

const MIME_TYPES = {
  default: "application/octet-stream",
  html: "text/html",
  js: "text/javascript",
  css: "text/css",
  png: "image/png",
  jpg: "image/jpeg",
  gif: "image/gif",
  ico: "image/x-icon",
  svg: "image/svg+xml",
  json: 'application/json',
  woff: 'font/woff',
  wav: 'audio/wav',
  ogg: 'video/ogg',
  mp4: 'video/mp4',
  webm: 'video/webm',
  ffm: 'video/webm'
};

const STATIC_PATH = process.cwd();
const toBool = [() => true, () => false];

export function main() {
  const prepareFile = async (url) => {
    const paths = [STATIC_PATH, url];
    if (url.endsWith("/")) paths.push("index.html");
    const filePath = join(...paths);
    const pathTraversal = !filePath.startsWith(STATIC_PATH);
    const exists = await promises.access(filePath).then(...toBool);
    const found = !pathTraversal && exists;
    const streamPath = found ? filePath : STATIC_PATH + "/404.html";
    const ext = extname(streamPath).substring(1).toLowerCase();
    const stream = createReadStream(streamPath);
    return { found, ext, stream };
  };

  createServer(async (req, res) => {
    const file = await prepareFile(req.url);
    const statusCode = file.found ? 200 : 404;
    const mimeType = MIME_TYPES[file.ext] || MIME_TYPES.default;
    res.writeHead(statusCode, { "Content-Type": mimeType });

    const parser = new Transform();
    parser._transform = function(data, encoding, done) {
      const header = "V I D E O"; 
      const message = `код ${statusCode}`;
      this.push(mimeType == 'text/html' ? data.toString().replace(/{header}/g, header).replace(/{message}/g, message) : data);
      done();
    };

    file.stream.pipe(parser).pipe(res);
    console.log(`${req.method} ${req.url} ${statusCode}`);
  }).listen(PORT);
  console.log(`\n\x1b[38;2;255;128;0mСервер запущен:  \x1b[34mhttp://${HOST}:${PORT}\x1b[39m\n`)
  exec(`start http://${HOST}:${PORT}`)
}
// https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Node_server_without_framework