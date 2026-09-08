# BCCWJ_EyeTrack_FORMAL_AB_H2_FROM_B05_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_AB_H2_FROM_B05`; Planned project name: `BCCWJ_EyeTrack_FORMAL_AB_H2_FROM_B05_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: recovery; Condition: AB; Half: 2; Articles: B05.
- Import: `02_DESIGN_TABLES/order01_AB_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `91a1d592909a01c2d0c7c2d9ccf0fc24bab373f86c300be0b3957d83391ab1f2`.
- Groups: 3; article events: 3; total image presentations including standalone instructions: 6 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `RECOVERY_00_RECALIBRATION_INTRO` | `RECOVERY_00_recalibration_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_RECOVERY_H2` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `RECOVERY_01_CONTINUE` | `RECOVERY_01_continue_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G37_F10_B05_FIX` | `FIXATION_CHECK_F10_B05` | FIX |
| 5 | group | `G38_F10_B05_READ` | `READ_TEMPLATE_F10_B05` | READ |
| 6 | group | `G39_F10_B05_QUESTION` | `QUESTION_TEMPLATE_F10_B05` | QUESTION |
| 7 | image_stimulus | `FORMAL_05_END` | `FORMAL_05_end_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G37_F10_B05_FIX

- Internal Stimulus: `FIXATION_CHECK_F10_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 72 | `O01_AB_E071` | `FIX_B05` | `FIXATION_BG_1920x1080_WHITE` |

### G38_F10_B05_READ

- Internal Stimulus: `READ_TEMPLATE_F10_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 73 | `O01_AB_E072` | `B_21` | `R_B_21_space0` |

### G39_F10_B05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F10_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 74 | `O01_AB_E073` | `Q16` | `Q_16_after_B_21` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
