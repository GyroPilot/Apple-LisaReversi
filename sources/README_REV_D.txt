Lisa Reversi 1.0 REV D -- 25-Sep-2026.  Tool 419309.  RELEASE BUILD.
From REV C, which passed every test on the FPGA and the 2/10.  NOT yet
compiled.

WHAT CHANGED SINCE REV C
  1. The folded last ply of the search now stops at the first candidate
     that reaches beta -- the alpha-beta cutoff the rest of the search
     always had.  Without it REV C looked at 2.8 x more positions than
     REV B and only halved the work; with it the position count matches
     REV B and the work is 3.9 x less than REV B (30 random positions,
     identical scores).  On the 2/10 the early-game move that took 8.0 s
     (2,960 positions) should now be about 3 s and ~1,000 positions; a
     mid-game move about 2 s.
  2. Version 1.0 REV D (GLOBALS, About).  No other change.

PRE-FLIGHT (done here)
  Free Pascal check clean; the REV D engine matched the REV B search on
  160 random positions (0 mismatches) and played 16 games at levels 1-4
  in both colours with no illegal move; braces MAIN 64/64, GLOBALS
  77/77; menus, alerts, globals unchanged from REV C.

FILES TO SEND (three) -- ALL THREE ARE THE SAME SIZE AS THE C FILES:
go by the timestamps and the REV D line on page 1.
    RVSMAIND.TEXT      37,888  ->  RVS/MAIN.TEXT     SAME SIZE as C
    RVSGLOBALSD.TEXT    9,216  ->  RVS/GLOBALS.TEXT  SAME SIZE
    RVSALERTSD.TEXT     6,144  ->  RVS/ALERTS.TEXT   SAME SIZE
UNCHANGED -- already on the Lisa, send only if missing (L RVS/=):
    RVSCOMPD / RVSLINKD / RVSMAKED / RVSINSTALLD .TEXT (comment line only)
    RVS/ICON.BIN (unchanged since REV A)

BUILD
  1. Office System: Save & Put Away Lisa Reversi (not Set Aside).  Do not
     trash the icon.  Empty the Wastebasket.
  2. Workshop:  R <RVS/MAKE
  3. Workshop:  R <RVS/INSTALL
  4. L RVS/= -> RVS.OBJ has today's time.  Restart the Office System.
     About must say "1.0 REV D".

TEST (2/10)
  1. About 1.0 REV D.
  2. Level 4, a move with about 35 discs on the board, stopwatch: expect
     about 2 s (REV B: 5.5-5.9 s in that phase).  Note the position
     count -- it should be back in the hundreds.
  3. One game at level 4 to the end; the longest endgame move.
  Then it is the release: floppy master on the FPGA (the tool alone --
  no LisaFileMover needed, nothing to copy), image LISA_REVERSI_1_0.dc42
  to me for the check, then GitHub, BBS, GlobalTalk, LisaList2.
