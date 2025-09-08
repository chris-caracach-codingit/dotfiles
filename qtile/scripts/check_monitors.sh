#!/bin/bash

# This script checks if the HDMI screen is connected and if it is, it runs the external.sh script
# external.sh script is responsible for setting up the external monitor

if xrandr | grep "HDMI" | grep " connected"; then
    ~/.config/qtile/scripts/external.sh 
fi