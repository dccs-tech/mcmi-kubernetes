#!/usr/bin/env bash
#
# Install Kubernetes related packaging
#
set -e

apt-key adv --fetch-keys https://packages.cloud.google.com/apt/doc/apt-key.gpg 2>/dev/null
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl
rm -rf /var/lib/apt/lists/*

curl -o helm_install.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get 2>/dev/null
chmod 700 helm_install.sh
./helm_install.sh -v v2.16.1
