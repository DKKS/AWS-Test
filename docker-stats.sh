#!/bin/bash

while true; do
  echo $(date +%x_%r) >> /root/docker-stats.log 2>&1 
  sudo docker stats --no-stream >> /root/docker-stats.log 2>&1 
  sleep 8;
done
