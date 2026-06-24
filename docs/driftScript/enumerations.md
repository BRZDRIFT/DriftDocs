## ColorType
```sq
enum ColorType
{
    Invalid = -1,
    Normal,
    Rainbow,
    Water,
    Lava,
}
```


## Expr.DynValType
```sq
enum Expr.DynValType
{
    Invalid = 0,
    PlayerResearch,	# int
    UnitResearch,	# int
    SimVar,	# int|float|bool|string
    PlayerVar,	# int|float|bool|string
    ForceVar,	# int|float|bool|string
    UnitVar,	# int|float|bool|string
    PlayerWeaponsUpgrade,	# int
    PlayerArmorUpgrade,	# int
    PlayerSpeedUpgrade,	# int
    Gemstone,	# float
    Fungus,	# float
    Supply,	# int
    MaxSupply,	# int
    SupplyBlocked,	# bool
    SiegedOrSieging,	# bool
    UnsiegedOrUnsieging,	# bool
}
```


## Expr.BinaryOp
```sq
enum Expr.BinaryOp
{
    Invalid = 0,
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
```


## Expr.UnaryOp
```sq
enum Expr.UnaryOp
{
    Invalid = 0,
    Not,
    Negate,
}
```


## Race
```sq
enum Race
{
    Invalid = 0,
    Human,
    Robot,
    Monster,
}
```


## DeathCause
```sq
enum DeathCause
{
    Unknown = 0,
    FellIntoSpace,
    AutoAttack,
    Barrel,
    Railgun,
    Grenade,
    PlasmaGun,
    LightningGun,
    Rocket,
    SeekingRocket,
    Nuke,
}
```


## EffectType
```sq
enum EffectType
{
    Invalid = 0,
    BlackHole,
    Visual_QuadDamage,
    Visual_DefMatrix,
}
```


## AttackType
```sq
enum AttackType
{
    Invalid = 0,
    Laser,
    Punch,
    Missile,
    Orb,
    SiegeBlast,
    SmokeBlast,
    ShortLaser,
    Shotgun,
    Grenade,
}
```


## VictoryStatus
```sq
enum VictoryStatus
{
    Invalid = -1,
    Pending,
    Victory,
    Defeat,
    Draw,
}
```

- A `VictoryStatus::Pending` indicates the player is not yet assigned Victory/Defeat, usually meaning the player is still playing.
- `Draw` or `Tie` is not yet supported.
## SpecialPlayer
```sq
enum SpecialPlayer
{
    Invalid = 0,
    Neutral,
    Hostile,
    Rescue,
}
```

- The above are the `PlayerIDs` for the special players `Neutral`, `Hostile`, and `Rescue`
- The players `Neutral`, `Hostile`, and `Rescue` are automatically assigned to the `Neutral` Force
- These 3 special players exist in every game and game-mode.
- `Note:` Normal PlayerIDs are positive, with values: `[1-16]`
## SpecialForce
```sq
enum SpecialForce
{
    Invalid = 0,
    Neutral,
}
```

- The Force `Neutral` (`id = -1`) is special and exists in every game.
- The players `Neutral`, `Hostile`, and `Rescue` are automatically assigned to the `Neutral` Force
- `Note:` Normal ForceIDs are positive integers
## CommandType
```sq
enum CommandType
{
    Invalid = "",
    Attack,	# valid params: [m_unitID, m_location, m_pos]
    Hold,	# valid params: []
    Stop,	# valid params: []
    Move,	# valid params: [m_unitID, m_location, m_pos]
    RightClick,	# valid params: [m_unitID, m_location, m_pos]
    Patrol,	# valid params: [m_location, m_pos]
}
```

- `string` identifiers for `Spells` can be used as well.
- more to be added later
## EventType
```sq
enum EventType
{
    Invalid = 0,
    PlayerNameChanged,	# Populates m_playerID, m_playerName, m_oldPlayerName,
	# m_playerName2, m_oldPlayerName2,
	# m_playerNameColor, m_oldPlayerNameColor
    PlayerNameColorChanged,	# Populates m_playerID, m_playerName, m_oldPlayerName,
	# m_playerName2, m_oldPlayerName2,
	# m_playerNameColor, m_oldPlayerNameColor
    PlayerLeftGame,	# Populates m_playerID, m_playerName, m_playerName2,
    TextCommand,	# Populates m_playerID, m_playerName, m_playerName2, m_cmd
    UnitEnteredLocation,	# Populates m_unitID, m_location
    UnitExitedLocation,	# Populates m_unitID, m_location
    Sound2dDestroyed,	# Populates m_soundID
    Sound3dDestroyed,	# Populates m_soundID
    SwitchEvent,	# Populates m_playerID, m_unitID
    UnitPlayerChanged,	# Populates m_oldPlayerID, m_playerID, m_unitID
    ButtonPushed,	# Populates m_playerID, m_unitID
    Explosion,	# Populates m_radius, m_pos, m_explosionEventType
    ChatMessage,	# Populates m_playerID, m_playerName, m_playerName2, m_text
    ItemPickup,	# Populates m_playerID, m_unitID, m_pos, m_itemUnitType, m_itemTag
    CustomSpellEvent,	# Populates m_playerID, m_unitID, m_pos, m_customSpellEventTag
    UnitDeath,	# Populates m_unitID, m_unitType, m_unitTag, m_playerID, m_killerPlayerID, m_deathCause
    TimerExpired,
}
```


## ExplosionEventType
```sq
enum ExplosionEventType
{
    Invalid = 0,
    Nuke,
    Barrel,
}
```


## ShapeType
```sq
enum ShapeType
{
    Invalid = 0,
    Circle,
    Square,
    Rectangle,
}
```


## BoundsCheck
```sq
enum BoundsCheck
{
    Invalid = 0,
    Center,	# Unit's center position is in location
    Touching,	# Unit is fully inside or touching location
    Inside,	# Unit fully inside a location
}
```

- The `BoundsCheck` enum is used in unit search queries within locations.
## LocationProp
```sq
enum LocationProp
{
    Invalid = 0,	# Access/Type
    TopLeft,	# Read (Vec2)
    TopRight,	# Read (Vec2)
    BottomLeft,	# Read (Vec2)
    BottomRight,	# Read (Vec2)
    Center,	# Read (Vec2)
    Size,	# Read (Vec2)
    AABR,	# Read (AABR)
}
```


## GunShipState
```sq
enum GunShipState
{
    Invalid = -1,
    Normal,
    StarShot,
    BigGunLevel1,
    BigGunLevel2,
    ChainGunLevel1,
    ChainGunLevel2,
}
```


## UnitProp
```sq
enum UnitProp
{
    Invalid = 0,	# Access/Type
    MaxHealth,	# Read (int)
    Health,	# Read-Write (float)
    MaxSpeed,	# Read (float)
    Size,	# Read (float)
    UnitType,	# Read (string)
    IsOnFire,	# Read (bool)
    ParentJeep,	# Read-Write (int)
    ParentDropship,	# Read-Write (int)
    ParentStarShip,	# Read-Write (int)
    UNUSED,
    ParentBunker,	# Read-Write (int)
    GunShipState,	# Read-Write (GunShipState)
    Level,	# Read-Write (int)
    Tag,	# Read-Write (string)
    PlayerID,	# Read-Write (int)
    ForceGhostMode,	# Read-Write (bool)
	# Ghost mode allows units to walk through
	# other units (similar to workers harvesting
	# resources)
    FriendlyName,	# Read-Write (string)
	# Allows you to override unit friendly name
	# on a per-unit basis.
    ForceInvulnerable,	# Read-Write (bool)
    LookAtDirection,	# Read-Write (Vec2)
    DriftMode,	# Read-Write (bool)
    IsCritter,	# Read (bool)
    CritterFlag,	# Read-Write (bool)
    IsSpeechBubbleActive,	# Read (bool)
    Position,	# Read-Write (Vec2)
    LockUnitToJeep,	# Read-Write (bool)
    QuadDamageTicksRemaining,	# Read-Write (int)
}
```


## SimProp
```sq
enum SimProp
{
    Invalid = 0,
    ThemeColor,	# Read-Write (Vec4)
    GlowColor,	# Read-Write (Vec4)
    EnableChatMessageEvents,	# Read-Write (bool)
    EnableUnitDeathEvents,	# Read-Write (bool)
    Timer,	# Read-Write (int)
}
```


## DecalProp
```sq
enum DecalProp
{
    Invalid = 0,	# Access/Type
    Position,	# Read-Write (Vec2)
    Rotation,	# Read-Write (float)
    Size,	# Read-Write (Vec2)
    Tag,	# Read-Write (string)
    InterpolateTransforms,	# Read-Write (bool)
    RestrictToSpace,	# Read-Write (bool)
}
```


## PlayerProp
```sq
enum PlayerProp
{
    Invalid = 0,	# Access/Type
    Fungus,	# Read-Write (float)
    Gemstone,	# Read-Write (float)
    Supply,	# Read (int)
    MaxSupply,	# Read (int)
    NumKills,	# Read (int)
    NumDeaths,	# Read (int)
    PlayerName,	# Read-Write (string)
	# Is Write-Enabled only for computer players
    FullMapVision,	# Read-Write (bool)
	# When set to true, player
	# is given vision of entire map
    NumUnitsProduced,	# Read (int)
    TagID,	# Read (int)
    ChoseRandom,	# Read (bool)
    Race,	# Read (int)
    StartLocationPosition,	# Read-Write (int)
    Score,	# Read-Write (int)
    IsNormalPlayer,	# Read (bool)
    IsHumanPlayer,	# Read (bool)
    IsComputerPlayer,	# Read (bool)
    IsHostilePlayer,	# Read (bool)
    IsNeutralPlayer,	# Read (bool)
    IsRescueablePlayer,	# Read (bool)
    IsInGame,	# Read (bool)
    VictoryStatus,	# Read-Write (VictoryStatus)
    AlliedVictory,	# Read-Write (bool)
    Color,	# Read-Write (Vec3)
    ForceID,	# Read (int)
    PlayerNameColor,	# Read-Write		(int) (i.e. ColorDesc)
	# Is Write-Enabled only for computer players
    ColoredPlayerName,	# Read (string)
	# Equivalent to:
	# gx_get_player_prop(PlayerProp.PlayerNameColorDesc, playerID)
	# + PlayerName
    ColoredPlayerName2,	# Read (string)
	# Equivalent to:
	# gx_str_encode_color_id(ColorID.PushColor)
	# + gx_get_player_prop(PlayerProp.ColoredPlayerName, playerID)
	# + PlayerName
	# + gx_str_encode_color_id(ColorID.PopColor)
}
```


## ArmorType
```sq
enum ArmorType
{
    Invalid = 0,
    Light,
    Medium,
    Heavy,
}
```


## ForceProp
```sq
enum ForceProp
{
    Invalid = 0,	# Access/Type
    Score,	# Read-Write (int)
    Name,	# Read-Write (string)
    VictoryStatus,	# Read-Write (VictoryStatus)
}
```


## TerrainType
```sq
enum TerrainType
{
    Invalid = -1,
    Normal,	# See SecondaryTerrainTypeNormal
	# for valid secondary types
    Water,	# valid secondary types are [0 - 3]
    Lava,	# valid secondary types are [0 - 3]
    Diamond,	# valid secondary types is just 0
    Transparent,	# valid secondary types are [0 - 15]
    Glow,	# valid secondary types are [0 - 31]
    PlayerColor,	# valid secondary types are player_id, i.e. [1-16]
    Unpassable,	# !! Not a dynamic terrain type!
	# Cannot dynamically change or be set to!
	# valid secondary type is just 0 (currently)
    Space,	# valid secondary type is just 0
    CliffClosed,	# !! Not a dynamic terrain type!
	# Cannot dynamically change or be set to!
    CliffBorder,	# !! Not a dynamic terrain type!
	# Cannot dynamically change or be set to!
}
```


## SecondaryTerrainTypeNormal
```sq
enum SecondaryTerrainTypeNormal
{
    Invalid = -1,
    Normal,	# Units are normal on this type (no effects)
    Speed,	# Units move faster on this type
    AttackRate,	# Units have faster attack rate on this type
    Heal,	# Units heal faster on this type
    Forbidden,	# Units insta-die on this type
    Sniper,	# Units have increased range on this type
    MeleeOnly,	# Units have decreased range on this type
    Pacifist,	# Units are unable to attack on this type
}
```

- Should only be used in conjunction with `TerrainType.Normal`
## Unicode
```sq
enum Unicode
{
    Special_PushColor,
    Special_PopColor,
    Special_PushInvisible,
    Special_PopInvisible,
    Special_DefaultColor,
    Color_Effect_Water,
    Color_Effect_Lava,
    Color_Effect_Rainbow,
    Color_Black,
    Color_White,
    Color_Red,
    Color_Orange,
    Color_Yellow,
    Color_Chartreuse,
    Color_Green,
    Color_SpringGreen,
    Color_Aqua,
    Color_BabyBlue,
    Color_Blue,
    Color_Purple,
    Color_Pink,
    Emoji_GrinningFace,
}
```

- Useful unicode characters available in the game.
- `Special_PushColor` and `Special_PopColor` are sort of special, and is used for text.
    - `Special_PushColor` pushes the current color onto a color stack
    - `Special_PopColor` pops a color off, and sets current text color to it
    - Allows you to save the current arbitrary color, and then re-use it later.
- `Special_PushInvisible` and `Special_PopInvisible` are also special
	- All characters after `Special_PushInvisible` will be invisible unless highlighted until a corresponding `Special_PopInvisible` is reached.
- The `Color_*` unicode characters control text colors for all characters after
