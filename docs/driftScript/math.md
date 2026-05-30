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
- `float sqrt(x)` - returns square root of x
- `float sin(x)` - return sin of x
- `float asin(x)` - arcsin of x
- `float cos(x)` - return cos of x
- `float acos(x)` - arccos of x
- `float tan(x)` - return tan of x
- `float atan(x)` - arctan of x
- `float atan2(y, x)` - arctan2 of x
- `int rand()` - return random integer from [0, RAND_MAX]
- `mixed abs(x)` - return absolute value of x.
- `mixed min(x, y)` - returns the minimum of x and y.
- `mixed max(x, y)` - returns the maximum of x and y.
- `mixed clamp(val, min, max)` - clamps val to be between min and max
- `float lerp(x, y, a)` - linearly interpolate x -> y based on a [0, 1]
- `float floor(x)`
- `float ceil(x)`
- `float fmod(x, y)` - floating point modulo

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
