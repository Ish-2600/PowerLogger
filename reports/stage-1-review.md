# Independent Stage 1 review

Review date: 2026-11-06. Reviewer: separate model session, independent of the authoring session. Scope: project specification, original source, fixture, planned hardware/pins and completion gates. This is a design-document review, not a review of completed firmware or PCB files.

Verdict: useful, accurate baseline; no fundamental architecture blocker identified.

| Finding | Resolution |
| --- | --- |
| Missing measurable accuracy/calibration gate | Added provisional voltage/current/zero-offset limits, reference uncertainty requirement, error-budget and thermal validation criteria. |
| Freshness/timing insufficiently defined | Added averaging/conversion settings, timeout, conversion-ready requirement and completion timestamp; explicitly distinguish sequential from simultaneous acquisition. Stage 2 must test stale-data rejection and measure skew. |
| Every-module verification could be ambiguous | Added required module-to-test matrix, fault injection and separate adapter bench tests. |
| PCB release criteria insufficiently explicit | Added zero unrouted connections, schematic/layout consistency, reviewed ERC/DRC, protection envelope and separate CAD/vehicle-use release boundaries. |
| Original helper line count incorrect | Corrected to 21 lines. |

Reviewer independently confirmed fixture statistics, shunt arithmetic, INA226 scaling/range and proposed GPIO availability on the specified DevKitC. Datasheet/board reference links are in `docs/STAGE_1_DESIGN.md`.

A later user correction superseded the initial `.env` plan: no `.env` or `.env.example` is supplied. `.gitignore` excludes sensitive local files. The original contact-bearing PDF remains on disk and was removed from the Git index; existing history was not rewritten. This supersedes the reviewer's earlier observation about the temporary empty `.env` file.

All requested specification corrections have been incorporated. Hardware acceptance targets remain unmeasured until parts are assembled and tested. Independent implementation and hardware-design review are still required in later stages.

## Folder organization follow-up

The independent reviewer checked the reorganized folder, navigation links and updated dataset paths. Its one finding (the archived original README reference) was corrected. File-content checks, the relocated C++ syntax check and the input audit all passed after the move.
