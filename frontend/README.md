# client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Debug with VUE:
# download apache httpd server from the following site:
# https://www.apachehaus.com/cgi-bin/download.plx

# a. Open $apache_home/conf/httpd.conf
  b. Be sure the following settings:
    Define SRVROOT "$your_www_folder"
    #Define ENABLE_TLS13 "Yes"
    LoadModule proxy_module modules/mod_proxy.so
    LoadModule proxy_http_module modules/mod_proxy_http.so
    LoadModule headers_module modules/mod_headers.so
  c. Setting DocumentRoot:
  DocumentRoot "$your_vue_project_root_folder"
  <Directory "$your_vue_project_root_folder">
  d. Setting Apache proxy rules:
    Header always append X-Frame-Options SAMEORIGIN
    Header always append X-Content-Type-Options nosniff
    Header always append X-XSS-Protection "1;mode=block"
    ServerSignature Off
    ServerTokens Prod

    <VirtualHost _default_:80>
            # 80 is for Apache proxy server, 8080 is for Vue debug, and 5000 is for Flask server
            ErrorLog logs/error_log.txt
            ProxyPreserveHost On
            ProxyPass /api http://localhost:5000/api
            ProxyPass /static http://localhost:8080/static
            ProxyPass / http://localhost:8080/
    </VirtualHost>
  e. open httpd server and listening at 80 port
  f. in Vue project folder, run 'npm run serve' and debug at 8080 port
  g. open broswer and open url: http://localhost/ to preview and debug the vue page