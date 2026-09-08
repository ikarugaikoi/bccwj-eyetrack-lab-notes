# Copying Chinese Projects to Japanese

Complete the 42 Chinese projects first, then make their 42 Japanese counterparts, for 84 projects total. Check each Japanese copy using the steps below.

## Per-project procedure

1. Read the project's `clone_from_project_name` in SELECTED_BUILD_PLAN.json. Locate the Chinese source project that has been saved, reopened, and passed static checks. Use that verified source rather than a previous pilot.
2. Create an **independent copy** through a design-copy or design-export/import interface supported by the installed Pro Lab version. Verify its separate path and project identity. If a proposed command is unavailable, identify a supported design-copy method; leave private configuration files untouched.
3. Use the task's `project_name`, changing only the final `_ZH` to `_JA`. Preserve the condition, H1/H2, and FROM starting article.
4. Import the 19 images from instructions_JA into the Japanese copy's library. Retain the existing Excel table, media_name column, and Chinese source-project files.
5. Apply each `instruction_replacements` entry: find the ordinary instruction stimulus by `stimulus_name`, locate MAIN, and change its fixed Source from the Chinese image to the specified Japanese image. Keep the container and stimulus intact so their advancement parameters are preserved.
6. Check every listed page, including P/Q key checks, practice ending, half-time break, final ending, and the two recovery instructions.
7. Compare with the Japanese blueprint and verify that every referenced instruction points to `_JA`. Unreferenced Chinese images may remain in the library.
8. Compare all non-language settings with the Chinese source. Save and reopen the Japanese copy. Confirm that the Chinese source still references `_ZH` and remains unchanged.
9. Record static, runtime, hardware, and export acceptance separately for the Japanese copy, including its own trial run and hardware checks.

## Permitted changes

- Project name and independent storage location; internal project/object identifiers created by the software.
- Fixed Source in each instruction MAIN container (`_ZH` → `_JA`) and added Japanese media items.
- Language, source-project, and evidence-path fields in build logs.

## Required invariants

- Selection and contents of the four Excel files, design-table bindings, and article_block/row_type Subsets.
- Reading and comprehension-question images, original event_id, article order, G/P/F numbering, and Group/Stimulus names.
- MAIN/DOT layout, Original scaling, background, layers, minimum 100 ms, and Time=None.
- READ=Space; QUESTION accepts both Q/P; key checks P then Q; endings=7; FIX has no keys.
- DOT Continuous 300 ms/reset 34 ms, and all disabled Mouse/Look away/Media end conditions.
- Native calibration/validation settings and location. The calibration software's system-language interface is outside the PNG replacement scope; retain native functionality.

Copy design and materials without Recording/Participant data where supported. If the available copying method includes recordings, first inspect the software's design-export options. Keep copied Chinese test recordings separate from Japanese trial-run evidence and preserve the identity of real participant records. Retain the original Chinese projects and previous pilot data.
