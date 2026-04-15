# from moviepy.editor import VideoFileClip

from moviepy import VideoFileClip



clip = VideoFileClip("sample.mp4")



clip.write_gif("sample.gif", fps=10)

# you can play with it by changing the Number of frames per second (fps) [Frame Rate]



# Increasing FPS -> Increasing the Size -> Make the Animiation GIF Smoother

# Decreasing FPS -> Decreasing the Size -> Make the Animiation GIF Laggy
