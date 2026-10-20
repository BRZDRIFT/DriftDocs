## Table Constructors

### Syntaxes
There are 3 different syntaxes to construct tables.

- Default Syntax, `{ key = value }`
- Expression Syntax, `{ [expression] = value }`
- JSON Syntax, `{ "key": value }`

### Default Syntax
- Key must be a string literal without quotes. String cannot start with a number.
- Format: `{ key = value }`

```sq
# Example:
local myTable = { myKey: 6 }    # Creates: { "myKey": 6 }
                                # Note: It does not matter if `myKey` is
                                # also the name of a variable, the
                                # key will still be string literal "myKey"
```

### Expression Syntax
- The key is the evaluated expression inside []
- Format: `{ [expr] = value }`

```sq
# Example 1:
local myTable = { [7]: 6 }          # Creates: { 7: 6 }

# Example 2:
local myKey = "dog"
local myTable = { [myKey]: 6 }      # Creates: { "dog": 6 }
```

### JSON Syntax
- The key must be a string literal. Cannot use a variable or number for the key.
- Format: `{ "key": value }`

```sq
# Example:
local myTable = { "myKey": 6 }      # Creates: { "myKey": 6 }
```

### More Examples:
```sq
local a = { [3] = "abc" }           # Creates: { 3: "abc" }

# local b = { 3 = "abc" }           # invalid syntax, in Default Syntax,
                                    # key must not started with a number

# local c = { 3: "abc" }            # invalid syntax, in JSON Syntax,
                                    # key must be a "string"

local d = { "3": "abc" }            # Creates: { "3": "abc" }

# local e = { "3" = "abc" }         # invalid syntax, in Default Syntax,
                                    # string key must not have quotes

local myKey = "dog"

local f = { myKey = "test" }        # { "myKey": "test" }

local g = { [myKey] = "test" }      # { "dog": "test" }

# local h = { myKey: 4 }            # invalid syntax, in JSON Syntax,
                                    # key must be a "string"

local i = { "myKey": "test" }       # { "myKey": "test" }
```