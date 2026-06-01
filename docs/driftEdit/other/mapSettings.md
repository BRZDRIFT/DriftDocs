The `Map Settings` dialog allows you to set certain properties of the map.

- `Map Name`: The friendly name for the map. This field is `required`.
- `Max Players`: The maximum amount of players for this map. Required to be between `[1-16]`
- `[Custom] Is Custom Map?`: By enabling this, certain features are enabled/disabled.
    - Town Halls will not be created at spawn locations
    - Workers will not be created near spawn locations
    - Normal `Victory`/`Defeat` conditions are ignored
    - Certain `DriftScript` functions are only enabled for `Custom Maps`.
    - Default game modes `1v1`, `Teams`, `FFA`, `etc` will not be selectable in in-game `Create Game` Lobby.
    - Probably some more differences..
- `[Custom] Mode name`: Name of `Game Type` when `Is Custom Map?` is enabled.
- `Map Credits`: Allows you to show some textual credits information for map
- `Map Description`: Map description. Currently unused in-game.
- `Set DriftPaint`: Uploads a `.png`, `.jpg`, or `.DriftPaint` for pre-game loading screen.
    - Recommended Size: No larger than `1920x1080`.
- `Clear DriftPaint`: Removes current `DriftPaint` background