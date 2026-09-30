# 2026-09-30 Monitor height and validation-error trends

- Test date: 2026-09-30.
- Tester: Ikaruga.
- Test type: Exploratory equipment-positioning self-test with one person, excluded from the main-study participant sample.
- Original account language: Chinese.
- Document language: English.
- Translation review status: Not yet reviewed by a human.

Across these eighteen rounds, mean right-eye four-point validation Accuracy error was smaller when the monitor was raised, with the lowest value at 5.3 cm. The left eye did not show the same improvement. Only the last five rounds retain native results for the additional upper-left calibration point, so a complete comparison of six rounds at each of the three heights is not available for that point.

## Test method and data scope

A set of books was used to raise the monitor. The 10 cm and 5.3 cm elevations were the measured thicknesses of the whole set and approximately half the set, respectively. These numbers have no particular theoretical significance.

Three conditions were tested: no elevation, a 5.3 cm elevation, and a 10 cm elevation. Each block contained three rounds, in the following sequence, giving eighteen rounds in total and six at each height:

**10 cm → no elevation → 5.3 cm → 10 cm → no elevation → 5.3 cm.**

Ikaruga felt tired partway through the test, paused for a midday break, and resumed approximately two hours later.

The numerical results in this report were extracted from software files. The handwritten table is used only to identify rounds and heights, and its values no longer contribute to the numerical summaries. Earlier four-point validation metrics are reconstructed estimates from aligning the logs with the raw gaze stream; the final round was cross-checked against the natively saved results. Nine-point calibration metrics use the native results actually retained. The two sources are identified separately.

Accuracy is expressed in degrees (°); smaller values indicate smaller errors. The four validation locations are upper left, upper right, lower left, and lower right. The additional far-upper-left calibration point is summarized separately.

Round-by-round numerical comparisons support mapping handwritten rounds 1–7 to software log attempts 1–7, and rounds 8–18 to attempts 10–20. Log attempt 8 was an extra calibration not included in the handwritten table, for an unknown reason. Attempt 9 was a separate validation check triggered by accidentally selecting validation instead of recalibration. This report summarizes the eighteen handwritten rounds; the extra records remain archived.

The upper-right validation point in handwritten round eleven (log attempt thirteen) was treated as missing for both eyes because the tester was distracted. That round is excluded when calculating the mean across all four points, but its other three points are retained. Accordingly, the 10 cm condition has five complete validation rounds and the other two conditions have six each. Original software values and analysis values after missing-data handling are stored separately.

## Four-point validation results

The mean Accuracy across the four validation points was calculated for each complete round, then averaged across complete rounds at the same height, separately for each eye.

| Monitor elevation | Complete rounds | Mean left-eye error | Mean right-eye error |
| --- | ---: | ---: | ---: |
| None | 6 | 0.3532° | 0.5075° |
| 5.3 cm | 6 | 0.3615° | 0.4083° |
| 10 cm | 5 | 0.3578° | 0.4475° |

Relative to no elevation, mean right-eye error decreased by approximately **0.0993° (19.6%)** at 5.3 cm and **0.0601° (11.8%)** at 10 cm. Both repetitions of the condition sequence showed the ordering **5.3 cm < 10 cm < no elevation** for mean right-eye error.

Right-eye improvement did not occur at every validation point. At 5.3 cm, improvement was mainly at the upper-right and lower-right points; mean error at the upper-left validation point instead increased from approximately 0.544° without elevation to 0.597°.

Left-eye mean four-point error was similar across the three conditions and was slightly higher in both elevated conditions than without elevation. The left eye did not show the same overall improvement as the right eye.

## Additional upper-left calibration point

This is the far-upper-left point in nine-point calibration, distinct from the upper-left point in four-point validation. The software files retain native results for this point only for log attempts 16–20, corresponding to planned rounds 14–18. Missing earlier results are not filled in using OCR values.

| Monitor elevation | Rounds with native results | Mean left-eye error | Mean right-eye error |
| --- | ---: | ---: | ---: |
| None | 2 (planned rounds 14–15) | 0.4470° | 0.8090° |
| 5.3 cm | 3 (planned rounds 16–18) | 0.7900° | 0.9743° |
| 10 cm | 0 | Missing | Missing |

In these five available rounds, error at this point was greater at 5.3 cm, consistent in direction with the earlier handwritten observations. Because the numbers of available rounds differ and earlier results are missing, this partial comparison cannot be presented as a complete eighteen-round calibration comparison.

## Conclusions and interpretation

This single-person test suggests that monitor height may affect the eyes and screen locations differently: **raising the monitor was associated with a tendency toward smaller mean right-eye four-point validation error, lowest at 5.3 cm; left-eye validation did not show the same improvement. For the additional upper-left calibration point, the five retained native rounds showed greater error at 5.3 cm, but the available data do not permit a complete three-height comparison.**

This was an exploratory on-site test with limited design rigor and control: there was only one tester, conditions were presented in a fixed order, and a midday break of approximately two hours was taken because of fatigue. It is therefore difficult to separate monitor-height effects from changes in the tester's state.

The observed absolute differences in error across heights were small, also suggesting that personal state, fatigue, and attention may be more influential factors. This is one possible interpretation; the test did not compare the sizes of these factors' individual effects.

## Data sources

- [Software values, missing-data flags, and summary calculations](data/software_based_analysis.json)
- [Point-level software validation data and source labels](data/validation_points.csv)
- [Native upper-left calibration data](data/upper_left_calibration_native.csv)

The handwritten originals and earlier transcription remain archived as source records. The values, differences, and conclusions in this report have all been updated using the software data.

## Appendix: Accuracy values for the eighteen rounds

**All data below are from Ikaruga's own self-test.**

All values are in degrees (°). Each cell is ordered **left eye / right eye**, preserving the CSV's three-decimal precision. Rounds are numbered in the order of the eighteen-round test, with the corresponding software log attempt also shown.

Four-point validation values are the software-file reconstructed estimates, with the final round cross-checked against native saved results. The additional far-upper-left calibration column uses native saved values. “—” means that no native result was retained for that point; “Excluded” means the value was treated as missing because of distraction.

| Round | Log attempt | Elevation (cm) | Additional far-upper-left calibration | Validation upper left | Validation upper right | Validation lower left | Validation lower right |
| ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 1 | 10 | — / — | 0.182 / 0.513 | 0.326 / 0.755 | 0.678 / 0.183 | 0.165 / 0.345 |
| 2 | 2 | 10 | — / — | 0.314 / 0.078 | 0.345 / 0.318 | 0.130 / 0.285 | 0.161 / 0.393 |
| 3 | 3 | 10 | — / — | 0.295 / 0.602 | 0.514 / 0.699 | 0.121 / 0.435 | 0.310 / 0.507 |
| 4 | 4 | 0 | — / — | 0.447 / 0.546 | 0.160 / 0.222 | 0.427 / 0.416 | 0.283 / 0.803 |
| 5 | 5 | 0 | — / — | 0.336 / 0.596 | 0.168 / 0.771 | 0.647 / 0.068 | 0.417 / 0.575 |
| 6 | 6 | 0 | — / — | 0.176 / 0.316 | 0.368 / 0.459 | 0.036 / 0.269 | 0.430 / 0.611 |
| 7 | 7 | 5.3 | — / — | 0.347 / 0.405 | 0.562 / 0.288 | 0.756 / 0.253 | 0.534 / 0.782 |
| 8 | 10 | 5.3 | — / — | 0.814 / 0.692 | 0.386 / 0.258 | 0.629 / 0.087 | 0.369 / 0.263 |
| 9 | 11 | 5.3 | — / — | 0.073 / 0.569 | 0.105 / 0.412 | 0.301 / 0.310 | 0.352 / 0.192 |
| 10 | 12 | 10 | — / — | 0.596 / 0.695 | 0.455 / 0.277 | 0.355 / 0.227 | 0.289 / 0.561 |
| 11 | 13 | 10 | — / — | 0.635 / 0.682 | Excluded / Excluded | 0.268 / 0.438 | 0.363 / 0.360 |
| 12 | 14 | 10 | — / — | 0.619 / 0.811 | 0.109 / 0.775 | 0.808 / 0.132 | 0.384 / 0.358 |
| 13 | 15 | 0 | — / — | 0.324 / 0.393 | 0.371 / 0.635 | 0.281 / 0.438 | 0.291 / 0.370 |
| 14 | 16 | 0 | 0.561 / 0.740 | 0.220 / 0.573 | 0.416 / 0.778 | 0.421 / 0.202 | 0.108 / 0.607 |
| 15 | 17 | 0 | 0.333 / 0.878 | 0.263 / 0.839 | 0.401 / 0.563 | 0.539 / 0.417 | 0.947 / 0.714 |
| 16 | 18 | 5.3 | 0.657 / 0.902 | 0.513 / 0.963 | 0.412 / 0.519 | 0.261 / 0.342 | 0.089 / 0.124 |
| 17 | 19 | 5.3 | 0.781 / 0.964 | 0.403 / 0.336 | 0.257 / 0.253 | 0.435 / 0.629 | 0.109 / 0.428 |
| 18 | 20 | 5.3 | 0.932 / 1.057 | 0.324 / 0.618 | 0.211 / 0.610 | 0.283 / 0.400 | 0.151 / 0.065 |

The original CSV values for the upper-right point in round 11 (log attempt 13) were 3.517° for the left eye and 2.335° for the right eye. They were excluded from the statistics because the tester confirmed being distracted. Extra log attempts 8 and 9 are not among the eighteen rounds in this table.
