# pre-commit-alacritty-os-specific-shell-hook

This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfile repos.

## Defaults

    Windows:              C:/Program Files/PowerShell/7/pwsh.exe
    All other systems:    /bin/fish


## Example 

    # .pre-commit-config.yaml
    repos:
      - repo: https://github.com/oryon-dominik/pre-commit-alacritty-os-specific-shell
        rev: 1.0.1
        hooks:
          - id: alacritty-os-specific-shell
            args: [--windows=C:/Program Files/PowerShell/7/pwsh.exe --posix=/bin/fish]



## Development

In the repo you want to test the hook:

    pip install pre-commit
    pre-commit try-repo --verbose <path to the hook's local repo-directory>
