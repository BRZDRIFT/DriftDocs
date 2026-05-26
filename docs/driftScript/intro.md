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

Additions to squirrel and/or things you might want to know..

- `int` types are signed 64-bit
- `float` types modified to be a 64-bit `Q31.32` fixed point types
- more type information at {{math("scalar-types")}}
- encoding `utf-8`
- `Squirrel Standard Library` is not supported.
