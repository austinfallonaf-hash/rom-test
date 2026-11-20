# Bot interaction alpha

This cumulative partial English draft adds **106 native records**: 105 bot mood
and interaction lines (2974–3078), plus the ship-interior prompt 3079. Coverage
reaches **3,189 native records, 832 UI strings, 299 choice blocks and three bitmap
captions**. All preceding 3,083 catalog entries are identical.

## Voices and short allocations

Fifteen seven-line voices cover being addressed, idle talk, growing stronger,
hunger, irritation and severe hunger/stress. They retain master/boss/Captain/Bro
addresses, pomyu/zari/mel/osu/moshi quirks, a refined voice, military reporting,
childish talk, tough and reserved voices, rural diction and a singing voice.
The childlike wedding boast, jealousy, reluctance to work, desire for training,
hungry immobility and stress complaints remain distinct. English is condensed
to the original byte allocation and sixteen cells per line. Wording is provisional.

Seven original 200B:0007 bot-name insertions remain dynamic. The codec reserves
eleven cells, including the longest translated default name Mochimocchi. Two
short originally single-line records explicitly permit one added newline:

| Record | English | Encoded budget |
| --- | --- | --- |
| 3033 | NAME / Hungry! | 28 of 30 bytes |
| 3035 | NAME / Stuck! | 26 of 26 bytes |

Both declarations preserve the original portraits, reset and name argument in
order; only 2000 is inserted. All other new records retain their exact source
control stream, including 3054's trailing empty-line command. No added page,
portrait, variable, color or argument change is allowed. There are no new
anchored pages, label relocations, engine changes or codec changes.

All earlier active text and eight-byte descriptors match the bot-food ROM.
The 127 stored labels in 36 donors are unchanged, along with their original
source slots, native Berry 2954 and saved Japanese nicknames. Item effects,
recipes, inventory quantities, events and game mechanics are not edited.

## Runtime evidence and limits

The exact final ROM cold-boots and loads the native reference file A. The file,
ship wake and day-2 pause display are recorded in local/bot-interaction-evidence.
The player name, 500G and saved Merlin remain intact. Reference, default working
and isolated EEPROM hashes match; no in-game save is attempted and no savestate
from this or an older ROM is loaded or created.

Merlin's profile also retains Caster/Water, Charm, Fire v1 and the original stats.
The new mood dialogue was not reached in this run; the evidence README records
that limitation.
Build/control/width checks do not establish gameplay coverage of all 105 mood
branches, rare bot voices, dynamic custom names, or the ship-interior prompt.
Earlier bedtime/food/name/donor/regional scenes, five page exceptions, Parts
frame and VS/Transfer Pak branches still need gameplay checks.

Final ROM MD5: `83F535F27E7B191F1EA74D02478FFC35`.
Source and final ROMs are 32 MiB. CIC-6102 CRC1/CRC2 remain
`FFA89600 C278C65F`; original bootcode and other header bytes are untouched.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/bot-interaction-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/bot-interaction-alpha.z64 --patch local/bot-interaction-alpha.bps
```

Apply releases/bot-interaction-alpha.bps directly to the exact Japanese original;
do not stack release patches. The release manifest records ROM and patch hashes.
Floating IPS independently reproduces the ROM from the BPS. Read-only chksum64
agrees with the header. All **128 tests** pass in source and clean restoration.

The encrypted recovery ZIP round-trips byte-for-byte and restores all 783 manifested
payload hashes, source revision, ROM/BPS/reference save, evidence, executable
modes, emulator library symlink and the exact-ROM 16Kbit EEPROM profile. The
passphrase remains outside Git. See backups/README.md and RESTORE.md.

Next: bot task, meal and shower reactions at record **3080**. Preserve all
occupied native-label storage when allocating future text.

## New dialogue

Slash separates visible lines; NAME denotes the unchanged dynamic bot name.

| ID | English |
| --- | --- |
| 2974 | Yes, / Master? |
| 2975 | So bored... |
| 2976 | My back's / heavy! |
| 2977 | I'm hungry! |
| 2978 | So annoyed... |
| 2979 | Hungry! / Can't go! |
| 2980 | ......... |
| 2981 | Yes, Boss? |
| 2982 | Must train / harder! |
| 2983 | Got a bit / of a gut? |
| 2984 | Hungry! / Hungry! / Hungry! |
| 2985 | Wooooooar!!! |
| 2986 | Starved! / I'm done |
| 2987 | Wooooar!!! / Grrrrroar!!! / Pawoooooon!!! |
| 2988 | Need / anything? |
| 2989 | Hard work? / Not me... |
| 2990 | Prettier / Lovelier! |
| 2991 | I'm hungry! / May I dine? |
| 2992 | Stop it! / Let me be! |
| 2993 | I haven't / eaten lately... |
| 2994 | Eeeeeek!!! / That girl! / So jealous!! |
| 2995 | Pomyu? / Yes? |
| 2996 | Pomyu / Pomyu?? |
| 2997 | To grow / up, pomyu! |
| 2998 | Rrr, pomyu |
| 2999 | Mad, pomyu |
| 3000 | Rrr,pomyu / Rrr,pomyu / Rrr,pomyu |
| 3001 | Grr,pomyu / Grr,pomyu / Grr,pomyu |
| 3002 | Yes, zari? |
| 3003 | Zari?Zari |
| 3004 | Hate me, zari? |
| 3005 | Meat! Zari!!! |
| 3006 | Zari... / I feel bad |
| 3007 | Any food! / Now, zari! |
| 3008 | Zari zari / Hehe, zari |
| 3009 | Yes / Captain? |
| 3010 | I'll try! Osu! |
| 3011 | I'm getting / stronger! Osu! |
| 3012 | Hungry, sir! / Feed me! / Osu!! |
| 3013 | Lately / I'm stressed! |
| 3014 | Too hungry to go / Sorry, no use! |
| 3015 | I feel ill, sir |
| 3016 | Orders, / Captain? |
| 3017 | Captain, / I respect you! |
| 3018 | Captain! / Good work! |
| 3019 | Captain! / I'm hungry, sir |
| 3020 | Captain! / I'm stressed / out, sir! |
| 3021 | Captain! / I cannot even / move, sir! |
| 3022 | Captain! / Stress is MAX! / Help me, sir! |
| 3023 | Yes, mel? / Bro! |
| 3024 | Bro, play with / NAME! |
| 3025 | Mel??? |
| 3026 | Hungry mel! |
| 3027 | Hmph! / Mad, mel! |
| 3028 | NAME... / Too hungry to go |
| 3029 | Uhhh, mel |
| 3030 | What? / Bro? |
| 3031 | Bro, play with / NAME! |
| 3032 | NAME says / I'll wed you! |
| 3033 | NAME / Hungry! |
| 3034 | NAME / hates you, Bro! |
| 3035 | NAME / Stuck! |
| 3036 | Nyah-nyah! |
| 3037 | What is it? |
| 3038 | I must be / much stronger! |
| 3039 | I want / stronger foes! |
| 3040 | Hungry! |
| 3041 | Annoyed! |
| 3042 | Hungry! / No strength |
| 3043 | So annoyed... / So annoyed... / So annoyed... |
| 3044 | May I help? |
| 3045 | Chores are / such a pain |
| 3046 | I'm cool / aren't I?? |
| 3047 | Hungry! / Got any food? |
| 3048 | So annoyed! / No one's fault |
| 3049 | Hungry... / A pain... / Won't move |
| 3050 | Aaaaaaaaargh!!! / So annoyed... / So annoyed!!! |
| 3051 | What...? |
| 3052 | I'll obey... |
| 3053 | I'll follow you / for life...! |
| 3054 | Pardon, / may we eat soon? /  |
| 3055 | I'm stressed / What can I do? |
| 3056 | Must eat, / or I can't move |
| 3057 | Tense...tense... / Tense...tense... / Tense...tense... |
| 3058 | You / called me?? |
| 3059 | No jobs? / I'll walk |
| 3060 | I don't / need more / strength... |
| 3061 | Hungry... |
| 3062 | Feeling ill |
| 3063 | Hungry / Won't move |
| 3064 | Tense, eh / Tense, eh / Tense, eh |
| 3065 | Huh? / Huh? / Huh? |
| 3066 | Huh? Huh? / Yes? |
| 3067 | La la la la la / La la la la! / What? |
| 3068 | Hungry! / So hungry!! |
| 3069 | Mad, mad, mad! |
| 3070 | Hungry! / So hungry! / SO hungry!! |
| 3071 | Tense! Mad!... / Tense! Mad!... / Tense! Mad!... |
| 3072 | Yes,moshi? |
| 3073 | I'll do / all ya say! |
| 3074 | Why'm I / here, moshi? |
| 3075 | Feed me / please... |
| 3076 | Why work / me so hard, / moshi? |
| 3077 | Hungry! / Can't move |
| 3078 | Know my worth, / moshi?! / I'm so mad!!! |
| 3079 | Head / inside? |
