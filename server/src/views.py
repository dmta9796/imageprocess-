from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
import sys
import os
import zipfile
from PIL import Image
import datetime
# sys.path.append('./PyTorch-YOLOv3')
#import src.PyTorch-YOLOv3.models
# from man.PyTorchYOLOv3 import models
#from ../PyTorch-YOLOv3/models import *
dir_path = os.path.dirname(os.path.realpath(__file__))
import src.PyTorchYOLOv3.models as models
import src.PyTorchYOLOv3.detect as detect


def image_to_byte_array(image:Image):
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr


def index(request):
    return HttpResponse("Hello, world. http response")

@csrf_exempt
def data(request):
    data = request.body
    image = Image.open(io.BytesIO(data))
    start = datetime.datetime.now()
    processedimage = detect.detectimage(image)
    end = datetime.datetime.now()
    print((end-start).total_seconds())
    return HttpResponse(image_to_byte_array(processedimage))