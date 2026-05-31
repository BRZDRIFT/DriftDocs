## gx_include
```sq
void gx_include(string filename)
```

- Includes `filename` in current compilation.
- A file is only included once by `gx_include`; subsequent calls are ignored.
- Typically called at the top of your drift script file.

## gx_create_unit
```sq
int gx_create_unit(int params)
```

```sq
table params = {
    string m_unitType,              // Required
    int m_playerID,                 // Required
    Vec2 m_pos,                     // Optional
    string m_location,              // Optional
    int m_level = 1                 // Optional, default unit level = 1
}
```

```sq
local new_unit = gx_create_unit({ m_unitType = "Brute", m_playerID = 1, m_location = "my_cool_location" })
```

- Will create unit of type `m_unitType` at position `m_pos` or at location `m_location` for player `m_playerID`.
- It is undefined behavior to have both `m_pos` and `m_location` set.
- If neither `m_pos` nor `m_location` is set, unit will be created at `(0, 0)`
- Refer to {{type("Vec2")}} if needed.

## gx_get_sim_tick
```sq
int gx_get_sim_tick()
```

- Returns the current sim tick number in simulation.
- The {{entry("gx_sim_init")}} call will have `tick = 0`
- The first {{entry("gx_sim_update")}} call will have `tick = 1`
- The second {{entry("gx_sim_update")}} call will have `tick = 2`, etc..
- every tick corresponds to 50ms real time

## gx_sim_ticks_to_seconds
```sq
float gx_sim_ticks_to_seconds(int simTicks)
```

- converts simTicks to seconds
- equivalent to: `(simTicks.tofloat() / 20.0)`

## gx_seconds_to_sim_ticks
```sq
float gx_seconds_to_sim_ticks(float seconds)
```

- converts `seconds` to `simTicks`
- equivalent to: `(seconds * 20.0).tointeger()`

## gx_get_seconds
```sq
float gx_get_seconds()
```

- return game time in seconds
- equivalent to: `gx_sim_ticks_to_seconds(gx_get_sim_tick())`

## gx_get_bg_shader_val_float
```sq
float gx_get_bg_shader_val_float(int index);
```

- index must be between `[0-15]`

## gx_get_bg_shader_val_float
```sq
float gx_set_bg_shader_val_float(int index, int val);
```

- `index` must be between `[0-15]`
- values set with this function can be obtained in Background ShaderToy shader via shader function `int gx_get_bg_shader_val_float(int index)`

## gx_get_distance_between_units
```sq
float gx_get_distance_between_units(int unitID, int otherUnitID)
```

- returns the distance between the edges of two units
- will return 0 if one or both of the units do not exist

## gx_units_touching
```sq
bool gx_units_touching(int unit0, int unit1)
```

- Returns `true` if the two units are "touching" (nearby eachother)


## gx_get_nearby_units / gx_get_nearby_units_count
```sq
int[] gx_get_nearby_units(table params)
int gx_get_nearby_units_count(table params)
```

```sq
table params = {
    int m_unitID,                                   // unit_id to center search on
    float m_radius,                                 // search radius around unit
    int m_playerIDs[],                              // Optional, Filter for player_id
    int m_forceIDs[],                               // Optional, Filter for force_id
    string m_unitTypes[],                           // Optional, Filter for certain unit types
    string m_exceptUnitTypes[],                     // Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,                 // Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true               // Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,             // Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false             // Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false              // Optional, include projectiles (default: false)
}
```

- `m_unitID` required to be set
- `m_radius` required to be set
- returns units whos outer edges have a distance equal/less than `m_radius` from `m_unitID`.
- `note:` `m_unitID` will be included in part of query result

## gx_get_units / gx_get_units_count
```sq
int[] gx_get_units(table params)
int gx_get_units_count(table params)
```

```sq
table params = {
    string m_locations[],                           // Optional
    string m_aabrs[],                               // Optional
    string m_tags[],                                // Optional, Filter for unit tags
    BoundsCheck m_boundsCheck                       // Default: BoundsCheck.Center
    int m_playerIDs[],                              // Optional, Filter for player_id
    int m_forceIDs[],                               // Optional, Filter for force_id
    string m_unitTypes[],                           // Optional, Filter for certain unit types
    string m_exceptUnitTypes[],                     // Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,                 // Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true               // Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,             // Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false             // Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false              // Optional, include projectiles (default: false)
}
```

- If `m_locations` is defined:
    - Searches at `m_locations` for units
- If `m_aabrs` is defined:
    - Searches at `m_aabrs` for units
- If `m_locations` and `m_aabrs` is not defined:
    - Searches for units on entire map
- Refer to {{enum("BoundsCheck ")}} if needed.

## gx_create_explosion
```sq
void gx_create_explosion(table params)
```

```sq
table params = {
    float m_size,                   // Optional, Diameter of explosion
    Vec3 m_color = Vec3(1, 1, 0),   // Optional, ColorSRGB of explosion.
    string m_location,              // Optional, Location for explosion
    bool m_bPlaySound = true,       // Optional, defualt true
    string m_sound,                 // Optional, Sound to play
    string m_soundPack,             // Optional, Play random sound from soundpack
}
```

- Refer to {{type("Vec3")}} if needed.
- Only one `m_sound` or `m_soundPack` should be set
- If neither `m_sound` nor `m_soundPack` is set, default sound will be played.

Example:
```sq
gx_create_explosion( {
    m_color = Vec3(1, 0, .5),
    m_location = "my_location"
} )
```

- it is undefined behavior to set both `m_location` and `m_pos`
- if `m_size` is not set and `m_location` is set, the resolved size will be the minimum width/height of `m_location`
- if `m_size` is not set and `m_pos` is set, the resolved size will be `1`
- Explosions are purely visual. They do not do any damage.
- Default value for `m_color` is `Vec3(1,1,0)` aka `0xFFFF00` (yellow)
- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed.

## gx_kill_unit
```sq
void gx_kill_unit(int unit_id)
```

- kills the unit `unit_id`.
- It is safe to call this function on already killed units

## gx_kill_all_units
```sq
void gx_kill_all_units(table params = {})
```

```sq
table params = { 
    int m_playerIDs[],      // Optional
    int m_forceIDs[],       // Optional
}
```

- kills all units for any players that match the params
- It is valid to have both `m_forceIDs` and `m_playerIDs` set -- the players from `m_forceIDs` and `m_playerIDs` will be merged.
- if neither m_playerIDs or m_forceIDs is set, all units will be killed

## gx_get_kills
```sq
void gx_get_kills(int player_id, table params = {})
```

```sq
table params = {
    int m_playerID,
    bool m_bAlliedKills,
    bool m_bSelfKills,
    bool m_bNonAlliedKills,
}
```

- if `m_playerID` is set, none of `m_bAlliedKills`, `m_bSelfKills`, `m_bNonAlliedKills` should be set
- if empty {} is passed in for params, all kills will be returned, equivalent to:
`{ m_bAlliedKills = true, m_bSelfKills = rue, m_bNonAlliedKills = true }`
- Allied kills does not include self kills


## gx_is_unit_killed
```sq
void gx_is_unit_killed(int unit_id)
```

- returns if the unit `unit_id` is killed
- returns `true` if unit does not exist
- equivalent to calling `!gx_is_unit_alive(unit_id)`

## gx_remove_unit
```sq
void gx_remove_unit(int unit_id)
```

- marks the unit to be removed by game
- `unit_id` will be removed from game before the next {{entry("gx_sim_update")}} call
- It is safe to call this function on already killed or removed units

## gx_is_unit_removed
```sq
void gx_is_unit_removed(int unit_id)
```

- returns if unit is marked to be removed
- will still return `true` if unit_id does not exist

## gx_unit_exists
```sq
bool gx_unit_exists(int unit_id)
```

- checks if unit still exists in the game

## gx_is_unit_alive_and_constructed
```sq
bool gx_is_unit_alive_and_constructed(int unit_id)
```

- returns `true` if unit is alive and constructed
- returns `false` if unit_id is invalid or unit no longer exists in game

## gx_is_unit_alive
```sq
bool gx_is_unit_alive(int unit_id)
```

- returns `true` if unit is alive
- returns `false` if unit_id is invalid or unit no longer exists in game
- Note: This function still returns `true` if unit is not yet fully constructed
- equivalent to calling `!gx_is_unit_killed(unit_id)`

## gx_get_unit_position
```sq
Vec3<float> gx_get_unit_position(int unit_id)
```

- returns position of unit
- returns Vec3(0.0, 0.0, 0.0) if unit no longer exists

## gx_set_unit_position
```sq
void gx_set_unit_position(int unit_id, table params)
```

```sq
table params = {
    string m_location,     // Optional, location to put unit
}
```

Example:
```sq
gx_set_unit_position(some_unit, { m_location = "location_to_teleport_to" } )
```

- it is undefined to not set `m_location` 
- if `m_location` does not exist, unit will be teleported to Vec2(0.0, 0.0)


## gx_is_ground_unit
```sq
bool gx_is_ground_unit(int unit_id)
```

- returns if unit is currently a `ground` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_air_unit(unit_id)`

## gx_is_air_unit
```sq
bool gx_is_air_unit(int unit_id)
```

- returns if unit is currently an `air` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_ground_unit(unit_id)`

## gx_get_players
```sq
int[] gx_get_players(table params = {})
```

```sq
table params = {
    int m_forceIDs[],   # Optional if set, only consider players part of these forces
    int m_playerIDs[],  # Optional, if set, only consider these players
    VictoryStatus m_allowedVictoryStates[]      # filter
	bool m_bIncludeNormalPlayers = true;        # filter, default true
	bool m_bIncludeNeutralPlayer = false;       # filter, default false
	bool m_bIncludeRescuePlayer = false;        # filter, default false
	bool m_bIncludeHostilePlayer = false;       # filter, default false
	bool m_bPlayerMustBeInGame = true;          # filter, default true
}
```
- Function is used to query and/or filter playerIDs based on simple coonditions
- If neither m_forceIDs[] nor m_playerIDs[] is set, then will consider all players
- If `m_allowedVictoryStates` is not set, any victory state will be considered
- It is valid to have both `m_forceIDs` and `m_playerIDs` set -- the players from `m_forceIDs` and `m_playerIDs` will be merged.

## gx_get_player
```sq
int gx_get_player(int unit_id)
```
- returns the `player_id` for unit `unit_id`
- if unit does not exist, will return 0

## gx_print
```sq
void gx_print(string message, table params = {})
```

```sq
table params = {
    int m_forceIDs[],           // Optional, send message to only force_id
    int m_playerIDs[],          // Optional, send message to only player_id
    bool m_bPlaySound = true,   // Optional, default true
    string m_sound,             // Optional, sound to play,
    string m_soundPack          // Optional, play random sound from soundPack
}
```

- If both `m_forceIDs` and `m_playerIDs` are undefined, message will be sent to all players

Example
```sq
// display chat message 'Hello World!' to player 3
gx_print("Hello World!", { m_playerID = 3 } )

// display chat message 'Hello World!' to everyone in force 2
gx_print("Hello World!", { m_forceID = 2 } )

// display chat message 'Hello World!' to everyone
gx_print("Hello World!")

// equivalent to above, display chat message 'Hello World!' to everyone
gx_print("Hello World!", {})
```

- outputs text to game chat (or map editor console)
- useful for debugging as well
- `print(message)` is equivalent to `gx_print(message, {})`
- `params` are ignored when running in map editor's console

## gx_modify_scoreboard
```sq
void gx_modify_scoreboard(table params = {})
```

```sq
local params = {
    bool m_bDisplay,
    bool m_bShowForceScores,
    bool m_bShowPlayerScores
}
```

- Set `m_bDisplay` to show scoreboard, must be `true` if you want to display
- Set `m_bShowForceScores` to show scores for forces
- Set `m_bShowPlayerScores` to show scores for players
- You can set/add/get scores by using {{fn("property-getterssetters")}}

Example:
```sq
gx_modify_scoreboard({
    m_bDisplay = true,
    m_bShowPlayerScores = true,
    m_bShowForceScores = false
})

// Set score for 'Player 3' to 7
gx_set_player_prop(PlayerProp.Score, 3, 7)
```

## gx_set_victory_status
```sq
void gx_set_victory_status(table params)
```

```sq
table params = {
    int m_status = VictoryStatus.Victory,   // Optional
                                            // Valid options: VictoryStatus.Victory or VictoryStatus.Defeat
                                            // Default: VictoryStatus.Victory
    int m_playerIDs[],              // Optional
    int m_forceIDs[],               // Optional
    bool m_bAllPlayers = false,     // Optional, (default: false)
    bool m_bAllForces = false,      // Optional, (default: false)
    bool m_bKillAllUnits,           // Optional
                                    // if (m_status == VictoryStatus.Victory)
                                    //      default: false
                                    // if (m_status == VictoryStatus.Defeat)
                                    //      default: true
    string m_img,                   // Optional, (image to show)
    float m_imgSpeedFactor = 1,     // Optional, speed if m_img is animated gif
    string m_sound,                 // Optional, (sound to play)
    float m_volume = 1,             // Optional, (default: 1)
    float m_pitch = 1,              // Optional, (default: 1)
    ComplexColor m_color,           // Optional, ComplexColor for m_img
    ComplexColor m_bgColor,         // Optional, Background ComplexColor
}
```

- once a player or force is set to `victory` or `defeat`, future calls for that player/force will be ignored

## gx_is_players_mutually_allied
```sq
bool gx_is_players_mutually_allied(table params)
```

```sq
table params = {
    int m_forceIDs[],
    int m_playerIDs[],
    m_bCheckAlliedVictory = true
}
```

- Returns `true` if all the players represented by `m_forceIDs` and `m_playerIDs` are mutually allied with each other.
- It is valid to have both `m_forceIDs` and `m_playerIDs` set -- the players from `m_forceIDs` and `m_playerIDs` will be merged.
- If the number of resolved players from `m_forceIDs` and `m_playerIDs` is 1 or less, this function will always return `true`.

## gx_is_player_allied_to
```sq
bool gx_is_player_allied_to(int playerID, int otherPlayerID)
```

## gx_set_player_allied_to
```sq
bool gx_set_player_allied_to(int playerID, int otherPlayerID, bool bAlly)
```

## gx_map_init_copy_ud

Creates a copy of a `unit_data`.
A `unit_data` serves as a 'definition' for a type of unit.
Required for creating new custom unit types.

```sq
void gx_map_init_copy_ud(string unit_type, string new_unit_type)
```

The example below creates a new type of unit called "User_BabyBrute"
It copies the existing definition of "Brute" to "User_BabyBrute".

Example:

```sq
gx_map_init_copy_ud("Brute", "User_BabyBrute")
```

- NOTE!! It's preferred to use the Drift Wars Map Editor to add/edit units!!
- These functions are only for convenience
- new unit type name MUST begin with `User_`. This is to prevent naming collisions for future added official units.
- this function will be a no-op if `new_unit_type` name does not begin with `User_`
- This function will return empty string if `new_unit_type` already exists or if it does not start with `User_`.
- `ud` is short for `unit_definition` 
- Can only be called during {{entry("gx_map_init")}}
- any attempt to call this outside of the {{entry("gx_map_init")}} will be ignored.

## gx_map_init_modify_ud_props
```sq
void gx_map_init_modify_ud_props(string unit_type, table params = {})
```

```sq
table params = {
    string m_friendlyName,     // Optional, set unit's friendly name
    int m_maxHealth,           // Optional, set max health
    float m_maxSpeed,          // Optional, set max speed
    int m_baseArmor,           // Optional, sets base armor
    int m_size,                 // Optional, set unit size,
    int m_gemstoneCost,
    int m_fungusCost,
    int m_supplyCost,
    int m_buildTime
}
```

The example below creates a new type of unit called "User_BabyBrute".
It copies the existing `unit_definition` of "Brute" to "User_BabyBrute". 
It then sets properties such as friendly name, maxHealth, baseArmor, and size.

Example:

```sq
gx_map_init_copy_ud("Brute", "User_BabyBrute")
gx_map_init_modify_ud_props("User_BabyBrute", {
    m_friendlyName = "Baby Brute",
    m_maxHealth = 30,
    m_baseArmor = 0,
    m_size = 1
})
```

- Sets properties for a specific `unit_type`
- `ud` is short for `unit_definition` 
- Can only be called during {{entry("gx_map_init")}}
- any attempt to call this outside of the {{entry("gx_map_init")}} will be ignored.

## gx_map_init_add_build_structure_item
```sq
void gx_map_init_add_build_structure_item(string unitType, table params = {})
```

```
table params = {
    string m_structure,    // name of structure to build, i.e. "Microwave"
    Vec2 m_position,           // position in command card to place at, leaving empty will use default
    bool bBuildAdvanced = false     // default is false, if set to True, will be placed in 'build advanced' tab
}
```

- Can only be called during {{entry("gx_map_init")}}

## gx_map_init_remove_all_build_structure_items
```sq
void gx_map_init_remove_all_build_structure_items(string unitType)
```

- Remove all build structure items from worker
- Can only be called during {{entry("gx_map_init")}}

## gx_map_init_add_build_item
```sq
void gx_map_init_add_build_item(string unitType, table params)
```

```sq
table params = {
    string m_unitType,     // unit type to add
    string m_research,      // research to add
    Vec2 m_position        // position in command card
}
```

- Only one `m_unitType` or `m_research` should be set
- Can only be called during {{entry("gx_map_init")}}
- Remove all build items from structure

## gx_map_init_remove_all_build_items
```sq
void gx_map_init_remove_all_build_items(string unitType)
```

- Remove all build items from structure
- Can only be called during {{entry("gx_map_init")}}

## gx_fling_unit

throws the unit

```sq
void gx_fling_unit(int unit_id, table params = {})
```

```sq
table params = {
    Vec2 m_dir2d,          // Optional, 2d direction to throw unit. Does not need to be normalized.
    Vec3 m_dir3d,          // Optional, 3d direction to throw unit. Does not need to be normalized.
    float m_force = 1           // Optional, velocity to throw unit
    m_bFlingLookAtDir = false   // Optional, will fling unit in direction it is facing
    m_bFlingStructures = false  // Optional, if true, structures will be thrown
}
```

- If neither `m_dir2d` nor `m_dir3d` is set, unit will be thrown in random direction
- Only `m_dir2d` or `m_dir3d` should be set. Setting both is undefined behavior.
- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed. 

## gx_set_area_vision
```sq
void gx_set_area_vision(int player_id, table params)
```

```sq
table params = {
    string m_location,         // location to give or take away vision of (depending on m_bSet)
    string m_triangleGroup,    // triangle group to give or take away vision of (depending on m_bSet)
    bool m_bFullMapVision,      // If set to true, will give or take away vision of entire map (depending on m_bSet)
    bool m_bSet = true              // If true gives vision, else takes away vision. (default: true)
}
```

- This function gives or removes permanent vision of a `m_location`, `m_triangleGroup`, or `entire map`.
- Only one of `m_location`, `m_triangleGroup`, or `m_bFullMapVision` should be set.
- The only valid value of `m_bFullMapVision` is `true`. Setting to `false` is `undefined`.
- If you want to give `Full Map Vision` to a player, set `m_bFullMapVision` to `true` and `m_bSet` to `true`.
- If you want to remove `Full Map Vision` from a player, set `m_bFullMapVision` to `true` and `m_bSet` to `false`.
- The value of `m_bSet` determines if vision is given or taken away from player.

## gx_get_area_vision
```sq
bool gx_get_area_vision(int player_id, table params)
```

```sq
table params = {
    string m_location,         // location to query vision for
    string m_triangleGroup,    // triangle group to query vision for
    bool m_bFullMapVision      // If set to true, queries if player has full map vision
}
```

- This function queries if the player has permanent vision of a `location`, `triangleGroup`, or `entire map`.
- Only one of `m_location`, `m_triangleGroup`, or `m_bFullMapVision` should be set.
- The only valid value of `m_bFullMapVision` is `true`. Setting to `false` is `undefined`.

## gx_set_terrain_type
```sq
void gx_set_terrain_type(params = {})
```

```sq
table params = {
    TerrainType m_type         // Required. The type of terrain to change to. See TerrainType enum. 
    int m_secondary = 0         // Secondary terrain type. (default = 0)
    Vec2 m_index,          // 2d index of square to change terrain type of
    int m_index2,         // 0 or 1, 0 indicates bottom triangle, 1 indicates top.
                                // If index2 is not defined, entire square specified by m_index
                                // will be set to terrain type (i.e. both triangles, top and bottom).
                                // m_index and index2 are ignored if m_location is set.
    string m_location,          // location to set terrain tile types.,
    string m_triangleGroup       // triangle group to set terrian tile stype
}
```

Example that sets terrain at location `my_location` to Pacifist type:
```sq
gx_set_terrain_type({
    m_type = TerrainType.Normal,
    m_secondary = SecondaryTerrainTypeNormal.Pacifist,
    m_location = "my_location"
})
```

- Refer to {{enum("TerrainType")}} for valid `m_type` values
- If `m_type` is set to `TerrainType.Normal`, `m_secondary` must be one of {{enum("SecondaryTerrainTypeNormal")}} values
- Refer to {{type("Vec2")}} if needed.
- if only `m_index` is set, the square at `m_index` is set to terrain type (i.e. both bottom and top triangle)
- if `m_location` is set, the triangles within the `m_location` are set to the new terrain type
- if `m_triangleGroup` is set, the triangles within `m_triangleGroup` are set to the new terrain type
- if `m_location` is set, it is `undefined behavior` to also set  `m_index`, `m_index2`, or `m_triangleGroup`
- if `m_triangleGroup` is set, is it `undefined behavior` to also set `m_index`, `m_index2`, or `m_location`
- if `m_index` is set, it is `undefined behavior` to also set `m_location`, and `m_triangleGroup`

## gx_set_terrain_type_2
```sq
void gx_set_terrain_type_2(params = {})
```

```sq
table params = {
    TerrainType m_type              // Required. The type of terrain to change to. See TerrainType enum. 
    int m_secondary = 0             // Secondary terrain type. (default = 0)
    string m_locations[],           // location to set terrain tile types.,
    AABR m_aabrs[],                 // aabrs to set terrain tile type
    string m_excludeLocations[],    // location to NOT set terrain tile types.,
    AABR m_excludeAABRs[]           // aabrs to NOT set terrian tile stype
}
```

## gx_set_terrain_type_3
```sq
void gx_set_terrain_type_3(params = {})
```

```sq
table params = {
    float m_radius,
    Float2 m_center,
    TerrainType m_type,
    int m_secondary,
    int m_triGroups[]
}
```

- Set the triangle types overlapping region defined by `m_radius` and `m_center` to `m_type`/`m_secondary` if they belong to any of the tri groups specified in `m_triGroups`
- This function should be used if you are using barrels for 'destroying' terrain and making them space, or other terrain..

```sq
table params = {
    TerrainType m_type              // Required. The type of terrain to change to. See TerrainType enum. 
    int m_secondary = 0             // Secondary terrain type. (default = 0)
    string m_locations[],           // location to set terrain tile types.,
    AABR m_aabrs[],                 // aabrs to set terrain tile type
    string m_excludeLocations[],    // location to NOT set terrain tile types.,
    AABR m_excludeAABRs[]           // aabrs to NOT set terrian tile stype
}
```

## gx_get_terrain_type
```
Vec2<int> gx_get_terrain_type(Vec2 index, int index2 = 0)
```

- returns primary terrain type in `vec.m_x` and returns secondary terrain type in `vec.m_y`

## gx_set_player_camera_look_at
```
void gx_set_player_camera_look_at(int player_id, table params)
```

```sq
local params = {
    int m_unitID,
    string m_location
}
```

- Moves camera of `player_id` to look at `m_unit` or `m_location`
- One of `m_unit` or `m_location` should be set. Not both.

## gx_lock_player_camera
```sq
void gx_lock_player_camera(int player_id, table params = {})
```

```sq
local params = {
    int m_unitID,
    string m_location
}
```

- locks `player_id` camera to look at `m_unitID` or `m_location`.
- camera will follow `m_unitID` or `m_location` until `m_unitID` is removed from game
- can unlock camera by calling `gx_unlock_player_camera(player_id)`
- passing empty args for `params` will unlock the camera for `player_id`.

## gx_unlock_player_camera
```sq
void gx_unlock_player_camera(int player_id)
```

- unlocks `player_id` camera position set by {{fn("gx_lock_player_camera")}}
- equivalent to calling `gx_lock_player_camera(player_id, {})`

## gx_queue_command
```sq
gx_queue_command(int unit_ids[], CommandType command, table params = {}, bool bQueueCommand = false)
```

```sq
table params = {
    int m_unitID,            // unit to target
    string m_location,     // location to target
    Vec2 m_pos,          // position to target
}
```

- only one (or zero) unit_id, m_location, m_pos should be set
- some commands/spells only work when certain params are set
- (i.e., a spell that can only target units cannot target a `m_pos` or `m_location`)
- `CommandType` can also be a spell identifier
- if `bQueueCommand` is `true`, appends the command in the unit's command queue, otherwise command queue beforehand
- See {{enum("CommandType")}} for possible command values

## gx_set_speech_bubble
```sq
int gx_set_speech_bubble(int unit_id, table params = {})
```

```sq
table params = {
    string m_text,          // Speech Bubble text to display
    int m_duration = 60     // duration to display in ticks 
                            // set to -1 to make it last forever
                            // default: 60 ticks (3 seconds)
}
```

- set a speech bubble for unit_id
- returns an integer id for the speech bubble

## gx_remove_speech_bubble
```sq
int gx_remove_speech_bubble(int unit_id, int speechBubbleID)
```

- setting `speechBubbleID` to `0` will remove current speech bubble
- Remove speech bubble for unit if current speech bubble ID matches `speechBubbleID`

## gx_remove_current_speech_bubble
```sq
gx_remove_current_speech_bubble(int unit_id)
```

- Equivalent to calling `gx_remove_speech_bubble(unit_id, 0)`
- Remove speech bubble for unit

## gx_(get|set|add)_unit_ammo
```sq
int gx_get_unit_ammo(int unit_id, string ammoName)
void gx_set_unit_ammo(int unit_id, string ammoName, int count)
void gx_add_unit_ammo(int unit_id, string ammoName, int count)
```

- Can query and set how much `unit ammo` of type `ammoName` the unit is holding

## gx_(get|set|add)_player_ammo_in_unit
```sq
int gx_get_player_ammo_in_unit(int unit_id, string ammoName)
void gx_set_player_ammo_in_unit(int unit_id, string ammoName, int count)
void gx_add_player_ammo_in_unit(int unit_id, string ammoName, int count)
```

- Can query and set how much `player ammo` of type `ammoName` the unit is holding

## gx_get_player_ammo_total
```sq
int gx_get_player_ammo_total(int player_id, string ammoName)
```

- Returns how much `player ammo` of type `ammoName` the player has

```sq
local params = {
    string m_tag,             // Required                                 (string)
    int m_player_id = 0        // Optional, used to Filter. Default = 0.   (int)
}
```

- returns unit_id with the given `m_name` or
- unit name can be set in map editor.
- if multiple units have the same name, the first will be returned.

## Property Getters/Setters
- Allows you to get/set certain properties for `simulation`, `forces`, `players`, and `units`, and other things

```sq
// getters
mixed gx_get_map_prop(MapProp prop)
mixed gx_get_force_prop(ForceProp prop, int force_id)
mixed gx_get_player_prop(PlayerProp prop, int player_id)
mixed gx_get_unit_prop(UnitProp prop, int unit_id)
mixed gx_get_location_prop(LocationProp prop, string location)
mixed gx_get_decal_prop(DecalProp prop, int decal_id)

// setters
void gx_set_map_prop(MapProp prop, mixed val)
void gx_set_force_prop(ForceProp prop, int force_id, mixed val)
void gx_set_player_prop(PlayerProp prop, int player_id, mixed val)
void gx_set_unit_prop(UnitProp prop, int unit_id, mixed val)
void gx_set_decal_prop(DecalProp prop, int decal_id, mixed val)

// adders
void gx_add_force_prop(ForceProp prop, int force_id, mixed val)
void gx_add_player_prop(PlayerProp prop, int player_id, mixed val)
void gx_add_unit_prop(UnitProp prop, int unit_id, mixed val)
```

- Please refer to {{enum("MapProp")}}, {{enum("ForceProp")}}, {{enum("PlayerProp")}}, {{enum("UnitProp")}}, {{enum("DecalProp")}}, and {{enum("LocationProp")}} for possibles values you can get/set (and their types).
- Properties that are `int` or `float` and are `Read-Write` can use the `gx_add_*` functions

## UserData Getters/Setters
- Allows you to get/set userdata integers for `simulation`, `forces`, `players`, and `units`, and other things for your own purposes

```sq
// getters
int gx_get_sim_variable(string varName)
int gx_get_force_variable(int force_id, string varName)
int gx_get_player_variable(int player_id, string varName)
int gx_get_unit_variable(int unit_id, string varName)

// setters
void gx_set_sim_variable(string varName, int varValue)
void gx_set_force_variable(int force_id, string varName, int varValue)
void gx_set_player_variable(int player_id, string varName, int varValue)
void gx_set_unit_variable(int unit_id, string varName, int varValue)

// adders
void gx_add_sim_variable(string varName, int varValue)
void gx_add_force_variable(int force_id, string varName, int varValue)
void gx_add_player_variable(int player_id, string varName, int varValue)
void gx_add_unit_variable(int unit_id, string varName, int varValue)
```

- Calling `gx_get_*` to retrieve a non-existing `varValue` will return `0`.
- Only `int` values can be set.

## gx_modulo
```sq
mixed gx_modulo(mixed a, mixed b)
```

- function for wrapping `a` around `b`
- If both `a` and `b` are integer, the result will be integer
- If at least one `a` or `b` is a float, result will be float
- The return value will have same sign as `b`
- differs from the `%` operator for negative numbers

```sq
local result = 0
result = 2 % 5              // 2
result = gx_modulo(2, 5)    // 2
result = 5 % 5              // 0
result = gx_modulo(5, 5)    // 0
result = 6 % 5              // 1
result = gx_modulo(6, 5)    // 1
result = -1 % 5             // -1
result = gx_modulo(-1, 5)   // 4 !! <-- DIFFERENT THAN % operator
```

## gx_triangle_lerp
```sq
float gx_triangle_lerp(float begin, float end, float period, float x)
```

## gx_str_starts_with
```sq
bool gx_str_starts_with(string str, string val)
```

- returns `true` if `str` starts with `val`
- equivalent to squirrel's string library `startswith` function

## gx_str_ends_with
```sq
bool gx_str_ends_with(string str, string val)
```

- returns `true` if `str` ends with `val`
- equivalent to squirrel's string library `endswith` function

## gx_str_split
```sq
string[] gx_str_split(string str, string separators, bool bSkipEmpty = false)
```

- splits `str` by any of the characters found in `separators`.
- equivalent to squirrel's string library `split` function

## gx_str_replace(str, find, replace)
```
string gx_str_replace(string str, string find, string replace)
```

## gx_str_contains
```sq
bool gx_str_contains(string str, string search)
```

- returns `true` if `str` contains `search`

## gx_str_insert
```sq
string gx_str_insert(string str, string toInsert, int index)
```

- return a new string with `toInsert` inserted at position `index`

## gx_str_encode_color_id
```sq
string gx_str_encode_color_id(int colorID)
```

## gx_str_encode_color
```sq
string gx_str_encode_color(Vec3 color)
```

## gx_str_encode_color_hex3
```sq
string gx_str_encode_color_hex3(int hex3)
```

## gx_str_encode_complex_color
```sq
string gx_str_encode_complex_color(ComplexColor color)
```

## gx_str_color_username
```sq
string gx_str_color_username(ComplexColor color, string username)
```

Equivalent To / Implementation:
```sq
function gx_str_color_username(ComplexColor color, string username)
{
    return gx_str_encode_complex_color(color) + username
}
```

## gx_str_color_username_2
```sq
string gx_str_color_username_2(ComplexColor complexColor, string username)
```

Equivalent To / Implementation:
```sq
function gx_str_color_username_2(ComplexColor complexColor, string username)
{
    return Unicode.Special_PushColor
    + gx_str_color_username(complexColor, username)
    + Unicode.Special_PopColor
}
```

## gx_str_parse_command
```sq
string[] gx_str_parse_command(string cmd)
```

- splits a string based whitespace and handles quotes properly
- useful when handling the `EventType.TextCommand` event

## gx_convert_to_str
```sq
string gx_convert_to_str(mixed val)
```

- Safe function to convert a value to string
- returns `""` on failure

## gx_convert_to_int
```sq
int gx_convert_to_int(mixed val)
```

- Safe function to convert a value to integer
- returns `0` on failure

## gx_convert_to_float
```sq
float gx_convert_to_float(mixed val)
```

- Safe function to convert a value to float
- returns `0.0` on failure

## gx_sound2d_create
```sq
int gx_sound2d_create(table params = {})
```

```sq
params = {
    string m_sound,         // name of sound to play
    string m_soundPack,     // will play random sound from soundpack
    int m_forceIDs[],       // forceIDs that can hear the sound
    int m_playerIDs[],      // playerIDs that can hear the sound
    float m_volume = 1,     // Optional, volume multiplier (default = 1)
    float m_pitch = 1,      // Optional, pitch of sound (default = 1)
    bool m_bLoop = false    // Optional, controls if sound should loop
}
```
- You are required to set either `m_sound` or `m_soundPack` (but not both).
- If neither `m_forceIDs` nor `m_playerIDs` are set, sound will be heard by all players
- returns the `soundID`

## gx_sound2d_destroy
```sq
void gx_sound2d_destroy(int soundID)
```

- Will force a sound to stop and then be destroyed
- This is the only way to stop a sound that is looping (`m_bLoop = true`)
- After calling this, `gx_sound2d_is_playing` will return `false`
- It is not required to call this. Sound will automatically be destroyed when it is finished playing (assuming not looping).

## gx_sound2d_modify
```sq
void gx_sound2d_modify(int soundID, table params = {})
```

```sq
params = {
    float m_volume,     // Optional, volume multiplier
    float m_pitch       // Optional, pitch of sound
}
```

## gx_sound2d_is_playing
```sq
bool gx_sound2d_is_playing(int soundID)
```

- returns `true` if sound is currently playing

## gx_sound3d_create
```sq
int gx_sound3d_create(table params = {})
```

```sq
params = {
    string m_sound,         // name of sound to play
    string m_soundPack,     // play random sound from soundpack
    int m_unitID,           // Optional, unit for sound to attach to
    bool m_bStopSoundOnUnitDeath,           // Optional, default true if m_unitID is set
    Vec2 m_pos2d,           // Optional, 2d position for sound
    Vec3 m_pos3d,           // Optional, 3d position for sound
    float m_radius = 0,     // Optional, sound radius, default = 0
    float m_volume = 1,     // Optional, volume multiplier (default = 1)
    float m_pitch = 1,      // Optional, pitch of sound (default = 1)
    bool m_bLoop = false                    // Optional, controls if sound should loop
    bool m_bRandomLoopStartTime = false     // Optional
}
```

- Only one of `m_unitID`, `m_pos2d`, `m_pos3d` should be set
- Only one of `m_sound` or `m_soundPack` should be set
- Sound will only be played if current player has vision of circle created by the position of the sound and `m_radius`
- returns the `soundID`

## gx_sound3d_destroy
```sq
void gx_sound3d_destroy(int soundID)
```

- Will force a sound to stop and then be destroyed
- This is the only way to stop a sound that is looping (`m_bLoop = true`)
- After calling this, `gx_sound3d_is_playing` will return `false`
- It is not required to call this. Sound will automatically be destroyed when it is finished playing (assuming not looping).

## gx_sound3d_modify
```sq
void gx_sound3d_modify(int soundID, table params = {})
```

```sq
params = {
    float m_volume,     // Optional, volume multiplier
    float m_pitch,      // Optional, pitch of sound
    Vec2 m_pos2d,       // Optional
    Vec3 m_pos3d        // Optional
}
```

- `m_pos2d` and `m_pos3d` will be ignored if sound is attached to a unit

## gx_sound3d_is_playing
```sq
bool gx_sound3d_is_playing(int soundID)
```

- returns `true` if sound is currently playing

## gx_decal_create
```sq
int gx_decal_create(table params)
```

```sq
table params = {
    string m_preset,           // decal preset
    int m_alphaFn,
    int m_colorFn,
    bool m_bAlwaysDisplay,     // ignore fog of war checks
    bool m_bDisplayOnMinimap,
    Vec4 m_color,              // srgb with alpha
    Vec2 m_pos,
    float m_rotation,          // radians
    float m_size,
    Vec2 m_size,               // size, can either be Vec2<float> or float
    string m_tag,
    string m_texture,          // icon to use
    float m_speedFactor = 1.0       // animation speed if m_texture is animated GIF
}
```

- create decal with properties, all fields are optional
- only one (or zero) of `m_size` or `m_size2d` should be set

## gx_decal_modify
```sq
void gx_decal_modify(int decalID, table params)
```

```sq
table params = {
    string m_preset,                # decal preset
    int m_alphaFn,
    int m_colorFn,
    bool m_bAlwaysDisplay,          # ignore fog of war checks
    bool m_bDisplayOnMinimap,
    Vec4 m_color,                   # srgb with alpha
    Vec2 m_pos,
    float m_rotation,               # radians
    float m_size,
    string m_tag,
    string m_texture,               # icon to use
    float m_speedFactor = 1.0       animation speed if m_texture is animated GIF
}
```

- modify/overwrite decal properties, all fields are optional
- only one (or zero) of `m_size` or `m_size2d` should be set

## gx_decal_destroy
```sq
void gx_decal_destroy(int decalID)
```

- remove the decal from game

## gx_decal_get_all_by_tag
```sq
int[] gx_decal_get_all_by_tag(string tag)
```

- return all decalIDs that have their `m_tag` set to `tag`

## gx_decal_query
```sq
int[] gx_decal_query(table params)
```

```sq
table params = {
    AABR m_aabrs[],             # Optional
    string m_locations[],       # Optional
    bool m_bAll = false         # Optional, default false
}
```

- Searches inside all of the provided aabrs and locations for decals
- Query for decals inside `m_aabrs` and `m_locations`.
- Setting `m_bAll` to true will return all decals on the map

## gx_get_sim_image_colors
```sq
int[] gx_get_sim_image_colors(table params)
```

```sq
table params = {
    string m_img                   // Required, Icon Name
}
```

- Returns all the pixels in the image in hex3 format
- Alpha channel is ignored and not returned

## gx_draw_glow_image
```sq
void gx_draw_glow_image(table params)
```

```sq
table params = {
    string m_img,                   // Required, Icon Name
    AABR<int> m_aabr,               // AABR to draw to
    string m_location,              // Location to draw to
    AABR<int> m_excludeAABRs[],     // Optional, AABRs not to draw to
    string m_excludeLocations[],    // Optional, locations not to draw to
}
```

- `m_img` must be set
- Exactly one of `m_abbr` or `m_location` must be set

## gx_set_terrain_glow_color
```sq
void gx_set_terrain_glow_color(table params = {})
```
```sq
table params = {
    int m_index,        // Glow index to change, required
    int m_hex,          // srgb hex3 code for color to set
    Vec3<float> m_color // srgb color (each component [0.0-1.0]) for new color to set
}
```

- Only one `m_hex` or `m_color` should be set, not both.
- Internally, `m_hex` is converted to `m_color`.
- `m_hex` parameter is only given for convenience.

## gx_set_map_theme_color
```sq
void gx_set_map_theme_color(Vec4<float> srgb)
```

## gx_get_map_theme_color
```sq
Vec4<float> gx_get_map_theme_color()
```

## gx_set_map_glow_color
```sq
void gx_set_map_glow_color(Vec4<float> srgb)
```

## gx_get_map_glow_color
```sq
Vec4<float> gx_get_map_glow_color()
```

## gx_color_*

```sq
Vec3<float> gx_color_hsv_to_srgb(Vec3 hsv)
Vec3<float> gx_color_srgb_to_hsv(Vec3 srgb)
Vec3<float> gx_color_hex3_to_srgb(int hex3)
int gx_color_srgb_to_hex3(Vec3 srgb)

Vec4<float> gx_color_hsva_to_srgba(Vec4 hsva)
Vec4<float> gx_color_srgba_to_hsva(Vec4 srgba)
Vec4<float> gx_color_hex4_to_srgba(int hex4)
int gx_color_srgba_to_hex4(Vec4 srgba)

int gx_color_hex3_to_hex4(int hex3, int alpha = 0xFF)
int gx_color_hex4_to_hex3(int hex4)
```

- color conversion functions
- `hsva`: `hsva.m_x` is hue `[0-360]`, `hsva.m_y` is saturation `[0-100]`, `hsva.m_z` is value `[0-100]`, `hsva.m_w` is alpha `[0-1]`
- `srgba`: `srgba.m_x` is red `[0-1]`, `srgba.m_y` is green `[0-1]`, `srgba.m_z` is blue `[0-1]`, `srgba.m_w` is alpha `[0-1]`
- `hex4` is an integer with value `0xAARRGGBB` where AA is alpha, RR is red, GG is green, BB is blue
- `hex3` is an integer with value `0x00RRGGBB` where RR is red, GG is green, BB is blue

## gx_rand_float
```sq
float gx_rand_float(float min, float max)
```

## gx_rand_int
```sq
int gx_rand_int(int min, int max)
```

## gx_rand_unit_vec*
```sq
Vec2<float> gx_rand_unit_vec2()
Vec3<float> gx_rand_unit_vec3()
Vec4<float> gx_rand_unit_vec4()
```

## gx_unit_vec_or_random
```sq
Vec2<float> gx_unit_vec_or_random(Vec2 v)
Vec3<float> gx_unit_vec_or_random(Vec3 v)
Vec4<float> gx_unit_vec_or_random(Vec4 v)
```
- Computes the unit vector of `v`.
- Will return random unit vector if `v` has magnitude of `0`.

## gx_unit_vec_or_zero
```sq
Vec2<float> gx_unit_vec_or_zero(Vec2 v)
Vec3<float> gx_unit_vec_or_zero(Vec3 v)
Vec4<float> gx_unit_vec_or_zero(Vec4 v)
```

- Computes the unit vector of `v`.
- Will return zero-magnitude vector if unit vector `v` has magnitude of `0`.

## gx_terrain_offset_z_add
```sq
void gx_terrain_offset_z_add(Vec2<int> vertexPos, float offset)
```

## gx_terrain_offset_z_add_2
```sq
void gx_terrain_offset_z_add_2(table params)
```
```sq
table params = {
    AABR<int> m_aabrs[],        # Optional
    string m_locations[],       # Optional
    Vec2<int> m_vertices[],     # Optional
    float m_val,                # Required
}
```

## gx_terrain_offset_z_set
```sq
void gx_terrain_offset_z_set(Vec2<int> vertexPos, float offset)
```

## gx_terrain_offset_z_set_2
```sq
void gx_terrain_offset_z_set_2(table params)
```
```sq
table params = {
    AABR<int> m_aabrs[],        # Optional
    string m_locations[],       # Optional
    Vec2<int> m_vertices[],     # Optional
    float m_val,                # Required
}
```

## gx_terrain_offset_z_get
```sq
float gx_terrain_offset_z_get(Vec2<int> vertexPos)
```

## gx_aabr_contains
```sq
bool gx_aabr_contains(AABR aabr, Vec2 pt)
```

## gx_aabr_contains_or_touching
```sq
bool gx_aabr_contains_or_touching(AABR aabr, Vec2 pt)
```

## gx_force_select_units
```sq
void gx_force_select_units(int playerID, int unitIDs[])
```

- clears player's unit selection, and sets unitIDs as new selection

## gx_create_effect
```sq
int gx_create_effect(table params)
```

```sq
table params = {
    EffectType m_type,
    Vec2<float> m_pos,
    int m_duration,
    Vec4<float> m_color,    # srgb
    int m_playerID,
    int m_unitID
}
```

- Creates the Effect of type `m_type` and returns the Effect ID
- See {{enum("EffectType")}} for effects

## gx_destroy_effect
```sq
void gx_destroy_effect(int effectID)
```
- Destroys effect if it can be removed

## gx_create_nuke_unit
```sq
int gx_create_nuke_unit(table params)
```

```sq
table params = {
    float m_damage,
    int m_playerID,
    Vec2<float> m_pos,
    float m_radius
}
```

- Creates a nuke unit

## gx_register_for_location_events
```sq
void gx_register_for_location_events(bool bEnable, table params = {})
```

- Register to receive `UnitEnteredLocation` and `UnitExitedLocation` events
- no optional parameters currently
- Usually you will want to only call this one time time in the `gx_sim_init` function
- See {{enum("EventType")}} and {{eventQueue()}} for more information

## gx_triangle_lerp
```sq
float gx_triangle_lerp(float begin, float end, float period, float x)
```

- Lerp function

## gx_is_event_queue_empty
```sq
bool gx_is_event_queue_empty()
```

- Check if event queue is empty.
- See {{eventQueue()}}

## gx_pop_event_from_queue
```sq
Event gx_pop_event_from_queue()
```

- Pop event from event queue.
- See {{eventQueue()}}


# gx_update_map_hints
```sq
void gx_update_map_hints(local params)
```

```sq
params = {
    int m_forceIDs[],
    int m_playerIDs[],
    string m_button,
    string m_description,
    string m_hover,
    bool m_bDisplay
}
```

# gx_add_event_message
```sq
void gx_add_event_message(string message)
```

- Adds an event message visibly by all players on left side of screen


# gx_display_ui_elements
```sq
void gx_display_ui_elements(local params = {})
```

```sq
params = {
    bool m_bAll,
    bool m_bArmyCount,
    bool m_bIdleWorkers,
    bool m_bNumJeeps,
    bool m_bNotEnoughSupply,
    bool m_bResources,
    bool m_bClock,
    int m_forceIDs[],
    int m_playerIDs[]
}
```

- controls which UI elements are display for players matching `m_forceIDs` and `m_playerIDs`
- if both `m_forceIDs` and `m_playerIDs` are unset, function will affect all players 


# gx_add_center_message
```sq
int gx_add_center_message(local params = {})
```

```sq
params = {
    string m_msg,
    int m_forceIDs[],
    int m_playerIDs[],
    int m_duration = 100, // 5 seconds
}
```

- displays a player event message for player in middle of their screen for matching players
- if `m_duration` is `-1` message will be displayed forever until `gx_clear_center_messages` or `gx_clear_center_message_by_id` is called.
- returns `msgID` that can be used by `gx_clear_center_message_by_id` if needed.

# gx_clear_center_messages
```sq
void gx_clear_center_messages(local params = {})
```

```sq
params = {
    int m_forceIDs[],
    int m_playerIDs[]
}
```

- clears all messages for players match params
- if both `m_forceIDs` and `m_playerIDs` are empty, messages will be cleared for all players

# gx_clear_center_message_by_id
```sq
`void gx_clear_center_message_by_id(int msgID)`
```

- clear message with msgID `msgID`


# gx_paint_terrain
```sq
void gx_paint_terrain(table params)
```

```sq
params = {
    string m_location,
    AABR<Fixed> m_aabr,
    string m_img,           # img to paint
    Vec4<Float> m_srgba     # srgb multiplier
}
```

- only one of `m_location` or `m_aabr` should be set.


# gx_clear_terrain_paint
```sq
void gx_clear_terrain_paint(table params)
```

```sq
params = {
    string m_locations[],
    AABR<Fixed> m_aabrs[]
}
```