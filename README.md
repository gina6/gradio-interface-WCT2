# photorealistic_style_transfer  <a href="https://colab.research.google.com/github/gina6/WCT2-Gradio-Interface/master/WCT2-Gradio-Interface.ipynb" target="_parent"><img src="https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

Gradio Interface for Photorealistic Style Transfer via Wavelet Transforms - https://arxiv.org/abs/1903.09760

Original Keras + tensorflow implementation of WCT2 by [ptran1203](https://github.com/ptran1203) and [vunquitk11](https://github.com/vunquitk11). Original WCT2 implementation in [PyTorch](https://github.com/clovaai/WCT2) by [Jaejun-yoo](https://github.com/jaejun-yoo).


## 2. Results

| Content | Style | Result |
|--|--|--|
|![c1](/examples/input/in17.png)|![g1](/examples/style/tar17.png)| ![g1](/examples/output/out17.png) |
|![c1](/examples/input/in29.png)|![g1](/examples/style/tar29.png)| ![g1](/examples/output/out29.png) |
|![c1](/examples/input/in31.png)|![g1](/examples/style/tar31.png)| ![g1](/examples/output/out31.png) |
|![c1](/examples/input/in35.png)|![g1](/examples/style/tar35.png)| ![g1](/examples/output/out35.png) |
|![c1](/examples/input/in39.png)|![g1](/examples/style/tar39.png)| ![g1](/examples/output/out39.png) |
|![c1](/examples/input/in43.png)|![g1](/examples/style/tar43.png)| ![g1](/examples/output/out43.png) |
|![c1](/examples/input/in46.png)|![g1](/examples/style/tar46.png)| ![g1](/examples/output/out46.png) |
|![c1](/examples/input/in52.png)|![g1](/examples/style/tar52.png)| ![g1](/examples/output/out52.png) |
|![c1](/examples/input/in55.png)|![g1](/examples/style/tar55.png)| ![g1](/examples/output/out55.png) |

#### Without segmentation map, model failed to transfer the images properly
|![c1](/examples/input/in20.png)|![g1](/examples/style/tar20.png)| ![g1](/examples/output/out20.png) |
|--|--|--|
