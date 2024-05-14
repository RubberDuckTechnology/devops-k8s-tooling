FROM bitnami/openldap:2.6.7
USER root

ENV LDAP_LOGLEVEL=-1
ENV LDAP_SKIP_DEFAULT_TREE=yes
ENV LDAP_CUSTOM_LDIF_DIR=/ldifs 

RUN mkdir /ldifs
COPY ldifs /ldifs

USER 1001
