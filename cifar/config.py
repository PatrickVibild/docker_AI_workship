import os

PATH_WEIGHT = os.environ.get('PATH_WEIGHT', '../weights/cifar_net.pth')
PATH_DATA = os.environ.get('PATH_DATA', '../data')
EPOCH = int(os.environ.get('EPOCH', '20'))
LR = float(os.environ.get('LR', '0.001'))
MOMENTUM = float(os.environ.get('MOMENTUM', '0.9'))
