`Cliffs / Ramps` allow you to add cliffs and ramps to your map.

- Drift Wars supports 5 levels of terrain
    - Each cliff layer has a height of `4 units`
    - The base Z dimensions for the layers are: `z=-4`, `z=0`, `z=4`, `z=8`, `z=12`
    - The default terrain-Z is at `z=0`
    - Additionally, the Height Map can adjust a terrain layer's height by an additional `+8` to `-8` units.

- Adding Cliffs
    - `Add Cliffs`: Allows you to add cliffs units can walk on.
    - `Add Closed Cliffs`: Allow you to add unwalkable cliffs.
    - You can set which terrain-level should use which 'cliff tileset' in the brush settings. It's currently a bit cumbersome, will be improved in future.
    - Compatible with {{sideControls("symmetry-mode")}}

- Adding Ramps
    - To create ramps, you need to 'assemble' them from smaller pieces.
    - Ramp pieces: `Left Ramp`, `Middle Ramp`, `Right Ramp`, `etc...`
    - Compatible with {{sideControls("symmetry-mode")}} depending on the symmetry mode selected
    - `Important!` You can rotate Ramp pieces by pressing `R` when placing.