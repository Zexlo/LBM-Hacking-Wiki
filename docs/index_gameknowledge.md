---
hide:
  - toc
---

!!! warn "Note"
	This page should be considered as a work in progress. Generally, this should help with understanding how various parts of the game work, and that understanding may not always be 100% correct.

## File Formats
Luigi's Mansion has a few proprietary file formats, some of which were used in other Nintendo games, while others are unique to this game in particular. Information about each can be found below.

[JMP - Tracks character, enemy, furniture, and object info for each map.](gameknowledge/file_formats/JMP.md){ .md-button } 

[TXP - For animating texture patterns by switching texture indices in MDL file materials.](gameknowledge/file_formats/TXP.md){ .md-button } 

##JMP
###Observers
One of the things that people seem to have the most trouble understanding is Observers, so here is a small rundown:

Observers are essentially "mini-programs" that constantly ask the game questions about what the current state of the game is. (Eg: "Are all the ghosts in this wave captured yet?", "Is flag 23 turned on?"). 
Think of them like an invisible eye that consistently monitors what condition needs to be met so that something can be done.

They are used for everything from making ghosts spawn to making the lights turn on when you've captured all the ghosts in a room.

Let's look at an example:

!!! example " diagram"

	``` mermaid
	graph LR
	A[Start] --> B{All ghosts caught?};
	B -->|No| C[Go back to start];
	C --> A;
	B ---->|Yes| E[Turn on lights];
	```

	
1. The observer will ask the game a "question" (Eg: "Have all the candles in this room been blown out?") - In programming terms these "questions" are known as Conditions.
2. The game itself will reply with an "answer" of either True (Yes) or False (No). - In programming terms these "answers" are known as bool's / Booleans.
3. If the reply from the game is True (Yes) then the observer will do something - More accurately, it will do whatever is specified in the observer's do_type field.

By using the cond_string_arg0 and string_arg0 fields in the observers you can link a multiple observers to activate after just one observer activates,

this will allow you to do more than just one thing after a ghost wave has been defeated for example.

You could however also create a "observer chain" to do this; "Is all the ghosts in this wave captured yet?" (True) -> Light Up The Room (True) -> Unlock The Doors (True) -> Spawn Chest (True)

"There's multiple ways to Rome" - You can get similar results with different approaches, we recommend you choose one that you find the most understandable / easy to use.

And that is essentially how all observers in the game work.

Now go experiment! - That's the best way of learning! :)

##RAM/DOL

###RAM
**Change Which Door Triggers the Foyer Gold Ghost Laugh & Sets Flag 3**

	8001bec0 386000xx
	xx - Door ID
	(Credit: CyrusLoS)
	
###DOL
**Force Portrait Ghosts to Use Params for HP**

	At offset 0xBDED0 paste/write 4800002c.
	(Credit: CyrusLoS)
	
**Add Treasure Drops to Regular Ghosts**

	Change the address listed at 0x358718 to 800d59ac.
	Add a entry for the ghost in question into iyapootable along with what you want it to drop.
	(Credit: LMFinish)

**Reverse Kieru (Spawn Animation) for Regular Ghosts**

Change the value at any of the offsets to 0E 52 to reverse the ghosts' spawn-in animation.

| Offset         | Model Archive                        |
| :----------    | :----------------------------------- |
| `0x33DD5E`     | obake01.szp                          |
| `0x33DF5E`     | obake02.szp                          |
| `0x33E17E`     | obake03.szp                          |
| `0x33E3BE`     | obake04.szp                          |
| `0x33E3BE`     | topoo.szp                            |
| `0x33E3BE`     | skul.szp                             |
| `0x33EBBA`     | heypo.szp                            |
| `0x33F8C2`     | tenjyo.szp                           |
| `0x33FA02`     | banaoba.szp                          |

(Credit: weirdboo)

**Beta Spinning Coins by Ralf (Upside Down Bug Fix by 0wen)**

	At offset 0xD50, paste/write 3C608000C0033D6CC03D0024EC21002AD03D0024A87C00A64815427C41700000
	At offset 0x15402C, paste/write 3800BC00B01E005E
	At offset 0x154D40, paste/write 4BEABD70
	(Credit: weirdboo, 0wen)
	
**Various RAM Addresses**

| Address         | Description                                                                                                                                |
| :----------     | :-----------------------------------------                                                                                                 |
| `80340D48`      | Yapoo Appear Type                                                                                                                          |
| `80340F48`      | Mapoo Appear Type                                                                                                                          |
| `804D2BE4`      | Flashlight Cone Size Modifier                                                                                                              |
| `804D2BEC`      | Flashlight RGB                                                                                                                             |
| `800D0E94`      | Luigi's Reaction to Poison Mushroom (probably)                                                                                             |
| `800466F4`      | Draw Out of Bounds Coin                                                                                                                    |
| `804D2BB8`      | Luigi's Walking Speed                                                                                                                      |
| `8003D6F0`      | Radar State (NOP for Always-On Radar)                                                                                                      |                                                                                 
| `801E1EA0`      | Coin Physics (If this address is nopped/zero'd out it will give you spinning coins, however, it spins periodically and not consistently.)  |
| `800BCAF0`      | Treasuretable JMP Loading                                                                                                                  |  
| `800BCAF4`      | Treasuretable JMP Loading                                                                                                                  |
| `804D9A0C`      | Nintendo Logo Color                                                                                                                        |
| `800B3B6C`      | Flashlight  On/Off Function (NOP to disable function)                                                                                      |
| `804D8597`      | Value of Ghost Counter (How Many Ghosts Luigi Currently Has)                                                                               |

(Credit: ScaredLuigiCrawling)
