import imageio
import glob
import time
import os

def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
        # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.04)

    return


def main():
    start = time.time()
    images_path = r'C:\Users\Administrator\Desktop\104_mapping\104mapping_clip'
    img_files = glob.glob(images_path + r"\*.jpg")
    gif_name = 'test.gif'
    print("正在处理中，总计读取图片%d帧..." % len(img_files))
    create_gif(img_files, gif_name)
    end = time.time()
    print("处理完成,总计用时:{:.2f}s".format(end - start))



if __name__ == "__main__":
    main()