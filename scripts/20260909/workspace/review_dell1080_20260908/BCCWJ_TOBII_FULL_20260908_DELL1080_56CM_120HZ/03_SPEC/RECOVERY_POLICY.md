# Recovery After a Failed Pre-Article Check

## Scope

This procedure applies when an article is blocked at its FIXATION_CHECK and none of its reading pages has been displayed. The experiment has no page-by-page drift checks within articles and no projects for resuming halfway through an article. Record interruptions during reading as incidents and flag the affected exposure.

The dot provides a local gaze trigger. If it fails, check eye position, tracking loss, display mapping, and trigger settings; use those findings to decide whether to recalibrate.

## Procedure

1. Identify the current article's FIX and confirm that none of its READ images has appeared. Record the last completed article, current article_block, and original half.
2. If recalibration is needed, end the current Recording using the operator's Stop recording command or an onsite-verified Esc/Shift+Esc method. Save the recording, including all preceding data.
3. Select the FROM project for the current article, with the same condition and H1/H2. If this is the first article of the half and its reading pages have never appeared, reuse the normal project.
4. Use the same participant_code. Create a new segment Recording and explicitly record its relationship to the previous segment; verify cross-project linkage of Participant records.
5. Present the recovery introduction, perform fresh native Calibration+Validation, and inspect the results.
6. After acceptance, present the continuation instruction and then the current article's FIX. Reading begins only after the configured FIX condition is met.
7. Complete the remaining articles of the half in their original order. Retain the appropriate break or final-ending page for that half.

## Identifier continuity

Preserve event_id, article_id, article_block, sample_screen, original formal_article_position, Group names, and internal Stimulus names during recovery. For example, B03 in AB_H2 remains F08 and G31–G33 when resuming from B03; retain its original numbering.

Example Recording names are `S001_AB_H1_SEG01` and `S001_AB_H1_SEG02_FROM_A03`. S001 illustrates naming; stimulus content remains as specified. Also record each segment's actual global start/end times and check its time base when aligning multiple Recordings.

## Incident handling

- Record exposure whenever a reading image has appeared, even for a single page. Flag rereading separately from first reading.
- For interruptions during reading or questions, retain the recording and flag the affected article. Apply the prespecified main-analysis rule. If a rule is missing, document the researcher's decision without selecting treatment based on observed data quality.
- A failed FIX before the next article cannot establish when drift began during the previous article. Assess completed data using the documented quality criteria.
- Preserve gaze-only FIX advancement; do not add keyboard bypasses or two-second automatic timeouts to reduce failures.
- Repeated FIX failure on the same unread article may be handled by restarting the same FROM project. The researcher must finalize retry limits and stopping rules.

## Incident record

Copy 05_QA/INCIDENT_LOG_TEMPLATE.json for each incident. Include at least participant_code, condition, half, segment, previous/new Recording, last completed article, recovery article, whether reading appeared, interruption reason, actual response, and calibration results. Template null values indicate unfilled fields; enter observed results truthfully.
