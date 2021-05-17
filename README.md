# Scalable Vehicle_Detection_on_Edge_Devices

### Compiling Kvazaar on Mac

#### Run the following commands


```
brew install automake libtool yasm

./autogen.sh

autoreconf -i

./configure

make 

sudo make install

brew install kvazaar

brew install ffmpeg

ffmpeg -i  input_avi.avi -c:v rawvideo -pixel_format yuv420p output_720x480p.yuv

kvazaar --input output_720x480p.yuv --output out.hevc

```

## Link to reference

https://github.com/ultravideo/kvazaar#using-kvazaar

https://core.ac.uk/download/pdf/250163878.pdf

https://ottverse.com/ffmpeg-convert-avi-mp4-to-yuv-raw-playback-yuv-ffplay/

https://videocompression.tech/hevc-tiling-modes/


