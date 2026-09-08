# BCCWJ_EyeTrack_FORMAL_DC_H2_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_DC_H2`; Planned project name: `BCCWJ_EyeTrack_FORMAL_DC_H2_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: DC; Half: 2; Articles: C01 → C02 → C03 → C04 → C05.
- Import: `02_DESIGN_TABLES/order04_DC_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `752cce739dc8e6d779c180ed98dda5994d2b8b64cd00f8cce240d7a11c840b23`.
- Groups: 15; article events: 26; total image presentations including standalone instructions: 29 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_03_RECALIBRATION_INTRO` | `FORMAL_03_recalibration_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H2` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_04_SECOND_HALF_START` | `FORMAL_04_second_half_start_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G25_F06_C01_FIX` | `FIXATION_CHECK_F06_C01` | FIX |
| 5 | group | `G26_F06_C01_READ` | `READ_TEMPLATE_F06_C01` | READ |
| 6 | group | `G27_F06_C01_QUESTION` | `QUESTION_TEMPLATE_F06_C01` | QUESTION |
| 7 | group | `G28_F07_C02_FIX` | `FIXATION_CHECK_F07_C02` | FIX |
| 8 | group | `G29_F07_C02_READ` | `READ_TEMPLATE_F07_C02` | READ |
| 9 | group | `G30_F07_C02_QUESTION` | `QUESTION_TEMPLATE_F07_C02` | QUESTION |
| 10 | group | `G31_F08_C03_FIX` | `FIXATION_CHECK_F08_C03` | FIX |
| 11 | group | `G32_F08_C03_READ` | `READ_TEMPLATE_F08_C03` | READ |
| 12 | group | `G33_F08_C03_QUESTION` | `QUESTION_TEMPLATE_F08_C03` | QUESTION |
| 13 | group | `G34_F09_C04_FIX` | `FIXATION_CHECK_F09_C04` | FIX |
| 14 | group | `G35_F09_C04_READ` | `READ_TEMPLATE_F09_C04` | READ |
| 15 | group | `G36_F09_C04_QUESTION` | `QUESTION_TEMPLATE_F09_C04` | QUESTION |
| 16 | group | `G37_F10_C05_FIX` | `FIXATION_CHECK_F10_C05` | FIX |
| 17 | group | `G38_F10_C05_READ` | `READ_TEMPLATE_F10_C05` | READ |
| 18 | group | `G39_F10_C05_QUESTION` | `QUESTION_TEMPLATE_F10_C05` | QUESTION |
| 19 | image_stimulus | `FORMAL_05_END` | `FORMAL_05_end_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G25_F06_C01_FIX

- Internal Stimulus: `FIXATION_CHECK_F06_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 40 | `O04_DC_E039` | `FIX_C01` | `FIXATION_BG_1920x1080_WHITE` |

### G26_F06_C01_READ

- Internal Stimulus: `READ_TEMPLATE_F06_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 41 | `O04_DC_E040` | `C_1` | `R_C_01_space0` |
| 42 | `O04_DC_E041` | `C_2` | `R_C_02_space0` |
| 43 | `O04_DC_E042` | `C_3` | `R_C_03_space0` |
| 44 | `O04_DC_E043` | `C_4` | `R_C_04_space0` |

### G27_F06_C01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F06_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 45 | `O04_DC_E044` | `Q03` | `Q_03_after_C_04` |

### G28_F07_C02_FIX

- Internal Stimulus: `FIXATION_CHECK_F07_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 46 | `O04_DC_E045` | `FIX_C02` | `FIXATION_BG_1920x1080_WHITE` |

### G29_F07_C02_READ

- Internal Stimulus: `READ_TEMPLATE_F07_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 47 | `O04_DC_E046` | `C_5` | `R_C_05_space0` |
| 48 | `O04_DC_E047` | `C_6` | `R_C_06_space0` |
| 49 | `O04_DC_E048` | `C_7` | `R_C_07_space0` |
| 50 | `O04_DC_E049` | `C_8` | `R_C_08_space0` |
| 51 | `O04_DC_E050` | `C_9` | `R_C_09_space0` |

### G30_F07_C02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F07_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 52 | `O04_DC_E051` | `Q07` | `Q_07_after_C_09` |

### G31_F08_C03_FIX

- Internal Stimulus: `FIXATION_CHECK_F08_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 53 | `O04_DC_E052` | `FIX_C03` | `FIXATION_BG_1920x1080_WHITE` |

### G32_F08_C03_READ

- Internal Stimulus: `READ_TEMPLATE_F08_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 54 | `O04_DC_E053` | `C_10` | `R_C_10_space0` |
| 55 | `O04_DC_E054` | `C_11` | `R_C_11_space0` |
| 56 | `O04_DC_E055` | `C_12` | `R_C_12_space0` |
| 57 | `O04_DC_E056` | `C_13` | `R_C_13_space0` |

### G33_F08_C03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F08_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 58 | `O04_DC_E057` | `Q11` | `Q_11_after_C_13` |

### G34_F09_C04_FIX

- Internal Stimulus: `FIXATION_CHECK_F09_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 59 | `O04_DC_E058` | `FIX_C04` | `FIXATION_BG_1920x1080_WHITE` |

### G35_F09_C04_READ

- Internal Stimulus: `READ_TEMPLATE_F09_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 60 | `O04_DC_E059` | `C_14` | `R_C_14_space0` |
| 61 | `O04_DC_E060` | `C_15` | `R_C_15_space0` |

### G36_F09_C04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F09_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 62 | `O04_DC_E061` | `Q17` | `Q_17_after_C_15` |

### G37_F10_C05_FIX

- Internal Stimulus: `FIXATION_CHECK_F10_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 63 | `O04_DC_E062` | `FIX_C05` | `FIXATION_BG_1920x1080_WHITE` |

### G38_F10_C05_READ

- Internal Stimulus: `READ_TEMPLATE_F10_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 64 | `O04_DC_E063` | `C_16` | `R_C_16_space0` |

### G39_F10_C05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F10_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 65 | `O04_DC_E064` | `Q18` | `Q_18_after_C_16` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
