
<figure markdown> 
# DOL codes
</figure>

!!! warning 

    You should know at **least** how to open and change hex in a file before attempting this.<br>
    Visit the [tutorial on HxD](https://www.lbmwiki.net/tutorials/06_Using_HxD) before attempting if you do not know how.

!!! tip

    Remember to use ```CTRL + B``` to copy **write** and NOT ```CTRL + V``` to copy **paste**.

##**Force Portrait Ghosts to Use Params for HP**

At offset ```0xBDED0``` paste/write ```4800002c.```
(Credit: CyrusLoS)
<br>

##**Add Treasure Drops to Regular Ghosts**

Change the address listed at ```0x358718``` to ```800d59ac```.
Add a entry for the ghost in question into iyapootable along with what you want it to drop.
(Credit: LMFinish)
<br>

##**Reverse Kieru (Spawn Animation) for Regular Ghosts**

Change the value at any of the offsets to ```0E 52``` to reverse the ghosts' spawn-in animation.

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
<br>

##**Beta Spinning Coins by Ralf (Upside Down Bug Fix by 0wen)**

At offset ```0xD50```, paste/write ```3C608000C0033D6CC03D0024EC21002AD03D0024A87C00A64815427C41700000```
At offset ```0x15402C```, paste/write ```3800BC00B01E005E```
At offset ```0x154D40```, paste/write ```4BEABD70```
(Credit: weirdboo, 0wen)