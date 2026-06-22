## Install DriftScript Language Support

1. In vscode, go to extensions..
2. Search and install: `DriftScript` by BRZDRIFT
3. Enable Auto Update..
4. Note: More improvements to come!

## DriftLibs detection

- The `DriftScript` language extension searches these directories for `DriftLibs`
    - system environment variable `GX_DRIFT_LIBS_DIR`
    - `%ProgramFiles(x86)%\Steam\steamapps\common\DriftWarsBeta\Dev\DriftLibs`
    - `%ProgramFiles(x86)%\Steam\steamapps\common\DriftWarsRTS\Dev\DriftLibs`
    - `~/.local/share/Steam/steamapps/common/DriftWarsBeta/Dev/DriftLibs`
    - `~/.local/share/Steam/steamapps/common/DriftWarsRTS/Dev/DriftLibs`