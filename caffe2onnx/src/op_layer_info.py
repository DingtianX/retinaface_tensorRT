from proto import caffe_upsample_pb2
from onnx import TensorProto
Layer_CONCAT = caffe_upsample_pb2.V1LayerParameter.CONCAT #3
Layer_CONVOLUTION = caffe_upsample_pb2.V1LayerParameter.CONVOLUTION #4
Layer_DROPOUT = caffe_upsample_pb2.V1LayerParameter.DROPOUT #6
Layer_INNER_PRODUCT = caffe_upsample_pb2.V1LayerParameter.INNER_PRODUCT #14
Layer_LRN = caffe_upsample_pb2.V1LayerParameter.LRN #15
Layer_POOLING = caffe_upsample_pb2.V1LayerParameter.POOLING #17
Layer_RELU = caffe_upsample_pb2.V1LayerParameter.RELU #18
Layer_SOFTMAX = caffe_upsample_pb2.V1LayerParameter.SOFTMAX #20
Layer_ELTWISE = caffe_upsample_pb2.V1LayerParameter.ELTWISE #25
Layer_UPSAMPLE = caffe_upsample_pb2.V1LayerParameter.UPSAMPLE #40
op_pname={"Conv":["_W","_b"],
          "BatchNorm":["_mean","_var"],
          "Scale":["_scale","_b"],
          "Reshape":["_shape"],
          "InnerProduct":["_W","_B"],
          "Upsample":["_Scale"],
          "PRelu":["_slope"],
          "ConvTranspose":["_W","_b"]
          }
op_ptype={"Conv":[TensorProto.FLOAT,TensorProto.FLOAT],
          "BatchNorm":[TensorProto.FLOAT,TensorProto.FLOAT],
          "Scale":[TensorProto.FLOAT,TensorProto.FLOAT],
          "Reshape":[TensorProto.INT64],
          "InnerProduct":[TensorProto.FLOAT,TensorProto.FLOAT],
          "Upsample":[TensorProto.FLOAT],
          "PRelu":[TensorProto.FLOAT],
          "ConvTranspose":[TensorProto.FLOAT,TensorProto.FLOAT]
          }