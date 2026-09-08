# Evidence for Independent Review on Mac

Create a separate `BCCWJ_PILOT_20260909_DELL1080_REVIEW` package, adjusting the date to the actual collection day. Keep it separate from the September 7 data. Use private transfer and exclude recruitment contact details and unnecessary identifying information.

## Required contents

1. `00_README.md`: actual collection date, anonymous participant_code, order/language/half/segment, associated Project/recording, completeness, incidents, and recovery article. Distinguish planning assumptions from measurements.
2. `01_NATIVE/`: backups of each actually used project/recording, exported through supported software methods. Retain designs, resources, raw recordings, and calibration/validation files. Create independent backups after recording writes finish. Verify that they open or pass structural/ZIP integrity checks.
3. `02_TSV/`: Recording gaze data with all columns, microsecond timestamps, and a single standard file format. Preserve raw gaze, both-eye validity, pixel and normalized coordinates, native eye positions, actual keys, Stimulus/ImageStart/ImageEnd, presentation resolution, media rectangles, sampling rate, and validation fields where available. Document missing fields without fabricating values.
4. `03_DESIGN/`: actual imported Excel files and per-Project verification of tables, Subsets, fixed Sources, bindings, and timing, including `check_native_project.py` output. Map original logical Project names to DELL1080 copy names.
5. `04_DISPLAY_AND_DEVICE/`: Dell model photograph, measured active area, Fusion installation photographs and screen-relative measurements, screenshots of Windows display selection/desktop+active signal/scaling/refresh rate, Manager Display Setup and read-back geometry, Pro Lab Record device frequency/display selection, each Project's resolution, and native-pixel presentation screenshots. Read-only SDK output is optional; SDK installation is not required.
6. `05_CALIBRATION/`: average and per-point/per-eye results, screenshots, and native files for every calibration/validation. Retain rejected attempts and retries as well as the accepted result.
7. `06_SETTINGS_AND_LOGS/`: completed onsite checklist, SITE_LOG_TEMPLATE.json copy, I-VT export-setting screenshots, configured PresentationLatency and whether it was independently measured, reference planes for eye-to-screen/tracker distances, brightness/ambient conditions, glasses/head-support status, breaks, and interruption logs. Use null/unmeasured for missing values.
8. `SHA256SUMS`: hash at least the native packages, original TSVs, and actual Excel files. Verify ZIP readability after compression; record package size and hash in README.

## Mac review objectives

- Confirm actual native-recording resolution of 1920×1080 and agreement between display area and onsite measurements, checking both recording and configuration evidence.
- Verify actual MAIN ImageStart at 1920×1080 at (0,0), DOT approximately 96×84 at (19.2,72), and PNG hashes matching the source materials.
- Recheck the relationship between gaze pixel and normalized columns; ensure that the previous Y−60 offset has not been applied to new recordings.
- Quantify 120Hz sampling, missing data/long gaps within reading pages, both-eye validity, and coordinate availability separately.
- Verify complete per-article event order, each page's Space, P/Q scoring, 7 endings, and recovery deduplication; flag affected articles' exposure accurately.
- Assess whether calibration/validation and local localization support bunsetsu-level analysis. A single pilot does not establish statistical power.

Return original evidence and itemized results. If an export function or field is unsupported, include the actual screen, error description, and outstanding checks.

## Optional read-only device-geometry export

Use only if a compatible official `tobii_research` Python SDK is already installed on the acquisition computer:

```powershell
py -3 05_QA\read_tracker_config.py --output "__MASKED_LOCAL_PATH_0921__"
```

The script discovers devices and reads current/available sampling rates, display-area dimensions, and 3D corners. It leaves calibration selection, frequency, and screen mapping unchanged. All detected devices are listed; the operator matches the actual serial number. If the device or SDK is unavailable, record unknown status. This optional step uses the compatible environment already configured onsite. Output includes device serial numbers and belongs only in the private research handoff package. Mock-getter tests have been completed; verification with an actual Fusion remains pending.
