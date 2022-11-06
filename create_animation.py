import glob
from PIL import Image
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frames[0].save(f"{frame_folder}.gif", format='GIF', append_images=frames[1:], save_all=True, duration=75, loop=0)



if __name__ == "__main__":
    make_gif("D:\Github Repository\SpaceWeather\matlab\examples\draftFigure")