# from moviepy.editor import VideoFileClip
from moviepy import VideoFileClip

clip = VideoFileClip("sample.mp4")

clip.write_gif("sample.gif", fps=30)