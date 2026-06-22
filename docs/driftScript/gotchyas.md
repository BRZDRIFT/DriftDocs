## How to return more than one value from a function?
- You can return the values using an array

```sq
function myFunction() {
	return [123, "second_return_value"];
}

local vals = myFunction()
print(vals[0])	# 123
print(vals[1])	# "second_return_value"
```

## Can I retrieve a global function object via a string lookup ?
- Yes, you can retrieve function object by accessing the root table

```sq
function myFunction(a, b) {
	return a+b;
}

local functionPtr = getroottable()["myFunction"];
local result = functionPtr(3, 5);
print(result)	# 8
```

## Use `local` for defining variables
- Variables must be defined using `local`
```sq
local myVariable = 7    # good!

myVariable2 = 8         # script-error! Forgot local keyword.
```

## Must use `<-` operator to add new key/value to dictionary
```sq
# need to use <- to add new key/value to dictionary
local myDictionary = {}
myDictionary["abc"] <- 7        # works
myDictionary["def"] = 9         # script error! key "def" does not exist!

# however, you can use = to modify existing value
myDictionary["abc"] = 10        # works, since key "abc" already exists
myDictionary["abc"] <- 12       # also works

# note: can also create dictionaries in-place
local myNewDictionary = { abc = 6, def = 9}   # no quotes for in-place string keys
myNewDictionary[15] <- "some string"        # keys can also be integers
```

## `=` assignment operator copies reference, not value! (for custom types)
```sq
local a = Vec2(2.0, 6.0)
local b = a			# reference copy
local c = clone a	# value copy
print(a is b)		# true, a and b reference same object
print(a is c)		# false, a and c reference different objects
print(a == c)	# true
```

- this behavior is only for non-primitive types (not `int`, `float`, `bool`, `string`)
- `=` assignment operator primitive types `int`, `float`, `bool`, `string` copy by value (not by reference)
- To make a copy of an object, use squirrel's builtin `clone` operator
- If you make your own types, it might be a good idea to create your own `._cloned(other)` function.

## Casting, ints, floats, strings, etc...
```sq
local a = 5       # a is type 'integer' of value 5
print(a)          # prints '5'
print(a / 2)      # prints '2.50',   # normal division always returns float 
print(a // 2)     # prints '2',   # floor division operator
print(a // -2)    # prints '-3', # floor division operator 
print(a // 2.0)   # prints '2.00',   # floor division operator
print(a // -2.0)  # prints '-3.00', # floor division operator 

local b = 5.0     # a is type 'float' of value 5.0
print(b)          # prints '5.00',    # floats always outputs to 2 decimals
print(b / 2)      # prints '2.50',    # float division acts as normal

# You can cast an integer to float or float to integer
# using the .tointeger() and .tofloat() functions

local c = b.tointeger()     # 'c' is now an integer with value 5
local d = a.tofloat()       # 'd' is now a float with value 5.0
local e = a.tointeger()     # .tointeger() acts a dummy functions
                            # for casting from 'int' -> 'int'
local f = b.tofloat()       # .tofloat() acts a dummy functions
                            # for casting from 'float' -> 'float'

local myString1 = e.tostring()
print(myString1)                    # prints '5'

local myString2 = f.tostring()
print(myString2)                    # prints '5.00'

# number to string conversions happen automatically
print("abc " + a)                   # prints "abc 5"             

# Warning!
# You are not allowed to cast using '(int) expr' and '(float) expr'
# syntax. You must use .tostring(), .tofloat(), .tointeger(), etc..
# local z = (int) f       # ERROR! Cannot do this type of casting

# You can also print Vec2, Vec3, Vec4, AABR types, see below:

# Prints: "My Int Vector = (4, 5)"
print("My Int Vector = " + Vec2(4, 5))

# Prints: "My Float Vector = (4.00, 5.00)"
print("My Float Vector = " + Vec2(4, 5).ToFloat())

# Prints: "My Float Vector = (4.00, 5.00)"
print("My Float Vector = " + Vec2(4.0, 5.0))
```

## Comments
- You can write single-line comments by using `#` or `#`
- Currently cannot write multi-line comment..
```sq
# this is a single line comment

# this is also a comment :)
```

## Common dictionary and array tasks
```sq
# deleting from dictionary
local myDictionary = { "abc": 6, "def": 7 }     # create dictionary
delete myDictionary["abc"]                  # delete "abc" from dictionary

# check if key in dictionary
local bResult = "def" in myDictionary
print(bResult)	# true

# arrays
local myArray = ["my_string", 6, 1, 2]      # create array
print(myArray[0])                   # prints "my_string"
myArray.append(7)                   # myArray:  ["my_string", 6, 1, 2, 7]
print(myArray[4])                   # prints 7
myArray.remove(1)           # remove at index 1, myArray: ["my_string", 1, 2, 7]
```

- See [http:#squirrel-lang.org/squirreldoc/reference/language.html](http:#squirrel-lang.org/squirreldoc/reference/language.html) for more language features.

## Dictionary and array foreach loops
```sq
# dictionary initializer syntax #1: { key = val }
# Possible Output (dictionary iteration order is unspecified):
# a -> 5
# c -> dog
# b -> 2
local myDict1 = { a = 5, b = 2, c = "dog"}
foreach (key, val in myDict1) {
	print(key + " -> " + val)
}

# dictionary initializer syntax #2: { "key": val }
# Possible Output (dictionary iteration order is unspecified):
# a -> 5
# c -> dog
# b -> 2
local myDict2 = { "a": 5, "b": 2, "c": "dog"}
foreach (key, val in myDict2) {
	print(key + " : " + val)
}

# dictionary single variable iteration..
# NOTE: this syntax outputs value, not key as in languages like python
# Possible Output (dictionary iteration order is unspecified):
# 5
# dog
# 2
local myDict3 = { "a": 5, "b": 2, "c": "dog"}
foreach (val in myDict3) {
	print(val)
}

# array initializer syntax: [val0, val1, etc]
# Output (array foreach iteration is ordered):
# 4
# 6
# dog
# 3
local myArray = [4, 6, "dog", 3]
foreach (val in myArray) {
	print(val)
}

# Output (array foreach iteration is ordered):
# 0 -> 4
# 1 -> 6
# 2 -> dog
# 3 -> 3
foreach (idx, val in myArray) {
	print(idx + " -> " + val)
}
```

- Please note, single variable foreach loop with dictionary outputs `value` and not `key`.
    - This is different from other languages like `Python`.
- dictionary foreach iteration order is `unspecified` (which is different than random)

## Other
- semicolons `;` at the end of lines are optional, similar to `Python`