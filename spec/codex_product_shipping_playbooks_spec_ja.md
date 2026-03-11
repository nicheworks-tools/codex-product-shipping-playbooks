# Codex Product Shipping Playbooks 仕様書

## 1. 文書の目的

本仕様書は、**Codex 向けに使える product shipping playbooks を、独自構造で設計・実装・公開するための基準文書**である。

本プロジェクトは、既存の Claude 系 skills リポジトリの**発想だけ**を参考にするが、**構造・命名・責務・公開物の見せ方は別物として再設計する**。

本仕様書は **MVP だけを定義する文書ではない**。MVP は通過点とし、最終的には **公開価値のある完成版** をゴールとする。

---

## 2. プロジェクトの基本方針

### 2.1 このプロジェクトは何か
このプロジェクトは、一般的な PM スキル集ではない。

これは、**既存 repo を前提に、仕様整理・実装計画・出荷確認・振り返りを反復可能にする playbooks / workflows 集**である。

### 2.2 このプロジェクトが目指すもの
以下の流れを、一定の品質で繰り返せる状態を目指す。

1. repo の現状把握
2. 変更要求の整理
3. 仕様差分の定義
4. 実装計画の作成
5. 受け入れ条件の定義
6. ship 前確認
7. docs / release artifacts 作成
8. 差分レビューと振り返り

### 2.3 このプロジェクトが目指さないもの
以下は主目的にしない。

- 一般的な PM フレームワーク集
- 市場分析テンプレ集
- GTM / OKR / persona 中心の上流文書集
- Claude skills 形式のクローン
- skill catalog そのものを再現すること

---

## 3. 差別化の前提

### 3.1 なぜそのままの skills 構造を採用しないのか
`skills/` や `SKILL.md` を中心にした構造は、外から見ると既存の Claude / Codex skills リポジトリの延長に見えやすい。

そのため本プロジェクトでは、**公開物の本体を playbook / workflow 中心にする**。

### 3.2 本プロジェクトの公開物の本体
公開物の本体は以下である。

- `playbooks/`
- `artifacts/`
- `gates/`
- `flows/`
- `adapters/`

必要であれば後から **Codex 互換形式へ変換する adapter** を用意するが、最初から skills 形式を本体にはしない。

### 3.3 公開価値の定義
公開価値は、次の一文で説明できなければならない。

**「Codex を、repo の中で仕様整理から出荷確認までより実務的に動かすための shipping workflow kit」**

---

## 4. 対象ユーザー

### 4.1 主対象
- 既存 repo を持つ個人開発者
- 小規模チームの開発者
- 仕様整理と実装 handoff を安定させたい人
- docs / changelog / pre-ship review を体系化したい人

### 4.2 副対象
- OSS メンテナ
- issue 駆動で作業する開発者
- release 前確認が属人化しているチーム

### 4.3 主対象にしない層
- アイデア段階のみの利用者
- 一般 PM 資料だけ欲しい利用者
- 市場分析や GTM を主目的とする利用者

---

## 5. 設計原則

### 5.1 clean-room 原則
- 既存 OSS の発想・問題意識・思想は参考にしてよい
- 文面、見出し構成、名前、テンプレ本文の直接転用は禁止
- README、命名、構成、責務は独自に書き直す

### 5.2 workflow-first 原則
- 思考カテゴリではなく、**repo 内で起きる作業フロー**を単位にする
- playbook は「いつ使うか」「何を出すか」「次にどう繋ぐか」が明確であること

### 5.3 shipping-first 原則
- 一般論より、spec / plan / acceptance / ship / retro を優先する
- docs / release artifacts / rollback / monitoring まで含める

### 5.4 adapter 原則
- 本体は独自構造で保持する
- 必要なら後から Codex 互換形式へ書き出す
- 互換のために本体設計を既存構造へ寄せない

### 5.5 local-first 原則
- ローカル Git 管理を前提とする
- markdown / text / scripts で可搬性を保つ
- 外部サービス依存を最小化する

---

## 6. 完成版の到達像

完成版では、以下を満たすことを目標とする。

### 6.1 構造面
- playbook / artifact / gate / flow / adapter の責務が分離されている
- repo 全体ルールは `AGENTS.md` にまとまっている
- docs だけで全体構造が理解できる

### 6.2 機能面
- 7〜9 個のコア playbook が存在する
- 各 playbook に必要な artifacts / gates / examples がある
- 実案件で issue → ship まで一周できる
- release artifacts と retro まで含む

### 6.3 品質面
- playbook 間の責務境界が明確
- artifact 名と gate 名が分かりやすい
- README だけで何に使うものか伝わる
- 「Codex で使う意味」が一文で説明できる

### 6.4 公開価値面
- Claude 系 skills のクローンに見えない
- 一般 PM テンプレ集にも見えない
- repo-aware / implementation-aware / ship-aware な価値が明確

---

## 7. 完成版ディレクトリ構成

```text
codex-product-shipping-playbooks/
├─ AGENTS.md
├─ README.md
├─ LICENSE
├─ .gitignore
├─ docs/
│  ├─ vision.md
│  ├─ architecture.md
│  ├─ workflows.md
│  ├─ artifacts-model.md
│  ├─ release-model.md
│  ├─ roadmap.md
│  ├─ quality-gates.md
│  ├─ naming.md
│  └─ changelog.md
├─ playbooks/
│  ├─ intake-repo/
│  │  ├─ PLAYBOOK.md
│  │  ├─ artifacts/
│  │  ├─ gates/
│  │  ├─ scripts/
│  │  └─ flow-example.md
│  ├─ spec-delta/
│  ├─ plan-change/
│  ├─ define-acceptance/
│  ├─ ship-check/
│  ├─ write-release-artifacts/
│  ├─ review-diff/
│  └─ post-ship-retro/
├─ artifacts/
│  ├─ spec-delta-template.md
│  ├─ change-plan-template.md
│  ├─ acceptance-template.md
│  ├─ pre-ship-review-template.md
│  ├─ release-note-template.md
│  ├─ changelog-entry-template.md
│  └─ rollback-note-template.md
├─ gates/
│  ├─ repo-intake-gate.md
│  ├─ spec-delta-gate.md
│  ├─ acceptance-gate.md
│  ├─ pre-ship-gate.md
│  ├─ release-artifacts-gate.md
│  └─ retro-gate.md
├─ flows/
│  ├─ issue-to-ship.md
│  ├─ repo-change-flow.md
│  ├─ diff-to-retro.md
│  └─ release-prep-flow.md
├─ examples/
│  ├─ small-repo/
│  ├─ issue-driven/
│  └─ release-cycle/
├─ scripts/
│  ├─ validate_structure.py
│  ├─ check_required_files.py
│  ├─ lint_markdown.py
│  └─ build_index.py
├─ adapters/
│  ├─ README.md
│  └─ export_codex_skill_format.py
└─ archive/
   ├─ deprecated-playbooks/
   └─ old-artifacts/
```

---

## 8. 各トップレベル要素の責務

### 8.1 `AGENTS.md`
repo 全体に適用する上位ルール。

#### 必須記載項目
- この repo は shipping playbooks であること
- skills クローンを目指さないこと
- 命名規則
- playbook 追加ルール
- artifact / gate / flow の責務分離
- repo を読んでから判断する原則
- docs / tests / release 観点を忘れない原則
- 禁止事項

### 8.2 `docs/`
思想、構造、命名、品質基準を固定する文書群。

### 8.3 `playbooks/`
実際の作業単位を定義する中核。

### 8.4 `artifacts/`
各 playbook が出力・参照する雛形を置く。

### 8.5 `gates/`
完了判定や確認観点を置く。

### 8.6 `flows/`
複数 playbook をまたいだ利用シナリオを置く。

### 8.7 `adapters/`
必要に応じて外部形式へ変換するための補助層。

---

## 9. `playbooks/` の仕様

### 9.1 基本原則
- 1フォルダ = 1作業責務
- 思考カテゴリではなく workflow 上の役割で分ける
- 各 playbook は「次に何へ繋ぐか」が明確であること

### 9.2 各 playbook フォルダの必須構成

```text
playbooks/<playbook-name>/
├─ PLAYBOOK.md
├─ artifacts/
├─ gates/
├─ scripts/
└─ flow-example.md
```

### 9.3 `PLAYBOOK.md` の必須項目
1. Playbook 名
2. 目的
3. いつ使うか
4. いつ使わないか
5. 必要な入力
6. 生成・更新する artifacts
7. 通過すべき gates
8. 手順
9. 注意事項
10. 次に繋ぐ playbook
11. 例

---

## 10. コア playbook 一覧

完成版では、以下 7 playbook をコアとする。

### 10.1 `intake-repo`
#### 目的
repo の構造、主要ファイル、制約、入口、既存作法を把握する。

#### 主な出力
- repo context memo
- key files list
- constraints list
- missing context notes

### 10.2 `spec-delta`
#### 目的
現状と変更要求の差分を整理し、仕様差分を定義する。

#### 主な出力
- spec delta draft
- in-scope / out-of-scope
- impacted surfaces
- assumption list

### 10.3 `plan-change`
#### 目的
仕様差分を実装計画へ落とし込む。

#### 主な出力
- change plan
- touch points
- implementation steps
- docs impact notes

### 10.4 `define-acceptance`
#### 目的
受け入れ条件、確認観点、手動テスト観点を定義する。

#### 主な出力
- acceptance definition
- edge cases
- done checklist
- manual verification notes

### 10.5 `ship-check`
#### 目的
ship 前に必要な確認を行い、抜け漏れを減らす。

#### 主な出力
- pre-ship review
- blockers / risks
- release readiness notes

### 10.6 `write-release-artifacts`
#### 目的
release note、changelog、必要な docs 更新を整理・作成する。

#### 主な出力
- release note draft
- changelog entry
- docs update memo
- user-facing summary

### 10.7 `review-diff`
#### 目的
diff / PR / 実装結果をもとに、変更の要約と学びを抽出する。

#### 主な出力
- change summary
- review notes
- follow-up items

### 10.8 `post-ship-retro`（拡張コア）
#### 目的
出荷後の結果をもとに振り返りを行い、次回改善を定義する。

#### 主な出力
- retro memo
- lessons learned
- next improvements

※ 完成版では含める。Foundation では後回し可。

---

## 11. `artifacts/` の仕様

### 11.1 役割
playbook が出力または更新する成果物の雛形を置く。

### 11.2 初期 artifact 一覧
- `spec-delta-template.md`
- `change-plan-template.md`
- `acceptance-template.md`
- `pre-ship-review-template.md`
- `release-note-template.md`
- `changelog-entry-template.md`
- `rollback-note-template.md`

### 11.3 artifact の要件
- 実務でそのまま使えること
- 抽象論で終わらないこと
- 誰が見ても用途が分かる名前であること

---

## 12. `gates/` の仕様

### 12.1 役割
各段階で「通っているか」を確認するための基準を置く。

### 12.2 初期 gate 一覧
- `repo-intake-gate.md`
- `spec-delta-gate.md`
- `acceptance-gate.md`
- `pre-ship-gate.md`
- `release-artifacts-gate.md`
- `retro-gate.md`

### 12.3 gate の要件
- 確認項目が具体的であること
- 過剰に長くしないこと
- 実装 / docs / ship 観点を含むこと

---

## 13. `flows/` の仕様

### 13.1 役割
複数 playbook をどう繋いで使うかを示す。

### 13.2 初期 flow 一覧
- `issue-to-ship.md`
- `repo-change-flow.md`
- `diff-to-retro.md`
- `release-prep-flow.md`

### 13.3 flow の要件
- どの順番で playbook を使うかが分かること
- 入力と出力の受け渡しが分かること
- 単独 playbook ではなく全体の流れが見えること

---

## 14. `adapters/` の仕様

### 14.1 役割
独自構造の本体を、必要なら他形式へ変換する。

### 14.2 初期 adapter
- `export_codex_skill_format.py`

### 14.3 adapter の方針
- adapter は補助層であり、本体ではない
- adapter の都合で本体構造を歪めない
- まずは export のみを想定し、import は後回し

---

## 15. 命名規則

### 15.1 playbook 名
- 動作が分かる kebab-case
- 例: `spec-delta`, `ship-check`

### 15.2 artifact 名
- `<purpose>-template.md`
- 例: `change-plan-template.md`

### 15.3 gate 名
- `<purpose>-gate.md`
- 例: `pre-ship-gate.md`

### 15.4 flow 名
- `<context>-flow.md` または `<from>-to-<to>.md`

### 15.5 script 名
- snake_case を基本とする

---

## 16. 文体仕様

### 必須方針
- 初心者にも意味が通る平易な文体
- 抽象語だけで逃げない
- repo / files / tests / docs / release など具体語を優先する
- 次の作業に繋がる形で書く

### 禁止方針
- 「万能」「最強」「確実」などの誇張語
- 一般 PM 論だけに寄ること
- 既存 skills リポジトリの文法に寄せること
- 責務が曖昧な playbook を作ること

---

## 17. 品質基準

各 playbook は以下を満たすこと。

1. 一文で役割を説明できる
2. 使う場面 / 使わない場面が明確
3. 入力 / 出力が具体的
4. 対応する artifact と gate がある
5. 次に繋ぐ playbook が定義されている
6. repo-aware / implementation-aware / ship-aware のどれかに明確に寄与する
7. Codex で使う意味が説明できる
8. 実案件で試せる flow がある

---

## 18. MVP と完成版の関係

### 18.1 MVP の位置付け
MVP は以下 5 playbook を中心に、一周回せる状態を指す。

- `intake-repo`
- `spec-delta`
- `plan-change`
- `define-acceptance`
- `ship-check`

これに対応する最小 artifact / gate / flow を揃え、実案件で issue → ship 直前まで回せる状態を MVP とする。

### 18.2 完成版との差
完成版では以下を追加で満たす。

- `write-release-artifacts`
- `review-diff`
- `post-ship-retro`
- adapter の整備
- docs / flows / examples の充実
- scripts の拡張

### 18.3 仕様上の考え方
本仕様書は MVP のためだけに構造を簡略化しない。完成版の構造を先に定義し、必要な部分から順に埋める方式を採る。

---

## 19. 初期マイルストーン

### Phase 1: Foundation
- repo 作成
- `AGENTS.md`
- `README.md`
- `docs/vision.md`
- `docs/architecture.md`
- `playbooks/` のコアフォルダ作成

### Phase 2: Core Flow MVP
- MVP 対象 5 playbook の `PLAYBOOK.md` 作成
- 最小 artifact / gate / flow 作成

### Phase 3: Practical MVP
- 実案件で試験運用
- examples 追加
- 責務調整と不要部分削減

### Phase 4: Shipping Expansion
- `write-release-artifacts`
- `review-diff`
- `post-ship-retro`
- docs / flows / examples 拡張

### Phase 5: Public Release Candidate
- README / docs / examples の公開品質化
- adapter 初版
- quality gates 明文化
- 公開判断

---

## 20. 受け入れ条件（完成版）

完成版として扱うには、最低限以下を満たすこと。

- コア playbook 群が揃っている
- 各 playbook に `PLAYBOOK.md` がある
- 必須 artifact と gate が存在する
- `flows/` が一通り揃っている
- `docs/` が整っている
- `README.md` だけで価値が伝わる
- 実際の repo 利用例がある
- 「skills クローンではない」ことを構造で説明できる
- 「Codex に入れる意味」を一文で説明できる

---

## 21. 保留事項

以下は将来検討事項として保留する。

- GPT 版への再設計
- adapter の多形式対応
- CLI 化
- HTML index 生成
- 自動 issue / PR 連携の強化

---

## 22. 結論

本プロジェクトは、**skills リポジトリの別名版**ではなく、**repo の中で仕様整理から出荷確認までを反復可能にする独自の shipping playbooks system** として設計する。

そのため、最初から

- playbook / artifact / gate / flow / adapter の独自構造
- workflow-first の責務分離
- shipping-first の価値定義
- adapter を補助層に置く設計

を前提とする。

本仕様書は、その完成版へ向けた基準文書とする。
