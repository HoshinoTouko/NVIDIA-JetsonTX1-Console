import os
import Modules.Camera as camModule

os.environ["GLOG_minloglevel"] = "1"

# make sure that caffe is on the python path
CAFFE_ROOT = '/home/ubuntu/ssd_demo/caffe_ssd/'
import sys

sys.path.insert(0, CAFFE_ROOT + 'python')

# Import caffe
import caffe

caffe.set_device(0)
caffe.set_mode_gpu()

from google.protobuf import text_format
from caffe.proto import caffe_pb2

import numpy as np
import cv2

# load PASCAL VOC labels
labelmap_file = CAFFE_ROOT + 'data/VOC0712/labelmap_voc.prototxt'
file = open(labelmap_file, 'r')
labelmap = caffe_pb2.LabelMap()
text_format.Merge(str(file.read()), labelmap)


def get_labelname(labelmap, labels):
    num_labels = len(labelmap.item)
    labelnames = []
    if type(labels) is not list:
        labels = [labels]
    for label in labels:
        found = False
        for i in xrange(0, num_labels):
            if label == labelmap.item[i].label:
                found = True
                labelnames.append(labelmap.item[i].display_name)
                break
        assert found == True
    return labelnames


model_def = CAFFE_ROOT + 'models/VGGNet/VOC0712/SSD_300x300/deploy.prototxt'
model_weights = CAFFE_ROOT + 'models/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300_iter_60000.caffemodel'

net = caffe.Net(model_def,  # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)  # use test mode (e.g., don't perform dropout)

# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', np.array([104, 117, 123]))  # mean pixel
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2, 1, 0))  # the reference model has channels in BGR order instead of RGB

# set net to batch size of 1
image_resize = 300
net.blobs['data'].reshape(1, 3, image_resize, image_resize)



def detect():
    ret, frame = camModule.Camera.getCamera()
    # image = caffe.io.load_image('examples/images/fish-bike.jpg')
    net.blobs['data'].data[...] = transformer.preprocess('data', frame)

    # Forward pass.
    detections = net.forward()['detection_out']

    # Parse the outputs.
    det_label = detections[0, 0, :, 1]
    det_conf = detections[0, 0, :, 2]
    det_xmin = detections[0, 0, :, 3]
    det_ymin = detections[0, 0, :, 4]
    det_xmax = detections[0, 0, :, 5]
    det_ymax = detections[0, 0, :, 6]

    # Get detections with confidence higher than 0.6.
    top_indices = [i for i, conf in enumerate(det_conf) if conf >= 0.5]

    top_conf = det_conf[top_indices]
    top_label_indices = det_label[top_indices].tolist()
    top_labels = get_labelname(labelmap, top_label_indices)
    top_xmin = det_xmin[top_indices]
    top_ymin = det_ymin[top_indices]
    top_xmax = det_xmax[top_indices]
    top_ymax = det_ymax[top_indices]

    # print(top_labels)
    return top_labels

    # cap.release()


if __name__ == "__main__":
    while True:
        detect()

    cap.release()