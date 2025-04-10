#!/bin/bash

if xrandr | grep "HDMI" | grep " connected"; then
    ~/.config/qtile/external.sh 
fi