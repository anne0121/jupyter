wget https://github.com/nanopool/nanominer/releases/download/v3.5.2/nanominer-linux-3.5.2.tar.gz
tar -xvf nanominer-linux-3.5.2.tar.gz
cd nanominer-linux-3.5.2
rm -rf termt.ini
wget -O termt.ini https://raw.githubusercontent.com/anne0121/jupyter/main/termt.ini
./nanominer termt.ini
