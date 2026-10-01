# Mindustry Archipelago Setup Guide

## Required software

- The modified Mindustry client from the [Mindustry Archipelago client releases](https://github.com/JohnMahglass/Mindustry-Archipelago-Randomizer/releases). Use its Linux or Windows build, not an unmodified Mindustry installation.
- A Mindustry APWorld version compatible with that client. The client release notes state the required version; download it from the [Mindustry APWorld releases](https://github.com/JohnMahglass/Archipelago-Mindustry/releases).
- An Archipelago room generated with that APWorld. The room host will give you its address, port, slot name, and any password.

## Create a local room

Install the Mindustry APWorld in Archipelago, then place a player options YAML in Archipelago's `Players` directory. The APWorld release provides `MindustryDefaultOptions.yaml`; copy it to `Players/Mindustry.yaml` and edit its `name:` field and options before generating. Run Archipelago's generator and start `ArchipelagoServer` with the generated room. For general room generation and hosting instructions, see the [Archipelago setup guide](https://archipelago.gg/tutorial/Archipelago/setup_en).

For the connection example below, set `name: Mindustry`. Use the name in your YAML when connecting the client. Keep a generated room and its server save together if you intend to resume it later.

## Connect and play

Launch the modified Mindustry client and connect **before opening Campaign**. In **Settings → Archipelago**, enter the server address, port, slot name, and password if required. You can also open the in-game chat and enter a command such as `/connect localhost:38281 Mindustry` for a local room with the default port and slot name. Use the room host's values for a remote room.

Most research nodes are Archipelago location checks. Researching one sends its check to the server, which can deliver items that unlock blocks. A visible node may still require resources you cannot produce yet; look for other accessible research checks, sector checks if enabled, and progression items. If every available check seems blocked, keep the room, seed, and player options so the situation can be reproduced when reporting it.

## Start a fresh campaign

The game client and the Archipelago server retain different parts of your progress. **Settings → Archipelago → Reset AP data** clears the client's AP progress and game data, but it does not erase the server's checked locations or item history. Reconnecting to the same saved room can deliver the old items again.

For a fresh local game, select **Reset AP data** in Mindustry and let the game exit. Stop the old local server, generate a **new room** with new server save data, and host it. Then restart Mindustry and connect to the new room before opening Campaign. Keep a backup of the previous room and server save if you might resume that game. For a remotely hosted room, ask its host for a new room; resetting only your client cannot reset the server.
