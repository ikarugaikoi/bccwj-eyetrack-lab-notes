# BCCWJ Eye-Tracking Lab Notes

Trilingual experiment logs and scripts for a Japanese reading eye-tracking study.

日本語読解の眼球運動実験に関する、中・日・英の実験記録とスクリプトを公開します。

本仓库公开日语阅读眼动实验的中日英三语日志及相关脚本。

Maintained by **Ikaruga**.

## Experiment logs · 実験記録 · 实验日志

| Date / 日期 / 日付 | 中文 | 日本語 | English |
|---|---|---|---|
| 2026-09-29 | [正式实验：BA／DC 流程与 C05 续录](zh/2026-09-29_01.md) | [本実験：BA／DC の手順と C05 の続きの録画](ja/2026-09-29_01.md) | [Main-study sessions: BA/DC workflows and C05 continuation](en/2026-09-29_01.md) |
| 2026-09-28 | [正式实验：校准判读与黑点检查](zh/2026-09-28_01.md) | [本実験：キャリブレーション結果の判読と黒点注視チェック](ja/2026-09-28_01.md) | [Main-study sessions: Interpreting calibration results and black-dot fixation checks](en/2026-09-28_01.md) |
| 2026-09-24 | [正式实验：CD／DC 流程与校准失败终止](zh/2026-09-24_01.md) | [本実験：CD／DC の手順とキャリブレーション不合格による中止](ja/2026-09-24_01.md) | [Main-study sessions: CD/DC workflows and termination after failed calibration](en/2026-09-24_01.md) |
| 2026-09-15 | [首次正式实验](zh/2026-09-15_01.md) | [初回の本実験](ja/2026-09-15_01.md) | [First main-study data collection](en/2026-09-15_01.md) |
| 2026-09-09 | [两位受试者的 pilot 试验](zh/2026-09-09_01.md) | [2 名の参加者による pilot 実験](ja/2026-09-09_01.md) | [Pilot sessions with two participants](en/2026-09-09_01.md) |
| 2026-09-07 | [眼动阅读流程试跑与设备配置问题复核](zh/2026-09-07_01.md) | [読解手順の試行と機器設定の再確認](ja/2026-09-07_01.md) | [Reading workflow test and equipment settings review](en/2026-09-07_01.md) |
| 2026-09-04 | [首次眼动阅读全流程测试](zh/2026-09-04_01.md) | [読解手順の初回通しテスト](ja/2026-09-04_01.md) | [First reading workflow test](en/2026-09-04_01.md) |

Each entry is available in Chinese, Japanese, and English and identifies the language of the original account. Observations, interpretations, and proposed explanations are distinguished in the logs.

各記録は中国語・日本語・英語で掲載し、元の記述言語を明記しています。観察事実、実験者の判断、推測される説明を区別して記録します。

每条记录均提供中文、日文和英文，并标明原始叙述语言。日志区分观察事实、实验者判断及推测。

## Structure · 構成 · 目录结构

```text
README.md
zh/YYYY-MM-DD_01.md
ja/YYYY-MM-DD_01.md
en/YYYY-MM-DD_01.md
scripts/20260909/README.md
```

Files with the same name refer to the same log entry. `_01`, `_02`, etc. distinguish entries on the same date. The September 9 entry covers two pilot sessions. New entries are added to the table above, newest first. Build-script snapshots are stored under `scripts/` by date.

同名のファイルは同一の記録です。同日に複数の記録がある場合は `_01`、`_02` などで区別します。9 月 9 日の記録は 2 名の pilot 実験をまとめたものです。新しい記録は上の一覧に日付の新しい順で追加します。構築スクリプトは `scripts/` に日付別で保存します。

同名文件对应同一条日志，同日多条以 `_01`、`_02` 等区分。9 月 9 日的日志合并记录了两位受试者的 pilot。新日志按日期倒序加入上方索引；搭建脚本按日期存放于 `scripts/` 目录。

Translations carry a human-review status. The Japanese and English translations for 2026-09-04, 2026-09-07, 2026-09-09, 2026-09-15, 2026-09-24, 2026-09-28, and 2026-09-29 have **not yet been reviewed by a human**; publication does not change that status.

訳文には人手による確認状況を明記します。2026-09-04、2026-09-07、2026-09-09、2026-09-15、2026-09-24、2026-09-28、2026-09-29 の日本語版・英語版は **人手による確認未実施** です。公開したことをもって確認済みとはしません。

译文注明人工确认状态。2026-09-04、2026-09-07、2026-09-09、2026-09-15、2026-09-24、2026-09-28 和 2026-09-29 的日文、英文译文均为 **未经过人工确认**，公开发布不改变该状态。

## Scripts · スクリプト · 脚本

The [masked Tobii project build scripts (2026-09-09)](scripts/20260909/README.md) have been uploaded. The bundle contains source code and configuration documentation; corpus text, stimulus images, and native projects are not included.

[Tobii プロジェクト構築スクリプト（2026-09-09 マスキング版）](scripts/20260909/README.md)を公開しました。ソースコードと設定資料を収録し、コーパス本文、刺激画像、ネイティブプロジェクトは含みません。

[Tobii project 搭建脚本（2026-09-09 脱敏版）](scripts/20260909/README.md)已上传，包含源码和配置文档，不含语料正文、刺激图片或原生工程。
