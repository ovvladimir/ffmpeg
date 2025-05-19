// https://qna.habr.com/q/599790
// https://www.npmjs.com/package/node-server-media
// npm install node-media-server - для 4 версии (не показывает видео в браузере)
// npm install node-media-server@2.6.6
import NodeMediaServer from 'node-media-server';
import { main } from "./server_web_2.js";
//import { start } from './stream.js';

const rtmpPort = 1935;
const httpPort = 8443;

const config = {
  rtmp: {
    port: rtmpPort,
    chunk_size: 60000,
    gop_cache: true,
    ping: 60,
    ping_timeout: 30
  },
  http: {
    port: httpPort,
    allow_origin: '*'
  }
}

new NodeMediaServer(config).run()
main()
//start()

// cd D:\1\PythonProjects\FFMPEG_Audio_Video\rtmp_mediaserver_test
// node server_media.js