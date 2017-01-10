#!/bin/bash

echo "###### Setup enviroment for Fujitsu's instance ######"

echo "What is your IP: "
read IP_EXT

ifaces=/etc/network/interfaces
apt_file=/etc/apt/apt.conf
env_file=/etc/environment
test -f $ifaces.orig || cp $ifaces $ifaces.orig
rm $ifaces
cat << EOF > $ifaces
#Configuring IP for Controller node

# LOOPBACK NET
auto lo
iface lo inet loopback

# External network
auto eth0
iface eth0 inet static
address $IP_EXT
netmask 255.255.255.192
gateway 10.164.180.65
dns-nameservers 10.164.180.65
EOF

if [ -f $apt_file ] ; then
rm $apt_file
fi
cat << EOF > $apt_file
Acquire::http::proxy "http://10.164.177.168:8080/";
Acquire::https::proxy "https://10.164.177.168:8080/";
Acquire::ftp::proxy "ftp://10.164.177.168:8080/";
Acquire::socks::proxy "socks://10.164.177.168:8080/";
EOF

rm $env_file
cat << EOF > $env_file
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
http_proxy="http://10.164.177.168:8080/"
https_proxy="https://10.164.177.168:8080/"
no_proxy=localhost,10.10.10.0/24,10.10.20.0/24,10.164.180.65/25,164.254.169.254
EOF

echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

reboot 

