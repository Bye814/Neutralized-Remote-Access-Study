# Neutralized Remote Access Study

A learning project based on an experimental Python agent/server application developed with substantial AI assistance.

**This repository contains a disabled code outline, not a working remote-access tool.** I am currently reviewing the code and refreshing my Python fundamentals to better understand the original design.

## Repository contents

- `agent.py` — disabled outline of the original agent functions.
- `server.py` — disabled outline of the original server functions and request handler.
- `tests/test_neutralization.py` — structural and runtime checks for the disabled implementation.
- `.gitignore` — excludes common generated files, binaries, and local configuration.

## Neutralization

All original function bodies, network configuration, imports, and startup actions were removed. Retained functions raise `RuntimeError` when called.

The code does not connect to a server, listen on a port, capture keystrokes or screenshots, execute remote commands, or register itself to run at startup.

## Run and test

Requires Python 3.10 or later. No third-party packages are needed.

```sh
python agent.py
python server.py
python -m unittest discover -s tests -v
```

Running either source file prints a notice and exits. The tests check the neutralized code; they do not validate the original application's functionality or security.

## Learning goals

- Understand Python functions, classes, and control flow.
- Understand the original client/server architecture.
- Learn about authentication, consent, and privacy.
- Understand what the tests verify and their limitations.

## AI assistance

AI was used extensively in the original experiment. The neutralized edition, tests, and initial documentation were also prepared with AI assistance. This repository records an ongoing learning exercise rather than an independently implemented or fully understood system.
