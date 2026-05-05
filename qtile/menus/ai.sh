#!/usr/bin/env bash
export DISPLAY="${DISPLAY:-:0}"

PROMPT=$(rofi -dmenu \
  -p "" \
  -lines 0 \
  -no-fixed-num-lines \
  -theme /home/chris-cit/.config/rofi/menu.rasi \
  -theme-str 'window { width: 700px; }
              mainbox { children: [inputbar]; }
              entry { placeholder: "Ask AI..."; }
              listview { enabled: false; }')

[ -z "$PROMPT" ] && exit

alacritty --title tgpt-sky -e bash -c "
tgpt --provider sky --interactive \"$PROMPT\" 2>/dev/null || tgpt --provider sky \"$PROMPT\";
exec bash
"
