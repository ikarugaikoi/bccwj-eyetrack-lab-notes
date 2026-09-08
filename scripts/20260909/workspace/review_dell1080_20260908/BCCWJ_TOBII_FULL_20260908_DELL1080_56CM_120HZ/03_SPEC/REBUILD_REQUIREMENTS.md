# Complete Build Requirements: DELL1080 / 56 cm / Fusion 120

This specification, BUILD_PARAMETERS.json, and the per-project blueprints define the build targets. Import files are in 02_DESIGN_TABLES in the complete material package; images, XLSX files, and native projects must be supplied separately. Chinese and Japanese versions use article and instruction images reviewed by the user.

For actual short names, see workspace/dell1080_20260908/name_mapping.json in the source bundle. For saved DOT import values and accepted differences, see ACCEPTED_DEVIATION.json and PRECISION_INCIDENT.md in the same directory.

## 1. Output scope and build order

Each language has 42 projects: 2 practice, 8 main-experiment, and 32 main-experiment recovery projects, for 84 in total. Complete the 42 Chinese projects first, then copy each to create the 42 Japanese projects. Follow the per-project blueprints for SECTION/Group/Stimulus names and retain their numbering.

| Order condition | Practice project | H1 | H2 |
|---|---|---|---|
| AB | PRACTICE_A | A01–A05 | B01–B05 |
| BA | PRACTICE_A | B01–B05 | A01–A05 |
| CD | PRACTICE_B | C01–C05 | D01–D05 |
| DC | PRACTICE_B | D01–D05 | C01–C05 |

PRACTICE_A uses C05→D03→C01; PRACTICE_B uses B05→A05→B03. For each condition/half, also build FROM projects covering article 2/3/4/5 through the end of that half: 32 per language. Recovery applies only when no reading page from the current article has been displayed. Create a separate Recording for each project; practice, H1, and H2 run independently.

Place new outputs in a separate DELL1080_20260908 directory. Planned project names use _ZH/_JA. If names conflict, append _DELL1080 to the actual name and record the mapping. Preserve internal G/F/P/Stimulus names from the blueprints. Create, copy, and export designs through supported software interfaces; leave private databases untouched. Keep previous Recording/Participant data separate from new results.

## 2. Display and device targets

| Item | Setting/status |
|---|---|
| Project type | Advanced Screen |
| Presentation resolution | 1920×1080 |
| Windows participant display | Desktop and active signal 1920×1080, 100% scaling, extended desktop, correct display selected |
| Physical active display area | Assumed approximately 527×296 mm, 23.8-inch-class 16:9; onsite model and measurements unverified |
| Display refresh rate | Planned approximately 60 Hz; record the actual value separately from gaze sampling rate |
| Eye tracker | Laboratory email confirmed the Tobii Pro Fusion 120 model |
| Gaze sampling rate | Select 120 Hz in Record and read back the actual recording value; nominal interval approximately 8.333 ms |
| Distance | Target perpendicular distance approximately 560 mm from the midpoint between the eyes to the screen plane; record the measurement and reference plane |
| Installation | After lower-bezel mounting, recheck Manager Display Setup; read back dimensions, 3D corners, and relative mounting position |

The 56 cm target preserves the pixel visual angle of the previous approximately 55 cm design: 550×(527/1920)/0.270≈559.12 mm, rounded to approximately 560 mm. Record the actual eye-midpoint-to-screen-plane distance onsite. Accept the display and mapping against the current installation, active area, and read-back geometry. Record any mismatch and pause onsite acceptance of that configuration.

## 3. Media and four design tables

Import reading 71, questions 20, fixation 2, and instructions_ZH 19 into each Chinese project: 112 images. The shared library covers all table references; Subsets determine which images a project presents. Add instructions_JA 19 to each Japanese copy. Retaining unreferenced Chinese images gives 131 library items; all referenced fixed instruction Sources must point to _JA.

| Condition | Import file |
|---|---|
| AB, PRACTICE_A | order01_AB_P_TRUE_Q_FALSE_DELL1080.xlsx |
| BA | order02_BA_P_TRUE_Q_FALSE_DELL1080.xlsx |
| CD, PRACTICE_B | order03_CD_P_TRUE_Q_FALSE_DELL1080.xlsx |
| DC | order04_DC_P_TRUE_Q_FALSE_DELL1080.xlsx |

Select files from 02_DESIGN_TABLES. Import only the first sheet, Tobii_Design, and name the table object Tobii_Design. Group_Map/Codebook are manual references. AB/BA contain 73 data rows each; CD/DC contain 64 each. Each table includes practice and main-experiment rows, with Subsets selecting the current project. The initial practice C05/B05 rows are expected.

The first 11 columns must remain: `article_block → row_type → media_name → DOT_W → DOT_H → DOT_X → DOT_Y → MAIN_W → MAIN_H → MAIN_X → MAIN_Y`. Retain the remaining 23 columns in their existing order.

In a new project, import this version's table before binding. Japanese copies retain that table. After switching table objects, individually verify every Source and all 8 coordinate-column bindings. If media_name is red, check the correspondence between library names and table values; retain column binding in reading containers.

## 4. Complete container settings

| Container | W | H | X | Y | Source |
|---|---:|---:|---:|---:|---|
| MAIN | 1 | 1 | 0 | 0 | See categories below |
| DOT | 0.05 | 0.07777778 | 0.01 | 0.06666667 | FIXATION_DOT_96x84_TOBII |

Exact DOT geometry is H=84/1080 and Y=72/1080. The table and all blueprints store 8 decimal places, giving approximately 96×84 px at (19.2,72). Preserve these values rather than manually rounding to 0.08/0.07. The visible circle is 16×16 px, centered approximately at (67.2,114); the transparent 96×84 container defines the trigger region. Preserve the original PNG.

- FIX: two Image containers, MAIN and DOT. MAIN uses fixed Source FIXATION_BG_1920x1080_WHITE; DOT uses the fixed dot image above. Bind all four MAIN coordinates to MAIN columns and all four DOT coordinates to DOT columns.
- READ and QUESTION: one Image container each, named MAIN; Source bound to media_name and four coordinates bound to MAIN columns.
- Standalone instructions, key checks, breaks, and endings: one MAIN each, with a fixed Source in the selected language and manually entered coordinates 1/1/0/0, independent of the table.
- All containers: Media scale=Original, Use as AOI off, Mouse click=None. MAIN has Gaze=None; enable Gaze only on the FIX DOT.
- Place the white MAIN beneath DOT. Verify visibility during an actual run; check the rendered layers as well as the list order.
- Display each 1920×1080 image at original size in rectangle (0,0,1920,1080), without the previous 60px top/bottom bars. Preserve scaling, cropping, typography, layout, and pagination; do not use Fit or stretch the images.

## 5. Common ordinary-stimulus properties and advancement

All ordinary stimuli: black background; Show mouse cursor off; Min presentation time enabled at 100 ms; Send TTL markers off; Time=None; Mouse click=None; Look away off; Media end=None. The 100 ms setting specifies minimum exposure; subsequent advancement follows the key or gaze conditions below. Verify that the default 2000 ms advancement is disabled in every new or copied template.

| Preset | Stimulus keyboard advancement | Container Gaze |
|---|---|---|
| INSTRUCTION_SPACE | Enabled, Space only | None |
| KEY_CHECK_P | Enabled, P only | None |
| KEY_CHECK_Q | Enabled, Q only | None |
| END_OPERATOR_7 | Enabled, 7 only | None |
| FIX | Disabled, no keys | DOT only: Continuous, 300 ms, Data loss reset 34 ms |
| READ | Enabled, Space only | None |
| QUESTION | Enabled, both Q and P advance | None |

__MASKED_TEXT_0087__

DOT Continuous requires one continuous dwell. Valid gaze leaving the container restarts the timer; 34 ms governs resetting after data loss. Keep Continuous, the specified region, and gaze-only advancement: no Accumulate, region enlargement, Space/7 bypass, or timeout bypass. The dot provides a local trigger/check without automatically correcting calibration error.

## 6. Three Groups per article

Each Group uses the same Tobii_Design table. Add two Subsets in order: article_block=current article, followed by row_type=fixation, reading, or question. Turn off Set at recording start for both; Values contains only the target value. Preserve original table-row order, with no Random/Shuffle/Repeat or additional filtering.

Create one internal Stimulus template per group. READ expands the selected rows into multiple reading images; QUESTION presents one question per article; FIX occurs once per article. Verify Excel row numbers, event_id, sample_screen, and media_name against the blueprint.

Practice uses G01–G09/P01–P03; H1 uses G10–G24/F01–F05; H2 uses G25–G39/F06–F10. BA_H1 starts at F01 even though its first article is B. FROM projects retain their normal parent project's numbering: AB_H2_FROM_B03 starts at F08/G31. All names are listed in the 84 blueprints for copying.

## 7. Top-level flows

Practice: PRACTICE_00_WELCOME → PRACTICE_01_READING_TASK → PRACTICE_02_QUESTION_KEYS_P_TRUE_Q_FALSE → PRACTICE_03_KEY_CHECK_INTRO → PRACTICE_04_KEY_CHECK_P → PRACTICE_05_KEY_CHECK_Q → PRACTICE_06_PRACTICE_INTRO → PRACTICE_07_CALIBRATION_INTRO → native Calibration+Validation → PRACTICE_08_FIXATION_INTRO → PRACTICE_09_START → FIX/READ/QUESTION for three articles → PRACTICE_10_END.

H1: FORMAL_00_INTRO → native Calibration+Validation → FORMAL_01_START_AND_BREAK_NOTICE → FIX/READ/QUESTION for the first five articles → FORMAL_02_BREAK (7 only to end recording).

H2: FORMAL_03_RECALIBRATION_INTRO → native Calibration+Validation → FORMAL_04_SECOND_HALF_START → FIX/READ/QUESTION for the last five articles → FORMAL_05_END (7 only to end recording).

Recovery: RECOVERY_00_RECALIBRATION_INTRO → native Calibration+Validation → RECOVERY_01_CONTINUE → FIX for the specified unread article, continuing through the last article of the half → original H1 break or H2 final-ending page. Omit the standard opening that announces five articles.

Opening and ending pages are standalone ordinary Stimuli, with no extra Group required. Each project contains exactly one native Calibration. If it cannot be renamed, retain its system name and record its position. Use native calibration functionality.

## 8. Calibration and onsite acceptance

Build settings: 9 targets, Validate Calibration on, Randomize target point order on, Target type Point, Calibration type Timed, white background and black targets. Calibration controls its own advancement; ordinary-stimulus 100 ms/Space settings do not apply. Verify the validation-point count separately in the software.

In Record, select Fusion120 and the correct participant display. Use Manager to recheck installation and display mapping. Perform native calibration and validation for each participant in each recording segment, regardless of any calibration performed in Manager. Evaluate actual quality point by point and eye by eye; reject poor results. The researcher must confirm and record acceptance thresholds, retry limits, and stopping rules.

The 56cm distance and active display area are planning targets. Record actual distance, model, installation, and tracking-range discrepancies truthfully; preserve metadata that reflects the measurements. Record actual brightness, ambient light, glasses stability, Refresh rate, Presentation latency, and export-filter settings. Use unmeasured/null for unknown values, not 0. Software building and static acceptance can proceed without hardware; hardware status remains pending.

## 9. Native-project checks and recovery

Complete 05_QA/ACCEPTANCE_CHECKLIST.md and ONSITE_CHECKLIST.md. In a short recording, leave each ordinary page untouched for at least 5 seconds to test for automatic advancement. Test both Q/P answers, 7 ending, and FIX continuous-dwell/region-exit behavior. Save, reopen, and export readable evidence.

If the pre-article FIX fails, record the incident and save the previous Recording. Confirm that no reading page from that article appeared. Open the FROM project for the same condition and half, using a new segment and new calibration. Record any previous reading exposure as an exception affecting first-reading status. See RECOVERY_POLICY.md. Preserve earlier segments and the established trigger and exclusion rules.

## 10. AOIs and analysis coordinates

06_REFERENCE_DO_NOT_IMPORT/AOI in the complete material package provides image-coordinate references: 71 screens and 1643 entries. Create and verify bunsetsu AOIs separately in Pro Lab. For the new 1080p layout, original-size MAIN starts at (0,0), so screen-to-image pixel offset=(0,0). Convert normalized coordinates using 1920/1080; avoid converting media coordinates twice. Confirm with actual ImageStart rectangles and native-resolution screenshots.

Archive the September 7 data separately. For that previous 1200p layout, y_screen−60 applies only when MAIN starts at y=60. Keep that offset separate from new recordings and record a display_profile_id for each configuration. At 56cm, a 32px character subtends approximately 0.899°, the 16px dot approximately 0.449°, and the 96×84 region approximately 2.695°×2.355°. These are near-axis visual-angle calculations. Verify tracking accuracy and trigger behavior onsite. DISPLAY_GEOMETRY.json contains the complete formulas and assumptions.
