## Vec2
```sq
class Vec2 {
    constructor(x=0.0, y=0.0)
    function _add(Vec2 other)               // returns Vec2
    function _sub(Vec2 other)               // returns Vec2
    function _mul((float|int|Vec2) other)   // returns Vec2
    function _div((float|int|Vec2) other)   // returns Vec2
    function _unm(Vec2 other)               // returns Vec2
    function _unp(Vec2 other)               // returns Vec2
    function _eq(Vec2 other)                // returns bool
    function _hash()                        // returns int
    function _tostring()                    // returns string
    function IsZero(other)                  // returns bool
    function Dot(Vec2 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function UnitVecOrZero()                // returns Vec2<float>
    function UnitVecOrRandom()              // returns Vec2<float>
    function NumComponents()                // returns 2
    function ToInt()                        // returns a copy as Vec2<int>
    function ToFloat()                      // returns a copy as Vec2<float>
    m_x = 0.0
    m_y = 0.0
}
```

Helper Create Functions:
```sq
function Float2(x, y)
function Int2(x, y)
```

- By default `Vec2` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y` to integers manually)
- Assignment operator `=` will only copy reference (not create a new `Vec2`)
- Use `clone` to make deep copy


## Vec3
```sq
class Vec3 {
    constructor(x=0.0, y=0.0, z=0.0)
    function _add(Vec3 other)               // returns Vec3
    function _sub(Vec3 other)               // returns Vec3
    function _mul((float|int|Vec3) other)   // returns Vec3
    function _div((float|int|Vec3) other)   // returns Vec3
    function _unm(Vec3 other)               // returns Vec3
    function _unp(Vec3 other)               // returns Vec3
    function _eq(Vec3 other)                // returns bool
    function _hash()                        // returns int
    function _tostring()                    // returns string
    function IsZero(other)                  // returns bool
    function Dot(Vec3 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function UnitVecOrZero()                // returns Vec3<float>
    function UnitVecOrRandom()              // returns Vec3<float>
    function NumComponents()                // returns 3
    function xy()                           // returns Vec2(m_x, m_y)
    function ToInt()                        // returns a copy as Vec3<int>
    function ToFloat()                      // returns a copy as Vec3<float>
    m_x = 0.0
    m_y = 0.0
    m_z = 0.0
}
```

- By default `Vec3` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y`, `m_z` to integers manually)
- Assignment operator `=` will only copy reference (not create a new `Vec3`)
- Use `clone` to make deep copy
- Helper create functions: `function Float3(x, y, z)` and `function Int3(x, y, z)`;

## Vec4
```sq
class Vec4 {
    constructor(x=0.0, y=0.0, z=0.0, w=0.0)
    function _add(Vec4 other)               // returns Vec4
    function _sub(Vec4 other)               // returns Vec4
    function _mul((float|int|Vec4) other)   // returns Vec4
    function _div((float|int|Vec4) other)   // returns Vec4
    function _unm(Vec4 other)               // returns Vec4
    function _unp(Vec4 other)               // returns Vec4
    function _eq(Vec4 other)                // returns bool
    function _hash()                        // returns int
    function _tostring()                    // returns string
    function IsZero(other)                  // returns bool
    function Dot(Vec4 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function UnitVecOrZero()                // returns Vec4<float>
    function UnitVecOrRandom()              // returns Vec4<float>
    function NumComponents()                // returns 4
    function xy()                           // returns Vec2(m_x, m_y)
    function xyz()                          // returns Vec3(m_x, m_y, m_z)
    function ToInt()                        // returns a copy as Vec4<int>
    function ToFloat()                      // returns a copy as Vec4<float>
    m_x = 0.0
    m_y = 0.0
    m_z = 0.0
    m_w = 0.0
}
```

- By default `Vec4` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y`, `m_z`, `m_w` to integers manually)
- Assignment operator `=` will only copy reference (not create a new `Vec4`)
- Use `clone` to make deep copy
- Helper create functions: `function Float4(x, y, z, w)` and `function Int4(x, y, z, w)`;

## AABR
Axis aligned bounding rectangle
```sq
class AABR {
    // Create an AABR given minPt and maxPt
    constructor(minPt = Vec2(), maxPt = Vec2())

    // Creates an AABR given any two points
    // Internally determines m_minPt and m_maxPt
    static function CreateFromPoints(Vec2 pt0, Vec2 pt1)
    
    // Methods
    function _tostring()            // returns string
    function _eq(AABR other)        // returns bool
    function _hash()                // returns int
    function _cloned(AABR orig)
    function GetSize()              // returns Vec2<int|float>
    function GetTopLeft()           // returns Vec2<int|float>
    function GetTopRight()          // returns Vec2<int|float>
    function GetBottomLeft()        // returns Vec2<int|float>
    function GetBottomRight()       // returns Vec2<int|float>
    function GetCenter()            // returns Vec2<float>
    function Contains(Vec2 pt)                  // returns true if pt is inside AABR
    function ContainsOrTouching(Vec2 pt)        // returns true if pt is inside or on edge of AABR
    function ToInt()                // returns a copy as AABR<int>
    function ToFloat()              // returns a copy as AABR<float>

    // Variables
    m_minPt = Vec2()
    m_maxPt = Vec2() 
}
```

- By default `AABR` has scalar type of `float`.
- However you can change scalar type to be `int` by passing `Vec2<int>`'s into the constructor
    - (or by setting `m_minPt` and `m_maxPt` to `Vec2<int>` manually)
- Assignment operator `=` will only copy reference (not create a new `AABR`)
- Use `clone` to make deep copy

## ComplexColor
```sq
class ComplexColor {
    constructor()
    constructor(Vec3<float> srgba)
    constructor(Vec4<float> srgba)
    constructor(ColorType colorType)
    constructor(ColorType colorType, Vec3<float> srgba)
    constructor(ColorType colorType, Vec4<float> srgba)
    function _eq(ComplexColor other)
    function _hash()
    function _cloned(ComplexColor orig)

    m_srgba = Vec4(1.0, 1.0, 1.0, 1.0)
    m_type = ColorType.Normal
}
```

## Expr
```sq
// Expr feature is work-in-progress.
// Will become more useful over time (hopefully)
// These are often used for setting requirements for units/spells/etc
// or calculating values dynamically.

// Classes:

Expr.Unary(Expr.UnaryOp op, Expr expr)                          // mixed
Expr.Binary(Expr.BinaryOp op, Expr Expr0, Expr expr1)           // mixed
Expr.DynVal(DynValType ty, Expr expr)                           // mixed
Expr.HasUnit(string unitName)                                   // bool
Expr.HasPlayerResearch(string playerResearch, int level = 1)    // bool
Expr.HasUnitResearch(string unitResearch, int level = 1)        // bool

// Enums:

enum Expr.UnaryOp {
    Invalid,
    Not,
    Negate
}

enum Expr.BinaryOp {
    Invalid,
    Add,
    Subtract,
    Multiply,
    Divide,
    EQ,
    NE,
    LT,
    GT,
    LE,
    GE,
    Or,
    And,
}

enum Expr.DynValType {
	Invalid,
	PlayerResearch,				// int
	UnitResearch,				// int
	SimVar,						// int|float|bool|string
	PlayerVar,					// int|float|bool|string
	ForceVar,					// int|float|bool|string
	UnitVar,					// int|float|bool|string
	PlayerWeaponsUpgrade,		// int
	PlayerArmorUpgrade,			// int
	PlayerSpeedUpgrade,		    // int
	Gemstone,					// float
	Fungus,						// float
	Supply,					    // int
	MaxSupply,					// int
	SupplyBlocked,				// bool
	SiegedOrSieging,			// bool
	UnsiegedOrUnsieging		    // bool
}
```

## Future additions
- More types and member functions to be added later
