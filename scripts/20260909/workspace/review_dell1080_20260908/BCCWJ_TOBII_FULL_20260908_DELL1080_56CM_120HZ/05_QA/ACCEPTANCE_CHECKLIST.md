# Build and Material Acceptance

Record checks individually for all 42 Chinese and 42 Japanese projects. Check a box only after verification with actual evidence; blank boxes are pending. Record material checks, Windows project checks, and onsite acceptance separately.

This checklist applies to the complete material package and native-project delivery package. Obtain the listed XLSX files, PNGs, and runtime outputs separately. Check DOT rounding against workspace/dell1080_20260908/ACCEPTED_DEVIATION.json in the source bundle.

## Delivered materials

- [ ] Fully extracted; verify_package.py reports PASS; all four current XLSX files, 131 PNGs, and 84 blueprints are present.
- [ ] Import only _DELL1080 files from 02_DESIGN_TABLES; keep historical inputs under 08_BUILD_SOURCE out of imports.
- [ ] BUILD_PARAMETERS, blueprints, and Excel coordinates agree; media names and hashes match; use supplied images/tables without regenerating them on Windows.

## Static checks for each project

- [ ] Independent new output; correct condition, language, H1H2, and FROM starting article; complete planned-to-actual name mapping.
- [ ] Advanced Screen, 1920×1080; verify Group count, all template names, Subsets, event counts, and sequence against the blueprint.
- [ ] One template per Group; two Subsets; Set at recording start off; no extra Shuffle/Random/Repeat.
- [ ] Correct four-coordinate MAIN/DOT bindings; standalone instruction MAIN fixed at 1/1/0/0; Original throughout.
- [ ] Fixed Sources and dynamic media_name resolved, with no red unmatched bindings; white background beneath DOT; Use as AOI off.
- [ ] Every page: Time=None, minimum 100ms, Mouse/Look away/Media end/TTL/cursor disabled.
- [ ] FIX has no keys; only DOT uses Continuous300ms/Data loss reset34ms; MAIN has no Gaze.
- [ ] READ: Space only; QUESTION: both P/Q; KEY_CHECK: P-only or Q-only as specified; practice/H1/H2 endings: 7 only.
- [ ] Exactly one native calibration, between the correct instructions: 9 points, validation enabled, random order, Point, Timed, white background and black targets.
- [ ] All fixed instruction Sources in Japanese copies replaced according to the list; non-language settings unchanged; Chinese source projects still correct.
- [ ] Save → close → reopen; native-design export readable; read-only checker passes or explicitly reports unsupported checks.

## Runtime and onsite checks

- [ ] Complete ONSITE_CHECKLIST; each ordinary page remains unchanged for 5 seconds without input.
- [ ] Test true/false answers, P/Q key checks, and 7 endings; valid gaze leaving FIX resets dwell; Space/7 cannot bypass it.
- [ ] Correct 1920×1080 display at 100%; actual MAIN rectangle (0,0,1920,1080), DOT approximately (19.2,72,96,84).
- [ ] Fusion120 actually records at 120Hz; model, installation, and mapping agree with measurements; eye-to-screen-plane distance approximately 56cm, with actual measurement recorded.
- [ ] Inspect native calibration/validation for every segment; use null for unmeasured values; researcher confirms blocked-FIX and retry rules.
- [ ] Rehearse saving an interrupted recording → new FROM recording → recalibration → unread starting article; accurately flag previous exposure.
- [ ] End normally with 7 and save; verify complete, readable exports; record static, hardware, and recording status separately.

Organize evidence for Mac review using RETURN_PACKAGE.md and keep each collection session separate. Attach actual evidence to native/hardware acceptance status.
