import os
import subprocess
import time
import argparse

FLAGS = None

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
download_folder = os.path.join(root_folder, "2_Training", "src", "keras_yolo3")
data_folder = os.path.join(root_folder, "Data")
model_folder = os.path.join(data_folder, "Model_Weights")

if __name__ == "__main__":
    # Delete all default flags
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    """
    Command line options
    """
    parser.add_argument(
        "--download_folder",
        type=str,
        default=download_folder,
        help="Folder to download weights to. Default is " + download_folder,
    )

    parser.add_argument(
        "--is_tiny",
        default=False,
        action="store_true",
        help="Use the tiny Yolo version for better performance and less accuracy. Default is False.",
    )

    FLAGS = parser.parse_args()

    if not FLAGS.is_tiny:
        weights_file = "yolov3.weights"
        h5_file = "yolo.h5"
        cfg_file = "yolov3.cfg"
        # Original URL: https://pjreddie.com/media/files/yolov3.weights
        gdrive_id = "1J7n26vaXBgTdlVpxOFzH75l_tVvj-D27"

    else:
        weights_file = "yolov3-tiny.weights"
        h5_file = "yolo-tiny.h5"
        cfg_file = "yolov3-tiny.cfg"
        # Original URL: https://pjreddie.com/media/files/yolov3-tiny.weights
        gdrive_id = "1LG40ON6geD3hgI8Hi2TlzAfsNWigxKie"

    if not os.path.isfile(os.path.join(download_folder, weights_file)):
        print(f"\nDownloading Raw {weights_file}\n")
        start = time.time()
        call_string = " ".join(
            [
                "cd ..",
                "\n",
                "cd",
                download_folder,
                "\n",
                "gdown",
                f"https://drive.google.com/uc?id={gdrive_id}",
            ]
        )

        subprocess.call(call_string, shell=True)

        end = time.time()
        print(f"Downloaded Raw {weights_file} in {end - start:.1f} seconds\n")

        call_string = f"python convert.py {cfg_file} {weights_file} {h5_file}"

        subprocess.call(call_string, shell=True, cwd=download_folder)
