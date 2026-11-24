# Say What Actually Broke

One line of software error copy, at most 200 characters, that tells the
user the brutal truth about what went wrong and makes them laugh on the way.

The line:

> Save failed: the disk is full of error logs about the disk being full. Delete one and try again.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`/output/entry.txt`. Nothing else: no network, no input, deterministic —
every run writes the same bytes.

## Why this line

- **Names the real failure in plain words:** the save failed because the
  disk is full — and the cause is named too (error logs), with the next step
  spelled out (delete one, try again).
- **Funny on a single read:** the disk is full *of the logs apologising
  for the disk being full* — the recursive irony every SRE has lived through.
- **Shippable:** dry, no profanity, no shock value; a team could paste it
  into a real error dialog tomorrow.

## License

MIT — see `LICENSE`.
