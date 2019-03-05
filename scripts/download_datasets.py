# -*- coding: utf-8 -*-
""" This script downloads datasets to the server using aria2c command.
Before you run this script, you need to add a class inherited from class 'Dataset' with correct download links,
you can rewrite the 'download()' function within your dataset class to customize the method to download data.

Usage: python download_datasets.py dataset_name
For example, 'python download_datasets.py username mnist' will download MNIST dataset to the specific directory
under `username` account
"""

import os
import os.path as osp
import sys
from socket import gethostname


class Dataset():
    def __init__(self, username):
        self.links = dict()
        self.name = self.__class__.__name__.lower()
        self.root_dir = get_root_dir(username)
        assert osp.exists(self.root_dir), "Error: {} is not a valid path".format(self.root_dir)

    def download(self):
        print('Downloading {} dataset to {}'.format(dataset, self.root_dir))
        download_dir = osp.join(self.root_dir, self.name)
        if not osp.exists(download_dir):
            os.mkdir(download_dir)
        for name, link in self.links.items():
            print('Downloading {} ...'.format(name))
            os.system('aria2c -d {} -x 8 {}'.format(download_dir, link))


class CIFAR(Dataset):
    def __init__(self):
        super(CIFAR, self).__init__()
        self.links = {
            # python version
            'cifar-10 [163MB]': 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',
            'cifar-100 [162MB]': 'https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz'
        }


class COCO(Dataset):
    def __init__(self):
        super(COCO, self).__init__()
        self.links = {
            # Images
            '2014 Train images [83K/13GB]' : 'http://images.cocodataset.org/zips/train2014.zip',
            '2014 Val images [41K/6GB]': 'http://images.cocodataset.org/zips/val2014.zip',
            '2014 Test images [41K/6GB]': 'http://images.cocodataset.org/zips/test2014.zip',
            '2015 Test images [81K/12GB]': 'http://images.cocodataset.org/zips/test2015.zip',
            '2017 Train images [118K/18GB]': 'http://images.cocodataset.org/zips/train2017.zip',
            '2017 Val images [5K/1GB]': 'http://images.cocodataset.org/zips/val2017.zip',
            '2017 Test images [41K/6GB]': 'http://images.cocodataset.org/zips/test2017.zip',
            '2017 Unlabeled images [123K/19GB]': 'http://images.cocodataset.org/zips/unlabeled2017.zip',
            # Annotations
            '2014 Train/Val annotations [241MB]': 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip',
            '2014 Testing Image info [1MB]': 'http://images.cocodataset.org/annotations/image_info_test2014.zip',
            '2015 Testing Image info [2MB]': 'http://images.cocodataset.org/annotations/image_info_test2015.zip',
            '2017 Train/Val annotations [241MB]': 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip',
            '2017 Stuff Train/Val annotations [1.1GB]': 'http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip',
            '2017 Panoptic Train/Val annotations [821MB]': 'http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip',
            '2017 Testing Image info [1MB]': 'http://images.cocodataset.org/annotations/image_info_test2017.zip',
            '2017 Unlabeled Image info [4MB]': 'http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip',
        }


class ImageNet(Dataset):
    def __init__(self):
        self.links = {
            'Dev-kit': 'http://image-net.org/image/ILSVRC2017/ILSVRC2017_devkit.tar.gz',
            'CLS-LOC [155GB]': 'http://image-net.org/image/ILSVRC2017/ILSVRC2017_CLS-LOC.tar.gz',
            'DET [55GB]': 'http://image-net.org/image/ILSVRC2017/ILSVRC2017_DET.tar.gz',
            'DET test [428MB]': 'http://image-net.org/image/ILSVRC2017/ILSVRC2017_DET_test_new.tar.gz',
        }
        self.name = 'ILSVRC'


class MNIST(Dataset):
    def __init__(self):
        super(MNIST, self).__init__()
        self.links = {
            # python version
            'train-images': 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
            'train-labels': 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz',
            'test-images': 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz',
            'test-labels': 'http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz'
        }


class MPII(Dataset):
    def __init__(self):
        super(MPII, self).__init__()
        self.links = {
            'Images [12.9GB]': 'https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1.tar.gz',
            'Annos [12.5MB]': 'https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1_u12_2.zip',
        }


def get_root_dir(username):
    hostname = gethostname()
    host_id = int(hostname[-1])
    if host_id < 3:
        return '/home/' + username + '/datasets/'
    elif host_id == 3:
        return '/home/Data/'
    elif host_id == 4:
        return '/data/datasets/'
    else:
        raise KeyError('Invalid hostname: {}'.format(hostname))
  
subclasses = vars()['Dataset'].__subclasses__()
names = [cls.__name__.lower() for cls in subclasses]
Datasets = dict(zip(names, subclasses))

if __name__ == "__main__":
    dataset = str(sys.argv[1]).lower()
    Datasets[dataset]().download()
