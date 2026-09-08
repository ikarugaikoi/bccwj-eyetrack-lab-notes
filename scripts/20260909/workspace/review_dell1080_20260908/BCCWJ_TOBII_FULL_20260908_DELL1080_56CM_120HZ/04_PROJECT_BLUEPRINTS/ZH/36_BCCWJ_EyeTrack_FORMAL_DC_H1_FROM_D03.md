# BCCWJ_EyeTrack_FORMAL_DC_H1_FROM_D03_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_DC_H1_FROM_D03`; Planned project name: `BCCWJ_EyeTrack_FORMAL_DC_H1_FROM_D03_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: recovery; Condition: DC; Half: 1; Articles: D03 → D04 → D05.
- Import: `02_DESIGN_TABLES/order04_DC_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `752cce739dc8e6d779c180ed98dda5994d2b8b64cd00f8cce240d7a11c840b23`.
- Groups: 9; article events: 13; total image presentations including standalone instructions: 16 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `RECOVERY_00_RECALIBRATION_INTRO` | `RECOVERY_00_recalibration_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_RECOVERY_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `RECOVERY_01_CONTINUE` | `RECOVERY_01_continue_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G16_F03_D03_FIX` | `FIXATION_CHECK_F03_D03` | FIX |
| 5 | group | `G17_F03_D03_READ` | `READ_TEMPLATE_F03_D03` | READ |
| 6 | group | `G18_F03_D03_QUESTION` | `QUESTION_TEMPLATE_F03_D03` | QUESTION |
| 7 | group | `G19_F04_D04_FIX` | `FIXATION_CHECK_F04_D04` | FIX |
| 8 | group | `G20_F04_D04_READ` | `READ_TEMPLATE_F04_D04` | READ |
| 9 | group | `G21_F04_D04_QUESTION` | `QUESTION_TEMPLATE_F04_D04` | QUESTION |
| 10 | group | `G22_F05_D05_FIX` | `FIXATION_CHECK_F05_D05` | FIX |
| 11 | group | `G23_F05_D05_READ` | `READ_TEMPLATE_F05_D05` | READ |
| 12 | group | `G24_F05_D05_QUESTION` | `QUESTION_TEMPLATE_F05_D05` | QUESTION |
| 13 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G16_F03_D03_FIX

- Internal Stimulus: `FIXATION_CHECK_F03_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 27 | `O04_DC_E026` | `FIX_D03` | `FIXATION_BG_1920x1080_WHITE` |

### G17_F03_D03_READ

- Internal Stimulus: `READ_TEMPLATE_F03_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 28 | `O04_DC_E027` | `D_9` | `R_D_09_space0` |
| 29 | `O04_DC_E028` | `D_10` | `R_D_10_space0` |

### G18_F03_D03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F03_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 30 | `O04_DC_E029` | `Q12` | `Q_12_after_D_10` |

### G19_F04_D04_FIX

- Internal Stimulus: `FIXATION_CHECK_F04_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 31 | `O04_DC_E030` | `FIX_D04` | `FIXATION_BG_1920x1080_WHITE` |

### G20_F04_D04_READ

- Internal Stimulus: `READ_TEMPLATE_F04_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 32 | `O04_DC_E031` | `D_11` | `R_D_11_space0` |
| 33 | `O04_DC_E032` | `D_12` | `R_D_12_space0` |

### G21_F04_D04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F04_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 34 | `O04_DC_E033` | `Q19` | `Q_19_after_D_12` |

### G22_F05_D05_FIX

- Internal Stimulus: `FIXATION_CHECK_F05_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 35 | `O04_DC_E034` | `FIX_D05` | `FIXATION_BG_1920x1080_WHITE` |

### G23_F05_D05_READ

- Internal Stimulus: `READ_TEMPLATE_F05_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 36 | `O04_DC_E035` | `D_13` | `R_D_13_space0` |
| 37 | `O04_DC_E036` | `D_14` | `R_D_14_space0` |
| 38 | `O04_DC_E037` | `D_15` | `R_D_15_space0` |

### G24_F05_D05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F05_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 39 | `O04_DC_E038` | `Q20` | `Q_20_after_D_15` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
