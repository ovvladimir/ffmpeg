import { createServer } from 'http';
import { readFile } from 'fs';

const host = '127.0.0.1';
const port = 1234;

readFile('./public/index.html', (err, html) => {
  if(err){
    throw err;
  }
  const server = createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-type', 'text/html; charset=utf-8;');
    res.write(html);
    res.end(`\nСервер запущен на порту: ${port}`);
  });

  server.listen(port, host, () => {
    console.log(`Сервер запущен:  http://${host}:${port}`);
  });
})
// cd server_test
// node server1.js