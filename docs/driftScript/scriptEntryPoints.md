# Entry Points

Your script code has 3 entry points.

## gx_map_init
```sq
function gx_map_init() {
    # your code here
}
```

- The very first entry-point function to be called.
    - Called before game begins, and even before minimap creation.
- This is the only place you are allowed to modify/copy unit datas (i.e. make your own units).
- This function is only called once.
- Global variables defined in this script are not accessible from the `gx_sim_*` functions
- Should be defined in `/MapInit.DriftScript`

## gx_sim_init
```sq
function gx_sim_init() {
    # your code here
}
```

- Called when game simulation is setup and ready.
- This is where your initialization code goes.
- This function is only called once.
- Global variables defined here are accessible to `gx_sim_update`
- At this point, {{fn("gx_get_sim_tick")}} will return 0.
- Should be defined in `/SimUpdate.DriftScript`

## gx_sim_update
```sq
function gx_sim_update() {
    # your code here
}
```

- Called once every simulation update (roughly every 50ms).
- On first invocation, {{fn("gx_get_sim_tick")}} will return 1.
    - On second invocation, {{fn("gx_get_sim_tick")}} will return 2, and so on..
- This is where your main script code goes.
- Global variables persist across `gx_sim_update` calls.
- Should be defined in `/SimUpdate.DriftScript`
