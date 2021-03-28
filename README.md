# iiitd-summer-project

### Compiling Kvazaar

brew install automake libtool yasm
./autogen.sh
autoreconf -i
./configure
make 
sudo make install
