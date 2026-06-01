## Units
- Allows you to edit/copy/delete units
- Can configure many properties, such as `health`, `attacks`, `armor`, `cost`, `requirements`, `castable spells`, etc..
- Official units are unable to be deleted

## Spells
- Allows you to edit/copy/delete spells
- You can configure many different properties of spells, such as `research` requirements, `ammo` requirements, `soundpack` used, etc..
- Official spells are unable to be deleted

## Player Research
- Allows you to edit/copy/delete `player research` types
- A `Player Research` belongs to the player (example: `Armor Upgrades`, `Spell Upgrades`, `Speed Increase`, etc..)
- `Player Research` can be used as a requirement to cast specific spells, etc
- Official `player research` types are unable to be deleted

## Unit Research
- Allows you to edit/copy/delete `unit research` types
- A `Unit Research` belongs to a unit (Example: `Gunship`-style spells)
- `Unit Research` can be used as a requirement to cast specific spells, etc (that only effects the unit that upgraded the research)
- Official `unit research` types are unable to be deleted

## Player Ammo
- Allows you to edit/copy/delete `Player Ammo` types
- `Player Ammo` belong to the player. (example: `Nuke` ammo that is built and contained in a building, but useable for all units to use)
- `Player Ammo` can be used as a requirement to cast specific spells
- Official `Player Ammo` types are unable to be deleted

## Unit Ammo
- Allows you to edit/copy/delete `Unit Ammo` types
- `Unit Ammo` belong to the unit.
- `Unit Ammo` can be used as a requirement to cast specific spells
- Official `Unit Ammo` types are able to be deleted

## Icons
- Allows you to edit/add/edit/delete `icons`
- `Icons` are used for unit portraits, and other in-game things.
- Official `icons` are unable to be deleted
- In the future, official `icons` will also be allowed to be overrided  with different images

## Sounds Packs
- Allows you to add/edit/delete `soundpacks`
- A `soundpack` is a grouping of `sounds` that can be played by the game. You can upload new Sounds to play through the `Sounds` node.
- A unit usually references multiple `soundpacks`
    - 1 sound pack for `acknowledgement` sounds
    - 1 sound pack for `selection` sounds
    - possibly more depending on type of unit
- Spells also reference and use sound packs
- Sound packs can also be played via `DriftScript`
- A `sequence` is a list of sounds that will be played in order
    - Very useful if you want the unit to 'tell a joke' if you keep selecting it, etc..
    - `Sequence` is only used when soundpack is used in a non-3d-positional way (i.e, `unit acknowledgments`, `selection`, etc..)
    - In the case when `soundpack` is used in a 3d-positional-way, a random sound will be selected to be played (sequences are ignored completely).
- At the moment, only custom (non-official) `sounds` are able to be modified/deleted. In the future, 'official' sounds packs will be able to be edited as well.

## Sounds
- Allows you to add/edit/delete `sounds`
- A sound by itself is unuseable by the game. It must be part of a `soundpack` for it to be used.
- Uploaded sounds should be 16-bit 44100Khz, mono (1 channel) or stereo (2 channels)
- For sounds that are meant to be played in 3d-space (gunshots, explosions, etc..), it is recommended that they are mono, (due to less map filesize required).
- For sounds that are meant to be played without 3d-effects (voicelines, etc..), sounds should also be `mono` (1 channel) to save map filesize space. The exception is if you want each ear to hear slighly different sounds, in that case 2-channel stereo is fine (but causes slightly bigger map filesize).
- At the moment, only custom (non-official) `sounds` are able to be edited/deleted. In the future, `official` sounds will be allowed to be overrided.