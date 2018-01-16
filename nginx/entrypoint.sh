#!/bin/bash
nginx
rm -rf /var/cache/pagespeed/*
mkdir /var/cache/pagespeed/
chown -R www-data:www-data /var/cache/pagespeed/
mkdir -p /usr/local/nginx/logs
touch /usr/local/nginx/logs/access.log
tail -f /usr/local/nginx/logs/error.log /usr/local/nginx/logs/access.log
