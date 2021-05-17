# Scalable Vehicle_Detection_on_Edge_Devices

### Compiling Kvazaar on Mac

#### Run the following commands


```

brew install automake libtool yasm

git clone --depth=50 https://github.com/ultravideo/kvazaar.git ultravideo/kvazaar

./autogen.sh

autoreconf -i

./configure

make 

sudo make install

brew install kvazaar

brew install ffmpeg

ffmpeg -i  video/input_1080x608p.avi -c:v rawvideo -pixel_format yuv420p output_720x480p.yuv

kvazaar -i output_720x480p.yuv --input-res 720x480 --tiles 2x2  -o output1.hevc

```

## Link to reference

https://github.com/ultravideo/kvazaar#using-kvazaar

https://travis-ci.org/github/ultravideo/kvazaar/jobs/763898332

https://core.ac.uk/download/pdf/250163878.pdf

https://ottverse.com/ffmpeg-convert-avi-mp4-to-yuv-raw-playback-yuv-ffplay/

https://videocompression.tech/hevc-tiling-modes/

