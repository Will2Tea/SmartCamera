import caffe
import numpy as np
import sys
import png
from PIL import Image

if len(sys.argv) != 3:
  print ("Usage: python convert_protomean.py proto.mean out.png")
  sys.exit()

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( sys.argv[1] , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
out = np.ascontiguousarray(out.transpose(1,2,0))
out = out.astype(np.uint8)
img = Image.fromarray(out, 'RGB')

img.save(sys.argv[2])
