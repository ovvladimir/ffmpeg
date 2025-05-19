import { exec } from "child_process";

const CAMERA = "Integrated Camera";
const MICROFONE = "Микрофон (Realtek(R) Audio)";
const stream_id = 'ovStream1967';
const destination = 'rtmp://127.0.0.1:1935/live';

export function start() {
    let ffmpeg = exec(
        `ffmpeg -hide_banner -rtbufsize 100M -channel_layout stereo \
        -f dshow -i "video=${CAMERA}:audio=${MICROFONE}" \
        -c:v libx264 -b:v 1M \
        -c:a aac -ac 2 -b:a 128k -ar 44100 \
        -preset ultrafast -tune zerolatency \
        -f flv ${destination}/${stream_id}`
    )
/*
    ffmpeg.stdout.on('data', function(data){
        console.log(data.toString());
    })

    ffmpeg.stderr.on('data', function(data){
        console.log(data.toString());
    })
*/
}