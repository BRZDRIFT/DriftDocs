# Math Library

## Constants
- `RAND_MAX`: 
    - Constant 64-bit int value of `0x7FFFFFFF`
- `PI`:
    - Constant float value for `PI` (`3.14159...`)
- `TAU`:
    - Constant float value for `2*PI` (`6.28318...`)
- `INT_MAX`:
    - `9223372036854775807`
- `INT_MIN`:
    - `-9223372036854775808`
- `INT_SMALLEST`:
    - `1`
- `FLOAT_MAX`:
    - `+9223372036854775807 / 4294967296` = `+2147483647.99999999976716935634...`
- `FLOAT_MIN`:
    - `-9223372036854775808 / 4294967296` = `-2147483648`
- `FLOAT_SMALLEST`:
    - `1 / 4294967296` = `0.00000000023283064365...`

## Functions
- `float sqrt(float x)` - returns square root of x
- `float sin(float x)` - return sin of x
- `float asin(float x)` - arcsin of x
- `float cos(float x)` - return cos of x
- `float acos(float x)` - arccos of x
- `float tan(float x)` - return tan of x
- `float atan(float x)` - arctan of x
- `float atan2(float y, float x)` - arctan2 of x
- `int rand()` - return random integer from [`0`, `RAND_MAX`]
- `int rand64()` - returns random integer from [`INT_MIN`, `INT_MAX`]
- `int rand_int(int min, int max)` returns random integer from [`min`, `max`]
- `float rand_float(float min, float max)` returns random float from [`min`, `max`]
- `mixed abs(mixed x)` - return absolute value of x.
- `mixed min(mixed x, mixed y)` - returns the minimum of x and y.
- `mixed max(mixed x, mixed y)` - returns the maximum of x and y.
- `mixed clamp(mixed val, mixed min, mixed max)` - clamps val to be between `min` and `max`
- `float lerp(float x, float y, float a)` - linearly interpolate x -> y based on [0, 1]
- `float floor(float x)`
- `float ceil(float x)`
- `mixed rem_euclid(mixed a, mixed b)` - similar to `%` operator, except result is always positive.

## Integer Division
- Integer division is trunucated (similar to C++ and rust, DIFFERENT than python)
     - `3/2 == 1`
     - `-3/2 == -1`

## % Modulo Operator
- result of `%` will have same sign as numerator (similar to c++/rust, DIFFERENT than python)
    - `-7 % 4 == -3`
    - `7 % -4 == 3`
    - `-7 % -4 == -3`
    - `-7.5 % 4.0 == -3.5`
    - `7.5 % -4.0 == 3.5`
    - you can use `rem_euclid` if you want the result to be positive
        - `rem_euclid(-7.5, 4.0) == .5`
        - `rem_euclid(7.5, -4.0) == 3.5`
        - `rem_euclid(7, -4) == 3`
        - `rem_euclid(-7, 4) == 1`

## Scalar Types
- `int`: 64-bit integer
    - max value: `+9,223,372,036,854,775,807`
    - min value: `-9,223,372,036,854,775,808`
    - note: many internal drift wars functions use `int32_t`
        - therefore try to keep values `<= 2147483647`
    - overflow is undefined, but most likely will work..
- `float`: custom 64-bit fixed point Q31.32
    - max value: `+9223372036854775807 / 4294967296` = `+2147483647.99999999976716935634...`
    - min value: `-9223372036854775808 / 4294967296` = `-2147483648`
    - smallest value: `1 / 4294967296` = `0.00000000023283064365...`
    - overflow is undefined, but most likely will work..

## Note
- Many of these functions are optimized for speed and not accuracy
