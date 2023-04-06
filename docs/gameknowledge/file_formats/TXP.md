#TXP
	
##Author(s)
opeyx

##Description
TXP files are used for texture pattern animations, switching sampler indices used for a particular material. Both are found instead of MDL files.

##Information
File should be padded with 0's to the nearest whole 32 byte when written.

##File Structure
- Header
- List of Material Animation Groups
- List of Key Data

##Header
!!! info "Missing Contents"
	Missing some info from LMHack. If you see this, add it back.

##Material Animation Groups
!!! info "Missing Contents"
	Missing some info from LMHack. If you see this, add it back.

##Key Data

The Key Data is used to index the different samplers. (Which in turn contains index of a texture as well as wrap u/v etc.) The Key Data is just a list of ushort's and to read it you use the Key Data Offsets per group and loop by Key Count.

Thanks To [KillzXGaming](https://github.com/KillzXGaming/LM_Research/wiki/TXP)
