# Django + Postgres + Nginx with pagespeed production-ready configuration
## Preparings:
1. Change Django environment variables in file environment_en.env
2. Change Nginx parms like domain name and ports in file nginx/nginx.conf
3. Move you signed fillchain ssl file to nginx/ssl/fullchain.pem
4. Move you domain private key to nginx/ssl/privkey.pem
5. Generate nginx/htpasswd for debug mode
## Usage:
> make debug 

run debug django configuration with djangoserver on 8000 port.

> make start

run production configuration, bind nginx on 443 and 80 ports.
