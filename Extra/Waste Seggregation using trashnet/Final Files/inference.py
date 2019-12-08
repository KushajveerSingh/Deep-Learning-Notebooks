from utils import *

def do_inference(model, path):
    img = open_img(path)
    return get_pred(model, img)

if __name__ == '__main__':
    model = prepare_model()
    print('Finished loading model------------------------------')
    print('-----------------------------------------------------')
    
    do_inference(model, path='data/glass51.jpg')
