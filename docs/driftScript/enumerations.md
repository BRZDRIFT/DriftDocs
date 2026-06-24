## Race
```sq
enum Race
{
    Invalid = 0,
    Human = 1,
    Robot = 2,
    Monster = 3
}
```


## DeathCause
```sq
enum DeathCause
{
    Unknown = 0,
    FellIntoSpace = 1,
    AutoAttack = 2,
    Barrel = 3,
    Railgun = 4,
    Grenade = 5,
    PlasmaGun = 6,
    LightningGun = 7,
    Rocket = 8,
    SeekingRocket = 9,
    Nuke = 10
}
```


## EffectType
```sq
enum EffectType
{
    Invalid = 0,
    BlackHole = 1,
    Visual_QuadDamage = 2,
    Visual_DefMatrix = 3
}
```


## AttackType
```sq
enum AttackType
{
    Invalid = 0,
    Laser = 1,
    Punch = 2,
    Missile = 3,
    Orb = 4,
    SiegeBlast = 5,
    SmokeBlast = 6,
    ShortLaser = 7,
    Shotgun = 8,
    Grenade = 9
}
```


## VictoryStatus
```sq
enum VictoryStatus
{
    Invalid = -1,
    Pending = 0,
    Victory = 1,
    Defeat = 2,
    Draw = 3
}
```

- A `VictoryStatus::Pending` indicates the player is not yet assigned Victory/Defeat, usually meaning the player is still playing.
- `Draw` or `Tie` is not yet supported.
## SpecialPlayer
```sq
enum SpecialPlayer
{
    Invalid = 0,
    Neutral = -1,
    Hostile = -2,
    Rescue = -3
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
    Neutral = -1
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
    Attack = "Attack",          # valid params: [m_unitID, m_location, m_pos]
    Hold = "Hold",              # valid params: []
    Stop = "Stop",              # valid params: []
    Move = "Move",              # valid params: [m_unitID, m_location, m_pos]
    RightClick = "RightClick",  # valid params: [m_unitID, m_location, m_pos]
    Patrol = "Patrol"           # valid params: [m_location, m_pos]
}
```

- `string` identifiers for `Spells` can be used as well.
- more to be added later
## EventType
```sq
enum EventType
{
    Invalid = 0,
    PlayerNameChanged = 1,
    PlayerNameColorChanged = 2,
    PlayerLeftGame = 3,         # Populates m_playerID, m_playerName, m_playerName2,
    TextCommand = 4,            # Populates m_playerID, m_playerName, m_playerName2, m_cmd
    UnitEnteredLocation = 5,    # Populates m_unitID, m_location
    UnitExitedLocation = 6,     # Populates m_unitID, m_location
    Sound2dDestroyed = 7,       # Populates m_soundID
    Sound3dDestroyed = 8,       # Populates m_soundID
    SwitchEvent = 9,            # Populates m_playerID, m_unitID
    UnitPlayerChanged = 10,     # Populates m_oldPlayerID, m_playerID, m_unitID
    ButtonPushed = 11,          # Populates m_playerID, m_unitID
    Explosion = 12,             # Populates m_radius, m_pos, m_explosionEventType
    ChatMessage = 13,           # Populates m_playerID, m_playerName, m_playerName2, m_text
    ItemPickup = 14,            # Populates m_playerID, m_unitID, m_pos, m_itemUnitType, m_itemTag
    CustomSpellEvent = 15,      # Populates m_playerID, m_unitID, m_pos, m_customSpellEventTag
    UnitDeath = 16,             # Populates m_unitID, m_unitType, m_unitTag, m_playerID, m_killerPlayerID, m_deathCause
    TimerExpired = 17
}
```


## ExplosionEventType
```sq
enum ExplosionEventType
{
    Invalid = 0,
    Nuke = 1,
    Barrel = 2
}
```


## ShapeType
```sq
enum ShapeType
{
    Invalid = 0,
    Circle = 1,
    Square = 2,
    Rectangle = 3
}
```


## BoundsCheck
```sq
enum BoundsCheck
{
    Invalid = 0,
    Center = 1,     # Unit's center position is in location
    Touching = 2,   # Unit is fully inside or touching location
    Inside = 3      # Unit fully inside a location
}
```

- The `BoundsCheck` enum is used in unit search queries within locations.
## LocationProp
```sq
enum LocationProp
{
    Invalid = 0,        # Access/Type
    TopLeft = 1,        # Read (Vec2)
    TopRight = 2,       # Read (Vec2)
    BottomLeft = 3,     # Read (Vec2)
    BottomRight = 4,    # Read (Vec2)
    Center = 5,         # Read (Vec2)
    Size = 6,           # Read (Vec2)
    AABR = 7            # Read (AABR)
}
```


## GunShipState
```sq
enum GunShipState
{
    Invalid = -1,
    Normal = 0,
    StarShot = 1,
    BigGunLevel1 = 2
    BigGunLevel2 = 3,
    ChainGunLevel1 = 4,
    ChainGunLevel2 = 5
}
```


## UnitProp
```sq
enum UnitProp
{
    Invalid = 0,                    # Access/Type
    MaxHealth = 1,  	            # Read (int)
    Health = 2,                     # Read-Write (float)
    MaxSpeed = 3,                   # Read (float)
    Size = 4,                       # Read (float)
    UnitType = 5,                   # Read (string)
    IsOnFire = 6,                   # Read (bool)
    ParentJeep = 7,                 # Read-Write (int)
    ParentDropship = 8,             # Read-Write (int)
    ParentStarShip = 9,             # Read-Write (int)
    ParentBunker = 11,              # Read-Write (int)
    GunShipState = 12,              # Read-Write (GunShipState)
    Level = 13,                     # Read-Write (int)
    Tag = 14,                       # Read-Write (string)
    PlayerID = 15,                  # Read-Write (int)
    ForceGhostMode = 16,            # Read-Write (bool)
    FriendlyName = 17,              # Read-Write (string)
    ForceInvulnerable = 18,         # Read-Write (bool)
    LookAtDirection = 19,           # Read-Write (Vec2)
    DriftMode = 20,                 # Read-Write (bool)
    IsCritter = 21,                 # Read (bool)
    CritterFlag = 22,               # Read-Write (bool)
    IsSpeechBubbleActive = 23,      # Read (bool)
    Position = 24,                  # Read-Write (Vec2)
    LockUnitToJeep = 25,            # Read-Write (bool)
    QuadDamageTicksRemaining = 26   # Read-Write (int)
}
```


## SimProp
```sq
enum SimProp
{
    Invalid = 0,
    ThemeColor = 1,                 # Read-Write (Vec4)
    GlowColor = 2,                  # Read-Write (Vec4)
    EnableChatMessageEvents = 3,    # Read-Write (bool)
    EnableUnitDeathEvents = 4,      # Read-Write (bool)
    Timer = 5                       # Read-Write (int)
}
```


## DecalProp
```sq
enum DecalProp
{
    Invalid = 0,                # Access/Type
    Position = 1,               # Read-Write (Vec2)
    Rotation = 2,               # Read-Write (float)
    Size = 3,                   # Read-Write (Vec2)
    Tag = 4,                    # Read-Write (string)
    InterpolateTransforms = 5,  # Read-Write (bool)
    RestrictToSpace = 6         # Read-Write (bool)
}
```


## PlayerProp
```sq
enum PlayerProp
{
    Invalid = 0,                # Access/Type
    Fungus = 1,                 # Read-Write (float)
    Gemstone = 2,               # Read-Write (float)
    Supply = 3,                 # Read (int)
    MaxSupply = 4,              # Read (int)
    NumKills = 5,               # Read (int)
    NumDeaths = 6,              # Read (int)
    PlayerName = 7,             # Read-Write (string)
    FullMapVision = 8,          # Read-Write (bool)
    NumUnitsProduced = 9,       # Read (int)
    TagID = 10,                 # Read (int)
    ChoseRandom = 11,           # Read (bool)
    Race = 12,                  # Read (int)
    StartLocationPosition = 16, # Read-Write (int)
    Score = 17,                 # Read-Write (int)
    IsNormalPlayer = 18,        # Read (bool)
    IsHumanPlayer = 19,         # Read (bool)
    IsComputerPlayer = 20,      # Read (bool)
    IsHostilePlayer = 21,       # Read (bool)
    IsNeutralPlayer = 22,       # Read (bool)
    IsRescueablePlayer = 23,    # Read (bool)
    IsInGame = 24               # Read (bool)
    VictoryStatus = 25,         # Read-Write (VictoryStatus)
    AlliedVictory = 26,         # Read-Write (bool)
    Color = 27,                 # Read-Write (Vec3)
    ForceID = 28,               # Read (int)
    PlayerNameColor = 29,       # Read-Write		(int) (i.e. ColorDesc)
                                # Is Write-Enabled only for computer players
    ColoredPlayerName = 30,     # Read (string)
                                # Equivalent to:
                                # gx_get_player_prop(PlayerProp.PlayerNameColorDesc, playerID)
                                # + PlayerName
    ColoredPlayerName2 = 31     # Read (string)
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
    Heavy
}
```


## ForceProp
```sq
enum ForceProp
{
    Invalid = 0,        # Access/Type
    Score = 1,          # Read-Write (int)
    Name = 2,           # Read-Write (string)
    VictoryStatus = 3   # Read-Write (VictoryStatus)
}
```


## TerrainType
```sq
enum TerrainType
{
    Invalid = -1,
    Normal = 0,
    Water = 2,          # valid secondary types are [0 - 3]
    Lava = 3,           # valid secondary types are [0 - 3]
    Diamond = 4,        # valid secondary types is just 0
    Transparent = 5,    # valid secondary types are [0 - 15]
    Glow = 6,           # valid secondary types are [0 - 31]
    PlayerColor = 8,    # valid secondary types are player_id, i.e. [1-16]
    Unpassable = 9,     # !! Not a dynamic terrain type!
    Space = 10,         # valid secondary type is just 0
    CliffClosed = 14,   # !! Not a dynamic terrain type!
    CliffBorder = 15    # !! Not a dynamic terrain type!
}
```


## SecondaryTerrainTypeNormal
```sq
enum SecondaryTerrainTypeNormal
{
    Invalid = -1,
    Normal = 0,     # Units are normal on this type (no effects)
    Speed = 1,      # Units move faster on this type
    AttackRate = 2, # Units have faster attack rate on this type
    Heal = 3,       # Units heal faster on this type
    Forbidden = 4,  # Units insta-die on this type
    Sniper = 5,     # Units have increased range on this type
    MeleeOnly = 6,  # Units have decreased range on this type
    Pacifist = 7    # Units are unable to attack on this type
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
    Emoji_GrinningFace
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
## ColorType
```sq
enum ColorType
{
    Invalid = -1
    Normal = 0,
    Rainbow = 1,
    Water = 2,
    Lava = 3
}
```


## Expr.DynValType
```sq
enum Expr.DynValType
{
	Invalid = 0,
	PlayerResearch = 2,				# int
	UnitResearch = 3,				# int
	SimVar = 4,						# int|float|bool|string
	PlayerVar = 5,					# int|float|bool|string
	ForceVar = 6,					# int|float|bool|string
	UnitVar = 7,					# int|float|bool|string
	PlayerWeaponsUpgrade = 8,		# int
	PlayerArmorUpgrade = 9,			# int
	PlayerSpeedUpgrade = 10,		# int
	Gemstone = 11,					# float
	Fungus = 12,					# float
	Supply = 13,					# int
	MaxSupply = 14,					# int
	SupplyBlocked = 15,				# bool
	SiegedOrSieging = 16,			# bool
	UnsiegedOrUnsieging = 17		# bool
}
```


## Expr.BinaryOp
```sq
enum Expr.BinaryOp
{
    Invalid = 0,
    Add = 1,
    Subtract = 2,
    Multiply = 3,
    Divide = 4,
    EQ = 5,
    NE = 6,
    LT = 7,
    GT = 8,
    LE = 9,
    GE = 10,
    Or = 11,
    And = 12
}
```


## Expr.UnaryOp
```sq
enum Expr.UnaryOp
{
    Invalid = 0,
    Not = 1,
    Negate = 2
}
```


