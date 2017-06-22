#!/bin/bash

wget https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 -O ~/confd
sudo chmod a+x ~/confd
sudo mv ~/confd /usr/local/bin/
