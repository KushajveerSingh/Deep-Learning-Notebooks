import pickle
import numpy as np

# Main pickle function to access the data in the files
def unpickle(file):
    with open(file, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
    
    # Useful data is only in first and second key
    keys = list(data.keys())

    return data[keys[2]], data[keys[1]]

if __name__ == "__main__":
    # All the files that came when downloaded CIFAR-10 dataset from official website
    # Here I exclude the batches.meta as we can manually create all the classes and the README file
    files = ['data_batch_1',
             'data_batch_2',
             'data_batch_3',
             'data_batch_4',
             'data_batch_5',
             'test_batch']

    # Create containers for the required data
    train_data = None
    train_labels = []

    # Get the train data from the first 4 files
    for i in range(5):
        image, label = unpickle(files[i])
        if i==0:
            train_data = image
        else:
            train_data = np.vstack((train_data, image))
        train_labels += label
    
    # Get the test data from the 5 file
    test_data, test_labels = unpickle(files[5])
    
    # Save all the files in .npz format
    np.savez(file="cifar_10", 
             train_data=train_data,
             train_labels=train_labels,
             test_data=test_data,
             test_labels=test_labels)

    # To load the data from .npz file
    # data = np.load("cifar_10.npz")
    # train_data = data['train_data']
    # train_labels = data['train_labels']
    # test_data = data['test_data']
    # test_labels = data['test_labels']