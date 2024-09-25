server {
    listen 80;
    server_name api.domain.io;
    return 301 https://api.domain.io$request_uri;
}

server {
    listen ${LISTEN_PORT} ssl;
    server_name api.domain.io;

    gzip on;
    gzip_vary on;
    gzip_min_length 1000;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css text/javascript text/xml image/svg+xml image/x-icon application/xml application/javascript application/x-javascript application/json font/woff2;
    gzip_disable "msie6";

    ssl_certificate /etc/nginx/ssl/certificate.pem;
    ssl_certificate_key /etc/nginx/ssl/privatekey.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_stapling on;
    ssl_stapling_verify on;

    add_header Strict-Transport-Security "max-age=31536000; includeSubdomains" always;

    location /static {
        alias /vol/static;
        expires 1M;
        access_log off;
        add_header Cache-Control "max-age=2629746, public";
        etag on;
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }

    # Security Headers
    add_header X-Frame-Options "DENY";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
}
