# BCCWJ_EyeTrack_PRACTICE_B_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_PRACTICE_B`; Planned project name: `BCCWJ_EyeTrack_PRACTICE_B_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: practice; Condition: CD; Half: None; Articles: B05 → A05 → B03.
- Import: `02_DESIGN_TABLES/order03_CD_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `c073fcceef41da0a377b876a9adefc77834e0043edc66119710f9ddc722839b1`.
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
| 12 | group | `G01_P01_B05_FIX` | `FIXATION_CHECK_P01_B05` | FIX |
| 13 | group | `G02_P01_B05_READ` | `READ_TEMPLATE_P01_B05` | READ |
| 14 | group | `G03_P01_B05_QUESTION` | `QUESTION_TEMPLATE_P01_B05` | QUESTION |
| 15 | group | `G04_P02_A05_FIX` | `FIXATION_CHECK_P02_A05` | FIX |
| 16 | group | `G05_P02_A05_READ` | `READ_TEMPLATE_P02_A05` | READ |
| 17 | group | `G06_P02_A05_QUESTION` | `QUESTION_TEMPLATE_P02_A05` | QUESTION |
| 18 | group | `G07_P03_B03_FIX` | `FIXATION_CHECK_P03_B03` | FIX |
| 19 | group | `G08_P03_B03_READ` | `READ_TEMPLATE_P03_B03` | READ |
| 20 | group | `G09_P03_B03_QUESTION` | `QUESTION_TEMPLATE_P03_B03` | QUESTION |
| 21 | image_stimulus | `PRACTICE_10_END` | `PRACTICE_10_end_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G01_P01_B05_FIX

- Internal Stimulus: `FIXATION_CHECK_P01_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 2 | `O03_CD_E001` | `FIX_B05` | `FIXATION_BG_1920x1080_WHITE` |

### G02_P01_B05_READ

- Internal Stimulus: `READ_TEMPLATE_P01_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 3 | `O03_CD_E002` | `B_21` | `R_B_21_space0` |

### G03_P01_B05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P01_B05`.
- Subset 1: `article_block=B05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 4 | `O03_CD_E003` | `Q16` | `Q_16_after_B_21` |

### G04_P02_A05_FIX

- Internal Stimulus: `FIXATION_CHECK_P02_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 5 | `O03_CD_E004` | `FIX_A05` | `FIXATION_BG_1920x1080_WHITE` |

### G05_P02_A05_READ

- Internal Stimulus: `READ_TEMPLATE_P02_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 6 | `O03_CD_E005` | `A_18` | `R_A_18_space0` |
| 7 | `O03_CD_E006` | `A_19` | `R_A_19_space0` |

### G06_P02_A05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P02_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 8 | `O03_CD_E007` | `Q15` | `Q_15_after_A_19` |

### G07_P03_B03_FIX

- Internal Stimulus: `FIXATION_CHECK_P03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 9 | `O03_CD_E008` | `FIX_B03` | `FIXATION_BG_1920x1080_WHITE` |

### G08_P03_B03_READ

- Internal Stimulus: `READ_TEMPLATE_P03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 10 | `O03_CD_E009` | `B_13` | `R_B_13_space0` |
| 11 | `O03_CD_E010` | `B_14` | `R_B_14_space0` |
| 12 | `O03_CD_E011` | `B_15` | `R_B_15_space0` |
| 13 | `O03_CD_E012` | `B_16` | `R_B_16_space0` |

### G09_P03_B03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_P03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 14 | `O03_CD_E013` | `Q10` | `Q_10_after_B_16` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
