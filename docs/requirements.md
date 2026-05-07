# 要件定義

## 目的

取り込み・バッチ処理・出力フロー は、Blenderで複数素材を取り込み、変換、出力する制作者 が 取り込み元、処理プリセット、出力先、失敗時アクションをバッチ単位で確認する。

## Source

- PICKUP Rank: 58
- Domain / Idea No: BlenderAddon / 3
- Repository: blender-import-batch-export-flow
- created_idea: `D:/AI/BlenderAddon/created_idea_003_blender-import-batch-export-flow`
- ZIP: `D:/AI/BlenderAddon/created_idea_003_blender-import-batch-export-flow/idea_003_blender-import-batch-export-flow.zip`
- README確認: 開始時点では正式 repo が存在しないため、README.md は存在しない。

## Functional Requirements

- R1: batchName、importPath、operation、exportPath を必須項目として検査する。
- R2: 必須項目不足は fail として分類する。
- R3: `presetUnverified` が true の場合は warning として分類し、手動確認理由を返す。
- R4: 複数アイテムの mixed-batch を pass / warning / fail に集計する。
- R5: 結果を CLI と docs/release evidence で再利用できる形にする。

## Non Functional Requirements

- UTF-8 で Markdown / JSON / JS / HTML / Python を保存する。
- 外部通信を既定で行わず、サンプルとローカル入力だけで検証できる。
- 手動テスト未実施であることを release 前 docs に明記する。

