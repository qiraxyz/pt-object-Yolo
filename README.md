
# Pony Town Object Detector

Pony Town vision model for detecting surrounding objects using Yolo11n pre-trained model. Used to create Pony Town AI.
## Setup with ultralytics

Installation with PIP

```bash
pip install ultralytics
```

see the detail : [ultralytics](https://docs.ultralytics.com/quickstart/#custom-installation-methods)


## Training Tests

To train test, run the following command

```bash
yolo train data=dataset/datav2/data.yaml model=yolo11n.pt epochs=500 lr0=0.001
```


## Latest Benchmark
![Benchmark](https://i.ibb.co.com/CpvS2QWp/results.png)


## Screenshots

![App Screenshot](https://i.ibb.co.com/SwKzm4Zq/tmpp057msis.png)

