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

- `_cmp` meta-function removed.
- `==` and `!=` operators changed to check for deep value-equality (instead of reference-equality)
    - works for all types (dictionaries, arrays, classes, etc..)
    - recursively checks all child members/arrays/dictionaries/etc for equality
    - always auto-generated for user classes
- the other comparison operators `<`, `<=`, `>`, and `>=` only generated for user classes when possible
    - will not be generated if class contains a dictionary or array
- new keywords `is` and `is_not` added that check for reference-equality.
    - Equivalent to squirrel's `==` and `!=` behavior.
- `array.find(value)` changed to check for value-equality rather than reference-equality
    - `array.find_ref(value)` added to check for reference-equality
- Dictionary keys restricted to types `int`, `float`, `bool`, and `string`
- `int` types are signed 64-bit
- `float` types modified to be a 64-bit `Q31.32` fixed point types
- more type information at {{math("scalar-types")}}
- encoding `utf-8`
- `Squirrel Standard Library` is not supported.
    - Although, DriftScript provides many functions with identical behavior.