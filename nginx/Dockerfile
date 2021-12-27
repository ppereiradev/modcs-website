#Download base image ubuntu 20.04
FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static
