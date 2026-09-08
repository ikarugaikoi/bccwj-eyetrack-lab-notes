# Pro Lab 25.7 Design Table Import Precision

The ZIP snapshots and qa outputs referenced here are held on the build host and in the native-project delivery evidence. The public source bundle provides the scripts and this incident description.

Status: on 2026-09-08, the user explicitly authorized continuation: "OK, record this deviation and continue building with it" (translated). Only the exact DOT_H / DOT_Y conversions listed in `ACCEPTED_DEVIATION.json` were accepted for the 84-project build. The original eight-decimal specification and failure reports were retained, with separate reports for checks under the accepted deviation.

The original Mac ZIP was retained, and all file-integrity checks passed. Both the actual DOT_H / DOT_Y values and their number formats in the original XLSX used 8 decimal places.

After using Update selected Design table in Pro Lab 25.7.1400 on VM __MASKED_LOCAL_ID_0001__ to update the independent new project D1080_PR_A_ZH, inspection of the saved native Current Design showed these conversions:

| Field | Mac target | Saved native table value | Actual geometry at 1080p | Difference from target |
|---|---|---|---|---|
| DOT_H | 0.07777778 | 0.0778 | 84.024 px | approximately +0.024 px |
| DOT_Y | 0.06666667 | 0.0667 | 72.036 px | approximately +0.036 px |

The combined bottom-edge difference is approximately +0.060 px. MAIN, DOT_W, and DOT_X are unaffected by this conversion. Effects on experimental results require separate assessment.

First comparison evidence: `../local_automation/bridge/responses/591787fb6e614669b389757a59bf38bb.zip`.

A compatibility experiment stored columns E/G as exact text in a separate `_TEXT8.xlsx` copy using artifact-tool. Worksheet-by-worksheet checks confirmed that only these two columns changed from numeric values to equivalent strings; other cell contents and formulas were unchanged. Pro Lab still saved the same four-decimal values. Second native snapshot: `../local_automation/bridge/responses/e422bcfac226403e940e1f18b07bca5e.zip`.

The preliminary suggestion in the discussion that the original file displayed only four decimals was withdrawn. Reading the format and checking the screenshots supplied with the Mac package confirmed eight decimals. Precision was lost during the current software import workflow. The software's private JSON/database and the original Mac checker's precision threshold were left unchanged. Failed checks remained recorded as failures.

Retain the original Mac checker and specification. Acceptance of this deviation requires an explicit acceptance record and separate derived results, alongside the difference report against the original eight-decimal specification. Use the original Mac XLSX as the import source. A strict eight-decimal requirement would require resolving the precision issue before acceptance.

The sample was restored using the original Mac XLSX, saved, and reopened. Of 750 bundled static checks, 742 passed; all 8 failures concerned DOT_H / DOT_Y and their effective bound values. The full table had 146 differences (73 rows × 2 columns). Native evidence: `../local_automation/bridge/responses/7e59968b23d342e092d2124a952a7604.zip`.

Inheritance comparison also found that the editor's top-level selected-object field had been cleared. Selecting PRACTICE_10_END through the UI restored that field to the page's exact native ID; the rest of the experimental design matched. Evidence: `../local_automation/bridge/responses/fafe2d4fd3594d34ae6f37d8b687b623.zip`. Subsequent inheritance checks recorded this one verified editor-selection change separately while maintaining all other experimental-setting requirements.

Further read-only inspection of `Tobii.Studio.AdvancedScreen.Design.dll` from a physical computer running the same version (25.7.1400.0) showed that `ExcelSheetFormatter.FormatCell` calls `Number.Format` for parseable numbers; the latter explicitly calls `Math.Round` to 4 decimal places. This explains the identical conversion of numeric and text cells. Method evidence and the DLL SHA256 are in `qa/import_formatter_evidence.json`. This binary evidence comes from the same-version installation on the physical computer; it has not been compared byte-for-byte with the VM DLL. The VM's actual import results were independently verified by the native snapshots above. The DLL, software, and private project data were left unchanged.
