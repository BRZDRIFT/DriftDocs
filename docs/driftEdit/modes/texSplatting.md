## Introduction
`Tex Splatting` allows you to 'paint' textures onto the map.  
Understanding how splatter terrain is rendered in `Drift Wars` can be a bit challenging..

## High Level Explanation

Rendering method:

- Splatter terrain is rendered using two passes.
    - Pass 1: Renders all `triangles` in `Tex Layer #1` using assigned `Atlas`, `Texture Group`, and `Blend Mode` from `Layer Settings`
    - Pass 2: Renders all `triangles` in `Tex Layer #2` using assigned `Atlas`, `Texture Group`, and `Blend Mode` from `Layer Settings`

Other:

- Each triangle on the map is rendered exactly once. A triangle cannot belong to both `Tex Layer #1` and `Tex Layer #2`
- You can define which `triangles` are part of which `Tex Layer` in the {{mode("texLayers")}} mode
- Each `Tex Layer` is assigned a single `Texture Group`, `Atlas`, and `Blend Mode`
- `Drift Wars` provides two seperate atlasses to better define 'hard' terrain edges in certain cases, and also allows for some other tricks. You can set which `atlas` is used for a given `Tex Layer` in `Layer Settings`
- `Drift Wars` provides two seperate `Texture Groups` consisting of 4 `Textures` each for performance reasons (rather than 1 `Texture Group` of 8 `textures`).
    - This limits each triangle to be blended only by the 4 `textures` in the `texture group` assigned to the triangle's `Tex Layer`
- `Tip`: You can create 'hard' `vertical`, `horizontal`, and `diagonal` edges by setting triangles to different `Tex Layers`
- `Tip`: Or you can create 'hard' `vertical` and `horizontal` edges by setting `Blend Mode` to `Nearest`.

## Layer Settings

- Assigns which `Atlas`, `Texture Group`, and `Blend Mode` the given `Tex Layer` should use.

## Atlas Settings

- Allows you to set the resolution for texture painting. Usually `Normal` is good enough.
- Setting to `High` will slightly degrade performance and increase map size, but may look better depending on the textures used.

## Paint/Brush Options
- There are various brush options available
- Compatible with {{sideControls("symmetry-mode")}}