# Redome プロジェクト

## 概要
Redomeは、動画処理と画像抽出に特化したPythonプロジェクトです。既存の`avi-mv.py`と`M to P.py`の機能を統合し、動画ファイルの変換とフレーム抽出機能を提供します。

## 主要機能

### 1. 動画形式変換 (`avi-mv.py`)
- **機能**: AVIファイルをMP4形式に変換
- **使用ライブラリ**: moviepy
- **入力**: `runs/detect/predict/video.avi`
- **出力**: `runs/detect/predict/video_converted.mp4`
- **コーデック**: libx264

### 2. 動画フレーム抽出 (`M to P.py`)
- **機能**: 動画から特定フレームを画像として保存
- **使用ライブラリ**: OpenCV (cv2)
- **操作方法**:
  - スペースキー: 現在のフレームを画像として保存
  - Qキー: プログラム終了
- **出力形式**: PNG画像
- **ファイル名**: `frame_XXXXX.png` (5桁の連番)

## 技術仕様

### 動画変換機能
```python
# 変換設定
input_path = 'runs/detect/predict/video.avi'
output_path = 'runs/detect/predict/video_converted.mp4'
codec = 'libx264'
```

### フレーム抽出機能
```python
# 表示設定
window_size = (960, 540)
frame_format = 'frame_{:05d}.png'
output_directory = "C:/sozai"
```



```

## 開発背景
- 動画ファイルの形式変換（AVI → MP4）
- 動画から特定フレームの抽出
- リアルタイムでの動画プレビューとフレーム選択



## 注意事項
- 動画ファイルのパスは適切に設定してください
- 出力ディレクトリの権限を確認してください
- 大きな動画ファイルの場合、処理時間が長くなる可能性があります



## 更新履歴
- v1.0.0: 初期バージョン（avi-mv.py, M to P.py統合） 