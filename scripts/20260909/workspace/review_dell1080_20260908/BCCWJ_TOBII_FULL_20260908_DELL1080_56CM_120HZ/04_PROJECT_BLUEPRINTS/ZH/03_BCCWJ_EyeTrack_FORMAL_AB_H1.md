# BCCWJ_EyeTrack_FORMAL_AB_H1_ZH

This blueprint lists the project configuration, stimulus sequence, and acceptance checks. Build separate projects for Chinese and Japanese instructions. For completion status and actual short names, see queue.json and name_mapping.json in workspace/dell1080_20260908, relative to the source bundle root.

- Profile: `DELL238_FHD_56CM_FUSION120_20260908`; 1920×1080, target distance 56cm, Fusion120 / 120Hz.
- Original logical name: `BCCWJ_EyeTrack_FORMAL_AB_H1`; Planned project name: `BCCWJ_EyeTrack_FORMAL_AB_H1_ZH`.
- Use a separate DELL1080 directory. If a project name conflicts, append _DELL1080 and record the name mapping.
- Type: formal; Condition: AB; Half: 1; Articles: A01 → A02 → A03 → A04 → A05.
- Import: `02_DESIGN_TABLES/order01_AB_P_TRUE_Q_FALSE_DELL1080.xlsx`; table object `Tobii_Design`.
- Table file SHA256: `91a1d592909a01c2d0c7c2d9ccf0fc24bab373f86c300be0b3957d83391ab1f2`.
- Groups: 15; article events: 29; total image presentations including standalone instructions: 32 (excluding native calibration).

Read 03_SPEC/REBUILD_REQUIREMENTS.md in full. MAIN=1/1/0/0; DOT=.05/.07777778/.01/.06666667; both use Original. Ordinary stimuli: 100ms minimum, Time=None. FIX: no keys; READ: Space only; QUESTION: both Q/P; ending: 7 only.

## All top-level elements

| Step | Type | Object name | Fixed Source or internal Stimulus | Advance preset |
|---:|---|---|---|---|
| 1 | image_stimulus | `FORMAL_00_INTRO` | `FORMAL_00_intro_ZH` | INSTRUCTION_SPACE |
| 2 | calibration | `CALIBRATION_H1` | `Native Calibration + Validation; 9 targets/Point/Timed` | CALIBRATION |
| 3 | image_stimulus | `FORMAL_01_START_AND_BREAK_NOTICE` | `FORMAL_01_start_and_break_notice_ZH` | INSTRUCTION_SPACE |
| 4 | group | `G10_F01_A01_FIX` | `FIXATION_CHECK_F01_A01` | FIX |
| 5 | group | `G11_F01_A01_READ` | `READ_TEMPLATE_F01_A01` | READ |
| 6 | group | `G12_F01_A01_QUESTION` | `QUESTION_TEMPLATE_F01_A01` | QUESTION |
| 7 | group | `G13_F02_A02_FIX` | `FIXATION_CHECK_F02_A02` | FIX |
| 8 | group | `G14_F02_A02_READ` | `READ_TEMPLATE_F02_A02` | READ |
| 9 | group | `G15_F02_A02_QUESTION` | `QUESTION_TEMPLATE_F02_A02` | QUESTION |
| 10 | group | `G16_F03_A03_FIX` | `FIXATION_CHECK_F03_A03` | FIX |
| 11 | group | `G17_F03_A03_READ` | `READ_TEMPLATE_F03_A03` | READ |
| 12 | group | `G18_F03_A03_QUESTION` | `QUESTION_TEMPLATE_F03_A03` | QUESTION |
| 13 | group | `G19_F04_A04_FIX` | `FIXATION_CHECK_F04_A04` | FIX |
| 14 | group | `G20_F04_A04_READ` | `READ_TEMPLATE_F04_A04` | READ |
| 15 | group | `G21_F04_A04_QUESTION` | `QUESTION_TEMPLATE_F04_A04` | QUESTION |
| 16 | group | `G22_F05_A05_FIX` | `FIXATION_CHECK_F05_A05` | FIX |
| 17 | group | `G23_F05_A05_READ` | `READ_TEMPLATE_F05_A05` | READ |
| 18 | group | `G24_F05_A05_QUESTION` | `QUESTION_TEMPLATE_F05_A05` | QUESTION |
| 19 | image_stimulus | `FORMAL_02_BREAK` | `FORMAL_02_break_ZH` | END_OPERATOR_7 |

## Article group bindings and expanded table rows

Use one internal template per group to present images in the order of the selected table rows. Turn off Set at recording start for both Subsets; configure operators as specified in the blueprint.

### G10_F01_A01_FIX

- Internal Stimulus: `FIXATION_CHECK_F01_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 15 | `O01_AB_E014` | `FIX_A01` | `FIXATION_BG_1920x1080_WHITE` |

### G11_F01_A01_READ

- Internal Stimulus: `READ_TEMPLATE_F01_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 16 | `O01_AB_E015` | `A_1` | `R_A_01_space0` |
| 17 | `O01_AB_E016` | `A_2` | `R_A_02_space0` |
| 18 | `O01_AB_E017` | `A_3` | `R_A_03_space0` |
| 19 | `O01_AB_E018` | `A_4` | `R_A_04_space0` |
| 20 | `O01_AB_E019` | `A_5` | `R_A_05_space0` |
| 21 | `O01_AB_E020` | `A_6` | `R_A_06_space0` |
| 22 | `O01_AB_E021` | `A_7` | `R_A_07_space0` |

### G12_F01_A01_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F01_A01`.
- Subset 1: `article_block=A01`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 23 | `O01_AB_E022` | `Q01` | `Q_01_after_A_07` |

### G13_F02_A02_FIX

- Internal Stimulus: `FIXATION_CHECK_F02_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 24 | `O01_AB_E023` | `FIX_A02` | `FIXATION_BG_1920x1080_WHITE` |

### G14_F02_A02_READ

- Internal Stimulus: `READ_TEMPLATE_F02_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 25 | `O01_AB_E024` | `A_8` | `R_A_08_space0` |
| 26 | `O01_AB_E025` | `A_9` | `R_A_09_space0` |
| 27 | `O01_AB_E026` | `A_10` | `R_A_10_space0` |
| 28 | `O01_AB_E027` | `A_11` | `R_A_11_space0` |
| 29 | `O01_AB_E028` | `A_12` | `R_A_12_space0` |

### G15_F02_A02_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F02_A02`.
- Subset 1: `article_block=A02`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 30 | `O01_AB_E029` | `Q05` | `Q_05_after_A_12` |

### G16_F03_A03_FIX

- Internal Stimulus: `FIXATION_CHECK_F03_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 31 | `O01_AB_E030` | `FIX_A03` | `FIXATION_BG_1920x1080_WHITE` |

### G17_F03_A03_READ

- Internal Stimulus: `READ_TEMPLATE_F03_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 32 | `O01_AB_E031` | `A_13` | `R_A_13_space0` |
| 33 | `O01_AB_E032` | `A_14` | `R_A_14_space0` |
| 34 | `O01_AB_E033` | `A_15` | `R_A_15_space0` |

### G18_F03_A03_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F03_A03`.
- Subset 1: `article_block=A03`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 35 | `O01_AB_E034` | `Q09` | `Q_09_after_A_15` |

### G19_F04_A04_FIX

- Internal Stimulus: `FIXATION_CHECK_F04_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 36 | `O01_AB_E035` | `FIX_A04` | `FIXATION_BG_1920x1080_WHITE` |

### G20_F04_A04_READ

- Internal Stimulus: `READ_TEMPLATE_F04_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 37 | `O01_AB_E036` | `A_16` | `R_A_16_space0` |
| 38 | `O01_AB_E037` | `A_17` | `R_A_17_space0` |

### G21_F04_A04_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F04_A04`.
- Subset 1: `article_block=A04`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 39 | `O01_AB_E038` | `Q13` | `Q_13_after_A_17` |

### G22_F05_A05_FIX

- Internal Stimulus: `FIXATION_CHECK_F05_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=fixation`.
- Preset: `FIX`.
- Container `MAIN`: Source fixed_media=`FIXATION_BG_1920x1080_WHITE`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.
- Container `DOT`: Source fixed_media=`FIXATION_DOT_96x84_TOBII`; coordinate bindings W→DOT_W, H→DOT_H, X→DOT_X, Y→DOT_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 40 | `O01_AB_E039` | `FIX_A05` | `FIXATION_BG_1920x1080_WHITE` |

### G23_F05_A05_READ

- Internal Stimulus: `READ_TEMPLATE_F05_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=reading`.
- Preset: `READ`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 41 | `O01_AB_E040` | `A_18` | `R_A_18_space0` |
| 42 | `O01_AB_E041` | `A_19` | `R_A_19_space0` |

### G24_F05_A05_QUESTION

- Internal Stimulus: `QUESTION_TEMPLATE_F05_A05`.
- Subset 1: `article_block=A05`; Subset 2: `row_type=question`.
- Preset: `QUESTION`.
- Container `MAIN`: Source bind_column=`media_name`; coordinate bindings W→MAIN_W, H→MAIN_H, X→MAIN_X, Y→MAIN_Y.

| Excel row | event_id | sample_screen | media_name |
|---:|---|---|---|
| 43 | `O01_AB_E042` | `Q15` | `Q_15_after_A_19` |

## Project acceptance

- [ ] Correct version, language, table hash, all names, and Subsets.
- [ ] Standalone instruction MAIN coordinates entered manually as 1/1/0/0; article container bindings correct; all Sources resolved.
- [ ] Time=None; both Q/P accepted for answers; 7 ends the recording; only DOT uses Continuous300ms/Data loss reset34ms.
- [ ] Exactly one calibration; all reading pages, questions, and ending presented in the sequence above.
- [ ] Record results and evidence separately for saving/reopening, read-only native checks, onsite trial runs, and exports.
