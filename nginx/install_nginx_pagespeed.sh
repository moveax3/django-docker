#!/bin/bash
bash <(curl -f -L -sS https://ngxpagespeed.com/install) --nginx-version latest -a '--with-http_ssl_module --with-http_v2_module' -y
