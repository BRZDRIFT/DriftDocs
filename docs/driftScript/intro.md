# Drift Script

## Introduction
`DriftScript` is the official scripting language of Drift Wars!  

`DriftScript` allows you to create custom game logic for both melee and custom maps.  
It is intended for people who already have good knowledge of other scripting languages such as `Python`.  

If you are new to programming and want to start programming in `DriftScript`, it is recommended you
visit [Python 3](https://www.python.org/downloads/) and learn `Python` first, as it is probably easier
to learn due to more learning material, and quicker feedback loops.

## Technical
`DriftScript` is a modified version of [Squirrel 3.2](http://squirrel-lang.org/squirreldoc/reference/language.html) language.

Please refer to the language reference manual here:  
[http://squirrel-lang.org/squirreldoc/reference/language.html](http://squirrel-lang.org/squirreldoc/reference/language.html)

Major changes from Squirrel:

- Comparison operator changes!
    - `_cmp` meta-function removed.
    - `==` and `!=` operators overhauled to check for deep value-equality (instead of reference-equality)
        - works for all types (dictionaries, arrays, classes, etc..)
        - recursively checks all child members/arrays/dictionaries/etc for equality
    - the other comparison operators `<`, `<=`, `>`, and `>=` are provided for user classes when possible
        - will not be provided if class contains a dictionary or array
    - new keywords `is` and `is_not` added to check for reference-quality.
        - Equivalent to squirrel's `==` and `!=`.
    - `array.find(value)` modified to check for value-equality rather than reference-equality
        - `array.find_ref(value)` added to check for reference-equality
- Dictionary changes:
    - Key types are restricted to `int`, `float`, `bool`, and `string`
- Type changes:
    - `int` types are signed 64-bit
    - `float` types modified to be a 64-bit `Q31.32` fixed point types
    - more type information at {{math("scalar-types")}}
- Encoding `utf-8`
- `Squirrel Standard Library` is not supported.
    - Although, DriftScript provides many functions with identical behavior.