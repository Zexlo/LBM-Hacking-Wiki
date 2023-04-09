#JMP
	
##Description
JMP files contain info about characters, enemies, furniture, and other objects for each map.

##Information
File should be padded with @'s to the nearest whole 32 byte when written.

##File Structure
- Header
- List of Fields
- List of Entries

##Header
| Offset         | Size    | Type       | Description                |
| :----------    | :------ | :-------   | :--------------------      |
| 0x00           | 4       | uint       | Entry Count                |
| 0x04           | 4       | uint       | Field Count                |
| 0x08           | 4       | uint       | Entry Offset               |
| 0x0C           | 4       | uint       | Entry Size                 |

##Field
| Offset         | Size    | Type       | Description                |
| :----------    | :------ | :-------   | :--------------------      |
| 0x00           | 4       | uint       | Hash                       |
| 0x04           | 4       | uint       | Bitmask                    |
| 0x08           | 2       | ushort     | Offset                     |
| 0x0A           | 1       | byte       | Shift                      |
| 0x0B           | 1       | byte       | Type                       |

##Entry

Each entry consists of values for each of the fields in JMP. Therefore, the lengthy and format of an entry depends on the amount of fields, as well as their type, bitmask, etc.

##Type
| Value          | Description    |
| :----------    | :-----------   |
|0x00            | Int            |
|0x01            | String         |
|0x02            | Float          |