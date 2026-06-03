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

Please refer to the squirrel language reference manual here:  
[http://squirrel-lang.org/squirreldoc/reference/language.html](http://squirrel-lang.org/squirreldoc/reference/language.html)

Major changes from Squirrel:

- Comparison operators and dictionaries reworked to use `_eq`, `_cmp`, and `_hash`
    - Added user-implementable `bool _eq(other)` meta-function.
        - Is invoked during `==` and `!=` comparisons
            - If `_eq` is not defined, will fallback to calling `_cmp` meta-function
            - If `_eq` and `_cmp` both do not exist, fall-back to reference-equality for `==`.
        - Note: This is DIFFERENT than Squirrel's `==` and `!=` which ALWAYS checks for reference equality.
        - Keywords `is` and `is_not` added to check for reference-equality (i.e. Squirrel's behavior)
    - Added function `int hash(obj1, obj2, ..)` that hashes objects/primitives
    - Added user-implementable `int _hash()` meta-function.
        - Is invoked in calls to `hash(obj, ...)`
        - If your custom class will be used as dictionary, you should implement `_eq` and `_hash` functions.
        - If `obj1 == obj2`, then `hash(obj1) == hash(obj2)` MUST be true.
            - If this is not true, your class will not work properly when used as keys in dictionaries.
    - Dictionaries now invoke `_hash` and `_eq`/`_cmp` for keys
        - Note: This is DIFFERENT than Squirrel which just checks for reference equality.
    - Array and Dictionary `==`/`!=` operators invoke sub-object's `_eq`/`_cmp` meta-functions.
        - Once again, this is DIFFERENT than Squirrel that checks for reference-equality.
        - Can always use `is` and `is_not` to compare if two arrays or dictionaries are the same object
    - Added function `int object_id(obj)` to get object id for class instances, arrays, and dictionaries
        - returns `0` for other types
    - `array.find(value)` modified to compare using `_eq`/`_cmp` rather than reference-equality
    - `array.find_ref(ref)` added to check for reference-equality (i.e. Squirrel's behavior)
- Type changes:
    - `int` types are signed 64-bit 
    - `float` types modified to be a 64-bit `Q31.32` fixed point types
    - more type information at {{math("scalar-types")}}
- Encoding `utf-8`
- `Squirrel Standard Library` is not supported.
    - Although, DriftScript provides many functions with identical behavior.

- Future TODOs:
    - Want to relax some of Squirrel's lexing rules.
        - `local = .1` is valid but `local a = 0.1` is not.. wtf??
            - floats currently cannot have a leading `0`
        - `local a = -1` and `local a = 1` are valid but `local = +1` is not, WTF??
            - integers/floats currently cannot have a leading `+`
    - Better error-handling and compilation/runtime errors.