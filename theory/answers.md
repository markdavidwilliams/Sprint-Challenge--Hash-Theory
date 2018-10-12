* Single regex that matches either of these:
  antelope rocks out
  antelopes rock out
<br>
`antelopes? rocks? out`

* Regex that matches either of goat, moat but not boat <br>
`[gm]oat`

*Regex that matches dates in YYYY-MM-DD format <br>
`[\d]{1,4}-[\d]{1,2}-[\d]{1,2}`

*Draw a state machine that corresponds with the follow regex: 
  ab*c+d?[ef]
  ```
  a ------- b ---- c ------ d ------- ef
  1         0+     1+      0/1        either one
  ```

* A lion can be sleeping, eating, hunting, or preening. Draw a state
  machine diagram for the lion and label the transition events that
  cause state transitions.

* The VT-100 terminal (console) outputs text to the screen as it
  receives it over the wire. One exception is that when it receives an
  ESC character (ASCII 27), it goes into a special mode where it looks
  for commands to change its behavior. For example:

      ESC[12;45f

  moves the cursor to line 12, column 45.

      ESC[1m

  changes the font to bold.

  * Come up with regexes for the two above sequences. The one to set the
    cursor position should accept any digits for the row and column. The
    bold sequence need only accept `1` (and is a trivial regex). (ESC is
    a single character which can be represented with `\e` in the regex.)

    `\e\[[0-9]+m?;?[0-9]*f*`


  * Draw a state machine diagram for a VT-100 that can consume regular character sequences as well as the two above ESC sequences.

    ```
    ESC[ ---- [0-9] ----- m --- ; ---- [0-9] ------ f
    1         1+        0/1    0+     0+         0+