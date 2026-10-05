from ultralytics import YOLO
import os, sys

model_path='decafia_best.onnx'
if not os.path.exists(model_path):
    print('MODEL_MISSING')
    sys.exit(0)
print('MODEL_FOUND', os.path.getsize(model_path))
# find a sample image
uploads_dir='static/uploads'
img=None
if os.path.isdir(uploads_dir):
    for root,dirs,files in os.walk(uploads_dir):
        for f in files:
            if f.lower().endswith(('.jpg','.jpeg','.png')):
                img=os.path.join(root,f)
                break
        if img: break
if not img:
    print('NO_SAMPLE_IMAGE')
    sys.exit(0)
print('SAMPLE_IMAGE',img)
try:
    model=YOLO(model_path, task='detect')
    print('MODEL_INIT_OK')
    res=model(img, conf=0.1, imgsz=640)
    print('INFERENCE_DONE')
    r=res[0]
    boxes = []
    if getattr(r,'boxes',None) is not None:
        for b in r.boxes:
            boxes.append({'cls':int(b.cls),'conf':float(b.conf)})
    print('BOXES', boxes)
    if hasattr(model,'names'):
        print('NAMES', model.names)
except Exception as e:
    import traceback
    traceback.print_exc()
    print('ERROR',e)
