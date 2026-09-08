# BCCWJ_EyeTrack_FORMAL_CD_H2_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_CD_H2`; Planned project name: `BCCWJ_EyeTrack_FORMAL_CD_H2_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: CD; Half: 2; Articles: D01 → D02 → D03 → D04 → D05.
- Import: `02_DESIGN_TABLES/order03_CD_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `c073fcceef41da0a377b876a9adefc77834e0043edc66119710f9ddc722839b1`.
- Groups: 15; article events: 25; total image presentations including standalone instructions: 28 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_03_RECALIBRATION_INTRO` | `FORMAL_03_recalibration_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H2` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_04_SECOND_HALF_START` | `FORMAL_04_second_half_start_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G25_F06_D01_FIX` | `FIXATION_CHECK_F06_D01` | FIX |
| 5 | group | `G26_F06_D01_READ` | `READ_TEMPLATE_F06_D01` | READ |
| 6 | group | `G27_F06_D01_QUESTION` | `QUESTION_TEMPLATE_F06_D01` | QUESTION |
| 7 | group | `G28_F07_D02_FIX` | `FIXATION_CHECK_F07_D02` | FIX |
| 8 | group | `G29_F07_D02_READ` | `READ_TEMPLATE_F07_D02` | READ |
| 9 | group | `G30_F07_D02_QUESTION` | `QUESTION_TEMPLATE_F07_D02` | QUESTION |
| 10 | group | `G31_F08_D03_FIX` | `FIXATION_CHECK_F08_D03` | FIX |
| 11 | group | `G32_F08_D03_READ` | `READ_TEMPLATE_F08_D03` | READ |
| 12 | group | `G33_F08_D03_QUESTION` | `QUESTION_TEMPLATE_F08_D03` | QUESTION |
| 13 | group | `G34_F09_D04_FIX` | `FIXATION_CHECK_F09_D04` | FIX |
| 14 | group | `G35_F09_D04_READ` | `READ_TEMPLATE_F09_D04` | READ |
| 15 | group | `G36_F09_D04_QUESTION` | `QUESTION_TEMPLATE_F09_D04` | QUESTION |
| 16 | group | `G37_F10_D05_FIX` | `FIXATION_CHECK_F10_D05` | FIX |
| 17 | group | `G38_F10_D05_READ` | `READ_TEMPLATE_F10_D05` | READ |
| 18 | group | `G39_F10_D05_QUESTION` | `QUESTION_TEMPLATE_F10_D05` | QUESTION |
| 19 | image_stimulus | `FORMAL_05_END` | `FORMAL_05_end_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G25_F06_D01_FIX

- Internal Stimulus: `FIXATION_CHECK_F06_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 41 | `O03_CD_E040` | `FIX_D01` | `FIXATION_BG_1920x1080_WHITE` |

### G26_F06_D01_READ

- Internal Stimulus: `READ_TEMPLATE_F06_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 42 | `O03_CD_E041` | `D_1` | `R_D_01_space0` |
| 43 | `O03_CD_E042` | `D_2` | `R_D_02_space0` |
| 44 | `O03_CD_E043` | `D_3` | `R_D_03_space0` |

### G27_F06_D01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F06_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 45 | `O03_CD_E044` | `Q04` | `Q_04_after_D_03` |

### G28_F07_D02_FIX

- Internal Stimulus: `FIXATION_CHECK_F07_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 46 | `O03_CD_E045` | `FIX_D02` | `FIXATION_BG_1920x1080_WHITE` |

### G29_F07_D02_READ

- Internal Stimulus: `READ_TEMPLATE_F07_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 47 | `O03_CD_E046` | `D_4` | `R_D_04_space0` |
| 48 | `O03_CD_E047` | `D_5` | `R_D_05_space0` |
| 49 | `O03_CD_E048` | `D_6` | `R_D_06_space0` |
| 50 | `O03_CD_E049` | `D_7` | `R_D_07_space0` |
| 51 | `O03_CD_E050` | `D_8` | `R_D_08_space0` |

### G30_F07_D02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F07_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 52 | `O03_CD_E051` | `Q08` | `Q_08_after_D_08` |

### G31_F08_D03_FIX

- Internal Stimulus: `FIXATION_CHECK_F08_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 53 | `O03_CD_E052` | `FIX_D03` | `FIXATION_BG_1920x1080_WHITE` |

### G32_F08_D03_READ

- Internal Stimulus: `READ_TEMPLATE_F08_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 54 | `O03_CD_E053` | `D_9` | `R_D_09_space0` |
| 55 | `O03_CD_E054` | `D_10` | `R_D_10_space0` |

### G33_F08_D03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F08_D03`.
- Subset 1: `article_block=D03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 56 | `O03_CD_E055` | `Q12` | `Q_12_after_D_10` |

### G34_F09_D04_FIX

- Internal Stimulus: `FIXATION_CHECK_F09_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 57 | `O03_CD_E056` | `FIX_D04` | `FIXATION_BG_1920x1080_WHITE` |

### G35_F09_D04_READ

- Internal Stimulus: `READ_TEMPLATE_F09_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 58 | `O03_CD_E057` | `D_11` | `R_D_11_space0` |
| 59 | `O03_CD_E058` | `D_12` | `R_D_12_space0` |

### G36_F09_D04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F09_D04`.
- Subset 1: `article_block=D04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 60 | `O03_CD_E059` | `Q19` | `Q_19_after_D_12` |

### G37_F10_D05_FIX

- Internal Stimulus: `FIXATION_CHECK_F10_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 61 | `O03_CD_E060` | `FIX_D05` | `FIXATION_BG_1920x1080_WHITE` |

### G38_F10_D05_READ

- Internal Stimulus: `READ_TEMPLATE_F10_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 62 | `O03_CD_E061` | `D_13` | `R_D_13_space0` |
| 63 | `O03_CD_E062` | `D_14` | `R_D_14_space0` |
| 64 | `O03_CD_E063` | `D_15` | `R_D_15_space0` |

### G39_F10_D05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F10_D05`.
- Subset 1: `article_block=D05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 65 | `O03_CD_E064` | `Q20` | `Q_20_after_D_15` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
