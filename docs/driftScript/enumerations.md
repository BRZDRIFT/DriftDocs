> Important!  
In your DriftScript code, DO NOT assume the numeric values of the enums will remain the same.  
Always use the enums and not hardcoded numeric values.  
Also DO NOT assume `Invalid` will always be equal to `0` or `-1`.

## BoundsCheck

```sq
enum BoundsCheck
{
	Invalid,
    Center,     // Unit's center position is in location
    Touching,   // Unit is fully inside or touching location
    Inside      // Unit fully inside a location
}
```

- The `BoundsCheck` enum is used in unit search queries within locations.  
- Primarily used in {{fn("gx_get_units-gx_get_units_count")}}

## SpecialPlayer
```sq
enum SpecialPlayer
{
    Invalid =  0,
    Neutral = -1,
    Hostile = -2,
    Rescue  = -3
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

## VictoryStatus
```sq
enum VictoryStatus
{
	Invalid,
	Pending,
	Victory,
	Defeat
}
```

- A `VictoryStatus::Pending` indicates the player is not yet assigned Victory/Defeat, usually meaning the player is still playing.
- `Draw` or `Tie` is not yet supported.

## ShapeType
```sq
enum ShapeType
{
    Invalid,
    Circle,
	Square,
	Rectangle
}
```

## DynVarType
```sq
enum DynVarType
{
    Invalid = 0,
    Constant = 1,
    FromPlayerResearch = 2,
    FromUnitResearch = 3,
    FromGlobalVar = 4,
    FromPlayerVar = 5,
    FromForceVar = 6,
    FromUnitVar = 7,
    PlayerWeaponsUpgrade = 8,
    PlayerArmorUpgrade = 9,
    PlayerSpeedUpgrade = 10,
    Gemstone = 11,
    Fungus = 12,
    Supply = 13,
    MaxSupply = 14,
	SupplyBlocked = 15
}
```

- The Force `Neutral` (`id = -1`) is special and exists in every game.
- The players `Neutral`, `Hostile`, and `Rescue` are automatically assigned to the `Neutral` Force
- `Note:` Normal ForceIDs are positive integers

## TerrainType
```sq
// Primary Terrain Types
enum TerrainType
{
	Invalid,
	
    Normal,         // See SecondaryTerrainTypeNormal
					// for valid secondary types

	Water,          // valid secondary types are [0 - 3]
	Lava,           // valid secondary types are [0 - 3]
	Diamond,        // valid secondary types is just 0
    Transparent,    // valid secondary types are [0 - 15]
    Glow,           // valid secondary types are [0 - 31]
	PlayerColor,    // valid secondary types are player_id, i.e. [1-16]

	Unpassable,     // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!
                    // valid secondary type is just 0 (currently)

	Space,          // valid secondary type is just 0

	CliffClosed,    // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!

	CliffBorder     // !! Not a dynamic terrain type!
					// Cannot dynamically change or be set to!
}
```

- Primarily used in {{fn("gx_set_terrain_type")}} and {{fn("gx_get_terrain_type")}}

## SecondaryTerrainTypeNormal
```sq
enum SecondaryTerrainTypeNormal
{
	Invalid,
	Normal,         // Units are normal on this type (no effects)
	Speed,          // Units move faster on this type
	AttackRate,     // Units have faster attack rate on this type
	Heal,           // Units heal faster on this type
	Forbidden,      // Units insta-die on this type
	Sniper,         // Units have increased range on this type
	MeleeOnly,      // Units have decreased range on this type
	Pacifist        // Units are unable to attack on this type
}
```

- Primarily used in {{fn("gx_set_terrain_type")}} and {{fn("gx_get_terrain_type")}}
- Should only be used in conjunction with `TerrainType.Normal`


## MapProp
```sq
enum MapProp
{
					    // Access		Type
	Invalid,
	ThemeColor,		        	// Read-Write	(Vec4<float>)
	GlowColor,			         // Read-Write	(Vec4<float>)
    EnableChatMessageEvents,     // Read-Write  (bool)
	EnableUnitDeathEvents, 		// Read-Write	(bool)
	Timer,						// Read-Write		(int)
}
```

## ForceProp
```sq
enum ForceProp
{
					// Access		Type
	Invalid,
	Score,			// Read-Write	(int)
	Name			// Read-Write	(string)
	VictoryStatus	// Read-Write	(VictoryStatus)
}
```

- Primarily used in {{fn("property-getterssetters")}}

## PlayerProp

```sq
enum PlayerProp
{
							// Access			Type
	Invalid,
	Fungus,                 // Read-Write     	(float)
	Gemstone,               // Read-Write     	(float)
	Supply,                 // Read        		(int)
	MaxSupply,              // Read        		(int)
	NumKills,               // Read        		(int)
	NumDeaths,              // Read        		(int)

    PlayerName,             // Read-Write  		(string)
							// Is Write-Enabled only for computer players

    FullMapVision,          // Read-Write     	(bool)
                            // When set to true, player
							// is given vision of entire map

    NumUnitsProduced,       // Read        		(int)
    TagID,                  // Read        		(int)
    ChoseRandom,            // Read        		(bool)
    Race,                   // Read        		(int)
    WeaponsLevel,           // Read-Write       (int)
    ArmorLevel,             // Read-Write       (int)

    SpeedLevel,             // Read-Write       (int)
	 						// (not implemented atm)
							
    StartLocationPosition,  // Read         	(Vec2)
	Score,					// Read-Write		(int)
    IsNormalPlayer, 		// Read				(bool)
    IsHumanPlayer, 			// Read				(bool)
    IsComputerPlayer,		// Read				(bool)
    IsHostilePlayer,		// Read				(bool)
    IsNeutralPlayer,		// Read				(bool)
    IsRescueablePlayer,		// Read				(bool)
	IsInGame,				// Read				(bool)
	VictoryStatus,			// Read-Write		(VictoryStatus),
	AlliedVictory,			// Read-Write		(bool)
	Color,					// Read-Write		(Vec3)
	ForceID					// Read				(int)
	PlayerNameColorDesc		// Read-Write		(int) (i.e. ColorDesc)
							// Is Write-Enabled only for computer players
							
	ColoredPlayerName		// Read 			(string)
							// Equivalent to:
							// gx_get_player_prop(PlayerProp.PlayerNameColorDesc, playerID)
							// + PlayerName

	ColoredPlayerName2		// Read				(string)
							// Equivalent to:
                            // gx_str_encode_color_id(ColorID.PushColor)
                            // + gx_get_player_prop(PlayerProp.ColoredPlayerName, playerID)
							// + PlayerName
							// + gx_str_encode_color_id(ColorID.PopColor)
}
```

- Primarily used in {{fn("property-getterssetters")}}

## UnitProp

```sq
enum UnitProp
{
							// Access			Type
	Invalid,
	MaxHealth,            	// Read      		(int)
	Health,                 // Read-Write     	(float)
	MaxSpeed,               // Read	        	(float)
	Size,                   // Read        		(float)
	UnitType,               // Read        		(string)
    IsOnFire,               // Read        		(bool)
    ParentJeep,             // Read-Write       (int)
	ParentDropship,         // Read-Write       (int)
	ParentStarShip,         // Read-Write       (int)
    ParentBunker,           // Read-Write       (int)
    GunShipState,           // Read-Write       (GunShipState)
	Level,					// Read-Write		(int)
    Tag,             		// Read-Write       (string)
    PlayerID,               // Read-Write       (int)
	
	ForceGhostMode,			// Read-Write		(bool)
							// Ghost mode allows units to walk through
							// other units (similar to workers harvesting
							// resources)

	FriendlyName,			// Read-Write		(string)
							// Allows you to override unit friendly name
							// on a per-unit basis.

	ForceInvulnerable,		// Read-Write		(bool)
    LookAtDirection,     	// Read-Write		(Float2)
    DriftMode,            	// Read-Write		(bool)
    IsCritter,     	        // Read	        	(bool)
    CritterFlag,       	    // Read-Write		(bool)
    IsSpeechBubbleActive,	// Read             (bool)
    Position,            	// Read-Write		(Float2)
    LockUnitToJeep,         // Read-Write       (bool)
	QuadDamageTicksRemaining, // Read-Write		(int)
}
```

- Primarily used in {{fn("property-getterssetters")}}
- Setting `Health` to `<= 0` will cause unit to be set to `killed` state.

## DecalProp
```sq
enum DecalProp
{
					        // Access	    Type
    Invalid,
    Position,               // Read/Write   Vec2<float>
    Rotation,               // Read/Write   float
    Size,                   // Read/Write   Vec2<float>
    Tag,                    // Read/Write   string
    InterpolateTransforms,  // Read/Write   bool
    RestrictToSpace         // Read/Write   bool
}
```

## LocationProp
```sq
enum LocationProp
{
					// Access		Type
	Invalid,
	TopLeft,        // Read 		(Vec2)
	TopRight,       // Read 		(Vec2)
	BottomLeft,     // Read 		(Vec2)
	BottomRight,    // Read 		(Vec2)
	Center,         // Read 		(Vec2)
	Size            // Read 		(Vec2)
    AABR,           // Read         (AABR)
}
```

- Primarily used in {{fn("property-getterssetters")}}

## GunShipState 
```sq
enum GunShipState
{
	Invalid,
    Normal,
    StarShot,
    BigGunLevel1,
    BigGunLevel2,
    ChainGunLevel1,
    ChainGunLevel2
}
```

- Primarily used for setting/getting unit property `GunShipState` in {{fn("property-getterssetters")}}

Example:
```sq
gx_set_unit_prop(unit_id, UnitProp.GunShipState, GunShipState.ChainGunLevel2)
```

- the above would give a gunship two chainguns

## ColorType
enum ColorType
{
	Invalid,
	Normal,
	Rainbow,
	Water,
	Lava
}

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
    Color_Black,                 	# 0x000000
    Color_White,                    # 0xFFFFFF
    Color_Red,                      # 0xFF0000
    Color_Orange,                   # 0xFF7F00
    Color_Yellow,                   # 0xFFFF00
    Color_Chartreuse,               # 0x7FFF00
    Color_Green,                    # 0x00FF00
    Color_SpringGreen,              # 0x00FF7F
    Color_Aqua,                     # 0x00FFFF
    Color_BabyBlue,                 # 0x007FFF
    Color_Blue,                     # 0x0000FF
    Color_Purple,                   # 0x7F00FF
    Color_Pink                      # 0xFF00FF
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

## CommandType
```sq
enum CommandType
{
	Invalid,
    Attack,             // valid params: [m_unitID, m_location, m_pos]
    Move,               // valid params: [m_unitID, m_location, m_pos]
    Hold,               // valid params: []
    Stop,               // valid params: []
    RightClick,         // valid params: [m_unitID, m_location, m_pos]
    Patrol              // valid params: [m_location, m_pos]
}
```

- Primarily used in {{fn("gx_queue_command")}}
- `string` identifiers for `Spells` can be used as well.
- more to be added later

## EffectType
```sq
enum EffectType
{
    Invalid,
    BlackHole,
	Visual_QuadDamage,
	Visual_DefMatrix
}
```

## EventType

```sq
enum EventType
{
    Invalid,           	 	// Invalid Event

    PlayerNameChanged,  	// Populates m_playerID, m_playerName, m_oldPlayerName,
							// m_playerName2, m_oldPlayerName2,
							// m_playerNameColor, m_oldPlayerNameColor

	PlayerNameColorChanged,	// Populates m_playerID, m_playerName, m_oldPlayerName,
							// m_playerName2, m_oldPlayerName2,
							// m_playerNameColor, m_oldPlayerNameColor

    PlayerLeftGame,     	// Populates m_playerID, m_playerName, m_playerName2,
    TextCommand             // Populates m_playerID, m_playerName, m_playerName2, m_cmd
	UnitEnteredLocation,	// Populates m_unitID, m_location
    UnitExitedLocation,		// Populates m_unitID, m_location
	Sound2dDestroyed,		// Populates m_soundID
	Sound3dDestroyed		// Populates m_soundID
    SwitchEvent,            // Populates m_playerID, m_unitID
    UnitPlayerChanged,      // Populates m_oldPlayerID, m_playerID, m_unitID
    ButtonPushed,           // Populates m_playerID, m_unitID
    Explosion               // Populates m_radius, m_pos, m_explosionEventType
    ChatMessage,            // Populates m_playerID, m_playerName, m_playerName2, m_text
    ItemPickup,             // Populates m_playerID, m_unitID, m_pos, m_itemUnitType, m_itemTag
	CustomSpellEvent,		// Populates m_playerID, m_unitID, m_pos, m_customSpellEventTag
	UnitDeath,				// Populates m_unitID, m_unitType, m_unitTag, m_playerID, m_killerPlayerID, m_deathCause
	TimerExpired,
}
```

## ExplosionEventType

```sq
enum ExplosionEventType
{
    Invalid,
    Nuke,
    Barrel
};
```

## DeathCause

```sq
enum DeathCause
{
    Unknown,
    FellIntoSpace,
    AutoAttack,
    Barrel,
    Railgun,
    Grenade,
    PlasmaGun,
    LightingGun,
 	Rocket,
    SeekingRocket,
	Nuke
};
```
