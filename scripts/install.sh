#!/usr/bin/env bash
#
# Install Kubernetes related packaging
#
set -e

wget -qO - https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - 2>/dev/null 1>&2
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl
rm -rf /var/lib/apt/lists/*

curl -o helm_install.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get 2>/dev/null
chmod 700 helm_install.sh
./helm_install.sh -v v3.2.4

ISTIO_VERSION=1.6.4

if [ ! -f /usr/local/bin/istioctl ]
then
    wget https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux-amd64.tar.gz 2>/dev/null
    tar -xzf istio-${ISTIO_VERSION}-linux-amd64.tar.gz
    cp -f istio-${ISTIO_VERSION}/bin/istioctl /usr/local/bin
fi
