# ADR 0002 - Relative path handling (know technical debt)

**Status:** Accepted temporarily - pending improvement
**Date:** 31/07/2026

## Context
Currently the program runs using "../data/equipos.json" as relative path, dependent on "os.getcwd()". This works as long as the program is always executed from the src/ folder, but could fail if executed from another location.

## Decision
Simple relative paths will be maintained for now, as the project is in an early stage (Module 2), prioritizing functionality rather than solving this robustness detail.

## Consequences
-Advantage: allows for faster progress at this early stage, without investing time in a more complex solution that isn't yet necessary.
-Risk/trade-off: the program could fail silently if executed from a location other than the expected one; particularly risky scenario if it ever reaches a real client.
-Pending future improvement: resolve paths using `__file__` (the location of the code file itself) instead of `os.getcwd()` (the directory from which it is executed) so that it works regardless of where it is run, before considering the CMMS ready for third-party use.