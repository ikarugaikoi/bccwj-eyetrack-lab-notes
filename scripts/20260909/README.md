# BCCWJ Eye-Tracking Experiment: DELL1080 Automated Build

This repository documents the preparation, UI configuration, acceptance checks, and delivery of DELL1080 experiment projects in Tobii Pro Lab. It covers 84 projects: 42 with Chinese instructions and 42 with Japanese instructions. Each language set includes practice, main-experiment, and recovery projects that resume from a specified article.

The target configuration is a 1920×1080 participant display, a 560 mm distance from the midpoint between the eyes to the screen plane, and Tobii Pro Fusion at 120 Hz. See the specifications and approved deviation record for exact parameters.

## Directory structure

| Directory | Contents |
|---|---|
| workspace/dell1080_20260908 | Project building, scheduling, acceptance, diagnostics, and delivery scripts |
| workspace/local_automation | Host–Windows VM communication, UI executor, and shared functions |
| workspace/review_dell1080_20260908 | DELL material comparison, specifications, project blueprints, material assembly, and validation tools |

## Suggested reading order

Start with these files in workspace/dell1080_20260908:

| File | Purpose |
|---|---|
| BUILD_STATUS.md | Completion status and outstanding onsite acceptance |
| prepare.py | Prepare independent project copies, materials, and task queues from the build plan |
| queue.json | Sources, names, execution stages, and completion status of all 84 tasks |
| name_mapping.json | Mapping between planned project names, actual short names, languages, and paths |
| build.py | Configure resolution through the Pro Lab UI, update tables, verify bindings, handle language versions, save/reopen, and export |
| acceptance.py, ACCEPTED_DEVIATION.json | Identify and strictly limit the accepted DOT import-rounding differences |
| audit_full_backup.py | Check configuration, tables, and resources in full native project backups |
| prepare_japanese.py | Prepare Japanese project copies from accepted Chinese project backups |
| transfer_japanese.py | Copy Japanese projects through native file-selection dialogs and verify the copies |
| continue_pipeline.py | Coordinate batch building, the Japanese phase, and delivery |
| finalize_delivery.py | Collect 84 project backups, acceptance evidence, and the delivery index |
| complete_delivery.py | Validate the restore helper, verify restored projects, and complete packaging |
| Restore-Projects.ps1 | Verify the delivery package and extract native backups into separate directories |

This reading order explains the workflow. Execution order depends on the task stage and destination directory state; queue.json records task completion.

## Diagnostics, experiments, and targeted recovery

These files are also in workspace/dell1080_20260908:

| File | Purpose |
|---|---|
| PRECISION_INCIDENT.md | Design Table import-precision findings, investigation, and acceptance rationale |
| inspect_import_precision.py | Read-only inspection of imported-number formatting logic |
| import_compat.mjs | Compatibility experiment with numeric values stored as text |
| review_sample.py | Update a sample project's table and collect configuration diagnostics |
| prepare_geometry.py | Handle display resolution and container geometry in stages |
| recover_export_48.py | Recover from the specific export issue affecting project 48 |

Each script assumes a particular starting state. Some operate on projects or create files. Check the issue, target project, and execution stage before use.

## Specifications, blueprints, and materials

workspace/review_dell1080_20260908/compare_materials.py compares images, AOIs, workbooks, and specifications before and after migration to verify material consistency and configuration differences.

BCCWJ_TOBII_FULL_20260908_DELL1080_56CM_120HZ in the same directory contains:

- 03_SPEC: build parameters, display geometry, key-scoring rules, and recovery requirements.
- 04_PROJECT_BLUEPRINTS: Chinese/Japanese project blueprints, naming, stimulus sequences, and build plans.
- 05_QA: configuration checkers, acceptance checklists, and onsite record templates.
- 08_BUILD_SOURCE/assemble_package.py: assemble the DELL material package from baseline inputs, approved materials, and target configuration.
- 08_BUILD_SOURCE/finalize_release.py: verify material consistency, reassembly results, and ZIP integrity.
- 08_BUILD_SOURCE/baseline_inputs: baseline checkers required for material assembly.
- 08_BUILD_SOURCE/audit_inputs: display-geometry calculations, device-configuration readers, and native-project checkers.

## Shared execution tools

workspace/local_automation/README.md describes communication, UI operations, and shared functions.

recipes/production_queue.json records acceptance status and backup hashes for source projects used in DELL migration preparation. bridge/scope.json defines the projects, paths, and backups the executor may access. These records may therefore include source, temporary test, and destination projects.

## Prerequisites and acceptance scope

This bundle contains source code and configuration documentation, with masking placeholders in text and absolute paths. Supply the Windows environment, actual paths, authorized images, workbooks, source-project backups, and executor EXE separately. Native projects, recordings, screenshots, and per-project QA outputs are managed separately by the experiment project.

Static software acceptance checks configuration, bindings, resources, and backup consistency. See BUILD_STATUS.md for completion status. Onsite acceptance additionally requires screen-mapping, calibration-quality, gaze-trigger, and real-recording checks.

Use and distribution of the corpus, stimulus images, and other materials are subject to their respective licenses. Confirm redistribution permission before publishing any materials.

## Index and integrity files

| File | Purpose |
|---|---|
| FILE_LIST.txt | Relative paths of all files in the bundle |
| SOURCE_INDEX.json | File provenance, byte counts, and current SHA-256 hashes |
| DEPENDENCIES.json | Python import relationships and relevant environment package versions |
| MASKING_REPORT.json | Masking details, provenance, and verification scope |
| SHA256SUMS.txt | SHA-256 hashes of current bundle files, excluding itself |

Hashes support file-integrity checks. Validation of content and experimental results requires the corresponding evidence. Install dependencies and test execution on the actual computer when preparing the runtime environment.
