
# ADIS - Animal Detection and Intrusion System

ADIS is an Animal Detection and Intrusion System. This repository uses utilities provided by [ultralytics/yolov5](https://github.com/ultralytics/yolov5) and also includes a custom script that uses PyTorch for detection.

## Installation

### Local Installation

To run ADIS on your local machine, first install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Deployment on Jetson Nano

For deployment on Jetson Nano, pull the Docker image from `ghcr.io/meenakshi-srm/adis_nano_cuda:latest`. This Docker image utilizes the GPU of Jetson Nano. Installing Python 3.8 on Jetson Nano that uses GPU can be troublesome, hence the Docker image is provided.

To pull and run the Docker image, use the following commands:

```bash
sudo docker pull ghcr.io/meenakshi-srm/adis_nano_cuda:latest
sudo docker run -it --gpus all --privileged --net host --name test ghcr.io/meenakshi-srm/adis_nano_cuda:latest
```

**Note:** Ensure that the camera is connected beforehand to include the hardware in the container.

## Usage

After installation, download the `best.pt` weight from the releases and place it in the `yolov5` folder. Then, run the detection script with the following command:

```bash
python3 detect.py --source 0 --weights best.pt --nosave --max-det 1 --max-conf 0.5
```
To use custom script, run the following command:

```bash
python3 custom_detect.py
```
It should use the first occurence of a camera and start the detection process.

This will start the detection process with the specified parameters.