#!/bin/bash

# script used to get stats on the main machine and echoing them in a JSON on the webhook response pages body 

CPU_temp=$(cat /sys/class/thermal/thermal_zone*/temp | head -n1 | awk '{print ($1 / 1000)"°C"}')
CPU_usage=$(mpstat 1 1 | grep "all" | awk '{print (100 - $NF)"%"}' | head -n1)
SSD_temp=$(smartctl -a /dev/nvme0 | grep Temperature: | awk '{print ($2)"°C"}')
SSD_health=$(smartctl -a /dev/nvme0 | grep Percentage | awk '{print (100 - $3 )"%"}')
SSD_usage=$(df -h /dev/nvme0n1p6 | awk '{print ($3) "/" ($2)}' | tail -n1)
SSD_available=$(df -h /dev/nvme0n1p6 | awk '{print ($4)}' | tail -n1)
RAM_usage=$(free -m | grep "Mem:" | awk '{print ($3/1000) "G/" ($2/1000) "G"}')
RAM_available=$(free -m | grep "Mem:" | awk '{print ($7/1000) "G"}')

echo '{"CPU_temp":"'$CPU_temp'","CPU_usage":"'$CPU_usage'","SSD_temp":"'$SSD_temp'","SSD_health":"'$SSD_health'","SSD_usage":"'$SSD_usage'","SSD_available":"'$SSD_available'","RAM_usage":"'$RAM_usage'","RAM_available":"'$RAM_available'"}'