The `Forces` dialog allows you to create `Forces` and assign `players` to those `Forces`

- A `Force` is a grouping of `players`
- `Players` that belong to the same `Force` does not necessarily mean they are on the same 'team'
- `Force` provides a useful grouping of `players` when writing `DriftScript`.
- The information in this dialog is only used for `custom` game-type maps

Important!

- There are always 3 implicit players and 1 implicit force in every Drift Wars map / game-mode.
- The 3 implicit players are: `Neutral` (`id = -1`), `Hostile` (`id = -2`), and `Rescue` (`id = -3`)
- The 1 implicit force is: `Neutral` (`id = -1`)
- All 3 implicit players are part of Force `Neutral` (`id = -1`)
- These special players/forces do not appear in game's scoreboard, post-stats, etc.

Each of the special/implicit players may have certain properties:

- `Neutral`: Cannot auto-attack, has no map vision
- `Rescue`: Cannot auto-attack, has no map vision, units change `PlayerID` when touched by a non-special player
- `Hostile`: Can auto-attack, has map vision, acts mostly as a normal player