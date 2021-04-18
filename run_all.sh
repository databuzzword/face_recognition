#!/usr/bin/env bash
set -eu
env | grep LABEL_STUDIO
mkdir -p $LABEL_STUDIO_DATABASE_DIR
mkdir -p $LABEL_STUDIO_DATA_DIR

export LABEL_STUDIO_USERNAME="label@ovh"
export LABEL_STUDIO_PASSWORD="label@ovh"

label-studio start --data-dir $LABEL_STUDIO_DATA_DIR --initial-project-description label --password $LABEL_STUDIO_PASSWORD --username $LABEL_STUDIO_USERNAME  -p $LABEL_STUDIO_PORT --init label &

supervisord -n -u 42420 -c /etc/supervisor/supervisor.conf
