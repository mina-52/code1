
import cv2
import os

# 動画ファイルのパス
video_path ="C:/guridonasi.mp4"

# 保存先ディレクトリ（なければ作成）
output_dir = "C:/sozai"        
os.makedirs(output_dir, exist_ok=True)

# 動画ファイルを開く
cap = cv2.VideoCapture(video_path)
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)  # ウィンドウ調整可能にする
cv2.resizeWindow("Video", 960, 540)  # 表示サイズを指定

if not cap.isOpened():
    print("動画ファイルを開けませんでした。")
    exit()

frame_count = 0  # フレーム数カウンタ
saved_count = 0  # 保存した画像の数

while True:
    ret, frame = cap.read()
    if not ret:
        print("動画の再生が終了しました。")
        break

    # 現在のフレームを表示
    cv2.imshow('Video', frame)

    # キー入力を待つ（30ミリ秒）
    key = cv2.waitKey(30) & 0xFF

    if key == ord(' '):  # スペースキーが押されたら画像保存
        filename = os.path.join(output_dir, f'frame_{frame_count:05d}.png')
        cv2.imwrite(filename, frame)
        print(f'保存しました: {filename}')
        saved_count += 1

    elif key == ord('q'):  # 'q' キーで終了
        print("終了します。")
        break

    frame_count += 1

# 後処理
cap.release()
cv2.destroyAllWindows()

