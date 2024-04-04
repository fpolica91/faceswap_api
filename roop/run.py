#!/usr/bin/env python3

from roop import core
import os


if __name__ == '__main__':
    # core.run()
    try:
        source_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'temp_images', 'test1.png')

        target_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'temp_videos', 'test1.mp4')
        output_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'content')
        core.run_api(source_path, target_path, output_path,
                     frame_processor=["face_swapper", "face_enhancer"])
    except Exception as e:
        print(e)
        print('Error in running the code')
        exit(1)
