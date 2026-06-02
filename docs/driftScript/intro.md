# Drift Script

## Introduction
`DriftScript` is the official scripting language of Drift Wars!  

`DriftScript` allows you to create custom game logic for both melee and custom maps.  
It is intended for people who already have good knowledge of other scripting languages such as `Python`.  

If you are new to programming and want to start programming in `DriftScript`, it is recommended you
visit [Python 3](https://www.python.org/downloads/) and learn `Python` first, as it is probably easier
to learn due to more learning material, and quicker feedback loops.

## Technical
`DriftScript` is a `!!HEAVILY!!` modified version of [Squirrel 3.2](http://squirrel-lang.org/squirreldoc/reference/language.html) language.

Please refer to the language reference manual here:  
[http://squirrel-lang.org/squirreldoc/reference/language.html](http://squirrel-lang.org/squirreldoc/reference/language.html)

Major changes from Squirrel:

- Comparison operators and dictionaries check for value-equality:
    - `==` and `!=` check for value-equality! (not reference equality, as-in squirrel)
        - In DriftScript, `==` and `!=` call the user-implemented `_eq` meta function.
            - If `_eq` is not defined, will fallback to calling `_cmp` meta function
            - If `_eq` and `_cmp` both do not exist, fall-back to reference equality for `==`.
        - Keywords `is` and `is_not` added to check for reference equality
    - Added new user-implementable `_hash` meta function.
        - automatically called when `hash(obj)` is called.
        - If your custom class will be used as dictionary, you should implement a `_eq` and `_hash` function.
        - If `obj1 == obj2`, then `hash(obj1) == hash(obj2)` MUST be true.
            - If this is not true, your class will not work properly when used as keys in dictionaries.
    - Added function `object_id(obj)` to get object id for class instances, arrays, and dictionaries
        - returns `0` for other types 
    - `array.find(value)` modified to check for value-equality rather than reference-equality
        - `array.find_ref(value)` added to check for reference-equality
- Type changes:
    - `int` types are signed 64-bit 
    - `float` types modified to be a 64-bit `Q31.32` fixed point types
    - more type information at {{math("scalar-types")}}
- Encoding `utf-8`
- `Squirrel Standard Library` is not supported.
    - Although, DriftScript provides many functions with identical behavior.