# BCCWJ_EyeTrack_FORMAL_BA_H1_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_BA_H1`; Planned project name: `BCCWJ_EyeTrack_FORMAL_BA_H1_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: BA; Half: 1; Articles: B01 → B02 → B03 → B04 → B05.
- Import: `02_DESIGN_TABLES/order02_BA_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `8309de64e5899fc61bb291740919cb1bf2e37f90d14cc85a8589181b681dbd8d`.
- Groups: 15; article events: 31; total image presentations including standalone instructions: 34 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_00_INTRO` | `FORMAL_00_intro_JA` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_01_START_AND_BREAK_NOTICE` | `FORMAL_01_start_and_break_notice_JA` | INSTRUCTION_SPACE |
| 4 | group | `G10_F01_B01_FIX` | `FIXATION_CHECK_F01_B01` | FIX |
| 5 | group | `G11_F01_B01_READ` | `READ_TEMPLATE_F01_B01` | READ |
| 6 | group | `G12_F01_B01_QUESTION` | `QUESTION_TEMPLATE_F01_B01` | QUESTION |
| 7 | group | `G13_F02_B02_FIX` | `FIXATION_CHECK_F02_B02` | FIX |
| 8 | group | `G14_F02_B02_READ` | `READ_TEMPLATE_F02_B02` | READ |
| 9 | group | `G15_F02_B02_QUESTION` | `QUESTION_TEMPLATE_F02_B02` | QUESTION |
| 10 | group | `G16_F03_B03_FIX` | `FIXATION_CHECK_F03_B03` | FIX |
| 11 | group | `G17_F03_B03_READ` | `READ_TEMPLATE_F03_B03` | READ |
| 12 | group | `G18_F03_B03_QUESTION` | `QUESTION_TEMPLATE_F03_B03` | QUESTION |
| 13 | group | `G19_F04_B04_FIX` | `FIXATION_CHECK_F04_B04` | FIX |
| 14 | group | `G20_F04_B04_READ` | `READ_TEMPLATE_F04_B04` | READ |
| 15 | group | `G21_F04_B04_QUESTION` | `QUESTION_TEMPLATE_F04_B04` | QUESTION |
| 16 | group | `G22_F05_B05_FIX` | `FIXATION_CHECK_F05_B05` | FIX |
| 17 | group | `G23_F05_B05_READ` | `READ_TEMPLATE_F05_B05` | READ |
| 18 | group | `G24_F05_B05_QUESTION` | `QUESTION_TEMPLATE_F05_B05` | QUESTION |
| 19 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G10_F01_B01_FIX

- Internal Stimulus: `FIXATION_CHECK_F01_B01`.
- Subset 1: `article_block=B01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 15 | `O02_BA_E014` | `FIX_B01` | `FIXATION_BG_1920x1080_WHITE` |

### G11_F01_B01_READ

- Internal Stimulus: `READ_TEMPLATE_F01_B01`.
- Subset 1: `article_block=B01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 16 | `O02_BA_E015` | `B_1` | `R_B_01_space0` |
| 17 | `O02_BA_E016` | `B_2` | `R_B_02_space0` |
| 18 | `O02_BA_E017` | `B_3` | `R_B_03_space0` |
| 19 | `O02_BA_E018` | `B_4` | `R_B_04_space0` |
| 20 | `O02_BA_E019` | `B_5` | `R_B_05_space0` |
| 21 | `O02_BA_E020` | `B_6` | `R_B_06_space0` |

### G12_F01_B01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F01_B01`.
- Subset 1: `article_block=B01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 22 | `O02_BA_E021` | `Q02` | `Q_02_after_B_06` |

### G13_F02_B02_FIX

- Internal Stimulus: `FIXATION_CHECK_F02_B02`.
- Subset 1: `article_block=B02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 23 | `O02_BA_E022` | `FIX_B02` | `FIXATION_BG_1920x1080_WHITE` |

### G14_F02_B02_READ

- Internal Stimulus: `READ_TEMPLATE_F02_B02`.
- Subset 1: `article_block=B02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 24 | `O02_BA_E023` | `B_7` | `R_B_07_space0` |
| 25 | `O02_BA_E024` | `B_8` | `R_B_08_space0` |
| 26 | `O02_BA_E025` | `B_9` | `R_B_09_space0` |
| 27 | `O02_BA_E026` | `B_10` | `R_B_10_space0` |
| 28 | `O02_BA_E027` | `B_11` | `R_B_11_space0` |
| 29 | `O02_BA_E028` | `B_12` | `R_B_12_space0` |

### G15_F02_B02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F02_B02`.
- Subset 1: `article_block=B02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 30 | `O02_BA_E029` | `Q06` | `Q_06_after_B_12` |

### G16_F03_B03_FIX

- Internal Stimulus: `FIXATION_CHECK_F03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 31 | `O02_BA_E030` | `FIX_B03` | `FIXATION_BG_1920x1080_WHITE` |

### G17_F03_B03_READ

- Internal Stimulus: `READ_TEMPLATE_F03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 32 | `O02_BA_E031` | `B_13` | `R_B_13_space0` |
| 33 | `O02_BA_E032` | `B_14` | `R_B_14_space0` |
| 34 | `O02_BA_E033` | `B_15` | `R_B_15_space0` |
| 35 | `O02_BA_E034` | `B_16` | `R_B_16_space0` |

### G18_F03_B03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F03_B03`.
- Subset 1: `article_block=B03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 36 | `O02_BA_E035` | `Q10` | `Q_10_after_B_16` |

### G19_F04_B04_FIX

- Internal Stimulus: `FIXATION_CHECK_F04_B04`.
- Subset 1: `article_block=B04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 37 | `O02_BA_E036` | `FIX_B04` | `FIXATION_BG_1920x1080_WHITE` |

### G20_F04_B04_READ

- Internal Stimulus: `READ_TEMPLATE_F04_B04`.
- Subset 1: `article_block=B04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 38 | `O02_BA_E037` | `B_17` | `R_B_17_space0` |
| 39 | `O02_BA_E038` | `B_18` | `R_B_18_space0` |
| 40 | `O02_BA_E039` | `B_19` | `R_B_19_space0` |
| 41 | `O02_BA_E040` | `B_20` | `R_B_20_space0` |

### G21_F04_B04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F04_B04`.
- Subset 1: `article_block=B04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 42 | `O02_BA_E041` | `Q14` | `Q_14_after_B_20` |

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
