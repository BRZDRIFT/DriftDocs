## OnBuildItemComplete Callback

```sq
void on_build_item_complete_callback(table params)
```

```sq
table params = {
    int m_builderPlayerID,
    int m_builderUnitID,
    BuildItemType m_buildItemType,
    string m_buildItemName,
    int m_buildItemLevel,
    int m_createdUnitID
}
```

- Called when a build item completes in a production unit.
- Must set `m_onBuildItemCompleteCallbackName` via `gx_map_init_modify_ud_props` to enable this callback
- `m_createdUnitID` will be 0 if `buildItemType` is not `BuildItemType.Unit`
- `m_buildItemName` is the identifier for a `ud`, `player research`, `unit research`, `player ammo`, or `unit ammo` depending on `m_buildItemType`

## OnResearchComplete Callback

```sq
void on_research_complete_callback(int unitID, string researchName, int researchLevel [, table extra])
```

```sq
table extra = {
    bool m_bSetByScript,
    int m_oldLevel
}
```

- Called when a player or unit research is complete
- Note: `extra` parameter is optional
- Must set `m_onFinishedCallbackName` via `gx_map_init_modify_player_research_props` or `gx_map_init_modify_unit_research_props` to enable this callback
- Can also set `m_onFinishedCallbackName` via Data Editor for the specific research