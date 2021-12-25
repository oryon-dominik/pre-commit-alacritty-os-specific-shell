# pre-commit-alacritty-os-specific-shell-hook

This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfiles repos.

## development

In the repo you want to test the hook:

    pip install pre-commit
    pre-commit try-repo --verbose <path to the hook's local repo-directory (commit all changes !!)>
