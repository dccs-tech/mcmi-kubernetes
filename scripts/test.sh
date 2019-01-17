#!/usr/bin/env bash
# Test script

set -e

SCRIPT_DIR="$(cd "$(dirname "$([ `readlink "$0"` ] && echo "`readlink "$0"`" || echo "$0")")"; pwd -P)"
cd "$SCRIPT_DIR/.."

SOME_VARIABLE="${1:-original}"

#-------------------------------------------------------------------------------

echo "Hello with ${SOME_VARIABLE}"
