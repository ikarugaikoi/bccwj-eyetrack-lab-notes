# Shared Execution Layer for DELL Automation

This directory provides file-based communication between the host and Windows VM, UI operations, native-configuration reading, and safety constraints for the DELL build. The build and acceptance workflow is in ../dell1080_20260908.

## Communication and execution

On the host, controller.py writes operation requests to bridge/requests. On Windows, guest_agent.py reads requests, performs permitted operations, and writes results to bridge/responses.

UI operations use observed windows and controls. The executor checks the project allowlist, window state, focus, and snapshot freshness. Native-configuration reading and backup restoration have additional path and hash constraints.

| File | Responsibility |
|---|---|
| controller.py | ROOT/BRIDGE paths, command request/response communication, and CLI debugging |
| guest_agent.py | Windows UI executor, window and snapshot checks, restricted configuration reading, and backup restoration |
| ui.py | Save UI snapshots, find unique controls, provide the UI client, and support interactive debugging |
| TobiiLocalAgent.spec | PyInstaller configuration for guest_agent.py |

## Shared functions

| File | Functions and purpose |
|---|---|
| production.py | descendants traverses control descendants; verify_container_ui checks container AOI and Original scaling; set_panel controls property panels; open_editor opens the stimulus editor |
| batch.py | exact_dialog finds a uniquely matching dialog |
| runner.py | write writes JSON; normalize normalizes names for comparison; read_design reads native-configuration snapshots returned by the executor |
| prolab.py | submit_dialog submits a dialog and verifies that it closes |

## Configuration and helpers

| File | Purpose |
|---|---|
| bridge/scope.json | Allowlist of project names, exact paths, and backups permitted for restoration |
| recipes/production_queue.json | Source-project acceptance status and backup hashes used by DELL prepare.py to validate migration inputs |
| PAUSE_LOCAL.cmd | Set the pause flag checked by controller.command before subsequent operations |
| RESUME_LOCAL.cmd | Clear the pause flag; the corresponding build task can then be started manually |
| requirements-lock.txt | Package-version record for the execution tools and their packaging |

Source, temporary test, and destination projects all participate in migration, so the allowlist contains several project categories. The allowlist limits access; the source queue validates migration inputs. queue.json and scheduling scripts in the DELL directory manage actual execution tasks.

## Runtime requirements

The Windows executor requires the appropriate UI automation dependencies, and the host and VM require an accessible shared directory. Absolute paths in this bundle are masking placeholders; configure actual authorized paths before use.

Supply the runtime environment, executor EXE, native projects, and experimental materials separately. Verify execution on the actual host and eye tracker. See the acceptance documents under ../review_dell1080_20260908 for onsite requirements.
