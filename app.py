import gradio as gr
from utils.model import WCT2
import cv2
import numpy as np

# load model
model = WCT2()
model.load_weight('./photorealistic_style_transfer/checkpoints/wtc2.h5')

# Helper Functions
# Scale Image according to given width or height
def image_resize(img, width):

  # original size of the img
  original_h = img.shape[0]
  original_w = img.shape[1]

  # ratio to new width
  r = width / float(original_w)

  # new dimensions
  dim = (width, int(original_h * r))

  # resize to new dimensions
  resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

  return resized

def preprocess(img, size):

  # set color mode to BGR
  bgr_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

  # resize image
  resized_img = image_resize(bgr_img, size)

  # expand the array by one dimension
  processed_img = np.expand_dims(resized_img, 0)

  return processed_img



def pst(input_img, style_img):

  # preprocess images
  image_size = 512
  content = preprocess(input_img, image_size)
  style = preprocess(style_img, image_size)

  # transfer the style
  gen_img = model.transfer(content, style, 1.0)

  # write generated img to a png file
  cv2.imwrite('./output/output.png', gen_img[0])

  # transform array to PIL img
  # final_img = PIL.Image.fromarray(gen_img[0], 'RGB')
  final_img = './output/output.png'

  return final_img

# Interface attributes
iface_input = [gr.inputs.Image(label="Original Image"), gr.inputs.Image(label="Style Image")]
iface_output = [gr.outputs.Image(type='file')]
iface_title = "Photorealistic Style Transfer with WCT2"
iface_description = "Transfer the style of a photo to your own. The model implementation is based on a Tensorflow and Keras implementation by https://github.com/ptran1203/photorealistic_style_transfer"

iface = gr.Interface(
  fn = pst, 
  inputs= iface_input,
  outputs= iface_output,
  title = iface_title,
  description = iface_description
  )

iface.launch()