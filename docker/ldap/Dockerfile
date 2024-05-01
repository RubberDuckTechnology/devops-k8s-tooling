FROM ubuntu:20.04

RUN apt-get update && apt-get install -y samba krb5-user krb5-config winbind libpam-winbind libnss-winbind \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Avoid prompts from packages expecting interactive input
ENV DEBIAN_FRONTEND=noninteractive

# Copy your smb.conf file into the image
COPY docker/ldap/smb.conf /etc/samba/smb.conf

# Provision the Samba domain
RUN samba-tool domain provision --use-rfc2307 --realm=LOCALDOMAIN.LOCAL \
    --domain=LOCALDOMAIN --adminpass='Password_123' --server-role=dc --dns-backend=SAMBA_INTERNAL

# Expose necessary ports
EXPOSE 53 88 135 139 389 445 464 636 1024-5000 3268-3269

# Command to run Samba
CMD ["samba", "--foreground", "--log-stdout"]
