# BCCWJ_EyeTrack_FORMAL_BA_H1_FROM_B05_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_BA_H1_FROM_B05`; Planned project name: `BCCWJ_EyeTrack_FORMAL_BA_H1_FROM_B05_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: recovery; Condition: BA; Half: 1; Articles: B05.
- Import: `02_DESIGN_TABLES/order02_BA_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `8309de64e5899fc61bb291740919cb1bf2e37f90d14cc85a8589181b681dbd8d`.
- Groups: 3; article events: 3; total image presentations including standalone instructions: 6 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `RECOVERY_00_RECALIBRATION_INTRO` | `RECOVERY_00_recalibration_intro_JA` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_RECOVERY_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `RECOVERY_01_CONTINUE` | `RECOVERY_01_continue_JA` | INSTRUCTION_SPACE |
| 4 | group | `G22_F05_B05_FIX` | `FIXATION_CHECK_F05_B05` | FIX |
| 5 | group | `G23_F05_B05_READ` | `READ_TEMPLATE_F05_B05` | READ |
| 6 | group | `G24_F05_B05_QUESTION` | `QUESTION_TEMPLATE_F05_B05` | QUESTION |
| 7 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G22_F05_B05_FIX

- Internal Stimulus: `FIXATION_CHECK_F05_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 43 | `O02_BA_E042` | `FIX_B05` | `FIXATION_BG_1920x1080_WHITE` |

### G23_F05_B05_READ

- Internal Stimulus: `READ_TEMPLATE_F05_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 44 | `O02_BA_E043` | `B_21` | `R_B_21_space0` |

### G24_F05_B05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F05_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 45 | `O02_BA_E044` | `Q16` | `Q_16_after_B_21` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
