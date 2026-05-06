#!/bin/bash
export DISPLAY="${DISPLAY:-:0}"

# Inject a static textbox widget at the top of mainbox so the Arch
# glyph (nf-linux-archlinux, U+F303) shows in drun mode. -mesg doesn't
# render reliably with -show drun, so we bake the icon into the theme.
rofi -show drun \
    -theme "$HOME/.config/rofi/menu.rasi" \
    -theme-str 'mainbox {
                  children: [textbox-arch, inputbar, listview];
                  spacing: 10px;
                }
                textbox-arch {
                  content: "";
                  font: "Hack Nerd Font Mono 44";
                  text-color: #88c0d0;
                  horizontal-align: 0.5;
                  vertical-align: 0.5;
                  padding: 0px;
                  background-color: transparent;
                }'
