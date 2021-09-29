#!/bin/bash
apt update
apt upgrade
apt install redis-server
if [[ "$( echo 'ping' | /usr/bin/redis-cli )" == "PONG" ]] ; then
    echo "ping worked"
else
    echo "ping FAILED"
fi
systemctl status redis
systemctl status redis-server
exit 0