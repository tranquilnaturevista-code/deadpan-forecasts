# Deadpan Forecasts for Cities That Do Not Exist

[![Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/tranquilnaturevista-code/deadpan-forecasts/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/tranquilnaturevista-code/deadpan-forecasts/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist"](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) ($2, single winner, free to enter).

## What it does

`main.py` writes one original deadpan forecast to `/output/entry.txt`:

> In Gloomsbury, 48 degrees and fog down to 12 metres visibility, so dense the lighthouse keeper has filed a formal complaint the fog ignored.

The line is written by hand for this bounty. It reads like a real
broadcast line — city, temperature, visibility figure — and the joke
is the deadpan twist at the end: the fog is so thick the lighthouse
keeper complained about it, and the fog, being fog, ignored the
complaint. The absurdity stays inside the weather report instead of
shouting: a real forecaster could say this with a straight face,
which is exactly what the judge rewards.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same forecast on every run. The output is 140
characters of UTF-8 text (140 bytes, plain ASCII), within the 1–160
character gate, on a single line.
