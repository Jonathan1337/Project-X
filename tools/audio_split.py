from moviepy import VideoFileClip
from pathlib import Path

input_path = r'C:\Users\Administrator\Downloads\The.Office.US.S03.1080p.BluRay.x265-RARBG\The.Office.US.S03E18.1080p.BluRay.x265-RARBG.mp4'

input_filename = Path(input_path).stem

output_path = f"{input_filename}.mp3"

video = VideoFileClip(input_path)

video.audio.write_audiofile(output_path)