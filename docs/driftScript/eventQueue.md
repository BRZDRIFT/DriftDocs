## Event Queue

Event Structure:
```sq
table Event
{
    EventType m_type = EventType::Invalid;
    ComplexColor m_oldPlayerNameColor;
    string m_oldPlayerName;
    string m_oldPlayerName2;
    ComplexColor m_playerNameColor;
    string m_playerName;
    string m_playerName2;
    int m_oldPlayerID;
    int m_playerID;
    string m_cmd;
    string m_text;
    int m_unitID;
    int m_itemPickupUnitID;
    string m_location;
    string m_itemUd;
    string m_itemTag;
    string m_customSpellEventTag;
    string m_ud;
    string m_unitTag;
    DeathCause m_deathCause;
    int m_killerPlayerID;
    Vec2<float> m_pos;
    float m_radius;
    int m_soundID;
    bool m_bVal;
    ExplosionEventType m_explosionEventType;
}
```

- Look at the comments in the definition of {{enum("EventType")}} to see which fields each `EventType` populates.
- TODO: Better explain which fields are populated depending on `m_type`

Example of reading events from queue

```sq
function gx_sim_update()
{
    while (!gx_is_event_queue_empty())
    {
        local ev = gx_pop_event_from_queue()
        if (ev.m_type == EventType.PlayerLeftGame)
        {
            print("Player " + ev.m_playerID + " has left the game!")
        }
        else if (ev.m_type == EventType.PlayerNameChanged)
        {
            print(ev.m_oldPlayerName + " changed name to " + ev.m_playerName)
        }
    }

    # do rest of game logic
}
```

Functions that operate on event queue:

- {{fn("gx_is_event_queue_empty")}}
- {{fn("gx_pop_event_from_queue")}}

Note:

- Any unpopped events are automatically popped off of queue after each {{entry("gx_sim_update")}} call.
