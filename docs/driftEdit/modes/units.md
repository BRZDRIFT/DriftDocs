## Units

- Thi mode allows you to add/delete units on the map for the current player.
- You can change the current player using the dropdown below the unit list
- Selecting units, and then press `Enter` will open up a dialog for additional unit options, such as changing player ID, gemston amount, etc
    - Different types of units may offer different options in dialog
    - You can also provide string identifiers to units in the options dialog, which can be using for scripting and other things.
        - Example: In order for a gateway to teleport units to another gateway, you need to provide each gateway a string identifier and set up the destination gateway in the options
- Compatible with {{sideControls("symmetry-mode")}}, {{sideControls("enable-unit-stacking")}}, 
and {{sideControls("adddel-only-if-symmetries-are-valid")}}, 


## Unit Groups

- You can assign unit groups to certain units, which can be helpful for scripting.
- Certain units have properties/abilities that may reference unit groups
    - Example: Control Panel can a reference group of Trap Doors to enable opening/closing them
