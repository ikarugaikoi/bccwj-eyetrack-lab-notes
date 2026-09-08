# BCCWJ_EyeTrack_FORMAL_CD_H1_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_CD_H1`; Planned project name: `BCCWJ_EyeTrack_FORMAL_CD_H1_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: CD; Half: 1; Articles: C01 → C02 → C03 → C04 → C05.
- Import: `02_DESIGN_TABLES/order03_CD_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `c073fcceef41da0a377b876a9adefc77834e0043edc66119710f9ddc722839b1`.
- Groups: 15; article events: 26; total image presentations including standalone instructions: 29 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_00_INTRO` | `FORMAL_00_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_01_START_AND_BREAK_NOTICE` | `FORMAL_01_start_and_break_notice_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G10_F01_C01_FIX` | `FIXATION_CHECK_F01_C01` | FIX |
| 5 | group | `G11_F01_C01_READ` | `READ_TEMPLATE_F01_C01` | READ |
| 6 | group | `G12_F01_C01_QUESTION` | `QUESTION_TEMPLATE_F01_C01` | QUESTION |
| 7 | group | `G13_F02_C02_FIX` | `FIXATION_CHECK_F02_C02` | FIX |
| 8 | group | `G14_F02_C02_READ` | `READ_TEMPLATE_F02_C02` | READ |
| 9 | group | `G15_F02_C02_QUESTION` | `QUESTION_TEMPLATE_F02_C02` | QUESTION |
| 10 | group | `G16_F03_C03_FIX` | `FIXATION_CHECK_F03_C03` | FIX |
| 11 | group | `G17_F03_C03_READ` | `READ_TEMPLATE_F03_C03` | READ |
| 12 | group | `G18_F03_C03_QUESTION` | `QUESTION_TEMPLATE_F03_C03` | QUESTION |
| 13 | group | `G19_F04_C04_FIX` | `FIXATION_CHECK_F04_C04` | FIX |
| 14 | group | `G20_F04_C04_READ` | `READ_TEMPLATE_F04_C04` | READ |
| 15 | group | `G21_F04_C04_QUESTION` | `QUESTION_TEMPLATE_F04_C04` | QUESTION |
| 16 | group | `G22_F05_C05_FIX` | `FIXATION_CHECK_F05_C05` | FIX |
| 17 | group | `G23_F05_C05_READ` | `READ_TEMPLATE_F05_C05` | READ |
| 18 | group | `G24_F05_C05_QUESTION` | `QUESTION_TEMPLATE_F05_C05` | QUESTION |
| 19 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G10_F01_C01_FIX

- Internal Stimulus: `FIXATION_CHECK_F01_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 15 | `O03_CD_E014` | `FIX_C01` | `FIXATION_BG_1920x1080_WHITE` |

### G11_F01_C01_READ

- Internal Stimulus: `READ_TEMPLATE_F01_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 16 | `O03_CD_E015` | `C_1` | `R_C_01_space0` |
| 17 | `O03_CD_E016` | `C_2` | `R_C_02_space0` |
| 18 | `O03_CD_E017` | `C_3` | `R_C_03_space0` |
| 19 | `O03_CD_E018` | `C_4` | `R_C_04_space0` |

### G12_F01_C01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F01_C01`.
- Subset 1: `article_block=C01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 20 | `O03_CD_E019` | `Q03` | `Q_03_after_C_04` |

### G13_F02_C02_FIX

- Internal Stimulus: `FIXATION_CHECK_F02_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 21 | `O03_CD_E020` | `FIX_C02` | `FIXATION_BG_1920x1080_WHITE` |

### G14_F02_C02_READ

- Internal Stimulus: `READ_TEMPLATE_F02_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 22 | `O03_CD_E021` | `C_5` | `R_C_05_space0` |
| 23 | `O03_CD_E022` | `C_6` | `R_C_06_space0` |
| 24 | `O03_CD_E023` | `C_7` | `R_C_07_space0` |
| 25 | `O03_CD_E024` | `C_8` | `R_C_08_space0` |
| 26 | `O03_CD_E025` | `C_9` | `R_C_09_space0` |

### G15_F02_C02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F02_C02`.
- Subset 1: `article_block=C02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 27 | `O03_CD_E026` | `Q07` | `Q_07_after_C_09` |

### G16_F03_C03_FIX

- Internal Stimulus: `FIXATION_CHECK_F03_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 28 | `O03_CD_E027` | `FIX_C03` | `FIXATION_BG_1920x1080_WHITE` |

### G17_F03_C03_READ

- Internal Stimulus: `READ_TEMPLATE_F03_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 29 | `O03_CD_E028` | `C_10` | `R_C_10_space0` |
| 30 | `O03_CD_E029` | `C_11` | `R_C_11_space0` |
| 31 | `O03_CD_E030` | `C_12` | `R_C_12_space0` |
| 32 | `O03_CD_E031` | `C_13` | `R_C_13_space0` |

### G18_F03_C03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F03_C03`.
- Subset 1: `article_block=C03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 33 | `O03_CD_E032` | `Q11` | `Q_11_after_C_13` |

### G19_F04_C04_FIX

- Internal Stimulus: `FIXATION_CHECK_F04_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 34 | `O03_CD_E033` | `FIX_C04` | `FIXATION_BG_1920x1080_WHITE` |

### G20_F04_C04_READ

- Internal Stimulus: `READ_TEMPLATE_F04_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 35 | `O03_CD_E034` | `C_14` | `R_C_14_space0` |
| 36 | `O03_CD_E035` | `C_15` | `R_C_15_space0` |

### G21_F04_C04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F04_C04`.
- Subset 1: `article_block=C04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 37 | `O03_CD_E036` | `Q17` | `Q_17_after_C_15` |

### G22_F05_C05_FIX

- Internal Stimulus: `FIXATION_CHECK_F05_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 38 | `O03_CD_E037` | `FIX_C05` | `FIXATION_BG_1920x1080_WHITE` |

### G23_F05_C05_READ

- Internal Stimulus: `READ_TEMPLATE_F05_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 39 | `O03_CD_E038` | `C_16` | `R_C_16_space0` |

### G24_F05_C05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F05_C05`.
- Subset 1: `article_block=C05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 40 | `O03_CD_E039` | `Q18` | `Q_18_after_C_16` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
