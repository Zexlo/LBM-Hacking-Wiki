
<figure markdown> 
# RAM codes
</figure>

##**Various RAM Addresses**

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


##**Door ID for setting flag 3 and triggering ghost laugh in foyer**

            RAM ADDRESS: 8001bec0 386000xx

            xx - Door ID

            (Credit: CyrusLoS)