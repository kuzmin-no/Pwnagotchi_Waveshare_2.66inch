#!/bin/bash

pwnagotchi_pkg_path=/usr/local/lib/python3.7/dist-packages/pwnagotchi

sudo mkdir $pwnagotchi_pkg_path/ui/hw/libs/waveshare/v266inch
sudo cp -rf patch/* $pwnagotchi_pkg_path
