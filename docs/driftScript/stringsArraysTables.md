## string
```sq
string.len()
string.empty()
string.tointeger([base])
string.tofloat()
string.tostring()
string.replace(search, replace)
string.contains(search)
string.startswith(search)
string.endswith(search)
string.split(sep)
string.tolower()
string.toupper()
string.normalchars()
string.weakref()
```

## array
```sq
array.len()
array.append(val)
array.extend(array)
array.empty()
array.push(val)
array.pop()
array.top()
array.insert(idx, val)
array.remove(idx)
array.resize([size], [fill])
array.reverse()
array.sort([compare_func])
array.slice(start[, end])
array.weakref()
array.tostring()
array.clear()
array.map(func(item_value, [item_index], [array_ref]))
array.apply(func([item_value, [item_index], [array_ref]))
array.reduce(func(prevval, curval)[, initializer])
array.filter(func(index, val))
array.find(value)
array.find_ref(value)
```

## table
```sq
table.len()
table.empty()
table.tostring()
table.clear()
table.filter(func(key, val))
table.keys()
table.values()

# delete item:
delete table[key]

# check key in table:
key in table

# check key not in table:
key not_in table
```
