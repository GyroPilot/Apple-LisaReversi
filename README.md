# Lisa Reversi

Reversi for the Apple Lisa Office System. An 8 x 8 board drawn with
QuickDraw, you as black against the Lisa as white (or the other way round),
four playing levels, legal-move dots, unlimited undo, and an exact endgame:
at the two harder levels the Lisa plays the last eight or nine moves
perfectly.

Tool number **419309** in the GyroPilot series (LISACom 419306, Atkinsonpoint
slide show 419307, Lisa Slide Puzzle 419308, LOS Installer 419310,
LisaFileMover 419311). Written in Lisa Pascal with the Workshop 3.0 toolchain
for Lisa Office System 3.1, and proven on a real Lisa 2/10.

## Status

**1.0 (REV D) -- released September 2026.** REV C passed the full test list
on the LisaFPGA and the 2/10; REV D adds the missing cutoff in the search's
last ply (same moves, a third of the work) and the 1.0 version. See
CHANGELOG.md.

## Playing

- Click a cell, or steer the cursor with the keypad (4 6 8 2, or J L I K)
  and press RETURN or SPACE. Dots mark your legal moves; D hides them.
- N starts a new game, U takes back your last move and the Lisa's reply
  (all the way back to the opening), S switches sides so the Lisa opens as
  black and you play white.
- Level 1 to 4 (keys 1-4 or the Level menu) is how many moves ahead the
  Lisa looks. Level 2 is the default. At levels 3 and 4 she also solves the
  end of the game exactly from eight or nine empties.
- The panel on the right shows the score, the level, the last moves, the
  cursor cell and how many positions the Lisa examined.
- Passes are automatic with a note; the game ends when neither side can
  move, with the score and a you-win / Lisa-wins / draw note.

Timing on a stock Lisa 2/10 (5 MHz), stopwatch, including the board
repaints: level 4 takes about 3 to 4 seconds a move in the middle game
(405 positions in 3.6 s in a 36-disc position) and up to about 5 seconds
in the exact endgame; levels 1 and 2 are instant.

## Where to get it

- The Apple Lisa BBS (port 1983): Floppy Images > Releases, LISA_REVERSI_1_0.dc42
- GlobalTalk: the LisaGaming Zone
- This repository: releases/LISA_REVERSI_1_0.dc42

**Installing from the floppy:** mount the image, open the floppy, drag or
duplicate Lisa Reversi onto your hard disk. Nothing else to copy.

## Layout

    sources/RVS-MAIN.TEXT      the program: board, rules, search, panel, events
    sources/RVS-GLOBALS.TEXT   unit RvsGlobals: constants, state, Filer handshake
    sources/RVS-ALERTS.TEXT    alerts + menus, Alert tool input
    sources/RVS-COMP.TEXT      Workshop exec: the two compiles
    sources/RVS-LINK.TEXT      Workshop exec: the link (RVS/RVS.OBJ)
    sources/RVS-MAKE.TEXT      Workshop exec: COMP, LINK, Filemgr copies, Alert tool
    sources/RVS-INSTALL.TEXT   Workshop exec: InstallTool alone (run after MAKE)
    sources/RVS*D.TEXT         the same seven, page-formatted for the Lisa (REV D)
    sources/fmt_text.py        REQUIRED for building: converts each source to the
                               Workshop paged .TEXT format (1024-byte header page,
                               no line straddling a 1024 boundary, bare CR line
                               endings). Raw text files will not compile.
    sources/README_REV_D.txt   the build and test notes that shipped with REV D
    icon/RVSICONA.BIN          the tool icon as a Lisa FONT file ({T419309}ICON)
    icon/lisaicon2.py          builds an ICON file from a 48x32 PNG (icon + mask)
    icon/rvs_icon_A.png        the icon artwork
    releases/LISA_REVERSI_1_0.dc42   the release floppy (DiskCopy 4.2, 400K)

## Building on the Lisa

Send the seven `RVS*D.TEXT` files to the Workshop volume as `RVS/MAIN.TEXT`,
`RVS/GLOBALS.TEXT`, `RVS/ALERTS.TEXT`, `RVS/COMP.TEXT`, `RVS/LINK.TEXT`,
`RVS/MAKE.TEXT` and `RVS/INSTALL.TEXT`, and the icon as `RVS/ICON.BIN`
(binary). The icon must carry that exact name before MAKE runs. In the
Office System, Save & Put Away the tool if it is running. Then in the
Workshop:

    R <RVS/MAKE        compile, link, place Obj and ICON, compile the phrases
    R <RVS/INSTALL     register the tool with the Office System

## How the Lisa plays

Negamax with alpha-beta, one to four plies. The score is carried down the
recursion rather than recomputed at each leaf: a move's value is the parent's
score plus the cell's weight plus twice the weight of the discs it turns, so
the last ply needs no board copy and no rescan. Evaluation is a positional
weight table (corners 100, X-squares -50, C-squares -20, other edges 10/5,
the ring inside the edge -2, the middle -1) until the last twelve empties,
then the disc difference. From nine empties (level 4) or eight (level 3)
the search runs to the last disc. Empty cells with no opponent disc beside
them are skipped, and range checking is off inside the search. Ties at the
root are broken at random, so the Lisa does not play the same game twice.

## Conventions

- Source file names are 8-character identifiers on the Lisa; the RVS- prefix
  keeps this tool's files apart from LMX- (LISACom), SLD- (Atkinsonpoint),
  PZL- (Slide Puzzle), INS- (LOS Installer) and LFU- (LisaFileMover) on a
  shared Workshop volume.
- Menus are matched to the mi* constants in GLOBALS by position, so MAIN,
  GLOBALS and ALERTS always ship together.
- Every source carries a REV header; page-formatted copies sent to the Lisa
  are named with the revision letter (for example RVSMAIND.TEXT).
- Tool icons are a Lisa FONT (chars 0..2, 48x32). Only the Obj file carries a
  Desktop label; ICON and PHRASE files do not.
- The window's live rectangle is re-read before every draw (SyncPort).

## Credits

T. O'Connor (bmwcyclist on LisaList2), 2026, with Claude. Window and event
skeleton cloned from Lisa Slide Puzzle 1.0. Thanks to the LisaList2
regulars for the tool number list and the Workshop lore.
