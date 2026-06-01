`Tags` dialog allows you to define `Tags` for your custom game mode.

- A `tag` are the options a `player` can choose during the `game lobby` screen (i.e.: race selection, etc)
- You can also restrict the amount a certain `tag` can be chosen by the players. If you set the `Max Players` to `1`, then only one player in the entire game will be allowed to select that `tag`.
- The `Theme` column defines which race icons and sounds should be associated with that `tag`.
- The default tags for `melee` maps are `[ 'Humans', 'Robots', 'Monsters' ]`
- The information in this dialog is only used for `custom` game-type maps!! 
- `Melee` maps will always use `Humans`, `Robots`, `Monsters`.
- You must check the `Enable Custom Tags` checkbox to enable this feature -- otherwise the default `tag` settings will be used for your map:
    - `TagID : Name : Max Players : Theme`:
    - `1 : Humans : 16 : Humans`
    - `2 : Robots : 16 : Robots`
    - `3 : Monsters : 16 : Monsters`

> Important!  
It is up to you that you provide adequate `Tags` and `MaxPlayers` values so every player in your map can select a `Tag`. If not enough `Tags` can be allocated for all the players in the game, your map may be unplayable.