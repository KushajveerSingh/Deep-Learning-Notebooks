import torch
import torch.nn as nn
from torchvision import models
from collections import OrderedDict

# VGG16
def make_layers(cfg, batch_norm=False):
    layers = []
    in_channels = 3
    for v in cfg:
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2, return_indices=True)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            layers += [conv2d, nn.ReLU()]
            in_channels = v
    return nn.Sequential(*layers)

class VGG(nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        cfg = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']
        self.features = make_layers(cfg)
        self.avgpool = nn.AdaptiveAvgPool2d((7,7))
        self.classifier = nn.Sequential(
            nn.Linear(512*7*7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes)
        )
        
        self.conv_layer_indices = [0, 2, 5, 7, 10, 12, 14, 17, 19, 21, 24, 26, 28]
        self.feature_maps = OrderedDict()
        self.pool_locs = OrderedDict()
        
    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

def get_vgg16():
    model = VGG()
    model.load_state_dict(torch.load('/home/kushaj/Desktop/Data/vgg.pth'))
    return model


# VGG16 Deconv
def make_deconv_layer(cfg):
    layers = []
    in_channels = 512
    
    for v in cfg:
        if v == 'M':
            layers += [nn.MaxUnpool2d(2, stride=2)]
        else:
            conv2d_t = nn.ConvTranspose2d(in_channels, v, kernel_size=3, padding=1)
            layers += [nn.ReLU(), conv2d_t]
            in_channels = v
    return nn.Sequential(*layers)
            
class VGG_Deconv(nn.Module):
    def __init__(self):
        super().__init__()
        cfg = ['M', 512, 512, 512, 'M', 512, 512, 256, 'M', 256, 256, 128, 'M', 128, 64, 'M', 64, 3]
        self.features = make_deconv_layer(cfg)
        
        self.conv2deconv_indices = {
                0:30, 2:28, 5:25, 7:23,
                10:20, 12:18, 14:16, 17:13,
                19:11, 21:9, 24:6, 26:4, 28:2
                }

        self.unpool2pool_indices = {
                26:4, 21:9, 14:16, 7:23, 0:30
                }
        
    def init_weight(self):
        vgg16 = models.vgg16(pretrained=True)
        for idx, layer in enumerate(vgg16.features):
            if isinstance(layer, nn.Conv2d):
                self.features[self.conv2deconv_indices[idx]].weight.data = layer.weight.data
    
    def forward(self, x, layer, activation_idx, pool_locs):
        if layer in self.conv2deconv_indices:
            start_idx = self.conv2deconv_indices[layer]
        else:
            raise ValueError('layer is not a conv feature map')
        
        for idx in range(start_idx, len(self.features)):
            if isinstance(self.features[idx], nn.MaxUnpool2d):
                x = self.features[idx]\
                (x, pool_locs[self.unpool2pool_indices[idx]])
            else:
                x = self.features[idx](x)
        return x

def get_vgg16_deconv():
    return VGG_Deconv()