# Read-Only Checker Usage

Run from the complete material-package root with the required images, workbooks, and related inputs available. The first two checkers use the Python 3.8+ standard library. Replace masked paths in the public source bundle with actual authorized paths.

## 1. Complete material package

```powershell
py -3 05_QA\verify_package.py
```

Checks SHA256, PNG integrity and dimensions, actual XLSX XML, P/Q mappings, coordinates and ordering in four tables, 84 flows, and 142 language replacements. Run final transfer acceptance without --preflight, which skips hashes.

## 2. Readable native design exported by the software

```powershell
py -3 05_QA\check_native_project.py --project-root "__MASKED_LOCAL_PATH_0918__" --expected-project "BCCWJ_EyeTrack_FORMAL_AB_H1_ZH" --output "__MASKED_LOCAL_PATH_0919__"
```

--project-root must point exactly to the exported/extracted root containing Data/Design and Data/Names. For --expected-project, use the planned name from PROJECT_SCOPE.csv even if the actual name has a _DELL1080 suffix. Current is read by default; add --version 0 only when the export explicitly uses version 0. Inputs remain unchanged. Place output outside the input project directory.

For known 25.7-style structures, checks cover flow sequence, table rows/bindings/fixed Sources, dimensions, keys, timing, native calibration settings, Continuous, and data-loss reset. Report unsupported versions or unparseable structures. STATIC_CHECKS_PASSED_NOT_HARDWARE_VERIFIED indicates that the covered fields passed.

Use ONSITE_CHECKLIST to verify rendered layers and transparency, Use as AOI, display selection/scaling/physical installation, actual sampling/display timing, calibration quality, live keyboard/gaze behavior, and complete recording.

## 3. Optional read-only device output

Use only when a compatible official tobii_research SDK is already installed and the device is connected onsite:

```powershell
py -3 05_QA\read_tracker_config.py --output "__MASKED_LOCAL_PATH_0920__"
```

This read-only step leaves installation, sampling rate, calibration, and mapping unchanged. Record unknown status when the SDK or device is unavailable. Keep hardware serial numbers in private research records.
