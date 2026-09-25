# Lisa Reversi changelog

## 1.0 REV D -- 25 Sep 2026 -- RELEASE
- The folded last ply of the search stops at the first candidate that
  reaches beta (the cutoff the rest of the search always had). Same moves;
  the position count is back to REV B's and the work is 3.9 x less than
  REV B. Measured on the 2/10: level 4, 36 discs, 405 positions in 3.6 s
  (REV B: 494 positions in 5.9 s); longest exact-endgame move 4.7 s.
  Version 1.0.

## 0.3 REV C -- 25 Sep 2026 -- passed every test on the FPGA and the 2/10
- Search: the score is carried down the recursion and the last ply is
  folded into its parent (no board copy, no 64-cell scan per leaf);
  CountFlips returns the weight of the discs a move turns; empties with no
  opponent neighbour are skipped; range checking off in the search.
- Exact endgame: from 9 empties at level 4 and 8 at level 3 the search runs
  to the last disc.
- Switch Sides (Game menu, S): a new game with the Lisa opening as black.
- Undo resets the position count.

## 0.2 REV B -- 24 Sep 2026 -- all eight FPGA tests passed; 2/10 timed
- Panel key lines reflowed into three lines that fit the window; Keys
  alert one key per line. Level 4 measured on the 2/10: 494 positions in
  5.9 s (12 ms a position) -- the figure that drove REV C.

## 0.1 REV A -- 23 Sep 2026 -- compiled, installed and played first time on the 2/10
- First increment: 8 x 8 board in QuickDraw ovals, rules with passes and
  game over, cell cursor and mouse play, legal-move dots, unlimited undo,
  levels 1-4 (negamax, alpha-beta, corners-first ordering, positional
  weights, disc count in the last 12 empties), status panel, icon, tool
  419309. Lesson: the icon must be on the Workshop volume as RVS/ICON.BIN
  before MAKE runs, or the tool installs invisible.
