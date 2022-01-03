# Photorealistic Style Transfer with a Gradio Interface  <a href="https://colab.research.google.com/drive/1dS1w0WO7Rcvul7Zw-ztB5BwOmEiuTIsm?usp=sharing" target="_parent"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

Transfer the overall style of an image to your original image.

The original model was implemented with PyTorch by [Jaejun-yoo](https://github.com/jaejun-yoo) based on this paper https://arxiv.org/abs/1903.09760

The model used was implemented by [ptran1203](https://github.com/ptran1203) and [vunquitk11](https://github.com/vunquitk11) using Tensorflow and Keras. It is used here as a submodule. View the original repository [here](https://github.com/ptran1203/photorealistic_style_transfer).

I added a Gradio Interface where you can upload your images and screenshot the output.


## Usage

### 1. Google Colab (recommended)
Click [here](https://colab.research.google.com/drive/1dS1w0WO7Rcvul7Zw-ztB5BwOmEiuTIsm?usp=sharing) or on the "Open in Colab" badge in the title.

### 2. Locally
**Requirement: [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cudnn](https://developer.nvidia.com/cudnn) have to be installed**

#### 2.1 Clone the Repository
```
git clone https://github.com/gina6/gradio-interface-WCT2
```

#### 2.2 Run the app.py script
```
python app.py
```

