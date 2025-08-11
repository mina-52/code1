import moviepy.editor as mp

# .aviファイルのパス
input_path = 'runs/detect/predict/video.avi'
output_path = 'runs/detect/predict/video_converted.mp4'

clip = mp.VideoFileClip(input_path)
clip.write_videofile(output_path, codec='libx264')