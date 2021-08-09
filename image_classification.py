import json

import cv2
import numpy as np
from openvino.inference_engine import IECore
import os

device_type = os.getenv('DEVICE')
print("DEVICE:" + device_type)

ie = IECore()
net = ie.read_network(model="model/v3-small_224_1.0_float.xml")
exec_net = ie.load_network(net, device_type)

input_key = next(iter(exec_net.input_info))
output_key = next(iter(exec_net.outputs.keys()))

# The MobileNet network expects images in RGB format
image = cv2.cvtColor(cv2.imread("data/coco.jpg"), cv2.COLOR_BGR2RGB)
# resize to MobileNet image shape
input_image = cv2.resize(image, (224, 224))
# reshape to network input shape
input_image = np.expand_dims(input_image.transpose(2, 0, 1), 0)

result = exec_net.infer(inputs={input_key: input_image})[output_key]
result_index = np.argmax(result)


# Convert the inference result to a class name.
imagenet_classes = json.loads(open("utils/imagenet_class_index.json").read())
# The model description states that for this model, class 0 is background,
# so we add 1 to the network output to get the class name
imagenet_classes = {int(key) + 1: value for key, value in imagenet_classes.items()}
imagenet_classes[result_index]

print(imagenet_classes[result_index])
