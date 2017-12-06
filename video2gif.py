import imageio
import time
import cv2

def video2gif(video_path, gif_path, fps_gif=16):
    ims = []
    reader = imageio.get_reader(video_path)
    # fps_video = reader.get_meta_data()['fps']
    video_size = reader.get_meta_data()['size']
    video_width, video_height = video_size[0], video_size[1]
    for frames in reader:
        ims.append(frames)
    imageio.mimwrite(gif_path, ims, 'GIF', fps=fps_gif, subrectangles=True)

    return


def main():
    start = time.time()
    video_path = r'imageio:cockatoo.mp4' # 输入视频地址，修改引号内即可
    gif_path =  r'cockatoo.gif' # 输入gif地址，修改引号内即可
    print("正在处理中")
    video2gif(video_path, gif_path)
    end = time.time()
    print("处理完成,总计用时:{:.2f}s".format(end - start))



if __name__ == "__main__":
    main()