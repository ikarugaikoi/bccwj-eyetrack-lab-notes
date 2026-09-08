# BCCWJ_EyeTrack_FORMAL_DC_H1_JA

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_DC_H1`; Planned project name: `BCCWJ_EyeTrack_FORMAL_DC_H1_JA`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: DC; Half: 1; Articles: D01 → D02 → D03 → D04 → D05.
- Import: `02_DESIGN_TABLES/order04_DC_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `752cce739dc8e6d779c180ed98dda5994d2b8b64cd00f8cce240d7a11c840b23`.
- Groups: 15; article events: 25; total image presentations including standalone instructions: 28 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_00_INTRO` | `FORMAL_00_intro_JA` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_01_START_AND_BREAK_NOTICE` | `FORMAL_01_start_and_break_notice_JA` | INSTRUCTION_SPACE |
| 4 | group | `G10_F01_D01_FIX` | `FIXATION_CHECK_F01_D01` | FIX |
| 5 | group | `G11_F01_D01_READ` | `READ_TEMPLATE_F01_D01` | READ |
| 6 | group | `G12_F01_D01_QUESTION` | `QUESTION_TEMPLATE_F01_D01` | QUESTION |
| 7 | group | `G13_F02_D02_FIX` | `FIXATION_CHECK_F02_D02` | FIX |
| 8 | group | `G14_F02_D02_READ` | `READ_TEMPLATE_F02_D02` | READ |
| 9 | group | `G15_F02_D02_QUESTION` | `QUESTION_TEMPLATE_F02_D02` | QUESTION |
| 10 | group | `G16_F03_D03_FIX` | `FIXATION_CHECK_F03_D03` | FIX |
| 11 | group | `G17_F03_D03_READ` | `READ_TEMPLATE_F03_D03` | READ |
| 12 | group | `G18_F03_D03_QUESTION` | `QUESTION_TEMPLATE_F03_D03` | QUESTION |
| 13 | group | `G19_F04_D04_FIX` | `FIXATION_CHECK_F04_D04` | FIX |
| 14 | group | `G20_F04_D04_READ` | `READ_TEMPLATE_F04_D04` | READ |
| 15 | group | `G21_F04_D04_QUESTION` | `QUESTION_TEMPLATE_F04_D04` | QUESTION |
| 16 | group | `G22_F05_D05_FIX` | `FIXATION_CHECK_F05_D05` | FIX |
| 17 | group | `G23_F05_D05_READ` | `READ_TEMPLATE_F05_D05` | READ |
| 18 | group | `G24_F05_D05_QUESTION` | `QUESTION_TEMPLATE_F05_D05` | QUESTION |
| 19 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_JA` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G10_F01_D01_FIX

- Internal Stimulus: `FIXATION_CHECK_F01_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 15 | `O04_DC_E014` | `FIX_D01` | `FIXATION_BG_1920x1080_WHITE` |

### G11_F01_D01_READ

- Internal Stimulus: `READ_TEMPLATE_F01_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 16 | `O04_DC_E015` | `D_1` | `R_D_01_space0` |
| 17 | `O04_DC_E016` | `D_2` | `R_D_02_space0` |
| 18 | `O04_DC_E017` | `D_3` | `R_D_03_space0` |

### G12_F01_D01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F01_D01`.
- Subset 1: `article_block=D01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 19 | `O04_DC_E018` | `Q04` | `Q_04_after_D_03` |

### G13_F02_D02_FIX

- Internal Stimulus: `FIXATION_CHECK_F02_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 20 | `O04_DC_E019` | `FIX_D02` | `FIXATION_BG_1920x1080_WHITE` |

### G14_F02_D02_READ

- Internal Stimulus: `READ_TEMPLATE_F02_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 21 | `O04_DC_E020` | `D_4` | `R_D_04_space0` |
| 22 | `O04_DC_E021` | `D_5` | `R_D_05_space0` |
| 23 | `O04_DC_E022` | `D_6` | `R_D_06_space0` |
| 24 | `O04_DC_E023` | `D_7` | `R_D_07_space0` |
| 25 | `O04_DC_E024` | `D_8` | `R_D_08_space0` |

### G15_F02_D02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F02_D02`.
- Subset 1: `article_block=D02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 26 | `O04_DC_E025` | `Q08` | `Q_08_after_D_08` |

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
