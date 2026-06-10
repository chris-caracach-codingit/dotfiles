if status is-interactive
    nvm use v22.22.2 
    # Commands to run in interactive sessions can go here
end

# pnpm
set -gx PNPM_HOME "$HOME/.local/share/pnpm"
if not string match -q -- $PNPM_HOME $PATH
  set -gx PATH "$PNPM_HOME" $PATH
end
# pnpm end

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH

fish_add_path ~/.local/bin


# Ensure system paths are first
set -gx PATH /usr/local/bin /usr/bin /bin /usr/local/sbin /usr/sbin /sbin $PATH

# Nord shell colors
set -g fish_color_normal 88c0d0
set -g fish_color_command 81a1c1
set -g fish_color_param eceff4
set -g fish_color_error bf616a
