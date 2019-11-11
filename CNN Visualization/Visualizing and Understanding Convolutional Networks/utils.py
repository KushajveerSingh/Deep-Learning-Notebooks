import torch
import torch.nn as nn
import torchvision.transforms as transforms
import numpy as np
import cv2
from functools import partial

def get_image(path, torch_img=True):
    """
    if torch_img == True:
        return image that can be directly used by our CNN model
    else:
        return numpy resize image
    """
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    if torch_img:
        img = transform(img)
        img.unsqueeze_(0)

    return img 


def store_feature(model):
    def hook(module, input, output, key):
        if isinstance(module, nn.MaxPool2d):
            # we used return_inde=True when defining our MaxPool layers
            # so the first output is the output of MaxPool layer and
            # the second output is the indices of the max_locations and
            # we store it in a pool_locs variable that we would give to 
            # the deconvnet model.
            model.feature_maps[key] = output[0]
            model.pool_locs[key] = output[1]
        else:
            model.feature_maps[key] = output

    for idx, layer in enumerate(model._module.get('features')):
        layer.register_forward_hook(partial(hook, key=idx))


def visualize_layer(layer, vgg, vgg_deconv, top_k=9):
    """
    We are given a layer, say 5, and we want to get the activations for one of
    it's channels/features. By default, I use batch_size=1 for getting the
    visualizations and I use CPU for the computations.
    
    Arguments:
        layer :- the layer number of which we want to get visulizations (should
            be conv layer index)
        vgg :- the model returned by get_vgg()
        vgg_deconv :- the model returned by get_vgg_deconv()
        top_k :- the number of top activations that you want
    """

    # Num channels/features in the layer (batch_size, num_channels, height, weidth)
    num_feat = vgg.feature_maps[layer].shape[1]

    # Create clone of feature map for easy changes
    feat_map = vgg.feature_maps[layer].clone()

    # Now we want the feature map with maximu activation, which is simply done by
    # finding the maximum value in the tensor
    activations = []
    for i in range(num_feat):
        # Sequentially traverse all the feature maps and append the maximum value
        # in the feature map to the activations list.
        map = feat_map[0, i, :, :]
        activation = torch.max(map)
        activations.append(activation.item())

    # Get the indices for the top_k activations
    activations = np.array(activations)
    max_activation_idxs = activations.argsort()[-1:-top_k-1:-1]

    # Store the visualizations in a list
    images = []

    for i in max_activation_idxs:
        current_map = feat_map[:, i, :, :]
        current_max_activation = torch.max(current_map)

        tmp_feat_map = vgg.featrue_maps[layer].clone()

        # We zero out all the other activation maps/channels except the one we want
        # to get the visulizationsf for
        if i == 0:
            tmp_feat_map[:, 1:, :, :] = 0
        else:
            tmp_feat_map[:, :i, :, :] = 0
            if i != vgg.feature_maps[layer].shape[1] - 1:
                tmp_feat_map[:, i+1:, :, :] = 0
        
        # For the current selected activation map, zero out all the non-max values
        # and store it the tmp_feat_map array
        current_map = torch.where(current_map == current_max_activation,
                                  current_map,
                                  torch.zeros(current_map.shape))

        tmp_feat_map[0, i, :, :] = current_map

        # Run the deconv model
        deconv_output = vgg_deconv(tmp_feat_map, layer, vgg.pool_locs)

        # Get the image
        img = deconv_output.data.numpy()[0].transpose(1, 2, 0)
        img = (img - img.min()) / (img.max() - img.min()) * 255
        img = img.astype(np.uint8)

        images.append(img, int(current_max_activation))
    
    return images