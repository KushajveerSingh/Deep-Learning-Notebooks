import onnx
from onnx_tf.backend import prepare

import numpy as np
from PIL import Image


__all__ = ['prepare_model', 'open_img', 'classes', 'get_pred']


def prepare_model(path='mobilenetv2.onnx'):
    model = onnx.load(path)
    tf_rep = prepare(model, device='CPU', strict=True)
    return tf_rep


def open_img(path='glass51.jpg', size=(256, 256)):
    # Open image using PIL
    img = Image.open(path).resize(size).convert('RGB')
    a = np.asarray(img)
    a = a/255

    # Normalize image
    mean=np.array([0.485, 0.456, 0.406])
    std=np.array([0.229, 0.224, 0.225])
    a = (a - mean)/std
    
    # Convert Image to PyTorch format
    a = np.transpose(a, (1, 0, 2))
    a = np.transpose(a, (2, 1, 0))
    a = np.expand_dims(a, axis=0)
    return a.astype(np.float32, copy=False)


def get_pred(tf_rep, img):
    out = tf_rep.run(img)
    pred = np.argmax(out)
    
    if pred == 0 or pred == 3:
        pred = 0
    if pred == 4:
        pred = 3
    
    return pred


classes = ['paper', 
           'glass', 
           'metal',  
           'plastic']

def do_inference(model, path):
    img = open_img(path)
    return get_pred(model, img)