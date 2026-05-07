# 取り込み・バッチ処理・出力フロー

blender-import-batch-export-flow は Blenderで複数素材を取り込み、変換、出力する制作者 向けの closed alpha プロダクトです。取り込み元、処理プリセット、出力先、失敗時アクションをバッチ単位で確認する。

## Source

- PICKUP Rank: 58
- Domain / Idea No: BlenderAddon / 3
- Repository: blender-import-batch-export-flow
- 主な公開先: GitHub Release / BOOTH
- created_idea: `D:/AI/BlenderAddon/created_idea_003_blender-import-batch-export-flow`
- 同梱ZIP: `D:/AI/BlenderAddon/created_idea_003_blender-import-batch-export-flow/idea_003_blender-import-batch-export-flow.zip`
- 開始時 README: 存在しない


## Alpha Scope

- 代表シナリオ4件の自動検証
- 必須項目不足、警告、混在バッチの分類
- src/blender/ のホスト連携シェル
- QCDS、security/privacy、traceability、release checklist、manual test docs
- docs ZIP: `dist/blender-import-batch-export-flow-docs.zip`

## Commands

```powershell
npm test
node src/cli/index.js samples/representative-suite.json
npm run build:docs
```

手動テストは Codex 側では未実施です。手順は `docs/manual-test.md` と `docs/strict-manual-test-addendum.md` にあります。

