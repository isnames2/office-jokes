"""Write one office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library only. The joke is written as-is, exactly one line,
no trailing newline, so the output is byte-identical on every run.

The joke: a raise request, a promise to "look into it", and three managers
later it is still pending -- the turn lands at the end.
"""

import os
from pathlib import Path

JOKE = "I asked for a raise and my boss said he'd look into it. That was three managers ago."

out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
