#!/usr/bin/env bash
#
# Install Kubernetes related packaging
#
apt-key adv --fetch-keys https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list

apt-get install -y kubectl \
    && rm -rf /var/lib/apt/lists/*

curl -o /tmp/helm_install.sh https://raw.githubusercontent.com/helm/helm/v2.9.1/scripts/get \
    && chmod 700 /tmp/helm_install.sh
/tmp/helm_install.sh && rm -f /tmp/helm_install.sh