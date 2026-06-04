# Drift Shader

## Introduction

The `BG.ShaderToy.glsl` utilizes `DriftShader` to render the map and minimap background.

- It is based-off of `ShaderToy`, which uses `GLSL` as the shading language.
- Browse `https://www.shadertoy.com/` for documentation.

## Entry Function
```
void mainImage(out vec4 outSRGB, vec2 inPosition) {
  outSRGB = vec4(0, 1, 0, 1);
}
```

- You are required to set the output variable `outSRGB` to color you want the "pixel" to be.
- `outSRGB` is expected to be in `sRGB`
    - I would prefer the output to be in `linear`, but ShaderToy uses `sRGB` -- and I want to maintain as much similarity as possible.
    - If you want to output in `linear`, you need to set the option under `Background` tab in the map editor.
- There are other settings in the `Background` tab such as rotation, speed, enable dither, etc..

## Global Uniform Values
```
uniform vec3      iResolution;           // think of it as resolution (sort-of) (can be shrunk/stretched via Background tab)
uniform float     iTime;                 // game-time (in seconds)
uniform int       iFrame;                // present but not supported yet (always 0)
uniform vec3      iChannelResolution[4]; // channel resolution (in pixels)
uniform vec4      iMouse;                // present but not supported yet (always vec4(0,0,0,0))
uniform sampler2D iChannel0;             // texture/sampler #0 (can be set via Background tab)
uniform sampler2D iChannel1;             // texture/sampler #1 (can be set via Background tab)
uniform sampler2D iChannel2;             // texture/sampler #2 (can be set via Background tab)
uniform sampler2D iChannel3;             // texture/sampler #3 (can be set via Background tab)
```

## Color Conversion Functions
```
float gx_linear_to_srgb(float linear)
vec3 gx_linear_to_srgb(vec3 linear)
vec4 gx_linear_to_srgb(vec4 linear)
float gx_srgb_to_linear(float srgb)
vec3 gx_srgb_to_linear(vec3 srgb)
vec4 gx_srgb_to_linear(vec4 srgb)
```

## gx_get_bg_shader_val
```
float gx_get_bg_shader_val(int index)
```

- retrieves the shader value at slot `index`
- the initial shader values can be set under `Background -> Shader Values` in the map editor
- these values can be changed via `.DriftScript` using the `void gx_set_bg_shader_val(int index, float value)` function.

## gx_flip_uv
```
vec2 gx_flip_uv(vec2 uv) {
    uv.y = 1.0 - uv.y;
    return uv;
}
```

- Helper to convert between `ShaderToy (OpenGL)` and `DriftShader (vulkan)` coordinate systems
- (usually you don't need to use this, provided for convenience)

## gx_flip_frag_coord
```
vec2 gx_flip_frag_coord(vec2 fragCoord) {
    fragCoord.y = iResolution.y - uv.y;
    return fragCoord;
}
```

- Helper to convert between `ShaderToy (OpenGL)` and `DriftShader (vulkan)` coordinate systems
- (usually you don't need to use this, provided for convenience)

## Warning!!
Differences between `DriftShader` and `ShaderToy`!!
- `ShaderToy / WebGL` auto-initializes variables to `0`! `DriftShader` does not!!!
    - If you copy a `ShaderToy` shader and it is not working (or crashing), VERIFY all variables are manually initialized to `0` !
- `ShaderToy (OpenGL)` and `DriftShader (vulkan)` use different coordinate systems!
    - If you copy a `ShaderToy` shader to `DriftShader`, it may render upside-down!