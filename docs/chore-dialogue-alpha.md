# Chore dialogue alpha

This cumulative partial English draft adds **195 native dialogue records**
(3342–3536): fifteen thirteen-line voices speaking during ongoing chores.
Coverage reaches **3,646 native records, 832 UI strings, 299 choices and three
bitmap captions**. All preceding 3,451 catalog entries are identical.

## Wording and controls

Chatter covers cleaning/dust/vases, fishing/weather/sea life, massage, computer
repair and Pearlton stoking. Voices retain their different addresses and compact
pomyu/pyu, zari, mel, osu and moshi quirks, refined and military tones, a tough
voice, childish talk, rural diction, singing and idle grumbling. English is a
condensed draft constrained by each original allocation and sixteen-cell line.

The sunset/stars, sunburn/UV/air-con, sea-air rust, sharks/flying fish/dolphins,
blisters, fumes/smoke/soot, masks, shoulders/backache, requesting tea/pocket money,
and reluctance to work remain where the budgets allow. The shooting-star wish
to marry Bro, grandfather jokes and UFO abducting a cow remain source humor.
The military claim about Mu and a fish school 2,000m deep, slow typing of
Y-U-U-K-I / S-U-T-E-K-I, and Magi System error are text jokes, not new events.
Smelt retains the wakasagi fishing reference. Pearlton remains ship fuel.

All 195 source control streams are exact: original portraits, resets, line/page
commands and arguments remain in order. Three 200B:0007 bot-name insertions at
3435, 3445 and 3456 stay dynamic, reserving eleven cells. Their translations fit
without adding line breaks. There are no new page exceptions, newline opt-ins,
relocations or codec/engine changes. No item effects, quotas, chore results,
inventories, map flags or save mechanics are changed.

All fifteen fixed grids remain byte-for-byte identical, with full original
descriptor sizes. All 130 stored labels in 36 donors, their original relocated
source slots, Berry and saved nicknames are intact. Every preceding active byte
and eight-byte descriptor matches minigame-guide-alpha.

## Runtime coverage

The exact final ROM cold-boots and loads the reference file A. Recorded file,
wake, pause and Merlin profile screens retain day 2, 500G, player name and saved
Japanese Merlin nickname, original stats, Charm and Fire v1. Reference/default/
isolated EEPROMs retain their exact hash. No in-game save is attempted and no
savestate from this or an older ROM is loaded or created.

New ongoing-chore triggers were not reached. Source/control/budget/name-width and
actual-ROM-byte checks do not establish gameplay coverage of the 195 branches.
These and earlier minigame/pest/reaction/mood/bedtime/food/name/newline/donor/
regional scenes, five anchored pages, Parts frame and VS/Transfer Pak still need
gameplay checks. Evidence is in local/chore-dialogue-evidence.

Final MD5: `402853357DE447A4190C27EF71CFFE82`.
SHA-256: `4cddb0e49c8b71cd82f3873aed39d3aad19f76d8c37f01fb5c50cf7b877cb248`.
The 32 MiB ROM keeps CIC-6102 CRC1/CRC2 `FFA89600 C278C65F`.

## Build and recovery

```sh
python -m tools.build_story local/original.z64 \
  --menu translation/battle-moves-menu.json --story translation/chore-dialogue-text.json \
  --choices translation/story-choices.json --layout translation/interface-layout.json \
  --graphics translation/interface-graphics.json --update-checksum --validate-moves \
  --output local/chore-dialogue-alpha.z64 --patch local/chore-dialogue-alpha.bps
```

Apply the release BPS directly to the exact Japanese original, without stacking
patches. Floating IPS independently reproduces the target and read-only chksum64
agrees with the header. All **134 tests** pass in source and clean restoration.
Checks verify the exact 195 additions, all source controls and name arguments,
all preceding entries/active bytes/descriptors and every occupied label range.

The AES-256 archive uses two verified ciphertext parts and the existing passphrase,
which stays outside Git. Reassembly reproduces the ciphertext and decryption
reproduces the packaged ZIP. Clean restoration checks **840 payload files**,
source revision, ROM/BPS/save/evidence hashes, executable modes, library symlink
and the exact-ROM 16Kbit EEPROM profile. See backups/README.md and RESTORE.md for
exact join/decrypt commands; both parts are required.

Next: native equipment labels from **3537**. Reuse existing part/move terminology,
skip previously translated IDs such as Charm 3604, and preserve all occupied
storage when deriving free intervals. Do not overwrite earlier labels casually.

## New dialogue

Slash separates visible lines; NAME is the unchanged dynamic bot name.

| ID | English |
| --- | --- |
| 3342 | Cleaning / is tough... |
| 3343 | Vase... / Move! |
| 3344 | Warm / Feels nice |
| 3345 | Nice stars |
| 3346 | Orange sea... |
| 3347 | It's OK! / I'll catch it |
| 3348 | Wanna swim |
| 3349 | How's it / Feel good? |
| 3350 | I'm trying |
| 3351 | This... / That... / Hmm |
| 3352 | Can I fix it? |
| 3353 | So heavy / So hot |
| 3354 | Pearlton / smells nice! |
| 3355 | Huff! Huff! / Hah! Yah!! |
| 3356 | Achoo!! / Cough cough / Inhaled dust! |
| 3357 | Sunny! / Feels great! |
| 3358 | Hot... / Sultry night! |
| 3359 | Cheap / rod, eh? |
| 3360 | No fish / today, huh |
| 3361 | Sh-shark / Shark, Boss! |
| 3362 | Tap! Tap! / Tap away! / Massage is power |
| 3363 | Hi-ya! Hah! / Hi-ya! Hah! |
| 3364 | This stuff / A cinch |
| 3365 | Aaaah! / Tatatatata! / Wachaaa! |
| 3366 | Whew / So hot / Like a sauna |
| 3367 | Toryaaaa!! / Uryaaaa!! / Oryaaaa!! |
| 3368 | Don't stare / Help me! |
| 3369 | I... / hate dust! / How tiresome |
| 3370 | Sunlight / harms my skin / Oh! UV rays |
| 3371 | Hot... / Nice indoors / Air-con! |
| 3372 | Lovely sunset / Draws me in |
| 3373 | It's / cooler now... |
| 3374 | The vast sea! |
| 3375 | To serve / is lovely |
| 3376 | Sir!! / No touching! |
| 3377 | I want / piano lessons |
| 3378 | I'm bad / at computers! |
| 3379 | Me doing this?! |
| 3380 | This fire / Cool it down / So sweaty! |
| 3381 | Pomyu pomyu / Pomyu pomyu |
| 3382 | Fun, pomyu! |
| 3383 | Sunny, pomyu! |
| 3384 | So dark! / Scary, pyu |
| 3385 | Pomyu! / I want fish |
| 3386 | Pomyu... / No bites |
| 3387 | So high / Scary, pyu |
| 3388 | Gramps! Gramps / Pomyu pomyu |
| 3389 | Knead, tap / Fun, pomyu! |
| 3390 | Beep, pyu / Beep, pyu |
| 3391 | Pomyu? / Pomyumyu? |
| 3392 | Heavy / Heavy pyu |
| 3393 | Pomyu... |
| 3394 | Zari? / Dust here / too... |
| 3395 | Zari zari / Dirty room! |
| 3396 | Tasty fish / I want! |
| 3397 | Fish, zari / not Pearlton |
| 3398 | Grill it / Eat it, zari |
| 3399 | No fish / Not one, zari |
| 3400 | Pearlton / is afloat! |
| 3401 | Tap! Zari! / Stress relief |
| 3402 | Eat / Zari punch! |
| 3403 | Mad, zari! |
| 3404 | Computer runs / slowly, zari |
| 3405 | Zari zari / So tough |
| 3406 | Palm's / blistered! |
| 3407 | Tap, tap! / More dust! Osu! |
| 3408 | Achoo! / Achoo! / Dusty, Captain! |
| 3409 | Got a tan / Great! |
| 3410 | Sorry, sir! / The fish escaped |
| 3411 | Lots of / fish for us! / Osu! |
| 3412 | Sky's / looking grim |
| 3413 | Outside / is great / Osu! |
| 3414 | Doc! / Relax some more |
| 3415 | Doc! / Feel good |
| 3416 | Tough! / Very tough! |
| 3417 | ................ / ................ / Um... It's hard |
| 3418 | Pretty tough |
| 3419 | In soot / I'll try! / Osu! |
| 3420 | Clean / with gusto! |
| 3421 | C-Captain! / Shoulder cramp / Oww! |
| 3422 | Fishing / is so difficult |
| 3423 | Captain / I'm sleepy! |
| 3424 | Sunset glare / Eyes hurt! |
| 3425 | Captain! / Just spotted / Mu continent! |
| 3426 | 2,000m deep / Huge school / of fish, sir |
| 3427 | Tap! Tap! / Doc, sir? / Feel good? |
| 3428 | Haaaaaah!! / I'm sending chi / Quiet, please! |
| 3429 | No idea! / Captain! |
| 3430 | Y-U-U-K-I / S-U-T-E-K-I / Sorry, slow keys |
| 3431 | No Pearlton / It's the end! / Take care, sir! |
| 3432 | Captain / Danger! / Stay back! |
| 3433 | Dust, yuck |
| 3434 | Mel! / All polished |
| 3435 | Gulls! / NAME too / wants to fly! |
| 3436 | Mel mel / So lonely! |
| 3437 | Fishies / Come out, mel |
| 3438 | Fishies! / Where, mel? |
| 3439 | Mel mel? / Flying fish! |
| 3440 | Grandpa / Feel good? |
| 3441 | Mel... / My arms tire |
| 3442 | What? / So many buttons |
| 3443 | ??? / Dunno, mel |
| 3444 | Heave! Ho! |
| 3445 | NAME / Tired... |
| 3446 | Bro! / Move! / I'm cleaning |
| 3447 | Mind the vase / Easy... easy |
| 3448 | Hmm / Tropical! |
| 3449 | Falling star! / Let me marry / Bro... |
| 3450 | No fish / anywhere |
| 3451 | Looks / like rain! |
| 3452 | A dolphin / ride / far away! |
| 3453 | Gramps' back / Broad, nice! |
| 3454 | Gramps! / No farting! |
| 3455 | This PC / is a junker! |
| 3456 | NAME / Wanna play, Bro? |
| 3457 | Why so / heavy? / What's Pearlton? |
| 3458 | Bro / Help me too! |
| 3459 | So filthy... |
| 3460 | I want / other training |
| 3461 | Hot! / Heatstroke / I'll faint |
| 3462 | No fish / anywhere! |
| 3463 | Glary sunset! |
| 3464 | Wind's stronger |
| 3465 | Salty air / will rust me! |
| 3466 | Doc is stiff! |
| 3467 | Doc's back / is hunched |
| 3468 | Whoa! / Too hard / I'm dizzy! |
| 3469 | Can't / get it... |
| 3470 | Cough! / Smoke hurts eyes |
| 3471 | Pearlton / smells bad |
| 3472 | Dusty! / Need a mask... |
| 3473 | Cleaning? Ugh! / I may quit... |
| 3474 | So hooot / So hooot |
| 3475 | I'd fish / with a bang / Bam! |
| 3476 | Zzz... Snore... / Oh, no! / I nodded off! |
| 3477 | Sea's so vast / So big / Yahoooo! |
| 3478 | Fish with me |
| 3479 | Doc! / More / pocket money! |
| 3480 | Doc! / You smell oily / Take a shower? |
| 3481 | This much / A cinch! |
| 3482 | Wing it! / It'll fix! Hehe |
| 3483 | Chores / this hard? No! |
| 3484 | This chore / News to me! |
| 3485 | Dust flies / Where to...? |
| 3486 | Being watched / I'm nervous! |
| 3487 | Blue sky, sea / Feels good! |
| 3488 | I'll catch / fine fish / Just wait |
| 3489 | I vow / to catch a / huge fish! |
| 3490 | I don't / mind fishing |
| 3491 | Always / peace is best / Do you agree? |
| 3492 | How's it / Shoulders stiff / Just call me |
| 3493 | Massage is / my specialty / Feels good, eh? |
| 3494 | Runs poorly / Will it fix? / Let's try! |
| 3495 | A virus?! / Magi System?? / What's that? |
| 3496 | Hard work / Trust me! |
| 3497 | We need / Pearlton, so / handle with care |
| 3498 | Dust! / Nose tickles |
| 3499 | I like / it dirty! |
| 3500 | Bright sun, eh |
| 3501 | I saw a UFO! / It came down / and took a cow |
| 3502 | Humid! / Feels awful |
| 3503 | Rather / fish smelt |
| 3504 | Fish are free |
| 3505 | Shoulders / so stiff |
| 3506 | Nice, eh? / Nice, eh? / I try, eh? |
| 3507 | This chore / isn't / fun at all |
| 3508 | A robot / doesn't know / all about PCs |
| 3509 | So heavy! / So heavy! |
| 3510 | Keep doing this / My back'll ache |
| 3511 | Flap flap / Flap flap |
| 3512 | Make it / so clean! |
| 3513 | So hot! / So hot! |
| 3514 | Sleepy / So sleepy! |
| 3515 | Fish! / So many! / Why no catch? |
| 3516 | No fish / will bite |
| 3517 | Outside / Great! |
| 3518 | Tap tap tap / Tap tap tap / Nice, eh |
| 3519 | Adults / Why so stiff? |
| 3520 | Done / in a flash! / Clack clack |
| 3521 | Oh! / I goofed |
| 3522 | Heave! Ho! / Heave! Ho! |
| 3523 | I work / my hardest! |
| 3524 | Dull job / moshi? |
| 3525 | You / no work? / Moshi? |
| 3526 | Lend me / a straw hat |
| 3527 | Ya fish / too, moshi? |
| 3528 | No bites / Bored, eh! |
| 3529 | Cheap rod / can't catch fish |
| 3530 | Zzz... / Zzz... |
| 3531 | For Gramps / some tea / please |
| 3532 | Moshi? / Who rubs / me, then |
| 3533 | Break a PC? / Not my / fault, moshi! |
| 3534 | So difficult / Head in knots! |
| 3535 | Sweat drips! |
| 3536 | Wipe / my sweat / please |
