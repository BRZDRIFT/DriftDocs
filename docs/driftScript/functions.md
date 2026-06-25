## gx_get_bg_shader_val
```sq
float gx_get_bg_shader_val(int index)
```

- index must be between `[0-15]`
- get float value that is being used by the background gpu shader
## gx_set_bg_shader_val
```sq
void gx_set_bg_shader_val(int index, float val)
```

- index must be between `[0-15]`
- set float value that can be used by the background gpu shader
## gx_sim_ticks_to_seconds
```sq
float gx_sim_ticks_to_seconds(int ticks)
```

- converts simTicks to seconds
- equivalent to: `(simTicks / 20.0)`
- note: simulation runs every 50ms (20 times/second)
## gx_seconds_to_sim_ticks
```sq
int gx_seconds_to_sim_ticks(float seconds)
```

- converts `seconds` to `simTicks`
- equivalent to: `(seconds * 20).tointeger()`
- note: simulation runs every 50ms (20 times/second)
## gx_get_seconds
```sq
float gx_get_seconds()
```

- return game time in seconds
- equivalent to: `gx_sim_ticks_to_seconds(gx_get_sim_tick())`
## gx_str_encode_color_id
```sq
string gx_str_encode_color_id(int colorID)
```


## gx_str_encode_color
```sq
string gx_str_encode_color(Float3 color)
```


## gx_str_encode_complex_color
```sq
string gx_str_encode_complex_color(ComplexColor color)
```


## gx_str_encode_color_hex3
```sq
string gx_str_encode_color_hex3(int hex)
```


## gx_get_sim_tick
```sq
int gx_get_sim_tick()
```

- Returns the current sim tick number in simulation.
- The `gx_sim_init()` call will have `tick = 0`
- The first `gx_sim_update()` call will have `tick = 1`
- The second `gx_sim_update()` call will have `tick = 2`, etc..
- every tick corresponds to 50ms real time
## gx_create_unit
```sq
int gx_create_unit(table params)
```

```sq
table params = {
    string m_unitType,  # required
    int m_playerID,     # required
    Float2 m_pos,
    string m_location,
    int m_level,
    bool m_bForceGhostMode,
    bool m_bSieged,
    bool m_bLiftedStructure
}
```

- Will create unit of type `m_unitType` at position `m_pos` or at location `m_location` for player `m_playerID`.
- It is undefined behavior to have both `m_pos` and `m_location` set.
- If neither `m_pos` nor `m_location` is set, unit will be created at `(0, 0)`
- Units may not be placed at the exact center of `m_location`, if you need exact position use `m_pos`.
- Setting `m_bForceGhostMode` is shortcut so u don't need to set `set_unit_prop(UnitProp.ForceGhostMode, ..)` after unit creation.
## gx_get_distance_between_units
```sq
float gx_get_distance_between_units(int unit0, int unit1)
```

- returns the distance between the edges of two units
- will return 0 if one or both of the units do not exist
## gx_get_nearby_units
```sq
int[] gx_get_nearby_units(table params = {})
```

```sq
table params = {
    int m_unitID,                           # unit_id to center search on
    float m_radius,                         # search radius around unit
    int m_playerIDs[],                      # Optional, Filter for player_id
    int m_forceIDs[],                       # Optional, Filter for force_id
    string m_unitTypes[],                   # Optional, Filter for certain unit types
    string m_exceptUnitTypes[],             # Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,         # Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true,      # Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,     # Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false,    # Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false      # Optional, include projectiles (default: false)
}
```

- `m_unitID` required to be set
- `m_radius` required to be set
- returns units whos outer edges have a distance equal/less than `m_radius` from `m_unitID`.
- `note:` `m_unitID` will be included in part of query result
## gx_get_nearby_units_count
```sq
int gx_get_nearby_units_count(table params = {})
```

```sq
table params = {
    int m_unitID,                           # unit_id to center search on
    float m_radius,                         # search radius around unit
    int m_playerIDs[],                      # Optional, Filter for player_id
    int m_forceIDs[],                       # Optional, Filter for force_id
    string m_unitTypes[],                   # Optional, Filter for certain unit types
    string m_exceptUnitTypes[],             # Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,         # Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true,      # Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,     # Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false,    # Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false      # Optional, include projectiles (default: false)
}
```

- `m_unitID` required to be set
- `m_radius` required to be set
- returns units whos outer edges have a distance equal/less than `m_radius` from `m_unitID`.
- `note:` `m_unitID` will be included in part of query result
## gx_get_units
```sq
int[] gx_get_units(table params = {})
```

```sq
table params = {
    string m_locations[],                   # Optional
    string m_aabrs[],                       # Optional
    string m_tags[],                        # Optional, Filter for unit tags
    BoundsCheck m_boundsCheck               # Default: BoundsCheck.Center
    int m_playerIDs[],                      # Optional, Filter for player_id
    int m_forceIDs[],                       # Optional, Filter for force_id
    string m_unitTypes[],                   # Optional, Filter for certain unit types
    string m_exceptUnitTypes[],             # Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,         # Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true,      # Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,     # Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false,    # Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false      # Optional, include projectiles (default: false)
}
```

- If `m_locations` is defined:
    - Searches at `m_locations` for units
- If `m_aabrs` is defined:
    - Searches at `m_aabrs` for units
- If `m_locations` and `m_aabrs` is not defined:
    - Searches for units on entire map
- Refer to {{enum("BoundsCheck ")}} if needed.
## gx_get_units_count
```sq
int gx_get_units_count(table params = {})
```

```sq
table params = {
    string m_locations[],                   # Optional
    string m_aabrs[],                       # Optional
    string m_tags[],                        # Optional, Filter for unit tags
    BoundsCheck m_boundsCheck               # Default: BoundsCheck.Center
    int m_playerIDs[],                      # Optional, Filter for player_id
    int m_forceIDs[],                       # Optional, Filter for force_id
    string m_unitTypes[],                   # Optional, Filter for certain unit types
    string m_exceptUnitTypes[],             # Optional, ignore certain unit types
    bool m_bIncludeAirUnits = true,         # Optional, Set to false if you want to exclude air units
    bool m_bIncludeGroundUnits = true,      # Optional, set to false if you want to exclude ground units
    bool m_bIncludeKilledUnits = false,     # Optional, Set to true if you want to include killed units
    bool m_bIncludeRemovedUnits = false,    # Optional, set to true if you want to include removed units
    bool m_bIncludeProjectiles = false      # Optional, include projectiles (default: false)
}
```

- If `m_locations` is defined:
    - Searches at `m_locations` for units
- If `m_aabrs` is defined:
    - Searches at `m_aabrs` for units
- If `m_locations` and `m_aabrs` is not defined:
    - Searches for units on entire map
- Refer to {{enum("BoundsCheck ")}} if needed.
## gx_units_touching
```sq
int[] gx_units_touching(int u0, int u1)
```

- Returns `true` if the two units are "touching" (nearby eachother)
## gx_create_explosion
```sq
void gx_create_explosion(table params)
```

```sq
table params = {
    float m_size,
    Float3 m_color = Float3(1, 1, 0),
    string m_location,
    bool m_bPlaySound,
    string m_sound,
    string m_soundPack,
}
```

- Only one `m_sound` or `m_soundPack` should be set
- If neither `m_sound` nor `m_soundPack` is set, default sound will be played.

Example:
```sq
gx_create_explosion( {
    m_color = Float3(1, 0, .5),
    m_location = "my_location"
} )
```

## gx_kill_unit
```sq
void gx_kill_unit(int unitID)
```

- kills the unit `unit_id`.
- It is safe to call this function on already killed units
## gx_unit_exists
```sq
bool gx_unit_exists(int unitID)
```

- checks if unit still exists in the game
## gx_remove_unit
```sq
bool gx_remove_unit(int unitID)
```

- marks the unit to be removed by game
- `unit_id` will be removed from game before the next `gx_sim_update` call
- It is safe to call this function on already killed or removed units
## gx_is_unit_alive_and_constructed
```sq
bool gx_is_unit_alive_and_constructed(int unitID)
```

- returns `true` if unit is alive and constructed
- returns `false` if unit_id is invalid or unit no longer exists in game
## gx_is_unit_alive
```sq
bool gx_is_unit_alive(int unitID)
```

- returns `true` if unit is alive
- returns `false` if unit_id is invalid or unit no longer exists in game
- Note: This function still returns `true` if unit is not yet fully constructed
- equivalent to calling `!gx_is_unit_killed(unit_id)`
## gx_is_unit_killed
```sq
bool gx_is_unit_killed(int unitID)
```

- returns if the unit `unit_id` is killed
- returns `true` if unit does not exist
- equivalent to calling `!gx_is_unit_alive(unit_id)`
## gx_get_unit_position
```sq
Float3 gx_get_unit_position(int unitID)
```

- returns position of unit
- returns Float3(0.0, 0.0, 0.0) if unit no longer exists
## gx_is_ground_unit
```sq
bool gx_is_ground_unit(int unitID)
```

- returns if unit is currently a `ground` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_air_unit(unit_id)`
## gx_is_air_unit
```sq
bool gx_is_air_unit(int unitID)
```

- returns if unit is currently an `air` unit
- units are always in either the `ground` or `air` state
- note: knock-back effect can cause `ground` units to temporarily become `air` units
- equivalent to calling `!gx_is_ground_unit(unit_id)`
## gx_get_player
```sq
int gx_get_player(int unitID)
```

- returns the `player_id` for unit `unit_id`
- if unit does not exist, will return 0
## gx_get_players
```sq
int[] gx_get_players(table params = {})
```

```sq
table params = {
    int m_forceIDs[],
    int m_playerIDs[],
    VictoryStatus m_allowedVictoryStates[],
    bool m_bIncludeNormalPlayers = true,
    bool m_bIncludeNeutralPlayer = false,
    bool m_bIncludeRescuePlayer = false,
    bool m_bIncludeHostilePlayer = false,
    bool m_bPlayerMustBeInGame = false
}
```

- Function is used to query and/or filter playerIDs based on simple coonditions
- If neither m_forceIDs[] nor m_playerIDs[] is set, then will consider all players
- If `m_allowedVictoryStates` is not set, any victory state will be considered
- It is valid to have both `m_forceIDs` and `m_playerIDs` set -- the players from `m_forceIDs` and `m_playerIDs` will be merged.
## gx_fling_unit
```sq
void gx_fling_unit(int unitID, table params = {})
```

```sq
table params = {
    Float3 m_dir2d,
    Float3 m_dir3d,
    float m_force,
    bool m_bFlingLookAtDir = false,
    bool m_bFlingStructures = false
}
```

- If neither `m_dir2d` nor `m_dir3d` is set, unit will be thrown in random direction
- Only `m_dir2d` or `m_dir3d` should be set. Setting both is undefined behavior.
- Refer to {{type("Vec2")}} and {{type("Vec3")}} if needed.
## gx_set_victory_status
```sq
void gx_set_victory_status(table params)
```

```sq
table params = {
    int m_status = VictoryStatus.Victory,   # Valid options:
                                            # VictoryStatus.Victory or VictoryStatus.Defeat
                                            # Default: VictoryStatus.Victory
    int m_playerIDs[],
    int m_forceIDs[],
    bool m_bAllPlayers = false,
    bool m_bAllForces = false,
    bool m_bKillAllUnits,           # Optional
                                    # if (m_status == VictoryStatus.Victory)
                                    #      default: false
                                    # if (m_status == VictoryStatus.Defeat)
                                    #      default: true
    string m_img,                   # Optional, (image to show)
    float m_imgSpeedFactor = 1,     # Optional, speed if m_img is animated gif
    string m_sound,                 # Optional, (sound to play)
    float m_volume = 1,             # Optional, (default: 1)
    float m_pitch = 1,              # Optional, (default: 1)
    ComplexColor m_color,           # Optional, ComplexColor for m_img
    ComplexColor m_bgColor,         # Optional, Background ComplexColor
}
```

## gx_print
```sq
void gx_print(string msg, table params = {})
```

```sq
table params = {
    int m_forceIDs[],
    int m_playerIDs[],
    bool m_bPlaySound,
    string m_sound,
    string m_soundPack
}
```

- If both m_forceIDs and m_playerIDs are undefined, message will be sent to all players
## gx_is_unit_removed
```sq
bool gx_is_unit_removed(int unitID)
```

- returns if unit is marked to be removed
- will still return `true` if unit_id does not exist
## gx_set_unit_position
```sq
void gx_set_unit_position(int unitID, table params)
```

```sq
table params = {
    string m_location,      # location to put unit
}
```

Example:
```sq
gx_set_unit_position(some_unit, { m_location = "location_to_teleport_to" } )
```

- it is undefined to not set `m_location`
- if `m_location` does not exist, unit will be teleported to Float2(0.0, 0.0)
## gx_set_terrain_type
```sq
void gx_set_terrain_type(table params = {})
```

```sq
table params = {
    TerrainType m_type          # Required. The type of terrain to change to. See TerrainType enum.
    int m_secondary = 0         # Secondary terrain type. (default = 0)
    Int2 m_index,               # 2d index of square to change terrain type of
    int m_index2,               # 0 or 1, 0 indicates bottom triangle, 1 indicates top.
                                # If index2 is not defined, entire square specified by m_index
                                # will be set to terrain type (i.e. both triangles, top and bottom).
                                # m_index and index2 are ignored if m_location is set.
    string m_location,          # location to set terrain tile types.,
    string m_triangleGroup      # triangle group to set terrian tile stype
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

## gx_set_terrain_type_2
```sq
void gx_set_terrain_type_2(table params = {})
```

```sq
table params = {
    TerrainType m_type              # Required. The type of terrain to change to. See TerrainType enum.
    int m_secondary = 0             # Secondary terrain type. (default = 0)
    string m_locations[],           # location to set terrain tile types.,
    AABR m_aabrs[],                 # aabrs to set terrain tile type
    string m_excludeLocations[],    # location to NOT set terrain tile types.,
    AABR m_excludeAABRs[]           # aabrs to NOT set terrian tile stype
}
```

## gx_set_terrain_type_3
```sq
void gx_set_terrain_type_3(table params = {})
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
    TerrainType m_type              # Required. The type of terrain to change to. See TerrainType enum.
    int m_secondary = 0             # Secondary terrain type. (default = 0)
    string m_locations[],           # location to set terrain tile types.,
    AABR m_aabrs[],                 # aabrs to set terrain tile type
    string m_excludeLocations[],    # location to NOT set terrain tile types.,
    AABR m_excludeAABRs[]           # aabrs to NOT set terrian tile stype
}
```

## gx_get_terrain_type
```sq
Int2 gx_get_terrain_type(int index, int index2 = 0)
```

- returns primary terrain type in `vec.m_x` and returns secondary terrain type in `vec.m_y`
## gx_get_area_vision
```sq
bool gx_get_area_vision(int playerID, table params)
```


## gx_set_area_vision
```sq
void gx_set_area_vision(int playerID, table params)
```


## gx_set_player_camera_look_at
```sq
void gx_set_player_camera_look_at(int playerID, table params)
```

```sq
table params = {
    int m_unitID,
    string m_location
}
```


- Moves camera of `player_id` to look at `m_unit` or `m_location`
- One of `m_unit` or `m_location` should be set. Not both.
## gx_lock_player_camera
```sq
void gx_lock_player_camera(int playerID, table params = {})
```

```sq
table params = {
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
void gx_unlock_player_camera(int playerID)
```

- unlocks `player_id` camera position set by {{fn("gx_lock_player_camera")}}
- equivalent to calling `gx_lock_player_camera(player_id, {})`
## gx_get_kills
```sq
int gx_get_kills(int playerID, table params = {})
```


## gx_map_init_modify_ud_props
```sq
void gx_map_init_modify_ud_props(string unitName, table params)
```

```sq
table params = {
    string m_friendlyName,
    bool m_bHasHealth,
    int m_maxHealth,
    float m_maxSpeed,
    int m_baseArmor,
    ArmorType m_armorType,
    int m_size,
    int m_gemstoneCost,
    int m_fungusCost,
    int m_supplyCost,
    int m_buildTime
    Expr<bool> m_req,
    Expr<int> m_attackLevel,
    Expr<int> m_armorLevel
}
```

## gx_map_init_copy_ud
```sq
void gx_map_init_copy_ud(string name, string newName)
```


## gx_map_init_remove_all_build_structure_items
```sq
void gx_map_init_remove_all_build_structure_items(string name)
```


## gx_map_init_add_build_structure_item
```sq
void gx_map_init_add_build_structure_item(string unitType, table params = {})
```

```sq
table params = {
    string m_structure,             # name of structure to build, i.e. "Microwave"
    Float2 m_position,              # position in command card to place at, leaving empty will use default
    bool bBuildAdvanced = false     # default is false, if set to True, will be placed in 'build advanced' tab
}
```

## gx_map_init_remove_all_build_items
```sq
void gx_map_init_remove_all_build_items(string unitType)
```


## gx_map_init_add_build_item
```sq
void gx_map_init_add_build_item(string unitType, table params)
```

```sq
table params = {
    string m_unitType,      # unit type to add
    string m_research,      # research to add
    Float2 m_position       # position in command card
}
```

## gx_modify_scoreboard
```sq
void gx_modify_scoreboard(table params = {})
```

```sq
table params = {
    bool m_bDisplay,
    bool m_bShowForceScores,
    bool m_bShowPlayerScores
}
```

## gx_set_speech_bubble
```sq
int gx_set_speech_bubble(int unit_id, table params = {})
```

```sq
table params = {
    string m_text,          # Speech Bubble text to display
    int m_duration = 60     # duration to display in ticks
                            # set to -1 to make it last forever
                            # default: 60 ticks (3 seconds)
}
```

- set a speech bubble for unit_id
- returns an integer id for the speech bubble
## gx_remove_speech_bubble
```sq
void gx_remove_speech_bubble(int unit_id, int speechBubbleID)
```

- setting `speechBubbleID` to `0` will remove current speech bubble
- Remove speech bubble for unit if current speech bubble ID matches `speechBubbleID`
## gx_remove_current_speech_bubble
```sq
void gx_remove_current_speech_bubble(int unit_id)
```

- Equivalent to calling `gx_remove_speech_bubble(unit_id, 0)`
- Remove speech bubble for unit
## gx_get_sim_var
```sq
mixed gx_get_sim_var(string varName)
```


## gx_set_sim_var
```sq
void gx_set_sim_var(string varName, mixed varValue)
```


## gx_add_sim_var
```sq
void gx_add_sim_var(string varName, mixed varValue)
```


## gx_get_force_var
```sq
mixed gx_get_force_var(int force_id, string varName)
```


## gx_set_force_var
```sq
void gx_set_force_var(int force_id, string varName, mixed varValue)
```


## gx_add_force_var
```sq
void gx_add_force_var(int force_id, string varName, mixed varValue)
```


## gx_get_player_var
```sq
mixed gx_get_player_var(int player_id, string varName)
```


## gx_set_player_var
```sq
void gx_set_player_var(int player_id, string varName, mixed varValue)
```


## gx_add_player_var
```sq
void gx_add_player_var(int player_id, string varName, mixed varValue)
```


## gx_get_unit_var
```sq
mixed gx_get_unit_var(int unit_id, string varName)
```


## gx_set_unit_var
```sq
void gx_set_unit_var(int unit_id, string varName, mixed varValue)
```


## gx_add_unit_var
```sq
void gx_add_unit_var(int unit_id, string varName, mixed varValue)
```


## gx_set_unit_ammo
```sq
void gx_set_unit_ammo(int unit_id, string ammoName, int count)
```


## gx_get_unit_ammo
```sq
int gx_get_unit_ammo(int unit_id, string ammoName)
```


## gx_add_unit_ammo
```sq
void gx_add_unit_ammo(int unit_id, string ammoName, int count)
```


## gx_set_player_ammo_in_unit
```sq
void gx_set_player_ammo_in_unit(int unit_id, string ammoName, int count)
```


## gx_get_player_ammo_in_unit
```sq
int gx_get_player_ammo_in_unit(int unit_id, string ammoName)
```


## gx_add_player_ammo_in_unit
```sq
void gx_add_player_ammo_in_unit(int unit_id, string ammoName, int count)
```


## gx_get_player_ammo_total
```sq
int gx_get_player_ammo_total(int player_id, string ammoName)
```

```sq
table params = {
    string m_tag,           # Required                                 (string)
    int m_player_id = 0     # Optional, used to Filter. Default = 0.   (int)
}
```

- Returns how much `player ammo` of type `ammoName` the player has
- returns unit_id with the given `m_name` or
- unit name can be set in map editor.
- if multiple units have the same name, the first will be returned.
## gx_kill_all_units
```sq
void gx_kill_all_units(table params = {})
```

```sq
table params = {
    int m_playerIDs[],  # Optional
    int m_forceIDs[],   # Optional
}
```

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

## gx_is_player_allied_to
```sq
bool gx_is_player_allied_to(int playerID, int otherPlayerID)
```


## gx_set_player_allied_to
```sq
void gx_set_player_allied_to(int playerID, int otherPlayerID, bool bAlly)
```


## gx_register_for_location_events
```sq
void gx_register_for_location_events(bool bEnable, table params = {})
```

- Register to receive `UnitEnteredLocation` and `UnitExitedLocation` events
- no optional parameters currently
- Usually you will want to only call this one time time in the `gx_sim_init` function
- See {{enum("EventType")}} and {{eventQueue()}} for more information
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

## gx_sound2d_create
```sq
int gx_sound2d_create(table params = {})
```

```sq
table params = {
    string m_sound,         # name of sound to play
    string m_soundPack,     # will play random sound from soundpack
    int m_forceIDs[],       # forceIDs that can hear the sound
    int m_playerIDs[],      # playerIDs that can hear the sound
    float m_volume = 1,     # Optional, volume multiplier (default = 1)
    float m_pitch = 1,      # Optional, pitch of sound (default = 1)
    bool m_bLoop = false    # Optional, controls if sound should loop
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
table params = {
    float m_volume,     # Optional, volume multiplier
    float m_pitch       # Optional, pitch of sound
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
table params = {
    string m_sound,         # name of sound to play
    string m_soundPack,     # play random sound from soundpack
    int m_unitID,           # Optional, unit for sound to attach to
    bool m_bStopSoundOnUnitDeath,   # Optional, default true if m_unitID is set
    Float2 m_pos2d,         # Optional, 2d position for sound
    Float3 m_pos3d,         # Optional, 3d position for sound
    float m_radius = 0,     # Optional, sound radius, default = 0
    float m_volume = 1,     # Optional, volume multiplier (default = 1)
    float m_pitch = 1,      # Optional, pitch of sound (default = 1)
    bool m_bLoop = false                    # Optional, controls if sound should loop
    bool m_bRandomLoopStartTime = false     # Optional
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
table params = {
    float m_volume,     # Optional, volume multiplier
    float m_pitch,      # Optional, pitch of sound
    Float2 m_pos2d,     # Optional
    Float3 m_pos3d      # Optional
}
```

- `m_pos2d` and `m_pos3d` will be ignored if sound is attached to a unit
## gx_sound3d_is_playing
```sq
bool gx_sound3d_is_playing(int soundID)
```

- returns `true` if sound is currently playing
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
## gx_color_srgba_to_hex4
```sq
int gx_color_srgba_to_hex4(Float4 srgba)
```


## gx_color_srgb_to_hex3
```sq
int gx_color_srgb_to_hex3(Float3 srgb)
```


## gx_color_hsva_to_srgba
```sq
Float4 gx_color_hsva_to_srgba(Float4 hsva)
```


## gx_color_srgba_to_hsva
```sq
Float4 gx_color_srgba_to_hsva(Float4 srgba)
```


## gx_color_hsv_to_srgb
```sq
Float3 gx_color_hsv_to_srgb(Float3 hsv)
```


## gx_color_srgb_to_hsv
```sq
Float3 gx_color_srgb_to_hsv(Float3 srgb)
```


## gx_color_hex3_to_hex4
```sq
int gx_color_hex3_to_hex4(int hex3, int alpha = 0xFF)
```


## gx_color_hex4_to_hex3
```sq
int gx_color_hex4_to_hex3(int hex4)
```


## gx_color_hex4_to_srgba
```sq
Float4 gx_color_hex4_to_srgba(int hex4)
```


## gx_color_hex3_to_srgb
```sq
Float3 gx_color_hex3_to_srgb(int hex3)
```


## gx_draw_glow_image
```sq
void gx_draw_glow_image(table params)
```

```sq
table params = {
    string m_img,                   # Required, Icon Name
    AABR_int m_aabr,                # AABR to draw to
    string m_location,              # Location to draw to
    AABR_int m_excludeAABRs[],      # Optional, AABRs not to draw to
    string m_excludeLocations[],    # Optional, locations not to draw to
}
```

- `m_img` must be set
- Exactly one of `m_abbr` or `m_location` must be set
## gx_get_sim_image_colors
```sq
int[] gx_get_sim_image_colors(table params)
```

```sq
table params = {
    string m_img    # Required, Icon Name
}
```

- Returns all the pixels in the image in hex3 format
- Alpha channel is ignored and not returned
## gx_set_terrain_glow_color
```sq
void gx_set_terrain_glow_color(table params = {})
```

```sq
table params = {
  int m_index,      # Glow index to change, required
  int m_hex,        # srgb hex3 code for color to set
  Float3 m_color    # srgb color (each component [0.0-1.0]) for new color to set
}
```

- Only one `m_hex` or `m_color` should be set, not both.
- Internally, `m_hex` is converted to `m_color`.
- `m_hex` parameter is only given for convenience.
## gx_decal_create
```sq
int gx_decal_create(table params)
```

```sq
table params = {
    string m_preset,                # decal preset
    int m_alphaFn,
    int m_colorFn,
    bool m_bAlwaysDisplay,          # ignore fog of war checks
    bool m_bDisplayOnMinimap,
    Float4 m_color,                 # srgb with alpha
    Float2 m_pos,
    float m_rotation,               # radians
    float m_size,
    Float2 m_size,                  # size, can either be Float2 or float
    string m_tag,
    string m_texture,               # icon to use
    float m_speedFactor,            # animation speed if m_texture is animated GIF
    bool m_bOverlayOnSpace,
    bool m_bOverlayOnNormalTerrain
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
    int m_alphaFn,
    int m_colorFn,
    bool m_bAlwaysDisplay,      # ignore fog of war checks
    bool m_bDisplayOnMinimap,
    Float4 m_color,             # srgb with alpha
    Float2 m_pos,
    float m_rotation,           # radians
    float m_size,
    Float2 m_size,              # size, can either be Float2 or float
    string m_tag,
    string m_texture,           # icon to use
    float m_speedFactor,        # animation speed if m_texture is animated GIF
    bool m_bOverlayOnSpace,
    bool m_bOverlayOnNormalTerrain
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
int[] gx_decal_get_all_by_tag(string decalTag)
```

- return all decalIDs that have their `m_tag` set to `tag`
## gx_decal_get_by_tag
```sq
int gx_decal_get_by_tag(string decalTag)
```


## gx_decal_query
```sq
int[] gx_decal_query(table params)
```

```sq
table params = {
    AABR m_aabrs[],         # Optional
    string m_locations[],   # Optional
    bool m_bAll = false     # Optional, default false
}
```

- Searches inside all of the provided aabrs and locations for decals
- Query for decals inside `m_aabrs` and `m_locations`.
- Setting `m_bAll` to true will return all decals on the map
## gx_rand_float
```sq
float gx_rand_float(float min, float max)
```


## gx_rand_int
```sq
int gx_rand_int(int min, int max)
```


## gx_rand_unit_vec2
```sq
Float2 gx_rand_unit_vec2()
```


## gx_rand_unit_vec3
```sq
Float3 gx_rand_unit_vec3()
```


## gx_rand_unit_vec4
```sq
Float3 gx_rand_unit_vec4()
```


## gx_unit_vec_or_random
```sq
FloatN gx_unit_vec_or_random(FloatN val)
```

```sq
Float2 gx_unit_vec_or_random(Float2 val)
Float3 gx_unit_vec_or_random(Float3 val)
Float4 gx_unit_vec_or_random(Float4 val)
```

- Computes the unit vector of `v`.
- Will return random unit vector if `v` has magnitude of `0`.
## gx_unit_vec_or_zero
```sq
FloatN gx_unit_vec_or_zero(FloatN val)
```

```sq
Float2 gx_unit_vec_or_zero(Float2 val)
Float3 gx_unit_vec_or_zero(Float3 val)
Float4 gx_unit_vec_or_zero(Float4 val)
```

- Computes the unit vector of `v`.
- Will return zero-magnitude vector if unit vector `v` has magnitude of `0`.
## gx_terrain_offset_z_add
```sq
void gx_terrain_offset_z_add(Int2 vertexPos, float offset)
```


## gx_terrain_offset_z_set
```sq
void gx_terrain_offset_z_set(Int2 vertexPos, float offset)
```


## gx_terrain_offset_z_get
```sq
float gx_terrain_offset_z_get(Int2 vertexPos)
```


## gx_terrain_offset_z_add_2
```sq
void gx_terrain_offset_z_add_2(table params)
```

```sq
table params = {
    AABR_int m_aabrs[],     # Optional
    string m_locations[],   # Optional
    Int2 m_vertices[],      # Optional
    float m_val,            # Required
}
```

## gx_terrain_offset_z_set_2
```sq
void gx_terrain_offset_z_set_2(table params)
```

```sq
table params = {
    AABR_int m_aabrs[],     # Optional
    string m_locations[],   # Optional
    Int2 m_vertices[],      # Optional
    float m_val,            # Required
}
```

## gx_aabr_contains
```sq
bool gx_aabr_contains(AABR aabr, Float2 pt)
```


## gx_aabr_contains_or_touching
```sq
bool gx_aabr_contains_or_touching(AABR aabr, Float2 pt)
```


## gx_create_effect
```sq
int gx_create_effect(table params)
```

```sq
table params = {
    EffectType m_type,
    Float2 m_pos,
    int m_duration,
    Float4 m_color,     # srgb
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
    Float2 m_pos,
    float m_radius
}
- Creates a nuke unit
```

## gx_triangle_lerp
```sq
float gx_triangle_lerp(float begin, float end, float period, float x)
```

- Lerp function
## gx_queue_command
```sq
void gx_queue_command(int unit_ids[], CommandType command, table params = {}, bool bQueueCommand = false)
```

```sq
table params = {
    int m_unitID,            # unit to target
    string m_location,     # location to target
    Float2 m_pos,          # position to target
}
```

- only one (or zero) unit_id, m_location, m_pos should be set
- some commands/spells only work when certain params are set
- (i.e., a spell that can only target units cannot target a `m_pos` or `m_location`)
- `CommandType` can also be a spell identifier
- if `bQueueCommand` is `true`, appends the command in the unit's command queue, otherwise command queue beforehand
- See {{enum("CommandType")}} for possible command values
## gx_force_select_units
```sq
void gx_force_select_units(int playerID, int unitIDs[])
```

- clears player's unit selection, and sets unitIDs as new selection
## gx_add_event_message
```sq
void gx_add_event_message(string message)
```

- Adds an event message visibly by all players on left side of screen
## gx_display_ui_elements
```sq
void gx_display_ui_elements(table params = {})
```

```sq
table params = {
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

## gx_add_center_message
```sq
int gx_add_center_message(table params = {})
```

```sq
table params = {
    string m_msg,
    int m_forceIDs[],
    int m_playerIDs[],
    int m_duration = 100,   # 5 seconds
}
```

- displays a player event message for player in middle of their screen for matching players
- if `m_duration` is `-1` message will be displayed forever until `gx_clear_center_messages` or `gx_clear_center_message_by_id` is called.
- returns `msgID` that can be used by `gx_clear_center_message_by_id` if needed.
## gx_clear_center_messages
```sq
void gx_clear_center_messages(table params = {})
```

```sq
table params = {
    int m_forceIDs[],
    int m_playerIDs[]
}
```

- clears all messages for players match params
- if both `m_forceIDs` and `m_playerIDs` are empty, messages will be cleared for all players
## gx_update_map_hints
```sq
void gx_update_map_hints(table params)
```

```sq
table params = {
    int m_forceIDs[],
    int m_playerIDs[],
    string m_button,
    string m_description,
    string m_hover,
    bool m_bDisplay
}
```

## gx_clear_center_message_by_id
```sq
void gx_clear_center_message_by_id(int msgID)
```

- clear message with msgID `msgID`
## gx_clear_terrain_paint
```sq
void gx_clear_terrain_paint(table params)
```

```sq
table params = {
    string m_locations[],
    AABR_float m_aabrs[]
}
```

## gx_paint_terrain
```sq
void gx_paint_terrain(table params)
```

```sq
table params = {
    string m_location,
    AABR_float m_aabr,
    string m_img,
    Float4 m_srgba
}
```

- only one of `m_location` or `m_aabr` should be set.
## gx_clear_resource_ui_items
```sq
void gx_clear_resource_ui_items(table params = {})
```

```sq
table params = {
    int m_playerIDs[],
    int m_forceIDs[]
}
```

## gx_add_resource_ui_item
```sq
void gx_add_resource_ui_item(table params = {})
```

```sq
table params = {
    int m_playerIDs[],
    int m_forceIDs[],
    Expr<int> m_val,
    Expr<int> m_max,
    Expr<bool> m_bDisplayRed,
    string m_img
}
```

## gx_get_common_uds
```sq
string[] gx_get_common_uds(table params = {})
```

```sq
used for filtering, optional.
table params = {
    bool m_bStructure,
    Race m_race
}
```

## gx_get_ud_race
```sq
Race gx_get_ud_race(string unitType)
```


## gx_get_ud_auto_attack_anims
```sq
string[] gx_get_ud_auto_attack_anims(string unitType)
```


## gx_get_num_attacks_in_ud_auto_attack_anim
```sq
int gx_get_num_attacks_in_ud_auto_attack_anim(string unitType, string animName)
```


## gx_clear_ud_auto_attacks
```sq
void gx_clear_ud_auto_attacks(string unitType)
```


## gx_add_ud_auto_attack
```sq
void gx_add_ud_auto_attack(string unitType, AutoAttackTable params)
```

```sq
AutoAttackTable {
    float m_range,
    int m_animDuration,
    int m_cooldown,
    bool m_bMelee,
    bool m_bCanTargetAir,
    bool m_bCanTargetGround,
    string m_anim,
    Expr<bool> m_req,
    AttackTable m_attacks[]
}

AttackTable {
    AttackType m_type,
    float m_splashRadius,
    int m_dmg,
    DamageExtraTable m_dmgExtra
}

DamageExtraTable {
    int m_vsLight,
    int m_vsMedium,
    int m_vsHeavy
}
```

## gx_is_event_queue_empty
```sq
void gx_is_event_queue_empty()
```

- Check if event queue is empty.
## gx_pop_event_from_queue
```sq
Event gx_pop_event_from_queue()
```

- Pop event from event queue.
## gx_include
```sq
void gx_include(string filepath)
```

- Includes filename in current compilation.
- A file is only included once by gx_include; subsequent calls are ignored.
- Typically called at the top of your drift script file.
## gx_set_sim_prop
```sq
void gx_set_sim_prop(SimProp prop, mixed val)
```


## gx_get_sim_prop
```sq
mixed gx_get_sim_prop(SimProp prop)
```


## gx_get_unit_prop
```sq
mixed gx_get_unit_prop(UnitProp prop, int unitID)
```


## gx_set_unit_prop
```sq
void gx_set_unit_prop(UnitProp prop, int unitID, mixed val)
```


## gx_add_unit_prop
```sq
void gx_add_unit_prop(UnitProp prop, int unitID, mixed val)
```


## gx_get_location_prop
```sq
mixed gx_get_location_prop(LocationProp prop, string locationName)
```


## gx_set_location_prop
```sq
void gx_set_location_prop(LocationProp prop, string locationName, mixed val)
```


## gx_get_player_prop
```sq
mixed gx_get_player_prop(PlayerProp prop, int playerID)
```


## gx_set_player_prop
```sq
void gx_set_player_prop(PlayerProp prop, int playerID, mixed val)
```


## gx_add_player_prop
```sq
void gx_add_player_prop(PlayerProp prop, int playerID, mixed val)
```


## gx_get_decal_prop
```sq
mixed gx_get_decal_prop(DecalProp prop, int decalID)
```


## gx_set_decal_prop
```sq
void gx_set_decal_prop(DecalProp prop, int decalID, mixed val)
```


## gx_get_force_prop
```sq
mixed gx_get_force_prop(ForceProp prop, int forceID)
```


## gx_set_force_prop
```sq
void gx_set_force_prop(ForceProp prop, int forceID, mixed val)
```


## gx_add_force_prop
```sq
void gx_add_force_prop(ForceProp prop, int forceID, mixed val)
```


## hash
```sq
int hash(mixed object, ...)
```

- internally invokes all objects `_hash()` meta-function and combines the hashes together
## object_id
```sq
int object_id(object obj)
```

- returns a unique object id for class instances, arrays, and tables
- return 0 for other types
## rand_int
```sq
int rand_int(int min, int max)
```

- returns random number from `[min max]`
## rand_float
```sq
float rand_float(float min, float max)
```

- returns random number from `[min max]`
## rand
```sq
int rand()
```

- returns 32-bit random number from `[0, +2147483647]`, or (`0x7FFFFFFF`)
## rand_signed
```sq
int rand_signed()
```

- returns 32-bit random number from `[-2147483648, +2147483647]`
## rand64
```sq
int rand64()
```

- returns random number from `[-9223372036854775808, +9223372036854775807]`
## sqrt
```sq
float sqrt(float x)
```

- returns square root of x
## sin
```sq
float sin(float x)
```

- return sin of x
## asin
```sq
float asin(float x)
```

- arcsin of x
## cos
```sq
float cos(float x)
```

- return cos of x
## acos
```sq
float acos(float x)
```

- arccos of x
## tan
```sq
float tan(float x)
```

- return tan of x
## atan
```sq
float atan(float x)
```

- arctan of x
## atan2
```sq
float atan2(float y, float x)
```

- arctan2 of x
## lerp
```sq
float lerp(float x0, float x1, float t)
```

- linearly interpolate x -> y based on `[0, 1]`
## floor
```sq
float floor(float x)
```


## ceil
```sq
float ceil(float x)
```


## fmod
```sq
float fmod(float val, float divisor)
```

- return value will have same sign as `val`
## getroottable
```sq
table getroottable()
```

- get DriftScript's internal "root" table
- this table contains all of the global functions and constants
## getstackinfos
```sq
table getstackinfos(int level)
```


## assert
```sq
void assert(bool expr [, string msg])
```


## print
```sq
void print(string msg)
```

- print message to all players in game
- also outputs to console in map editor
- see `gx_print` for more functionality
## compilestring
```sq
function compilestring(string str)
```


## newthread
```sq
thread newthread(function fn)
```


## suspend
```sq
mixed suspend(mixed val, ...)
```


## array
```sq
[] array(int size = 0, mixed fill = null)
```

```sq
array.len()
array.append(val)
array.extend(array)
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

## type
```sq
string type(object obj)
```


## callee
```sq
function callee()
```


## dummy
```sq
void dummy()
```

- function that does nothing
## min
```sq
mixed min(mixed x, mixed y)
```

- returns the minimum of x and y
## max
```sq
mixed max(mixed x, mixed y)
```

- returns the maximum of x and y
## abs
```sq
mixed abs(mixed value)
```

- return absolute value of x
## clamp
```sq
mixed clamp(mixed value, mixed minValue, mixed maxValue)
```

- clamps val to be between `min` and `max`
## pow
```sq
float pow(float val, int exponent)
```


## table
```sq
{} table()
```

```sq
table.len()
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

## string
```sq
string string(text = "")
```

```sq
string.len()
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
string.weakref()
```

## Float2
```sq
Vec2 Float2(mixed x, mixed y)
```

- Helper function to create a `Vec2`
## Int2
```sq
Vec2 Int2(mixed x, mixed y)
```

- Helper function to create a `Vec2`
## Float3
```sq
Vec3 Float3(mixed x, mixed y, mixed z)
```

- Helper function to create a `Vec3`
## Int3
```sq
Vec3 Int3(mixed x, mixed y, mixed z)
```

- Helper function to create a `Vec3`
## Float4
```sq
Vec4 Float4(mixed x, mixed y, mixed z, mixed w)
```

- Helper function to create a `Vec4`
## Int4
```sq
Vec4 Int4(mixed x, mixed y, mixed z, mixed w)
```

- Helper function to create a `Vec4`
## AABR_float
```sq
AABR AABR_float(Vec2 minPt, Vec2 maxPt)
```

- Helper function to make AABR
## AABR_int
```sq
AABR AABR_int(Vec2 minPt, Vec2 maxPt)
```

- Helper function to make AABR
