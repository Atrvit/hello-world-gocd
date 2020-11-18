FROM python:3.7-stretch

WORKDIR /service

COPY . /service

ENV PORT 8080
EXPOSE 8080

ENTRYPOINT ["/service/entrypoint.sh"]
