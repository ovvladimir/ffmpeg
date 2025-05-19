import NodeMediaServer from 'node-media-server';
const rtmpPort = 1935;
const httpPort = 8443;
const cameraUrl = "Integrated Camera";

let config = {
    logType: 3,
    rtmp: {
    port: rtmpPort,
    chunk_size: 60000,
    gop_cache: true,
    ping: 60,
    ping_timeout: 30,
    },
    http: {
    port: httpPort,
    allow_origin: "*",
    },
    relay: {
    ffmpeg: "C:/Users/Lenovo/Documents/Distr/ffmpeg/bin/ffmpeg.exe",
    tasks: [
        {
        app: "cctv",
        mode: "static",
        edge: "rtsp://" + cameraUrl + "/h264_ulaw.sdp",
        name: "uterum",
        rtsp_transport: "udp",
        },
    ],
    },
};

let nms = new NodeMediaServer(config);
nms.run();