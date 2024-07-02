#! /bin/bash

find /var/log -type f -name "*.log"
find /etc -type f -mtime -7
find /var/log -type f -size +10M
find /var/log -type f -user root

find /var/log -type f -name "*.log" -exec grep -i "error" {} +
find /etc -type f -exec grep -in "failed" {} +
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' ips.txt

less /var/log/syslog
more /etc/passwd

tail -n 20 /var/log/syslog
tail -f /var/log/syslog
tail -f /var/log/*.log # find /var/log -type f -name "*.log" -exec tail -f {} +

cat /etc/hosts
cat /var/log/dpkg.log /var/log/fontconfig.log 
cat /var/log/dpkg.log /var/log/fontconfig.log > combined_logs.txt
cat -n /var/log/dpkg.log

find /var/log -type f -name "*log" -mtime -7 -exec grep -i "error" {} + 
#tail -f /var/log/*.log | grep -i "error" | less
find /etc -type f -name "*.conf" -exec more {} +