# Onsite Pre-Session Checklist

For a confirmed 23.8-inch-class, 16:9, native-1080p participant display. Blank boxes indicate pending checks. Complete display verification before main-experiment reading.

## A. Before participant arrival: hardware and display

- [ ] Photograph the full Dell model label, measure active illuminated width/height excluding the bezel, and document the Fusion mounting position.
- [ ] Use Identify to confirm the participant display and extended desktop; the operator display must not mirror it.
- [ ] Participant display desktop mode and active signal are both 1920×1080, with 100% scaling; retain the actual refresh-rate setting.
- [ ] No stretching, overscan, or unintended black borders; notifications/sleep cannot interrupt; power and USB meet device requirements.
- [ ] Repeat Manager Display Setup for the mounted Dell; measure installation spacing and align the white markers as shown. Save the name and read-back geometry.
- [ ] Approximately 527×296mm active area and 3D installation geometry match the onsite measurements; verify the current installation against read-back data.
- [ ] Record the actual 120Hz setting and device serial number. Complete this check with the eye tracker connected.
- [ ] Fix display mode, brightness/contrast, and ambient lighting; record cd/m² as unmeasured if no photometer is available.

## B. Projects and images

- [ ] Open only clearly identified new-version copies; previous-project backups are readable; condition and language are correct.
- [ ] Every Project to be used has 1920×1080 presentation resolution, this complete package's _DELL1080 table, and verified bindings.
- [ ] Every fixed instruction MAIN has coordinates 1/1/0/0; check standalone instructions and article groups page by page.
- [ ] Original reading/question/white-background/instruction images are 1920×1080, use Original, and have a MAIN pixel rectangle of 1920×1080 at (0,0).
- [ ] DOT is 96×84 at (19.2,72); the visible 16×16 circle is centered approximately at (67.2,114); the white background does not obscure it and the trigger region is unchanged.
- [ ] All Sources resolve, with no red bindings; actual presentation has no cropping on any edge. Save native-resolution screenshots for pixel-level checks.
- [ ] Review static-checker results. Separately verify Use as AOI, layers, and version-specific unsupported fields; record unimplemented checks as pending.

## C. Operator end-to-end trial run

- [ ] Complete the operator's own native calibration and validation; verify tracking across the full screen/text area. Calibrate participants separately.
- [ ] Leave ordinary instruction, reading, and question pages untouched for at least 5 seconds; no automatic advancement occurs.
- [ ] FIX passes with gaze inside the region, stays blocked while looking away, and does not accumulate separate short dwells interrupted by valid exits.
- [ ] Space/7 cannot bypass FIX; READ accepts only Space; QUESTION ends with either P or Q.
- [ ] Adult practice key checks: P page accepts only P; Q page accepts only Q.
- [ ] End practice, the H1 break, and H2 with an actual 7 keypress and save. Space must not end them.
- [ ] Check repeated/held Space behavior for unintended skipping of the next page.
- [ ] Every article presents all READ pages from the table and exactly one question, with no duplication, omission, or ordering errors.
- [ ] Rehearse FIX interruption → save → FROM project → new calibration → correct unread starting article. Check the start/end of every recovery segment statically.
- [ ] A short recording exports successfully; actual ImageStart, resolution, and 120Hz sampling intervals of approximately 8.33ms agree with targets.

## D. After participant arrival, before each segment

- [ ] Use a consistent participant_code and record condition, language, half, segment, and display_profile_id.
- [ ] Posture/glasses are stable, with no substantial reflections or obstruction; target eye-to-screen-plane distance is approximately 56cm. Record reference plane and measurement; both eyes appear normal in Position Guide and calibration coverage is acceptable.
- [ ] Perform the participant's own Pro Lab native calibration and validation; inspect each point and eye, rejecting poor results.
- [ ] Check local text-area/dot localization. Label visual inspection as such; report only measured accuracy values.
- [ ] The researcher has confirmed pilot quality goals and manual intervention/retry rules for blocked FIX. Preserve the planned timeout and statistical-exclusion settings.
- [ ] Screen/tracker remain stationary after calibration; recheck calibration after substantial glasses or chair adjustments.

## E. Failures and session completion

- [ ] For a blocked FIX, record the last completed article, current FIX, whether READ appeared, cause, response, and previous/new recording linkage.
- [ ] Preserve gaze-only advancement, DOT size, and Continuous mode; do not add automatic bypasses or Accumulate.
- [ ] If quality remains clearly unacceptable after recalibration, stop the eye-tracking portion and label data status accurately. Respect discomfort and withdrawal.
- [ ] H1 rest has no forced automatic continuation; recalibrate for H2 and record rest duration.
- [ ] All recordings saved; export backups after writing has finished and verify readability. Retain TSVs, calibration results, settings, and logs.
- [ ] Verify new 1080p data with offset (0,0); keep the September 7 data under its original 1200p and Y−60 configuration.

Final decision (complete onsite):

```text
Configuration/file checks:
Live hardware checks:
Calibration/localization results:
Unverified or failed items:
Continue pilot, usage restrictions, and decision-maker:
```
