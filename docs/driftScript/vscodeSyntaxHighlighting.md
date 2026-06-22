## Install DriftScript Language Support

1. In vscode, go to extensions..
2. Search and install: `DriftScript` by BRZDRIFT
3. Enable Auto Update..
4. Done!

## Tips

- Provides auto-complete, help hints, and syntax higlighting.
- You can comment/uncomment multiple selected lines with `Ctrl+/`
- More improvements and better syntax highlighting to come!

## DriftLibs detection

- The `DriftScript` language extension searches these directories for `DriftLibs`
    - system environment variable `GX_DRIFT_LIBS_DIR`
    - `%ProgramFiles(x86)%\Steam\steamapps\common\DriftWarsBeta\Dev\DriftLibs`
    - `%ProgramFiles(x86)%\Steam\steamapps\common\DriftWarsRTS\Dev\DriftLibs`
    - `~/.local/share/Steam/steamapps/common/DriftWarsBeta/Dev/DriftLibs`
    - `~/.local/share/Steam/steamapps/common/DriftWarsRTS/Dev/DriftLibs`