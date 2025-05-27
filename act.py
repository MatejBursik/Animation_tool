import cv2, os, sys
from tqdm import tqdm

def convert(name, fps, imgT, path):
    if not name:
        return "You did not input --name argument"

    if not fps:
        fps = 30
    elif fps.isdigit() and int(fps) > 0:
        fps = int(fps)
    else:
        return "Your --fps argument was not a positive integer"
    
    if not imgT:
        imgT = "png"
    elif imgT not in ["png", "jpeg", "tiff"]:
        return "Your --img argument is not supported"
    
    if not path:
        files = list(filter(lambda x:x[:-len(imgT)-1].isdigit(), os.listdir()))
        images =  [str(i) + "." + imgT for i in range(1, len(files)+1)]
    elif not os.path.isdir(path):
        return "Your --path argument does not exist"
    else:
        files = os.listdir(path)
        images = [path + "\\" + str(i) + "." + imgT for i in range(1, len(files)+1)]

    out_path = name + ".mp4"

    try:
        frame = cv2.imread(images[0])
        dimensions = (frame.shape[1],frame.shape[0])
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video = cv2.VideoWriter(out_path, fourcc, fps, dimensions)

        for i, img in tqdm(enumerate(images), total=len(images), desc="Writing frames"):
            video.write(cv2.imread(img))

        video.release()
    except:
        return "You are missing image/s"
    
    return "Done"

arg = sys.argv

name = False
fps = False
path = False
imgType = False

if "--name" in arg:
    name = arg[arg.index("--name") + 1]

if "--fps" in arg:
    fps = arg[arg.index("--fps") + 1]

if "--img" in arg:
    imgType = arg[arg.index("--img") + 1]

if "--path" in arg:
    path = arg[arg.index("--path") + 1]

print(convert(name, fps, imgType, path))
