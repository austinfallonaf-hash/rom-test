# Bot reactions alpha

This cumulative partial English draft adds **240 native dialogue records**
(3080–3319): fifteen sixteen-line voices reacting to chores, training, meals and
showers. Coverage reaches **3,429 native records, 832 UI strings, 299 choice
blocks and three bitmap captions**. All preceding 3,189 catalog entries match.

## Wording and controls

Each voice retains success/failure remarks for chores and training, ordinary
meal remarks, liked and disliked food reactions, and two shower remarks.
Master/boss/Captain/Bro addresses, refined and military speech, childlike and
tough voices, rural diction, singing and pomyu/zari/mel/osu/moshi quirks remain
distinct. Pomyu is shortened to pyu in tiny allocations. Some seven-cell lines
retain the praise/question or apology without the full catchphrase.

The broth, mayonnaise, dieting/weight, second stomach for dessert, tooth floss,
eating the plate, cheek-melting, oiling after showers, rust, shampoo/eyes,
free food, stomachache and sauna details remain where allocations allow.
English is a condensed draft, not an official localization. Item IDs, likes,
food effects, task results, inventories, events and save mechanics are unchanged.

All eighteen original bot-name insertions retain command 200B:0007. The codec
reserves eleven visible cells for the longest translated default name. Five
records explicitly add a newline, keeping their original controls as a
subsequence and inserting only one 2000 each:

| ID | English lines | Bytes used / original |
| --- | --- | --- |
| 3192 | NAME / Wow! | 22 / 28 |
| 3196 | NAME / Did well! | 32 / 32 |
| 3199 | NAME / Upset! | 26 / 30 |
| 3213 | Great! / NAME / Tired! | 40 / 48 |
| 3216 | NAME / I'm full! | 32 / 32 |

These are the only new control-stream differences. Every other portrait, reset,
line/page control and argument is exact. Each line fits sixteen cells and each
record fits its original allocation. No new pages, codec or engine changes are
needed. The earlier five anchored pages and two interaction newline opt-ins stay
identical.

All previous active bytes and eight-byte descriptors match bot-interaction-alpha.
The 127 stored labels in 36 donors are unchanged and disjoint; their original
relocated source slots remain intact. Berry 2954 and saved nicknames are intact.

## Runtime coverage

The exact final ROM cold-boots and loads native file A. Screenshots and a
completed log in local/bot-reactions-evidence record the native file menu, ship
wake, pause and Merlin profile: day 2, 500G, player name, Japanese saved Merlin
nickname, original stats, Charm and Fire v1. Reference/default/isolated EEPROMs
retain their exact hash. No in-game save is attempted and no savestate is loaded
or created.

New task, meal and shower triggers are not reached in this run. The new dialogue
has build, byte-budget, control-stream and dynamic-width checks, rather than full
gameplay validation. All reaction branches, name/newline contexts, prior mood,
bedtime, food, donor/regional scenes, five anchored pages, Parts frame and
VS/Transfer Pak still need gameplay checks.

Final MD5: `84DFA87A03D83DB3F2AD9A12264CF4CA`.
SHA-256: `925030105e47d2dbc908579849e9a99919dd74f4612128e1d4f2b5cede1ead5c`.
The original and target are 32 MiB. CIC-6102 CRC1/CRC2 remain
`FFA89600 C278C65F`; original bootcode and other header bytes are intact.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/bot-reactions-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/bot-reactions-alpha.z64 --patch local/bot-reactions-alpha.bps
```

Apply releases/bot-reactions-alpha.bps directly to the exact original Japanese
ROM; do not stack patches. Floating IPS independently reproduces the ROM and
read-only chksum64 agrees with the header. All **128 tests** pass in source and
after clean restoration. Checks inspect all new IDs/actual bytes/descriptors,
all earlier active bytes and all occupied label ranges.

The recovery ZIP contains **801 payload files**. Its AES-256 ciphertext is split
into .part001 and .part002 to stay within GitHub's per-file limit. The JSON index
records ordered names, sizes, part hashes and whole ciphertext hash. Parts are
individually verified, rejoined, checked against the original ciphertext and
decrypted. Decrypted ZIP bytes match the packaged ZIP exactly. Clean restoration
checks every file, source revision, save/evidence hashes, executable modes,
emulator library symlink and exact-ROM 16Kbit EEPROM profile. The passphrase stays
outside Git. See backups/README.md and RESTORE.md for the complete join/decrypt
commands; both parts are required. Earlier backups remain in their original
single-file format.

Next: minigame labels and instructions from **3320**. Inspect the fixed-grid
instruction reader from 3323 onward before choosing an encoding/layout; these
are not sixteen-cell labels. Preserve all occupied storage.

## New dialogue

Slash separates lines; NAME denotes the unchanged dynamic bot name.

| ID | English |
| --- | --- |
| 3080 | Did it! / Master! |
| 3081 | Is this OK? |
| 3082 | Huh... / I failed? |
| 3083 | So sorry! |
| 3084 | I tried! |
| 3085 | Did my / best! |
| 3086 | No good! |
| 3087 | Huh...? / How odd |
| 3088 | Thanks! |
| 3089 | I'm fired up! |
| 3090 | So very / tasty |
| 3091 | Want more! |
| 3092 | Cough! / Yuck! |
| 3093 | Not tasty! |
| 3094 | Refreshed |
| 3095 | Plating worn? |
| 3096 | Boss! Done / What else? |
| 3097 | Too easy! / Must train more! |
| 3098 | Huh? / Did I fail? |
| 3099 | Why? / I tried / so hard... |
| 3100 | Gotta / do this! |
| 3101 | Good for / a diet, eh |
| 3102 | Lost focus / halfway! |
| 3103 | Why look / away...?! |
| 3104 | Not sweet/hot / Not good/bad / OK... |
| 3105 | I'll gain fat |
| 3106 | This food... / Delicious!!! |
| 3107 | Fine broth |
| 3108 | This food... / Disgusting!! |
| 3109 | Not great / Add mayo / May help |
| 3110 | A finer / man now! |
| 3111 | Whew / Blood flows well |
| 3112 | Of course / I did it |
| 3113 | I can / do / most anything |
| 3114 | How odd / I failed? / No way! |
| 3115 | Vexed! / So vexed |
| 3116 | Quite / easy! |
| 3117 | Can this / make me / stronger? |
| 3118 | Wait! / That was a foul? |
| 3119 | Nooooo! / So vexing! |
| 3120 | Room for / dessert |
| 3121 | After meals / I feel happy |
| 3122 | Fine flavor / Memorable |
| 3123 | Quite tasty! |
| 3124 | This food / doesn't suit me / Too greasy |
| 3125 | This... / isn't tasty |
| 3126 | How lovely! |
| 3127 | Change my / shampoo, hmm? |
| 3128 | Yay pyu! |
| 3129 | Pomyu? / Win,pyu |
| 3130 | Boo,pomyu |
| 3131 | Pomyu... / Sorry! |
| 3132 | Wow,pyu |
| 3133 | Good?! |
| 3134 | Wah! Wah / Pomyu |
| 3135 | Tired,pyu |
| 3136 | Munch / Munch, pomyu |
| 3137 | Pomyu / Wipe lips |
| 3138 | Pomyu! / Very, very / tasty, pomyu! |
| 3139 | Pomyu? / Tasty! |
| 3140 | Pomyu! / Very very / nasty, pomyu! |
| 3141 | Pomyu? / Odd taste |
| 3142 | A bit / hot, pomyu |
| 3143 | Fresh! / Fresh,pyu |
| 3144 | Win, zari! |
| 3145 | Zari! / Chore expert |
| 3146 | Sorry,zari |
| 3147 | Zari / Bad at chores |
| 3148 | Zari / I train well! |
| 3149 | Yay zari |
| 3150 | Zari / I train badly |
| 3151 | I don't agree / Zari... |
| 3152 | Need floss / zari! |
| 3153 | Warming / up, zari! |
| 3154 | Zari! / Super tasty |
| 3155 | Zari? / Good! |
| 3156 | Zari! / Blech! Ugh! |
| 3157 | Zari? / Urp Urp |
| 3158 | Too / cool, zari |
| 3159 | Eager / zari! |
| 3160 | Done smoothly! / Osu! |
| 3161 | I tried hard! |
| 3162 | I blew it!Osu |
| 3163 | So sorry / I'm clumsy! |
| 3164 | Hard at end / Osu! |
| 3165 | Captain! / Heart races / Osu |
| 3166 | Failed! / No go |
| 3167 | Too weak / My apologies! |
| 3168 | Tasty! / Thank you! |
| 3169 | Hungry / Ate the plate / Osu |
| 3170 | So juicy! / So delicious!! |
| 3171 | So sweet / So tasty! |
| 3172 | Ugh... / Tastes awful! |
| 3173 | Not so tasty |
| 3174 | A shower / relieves stress! |
| 3175 | It felt / so good! / Osu! Osu! |
| 3176 | Done! / Captain! |
| 3177 | I'll try again! |
| 3178 | Apologies / Captain! |
| 3179 | Captain! / I'm a lousy bot / Sorry, no help! |
| 3180 | All out / With zeal! |
| 3181 | Captain! / Training / feels good |
| 3182 | Captain / Failed |
| 3183 | Captain! / Sorry, sir / Lacked zeal |
| 3184 | I can still / eat more! |
| 3185 | Whew... / I'm full |
| 3186 | So good / Got goosebumps |
| 3187 | It was tasty / sir! |
| 3188 | This food / I hate! / Chilling... |
| 3189 | This food / isn't for me |
| 3190 | Showers / are superb! |
| 3191 | After showers / I oil up! |
| 3192 | NAME / Wow! |
| 3193 | Bro, praise / NAME! |
| 3194 | Still little / Sorry, mel |
| 3195 | Mel? / No? |
| 3196 | NAME / Did well! |
| 3197 | Bro, you love / NAME! |
| 3198 | Mel... / Sorry |
| 3199 | NAME / Upset! |
| 3200 | NAME / Ate it all! |
| 3201 | Thanks, mel |
| 3202 | NAME... / So good I melt! |
| 3203 | Tasty! / Smiles,mel |
| 3204 | M-m-mel!? / Nasty, mel!! |
| 3205 | Mel mel / Not tasty |
| 3206 | NAME / Smooth! |
| 3207 | NAME / All clean! |
| 3208 | NAME! / Praise me / Praise me! |
| 3209 | I'm good? / Hehe! |
| 3210 | Bro... / I'm sorry |
| 3211 | Oops! / I failed! |
| 3212 | NAME / I tried hard! |
| 3213 | Great! / NAME / Tired! |
| 3214 | So what / So what / I failed, so? |
| 3215 | Your fault / Bro... |
| 3216 | NAME / I'm full! |
| 3217 | All gone / Fast, huh |
| 3218 | Delicious! / Want some, Bro? |
| 3219 | So fresh / Tasty |
| 3220 | NAME / Hate this, Bro! / You eat it! |
| 3221 | Not tasty / Boo! |
| 3222 | Bro! / Trying to peek?! |
| 3223 | Pretty, huh? / Heh |
| 3224 | I did it / Success |
| 3225 | I'm better! |
| 3226 | Not my fault! |
| 3227 | Oh man / Bad at chores |
| 3228 | Almost / gave up... |
| 3229 | Quite / tough! |
| 3230 | Won't get / strong! |
| 3231 | Oh, man / I messed up |
| 3232 | Power is / surging! |
| 3233 | Energized / Burp... |
| 3234 | Great broth / So tasty |
| 3235 | Pretty good / Want more! |
| 3236 | Never ate / worse food |
| 3237 | Not that good |
| 3238 | Yikes! / Showers aren't / for me! |
| 3239 | Whew / It's over! |
| 3240 | See that? / A genius? |
| 3241 | I can do it / if I try, see |
| 3242 | Huh? Huh? / How odd! |
| 3243 | What went wrong |
| 3244 | Quota met / Hooray |
| 3245 | In the end / I get it done |
| 3246 | Can't do it! |
| 3247 | Go easy / on me... |
| 3248 | All eaten / What next? |
| 3249 | The taste / is plain |
| 3250 | Wow! / This is great |
| 3251 | Quite tasty / But thirsty / Drinks bar? |
| 3252 | Ugh! Yuck / It stinks! |
| 3253 | Good food / is rare... |
| 3254 | Showers / feel great |
| 3255 | I now enjoy / my showers! |
| 3256 | A success |
| 3257 | I tried / my hardest! |
| 3258 | Things / don't go well |
| 3259 | Did I fail? |
| 3260 | This isn't / my real power! |
| 3261 | Must train more! |
| 3262 | Sorry! |
| 3263 | What caused / this failure? |
| 3264 | Fresh food / is good for you! |
| 3265 | Good food / is good to all |
| 3266 | Who knew / such good food / exists! |
| 3267 | Aromatic / Tasty! |
| 3268 | Hmm...! / This food / Er... |
| 3269 | Hmm... / The world has / many foods... |
| 3270 | Soothes my body / and my soul! |
| 3271 | Why not / try one too? |
| 3272 | Done, eh / Happy now? |
| 3273 | A walk / is easier |
| 3274 | Hmmm? / Hard, eh |
| 3275 | No way! / Not me! |
| 3276 | It's / easy, eh! |
| 3277 | So tired / Won't move |
| 3278 | Hmm... / Need exercise |
| 3279 | Told ya / I can't, eh |
| 3280 | Full, eh / Need a nap... |
| 3281 | Cough! / Ate too fast / Got stuck, eh |
| 3282 | Th-this is / tasty, eh! |
| 3283 | So tasty / So tasty! |
| 3284 | Blech! / Awful, eh!! |
| 3285 | Yuck / Anything / better, eh |
| 3286 | Dry well / No rust! |
| 3287 | Showers / are a bother |
| 3288 | NAME / Loves chores! |
| 3289 | Yay! Yay! / Yaaaay! |
| 3290 | Sorry! |
| 3291 | No go! No go / No good |
| 3292 | I tried! / I tried hard! |
| 3293 | Nice outdoors / Huh? Indoors? |
| 3294 | NAME / Hates training! |
| 3295 | So tough! / So tough! |
| 3296 | Thanks / Thanks again! / La la la! |
| 3297 | I ate it! |
| 3298 | NAME / Loves this food! |
| 3299 | Longed / for this |
| 3300 | Yuck! / NAME / I feel sick! |
| 3301 | Not so good |
| 3302 | Shampoo / Eyes hurt / Eyes hurt |
| 3303 | Dirt / all gone! |
| 3304 | Chores / are easy! |
| 3305 | Finally done |
| 3306 | Fail, moshi? |
| 3307 | Moshi? / Moshi?? |
| 3308 | Muscles / ache... |
| 3309 | Huff... / I hurt, eh |
| 3310 | Ain't ya / overworking me? |
| 3311 | Why ya / hurting me / so, moshi? |
| 3312 | Free food / I'm glad |
| 3313 | Next dish / please, eh |
| 3314 | So tasty / I'm trembling! |
| 3315 | Moshi? / Tomorrow too / Same food |
| 3316 | Awful food / What if I get / a bellyache? |
| 3317 | Odd taste / moshi |
| 3318 | So warm / I could melt! |
| 3319 | Moshi? / No sauna? |
