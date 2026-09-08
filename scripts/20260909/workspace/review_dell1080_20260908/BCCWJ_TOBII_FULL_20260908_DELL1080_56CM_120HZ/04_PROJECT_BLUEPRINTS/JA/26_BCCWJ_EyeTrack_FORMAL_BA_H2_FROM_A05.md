# BCCWJ_EyeTrack_FORMAL_BA_H2_FROM_A05_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_BA_H2_FROM_A05`; Planned project name: `BCCWJ_EyeTrack_FORMAL_BA_H2_FROM_A05_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: recovery; Condition: BA; Half: 2; Articles: A05.
- Import: `02_DESIGN_TABLES/order02_BA_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `8309de64e5899fc61bb291740919cb1bf2e37f90d14cc85a8589181b681dbd8d`.
- Groups: 3; article events: 4; total image presentations including standalone instructions: 7 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `RECOVERY_00_RECALIBRATION_INTRO` | `RECOVERY_00_recalibration_intro_JA` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_RECOVERY_H2` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `RECOVERY_01_CONTINUE` | `RECOVERY_01_continue_JA` | INSTRUCTION_SPACE |
| 4 | group | `G37_F10_A05_FIX` | `FIXATION_CHECK_F10_A05` | FIX |
| 5 | group | `G38_F10_A05_READ` | `READ_TEMPLATE_F10_A05` | READ |
| 6 | group | `G39_F10_A05_QUESTION` | `QUESTION_TEMPLATE_F10_A05` | QUESTION |
| 7 | image_stimulus | `FORMAL_05_END` | `FORMAL_05_end_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G37_F10_A05_FIX

- Internal Stimulus: `FIXATION_CHECK_F10_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 71 | `O02_BA_E070` | `FIX_A05` | `FIXATION_BG_1920x1080_WHITE` |

### G38_F10_A05_READ

- Internal Stimulus: `READ_TEMPLATE_F10_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 72 | `O02_BA_E071` | `A_18` | `R_A_18_space0` |
| 73 | `O02_BA_E072` | `A_19` | `R_A_19_space0` |

### G39_F10_A05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F10_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 74 | `O02_BA_E073` | `Q15` | `Q_15_after_A_19` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
