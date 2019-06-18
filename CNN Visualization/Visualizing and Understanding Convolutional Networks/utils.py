import json
import torch

def decode_predictions(preds, top=5):
    with open('/home/kushaj/Desktop/Data/imagenet_class_index.json') as f:
        class_index_dict = json.load(f)
        
    results = []
    for pred in preds:
        top_value, top_indices = torch.topk(pred, top)
        result = [tuple(class_index_dict[str(i.item())]) + (pred[i].item(),) \
                for i in top_indices]
        result = [tuple(class_index_dict[str(i.item())]) + (j.item(),) \
        for (i, j) in zip(top_indices, top_value)]
        results.append(result)

    return results