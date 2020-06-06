FROM postgres
COPY init.sql /docker-entrypoint-initdb.d/

ARG postgresdb
ARG postgresuser
ARG postgrespass

ENV POSTGRES_DB=${postgresdb}
ENV POSTGRES_USER=${postgresuser}
ENV POSTGRES_PASSWORD=${postgrespass}
