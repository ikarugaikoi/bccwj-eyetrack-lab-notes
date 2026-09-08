# BCCWJ_EyeTrack_PRACTICE_A_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_PRACTICE_A`; Planned project name: `BCCWJ_EyeTrack_PRACTICE_A_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: practice; Condition: AB; Half: None; Articles: C05 → D03 → C01.
- Import: `02_DESIGN_TABLES/order01_AB_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `91a1d592909a01c2d0c7c2d9ccf0fc24bab373f86c300be0b3957d83391ab1f2`.
- Groups: 9; article events: 13; total image presentations including standalone instructions: 24 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `PRACTICE_00_WELCOME` | `PRACTICE_00_welcome_JA` | INSTRUCTION_SPACE |
| 2 | image_stimulus | `PRACTICE_01_READING_TASK` | `PRACTICE_01_reading_task_JA` | INSTRUCTION_SPACE |
| 3 | image_stimulus | `PRACTICE_02_QUESTION_KEYS_P_TRUE_Q_FALSE` | `PRACTICE_02_question_keys_P_TRUE_Q_FALSE_JA` | INSTRUCTION_SPACE |
| 4 | image_stimulus | `PRACTICE_03_KEY_CHECK_INTRO` | `PRACTICE_03_key_check_intro_JA` | INSTRUCTION_SPACE |
| 5 | image_stimulus | `PRACTICE_04_KEY_CHECK_P` | `PRACTICE_04_key_check_P_JA` | KEY_CHECK_P |
| 6 | image_stimulus | `PRACTICE_05_KEY_CHECK_Q` | `PRACTICE_05_key_check_Q_JA` | KEY_CHECK_Q |
| 7 | image_stimulus | `PRACTICE_06_PRACTICE_INTRO` | `PRACTICE_06_practice_intro_JA` | INSTRUCTION_SPACE |
| 8 | image_stimulus | `PRACTICE_07_CALIBRATION_INTRO` | `PRACTICE_07_calibration_intro_JA` | INSTRUCTION_SPACE |
| 9 | calibration | `CALIBRATION_PRACTICE` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 10 | image_stimulus | `PRACTICE_08_FIXATION_INTRO` | `PRACTICE_08_fixation_intro_JA` | INSTRUCTION_SPACE |
| 11 | image_stimulus | `PRACTICE_09_START` | `PRACTICE_09_start_JA` | INSTRUCTION_SPACE |
| 12 | group | `G01_P01_C05_FIX` | `FIXATION_CHECK_P01_C05` | FIX |
| 13 | group | `G02_P01_C05_READ` | `READ_TEMPLATE_P01_C05` | READ |
| 14 | group | `G03_P01_C05_QUESTION` | `QUESTION_TEMPLATE_P01_C05` | QUESTION |
| 15 | group | `G04_P02_D03_FIX` | `FIXATION_CHECK_P02_D03` | FIX |
| 16 | group | `G05_P02_D03_READ` | `READ_TEMPLATE_P02_D03` | READ |
| 17 | group | `G06_P02_D03_QUESTION` | `QUESTION_TEMPLATE_P02_D03` | QUESTION |
| 18 | group | `G07_P03_C01_FIX` | `FIXATION_CHECK_P03_C01` | FIX |
| 19 | group | `G08_P03_C01_READ` | `READ_TEMPLATE_P03_C01` | READ |
| 20 | group | `G09_P03_C01_QUESTION` | `QUESTION_TEMPLATE_P03_C01` | QUESTION |
| 21 | image_stimulus | `PRACTICE_10_END` | `PRACTICE_10_end_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G01_P01_C05_FIX

- Internal Stimulus: `FIXATION_CHECK_P01_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 2 | `O01_AB_E001` | `FIX_C05` | `FIXATION_BG_1920x1080_WHITE` |

### G02_P01_C05_READ

- Internal Stimulus: `READ_TEMPLATE_P01_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 3 | `O01_AB_E002` | `C_16` | `R_C_16_space0` |

### G03_P01_C05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P01_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 4 | `O01_AB_E003` | `Q18` | `Q_18_after_C_16` |

### G04_P02_D03_FIX

- Internal Stimulus: `FIXATION_CHECK_P02_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 5 | `O01_AB_E004` | `FIX_D03` | `FIXATION_BG_1920x1080_WHITE` |

### G05_P02_D03_READ

- Internal Stimulus: `READ_TEMPLATE_P02_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 6 | `O01_AB_E005` | `D_9` | `R_D_09_space0` |
| 7 | `O01_AB_E006` | `D_10` | `R_D_10_space0` |

### G06_P02_D03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P02_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 8 | `O01_AB_E007` | `Q12` | `Q_12_after_D_10` |

### G07_P03_C01_FIX

- Internal Stimulus: `FIXATION_CHECK_P03_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 9 | `O01_AB_E008` | `FIX_C01` | `FIXATION_BG_1920x1080_WHITE` |

### G08_P03_C01_READ

- Internal Stimulus: `READ_TEMPLATE_P03_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 10 | `O01_AB_E009` | `C_1` | `R_C_01_space0` |
| 11 | `O01_AB_E010` | `C_2` | `R_C_02_space0` |
| 12 | `O01_AB_E011` | `C_3` | `R_C_03_space0` |
| 13 | `O01_AB_E012` | `C_4` | `R_C_04_space0` |

### G09_P03_C01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P03_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 14 | `O01_AB_E013` | `Q03` | `Q_03_after_C_04` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
