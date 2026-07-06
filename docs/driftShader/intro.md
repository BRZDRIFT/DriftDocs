# Drift Shader

## Introduction
`DriftShader` is responsible for rendering the background of maps.

- It is inspired by `ShaderToy`, which uses `GLSL` as the shading language.
- `BG.ShaderToy.glsl` is compiled to a shader and used to render the map and minimap background.
- Browse [https://www.shadertoy.com/](https://www.shadertoy.com/) for documentation and examples.

## Entry Function
```glsl
void mainImage(out vec4 outSRGB, vec2 fragCoord) {
  outSRGB = vec4(0, 1, 0, 1);
}
```

- You are required to set the output variable `outSRGB` to color you want the "pixel" to be.
- `outSRGB` is expected to be in `sRGB`
    - I would prefer the output to be in `linear`, but ShaderToy uses `sRGB` -- and I want to maintain as much similarity as possible.
    - If you want to output in `linear`, you need to set the option under `Background` tab in the map editor.
- There are other settings in the `Background` tab such as rotation, speed, enable dither, etc..

## Global Uniform Values
```glsl
uniform vec3      iResolution;              // resolution (sort-of)
uniform float     iTime;                    // game-time (seconds)
uniform int       iFrame;                   // not supported yet (always 0)
uniform vec3      iChannelResolution[4];    // iChannel# texture resolution
uniform vec4      iMouse;                   // not supported yet (vec4(0,0,0,0))
uniform sampler2D iChannel0;                // can set via Background tab
uniform sampler2D iChannel1;                // can be set via Background tab
uniform sampler2D iChannel2;                // can be set via Background tab
uniform sampler2D iChannel3;                // can be set via Background tab
```

## Color Conversion Functions
```glsl
float gx_linear_to_srgb(float linear)
float gx_srgb_to_linear(float srgb)
vec3 gx_linear_to_srgb(vec3 linear)
vec4 gx_linear_to_srgb(vec4 linear)
vec3 gx_srgb_to_linear(vec3 srgb)
vec4 gx_srgb_to_linear(vec4 srgb)
vec3 gx_hsv_to_srgb(vec3 hsv);
vec4 gx_hsv_to_srgb(vec4 hsva);
vec3 gx_srgb_to_hsv(vec3 srgb);
vec4 gx_srgb_to_hsv(vec4 srgba);
```

## gx_get_bg_shader_val
```glsl
float gx_get_bg_shader_val(int index)
```

- retrieves the shader value at slot `index`
- the initial shader values can be set under `Background -> Shader Values` in the map editor
- these values can be changed via `.DriftScript` using the `void gx_set_bg_shader_val(int index, float value)` function.

## gx_flip_uv
```glsl
vec2 gx_flip_uv(vec2 uv) {
    uv.y = 1.0 - uv.y;
    return uv;
}
```

- Helper to convert between `ShaderToy (OpenGL)` and `DriftShader (vulkan)` coordinate systems
- (usually you don't need to use this, provided for convenience)

## gx_flip_frag_coord
```glsl
vec2 gx_flip_frag_coord(vec2 fragCoord) {
    fragCoord.y = iResolution.y - uv.y;
    return fragCoord;
}
```

- Helper to convert between `ShaderToy (OpenGL)` and `DriftShader (vulkan)` coordinate systems
- (usually you don't need to use this, provided for convenience)

## VSCode Extension
- `WebGL GLSL Editor` or `GLSL Lint` vscode extensions (or any, really..)
- There is no driftwars specific extension yet

## Warning!!
There are differences between `DriftShader` and `ShaderToy`!!

- `ShaderToy / WebGL` auto-initializes variables to `0`! `DriftShader` does not!!!
    - If you copy a `ShaderToy` shader and it is not working (or crashing), VERIFY all variables are manually initialized to `0` !
- `ShaderToy (OpenGL)` and `DriftShader (vulkan)` use different coordinate systems!
    - If you copy a `ShaderToy` shader to `DriftShader`, it may render upside-down!
    - May need to use `gx_flip_uv` and `gx_flip_frag_coord`.
- `DriftShader` does not support all of `ShaderToy` inputs and features.