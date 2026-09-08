# BCCWJ_EyeTrack_FORMAL_BA_H2_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_BA_H2`; Planned project name: `BCCWJ_EyeTrack_FORMAL_BA_H2_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: BA; Half: 2; Articles: A01 → A02 → A03 → A04 → A05.
- Import: `02_DESIGN_TABLES/order02_BA_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `8309de64e5899fc61bb291740919cb1bf2e37f90d14cc85a8589181b681dbd8d`.
- Groups: 15; article events: 29; total image presentations including standalone instructions: 32 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_03_RECALIBRATION_INTRO` | `FORMAL_03_recalibration_intro_JA` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H2` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_04_SECOND_HALF_START` | `FORMAL_04_second_half_start_JA` | INSTRUCTION_SPACE |
| 4 | group | `G25_F06_A01_FIX` | `FIXATION_CHECK_F06_A01` | FIX |
| 5 | group | `G26_F06_A01_READ` | `READ_TEMPLATE_F06_A01` | READ |
| 6 | group | `G27_F06_A01_QUESTION` | `QUESTION_TEMPLATE_F06_A01` | QUESTION |
| 7 | group | `G28_F07_A02_FIX` | `FIXATION_CHECK_F07_A02` | FIX |
| 8 | group | `G29_F07_A02_READ` | `READ_TEMPLATE_F07_A02` | READ |
| 9 | group | `G30_F07_A02_QUESTION` | `QUESTION_TEMPLATE_F07_A02` | QUESTION |
| 10 | group | `G31_F08_A03_FIX` | `FIXATION_CHECK_F08_A03` | FIX |
| 11 | group | `G32_F08_A03_READ` | `READ_TEMPLATE_F08_A03` | READ |
| 12 | group | `G33_F08_A03_QUESTION` | `QUESTION_TEMPLATE_F08_A03` | QUESTION |
| 13 | group | `G34_F09_A04_FIX` | `FIXATION_CHECK_F09_A04` | FIX |
| 14 | group | `G35_F09_A04_READ` | `READ_TEMPLATE_F09_A04` | READ |
| 15 | group | `G36_F09_A04_QUESTION` | `QUESTION_TEMPLATE_F09_A04` | QUESTION |
| 16 | group | `G37_F10_A05_FIX` | `FIXATION_CHECK_F10_A05` | FIX |
| 17 | group | `G38_F10_A05_READ` | `READ_TEMPLATE_F10_A05` | READ |
| 18 | group | `G39_F10_A05_QUESTION` | `QUESTION_TEMPLATE_F10_A05` | QUESTION |
| 19 | image_stimulus | `FORMAL_05_END` | `FORMAL_05_end_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G25_F06_A01_FIX

- Internal Stimulus: `FIXATION_CHECK_F06_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 46 | `O02_BA_E045` | `FIX_A01` | `FIXATION_BG_1920x1080_WHITE` |

### G26_F06_A01_READ

- Internal Stimulus: `READ_TEMPLATE_F06_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 47 | `O02_BA_E046` | `A_1` | `R_A_01_space0` |
| 48 | `O02_BA_E047` | `A_2` | `R_A_02_space0` |
| 49 | `O02_BA_E048` | `A_3` | `R_A_03_space0` |
| 50 | `O02_BA_E049` | `A_4` | `R_A_04_space0` |
| 51 | `O02_BA_E050` | `A_5` | `R_A_05_space0` |
| 52 | `O02_BA_E051` | `A_6` | `R_A_06_space0` |
| 53 | `O02_BA_E052` | `A_7` | `R_A_07_space0` |

### G27_F06_A01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F06_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 54 | `O02_BA_E053` | `Q01` | `Q_01_after_A_07` |

### G28_F07_A02_FIX

- Internal Stimulus: `FIXATION_CHECK_F07_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 55 | `O02_BA_E054` | `FIX_A02` | `FIXATION_BG_1920x1080_WHITE` |

### G29_F07_A02_READ

- Internal Stimulus: `READ_TEMPLATE_F07_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 56 | `O02_BA_E055` | `A_8` | `R_A_08_space0` |
| 57 | `O02_BA_E056` | `A_9` | `R_A_09_space0` |
| 58 | `O02_BA_E057` | `A_10` | `R_A_10_space0` |
| 59 | `O02_BA_E058` | `A_11` | `R_A_11_space0` |
| 60 | `O02_BA_E059` | `A_12` | `R_A_12_space0` |

### G30_F07_A02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F07_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 61 | `O02_BA_E060` | `Q05` | `Q_05_after_A_12` |

### G31_F08_A03_FIX

- Internal Stimulus: `FIXATION_CHECK_F08_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 62 | `O02_BA_E061` | `FIX_A03` | `FIXATION_BG_1920x1080_WHITE` |

### G32_F08_A03_READ

- Internal Stimulus: `READ_TEMPLATE_F08_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 63 | `O02_BA_E062` | `A_13` | `R_A_13_space0` |
| 64 | `O02_BA_E063` | `A_14` | `R_A_14_space0` |
| 65 | `O02_BA_E064` | `A_15` | `R_A_15_space0` |

### G33_F08_A03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F08_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 66 | `O02_BA_E065` | `Q09` | `Q_09_after_A_15` |

### G34_F09_A04_FIX

- Internal Stimulus: `FIXATION_CHECK_F09_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 67 | `O02_BA_E066` | `FIX_A04` | `FIXATION_BG_1920x1080_WHITE` |

### G35_F09_A04_READ

- Internal Stimulus: `READ_TEMPLATE_F09_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 68 | `O02_BA_E067` | `A_16` | `R_A_16_space0` |
| 69 | `O02_BA_E068` | `A_17` | `R_A_17_space0` |

### G36_F09_A04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F09_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 70 | `O02_BA_E069` | `Q13` | `Q_13_after_A_17` |

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
