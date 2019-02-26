import os
import shutil

data_dir = '../../../../Data/PASCAL VOC/'
result_dir = '../../../../Data/Segmentation Data/'

# Create dirs
os.makedirs(result_dir + 'train')
os.makedirs(result_dir + 'val')
os.makedirs(result_dir + 'test')

dir_names = ['SegmentationClass', 'SegmentationObject', 'Images']
for phase in ['train', 'val', 'test']:
    if phase is not 'test':
        os.makedirs(result_dir + phase + '/' + dir_names[0])
        os.makedirs(result_dir + phase + '/' + dir_names[1])
    os.makedirs(result_dir + phase + '/' + dir_names[2])

# Move the images
train_name = data_dir + 'trainval/ImageSets/Segmentation/train.txt'
val_name = data_dir + 'trainval/ImageSets/Segmentation/val.txt'
test_name = data_dir + 'test/ImageSets/Segmentation/test.txt'

root = data_dir + 'trainval/'
trainval_images = data_dir + 'trainval/JPEGImages/'
test_images = data_dir + 'test/JPEGImages/'

for phase, file, image_dir in [('train', train_name, trainval_images), ('val', val_name, trainval_images), ('test', test_name, test_images)]:
    with open(file, 'r') as f:
        images = os.listdir(image_dir)
        for image_name, image in zip(f, images):
            image_jpg = image_name[:-1] + '.jpg'
            image_png = image_name[:-1] + '.png'
            if phase == 'train':
                shutil.copy(image_dir + image_jpg, result_dir + 'train/Images/')
                shutil.copy(root + dir_names[0] + '/' + image_png, result_dir + 'train/' + dir_names[0])
                shutil.copy(root + dir_names[1] + '/' + image_png, result_dir + 'train/' + dir_names[1])
            elif phase == 'val':
                shutil.copy(image_dir + image_jpg, result_dir + 'val/Images/')
                shutil.copy(root + dir_names[0] + '/' + image_png, result_dir + 'val/' + dir_names[0])
                shutil.copy(root + dir_names[1] + '/' + image_png, result_dir + 'val/' + dir_names[1])
            else:
                shutil.copy(image_dir + image_jpg, result_dir + 'test/Images/')
