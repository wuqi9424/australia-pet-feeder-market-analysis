# GitHub Publish Checklist

## Completed package preparation

- [x] Personal interview-preparation materials excluded.

- [x] Public data allowlist used; only six sanitised derived CSVs included.
- [x] Full raw/processed review text and acquisition artifacts excluded.
- [x] No account/session evidence, cookies or internal hash manifests copied.
- [x] Code uses portable repository-relative data locations; no credentials or network acquisition.
- [x] CSV UTF-8/Boolean/null values checked against frozen sources.
- [x] Descriptive modules and boundary tests run locally.
- [x] Public metrics/claims preserve sample and decision limits.
- [x] Recommendation marked recommended_for_validation; price range not WTP/launch price.
- [x] Tableau explicitly pending; preview slots are not screenshots.
- [x] Relative links checked; no absolute machine/private paths in the release.
- [x] MIT code/docs scope separated from third-party/derived data terms.
- [x] .gitignore excludes raw/private/session/temp material while allowing future final dashboard files.

## Owner checks before publishing

- [ ] Review README in GitHub's rendered preview, including tables, Mermaid in the workflow document and links. Local structural checks do not prove GitHub rendering.
- [ ] Review the complete staged file list/diff; initialise Git only inside this release folder, not the parent research workspace.
- [ ] Run a fresh secret scan immediately before upload; the current content review is not a guarantee about future edits.
- [ ] Review source/platform terms and attribution for the demonstration tables; MIT is not a data licence.
- [x] Owner-created repository configured as origin: `https://github.com/wuqi9424/australia-pet-feeder-market-analysis.git` on `main`.
- [ ] Obtain owner confirmation for the reviewed commit/push. This audit does not stage or publish files.
- [ ] After Tableau is actually built, add valid PNGs and optionally a reviewed package, update placeholders and record real native status.

The configured remote exists. Current working-tree changes remain uncommitted and unpushed by this audit; prior repository history is preserved. The internal pre-push audit remains local; it is not part of the public release.
