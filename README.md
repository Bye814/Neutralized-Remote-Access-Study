# Neutralized Remote Access Study

An inert, documented study edition derived from an experimental Python
agent/server project. **This repository is not a working remote-access tool.**
Function names and signatures are retained for discussion; every original
function implementation has been replaced with a fail-closed exception.

## What remains

- `agent.py`: an inert outline of the original agent functions.
- `server.py`: an inert outline of the original server functions and handler.
- `ANALYSIS_HE.md`: architecture, security findings, and neutralization notes.
- `tests/test_neutralization.py`: structural and runtime safety checks.

All original imports, connection configuration, shared keys, globals, startup
calls and functional bodies were removed. The handler no longer inherits from
an HTTP server handler. No binary, packager configuration, original source
copy, collected data or executable build instructions are included.

## Inspect and validate

Python 3.10+; no third-party dependencies.

```sh
python agent.py
python server.py
python -m unittest discover -s tests -v
```

Running either module only prints an inert-edition notice and exits. Calling
any retained function or handler method raises `RuntimeError`. Nothing is
listening on a port and no background task is started.

## Portfolio context

The original experiment used an agent polling a server for commands. It
included privacy-invasive and unsafe behavior; this edition documents those
findings without distributing the working implementation. See the Hebrew
analysis for the removed behaviors and limitations. The neutralization and
documentation were prepared with AI assistance; explain your own contribution
and what you understand accurately. This is not a claim of military admission
eligibility or production security certification.

## GitHub upload

Extract the ZIP into a new folder. Create an empty GitHub repository named
`Neutralized-Remote-Access-Study`. Use **Add file → Upload files** to upload
only this new folder's contents, including `.gitignore` and `tests`.
Do not upload the original agent/server files, EXE, tokens or personal logs.
The ZIP is a delivery package: extract it so GitHub can display the source.

No license has been selected; choose one before inviting reuse.
