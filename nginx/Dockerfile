FROM debian:latest
RUN apt-get update
RUN apt-get install -y curl sudo build-essential zlib1g-dev libpcre3 libpcre3-dev unzip
RUN apt-get install -y wget
RUN apt-get install -y libssl-dev
RUN mkdir /nginx
COPY install_nginx_pagespeed.sh /nginx/
WORKDIR /nginx
RUN bash install_nginx_pagespeed.sh
RUN ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 443
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
