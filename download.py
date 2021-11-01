import torch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os
from threading import Thread
try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2


def append(list_to_append, item_to_append):
    list_to_append.append(item_to_append)


def append_dict(dict_to_append, key, val):
    dict_to_append[key] = val


classes = pd.read_csv('./classes.csv')
labelnames = classes['LabelName'].tolist()
classnames = classes['DisplayName'].tolist()
__imageids = []
__imageids_and_bbox = {}
imageids = []
xmins = []
ymins = []
xmaxs = []
ymaxs = []
file_names = []
imageurls = []
imageurls_original = []
type_of_data = []
image_id = 0

imageid_and_labelname = pd.read_csv(
    './open_images_data/oidv6-train-annotations-human-imagelabels.csv')
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/test-annotations-human-imagelabels-boxable.csv'))
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/test-annotations-machine-imagelabels.csv'))
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/train-annotations-human-imagelabels-boxable.csv'))
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/train-annotations-machine-imagelabels.csv'))
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/validation-annotations-human-imagelabels-boxable.csv'))
imageid_and_labelname.append(pd.read_csv(
    './open_images_data/validation-annotations-machine-imagelabels.csv'))
for imageid, labelname in zip(tqdm(imageid_and_labelname['ImageID']), imageid_and_labelname['LabelName']):
    if labelname in labelnames:
        Thread(target=append, args=(__imageids, imageid)).start()

del imageid_and_labelname


xmin_ymin_xmax_ymax = pd.read_csv(
    './open_images_data/oidv6-train-annotations-bbox.csv')
xmin_ymin_xmax_ymax.append(pd.read_csv(
    './open_images_data/test-annotations-bbox.csv'))
xmin_ymin_xmax_ymax.append(pd.read_csv(
    './open_images_data/validation-annotations-bbox.csv'))
for i in tqdm(range(len(xmin_ymin_xmax_ymax))):
    info = xmin_ymin_xmax_ymax.iloc[i]
    if info['ImageID'] in __imageids:
        # __imageids_and_bbox[info['ImageID']] = [
        #     info['XMin'], info['YMin'], info['XMax'], info['YMax']]
        Thread(target=append_dict, args=(__imageids_and_bbox, info['ImageID'], [
               info['XMin'], info['YMin'], info['XMax'], info['YMax']])).start()
del xmin_ymin_xmax_ymax

urls = pd.read_csv(
    './open_images_data/oidv6-train-images-with-labels-with-rotation.csv')
urls.append(pd.read_csv(
    './open_images_data/test-images-with-rotation.csv'))
urls.append(pd.read_csv(
    './open_images_data/train-images-boxable-with-rotation.csv'))
urls.append(pd.read_csv(
    './open_images_data/validation-images-with-rotation.csv'))
for i in tqdm(range(len(urls))):
    url = urls.iloc[i]
    if url['ImageID'] in __imageids:
        urlretrieve(url['OriginalURL'], f"./data/{image_id}.png")
        xmin, ymin, xmax, ymax = __imageids_and_bbox[url['ImageID']]
        # file_names.append(f"./data/{image_id}.png")
        # type_of_data.append(url['Subset'])
        # imageurls.append(url['OriginalURL'])
        # imageurls_original.append(url['OriginalLandingURL'])
        # imageids.append(url['ImageID'])
        # xmins.append(xmin)
        # ymins.append(ymin)
        # xmaxs.append(xmax)
        # ymaxs.append(ymax)
        Thread(target=append, args=(ymaxs, ymax)).start()
        Thread(target=append, args=(xmaxs, xmax)).start()
        Thread(target=append, args=(ymins, ymin)).start()
        Thread(target=append, args=(xmins, xmin)).start()
        Thread(target=append, args=(imageids, url['ImageID'])).start()
        Thread(target=append, args=(
            imageurls_original, url['OriginalLandingURL'])).start()
        Thread(target=append, args=(imageurls, url['OriginalURL'])).start()
        Thread(target=append, args=(type_of_data, url['Subset'])).start()
        Thread(target=append, args=(
            file_names, f"./data/{image_id}.png")).start()
        image_id += 1

data = pd.DataFrame({
    'ImageIds': imageids,
    'XMin': xmins,
    'YMin': ymins,
    'XMax': xmaxs,
    'YMax': ymaxs,
    'File Name': file_names,
    'ImageUrls': imageurls,
    'Og_ImageUrls': imageurls_original,
    'Type of Data': type_of_data,
})
data.to_csv('./data.csv')
np.save('./output/__imageids.npy', __imageids)

np.save('./output/__imageids_and_bbox.npy', __imageids_and_bbox)
np.save('./output/imageids.npy', imageids)
np.save('./output/xmins.npy', xmins)
np.save('./output/ymins.npy', ymins)
np.save('./output/xmaxs.npy', xmaxs)
np.save('./output/file_names.npy', file_names)
np.save('./output/imageurls.npy', imageurls)
np.save('./output/imageurls_original.npy', imageurls_original)
np.save('./output/type_of_data.npy', type_of_data)
np.save('./output/image_id.npy', image_id)
torch.save({
    'ImageIds': imageids,
    'XMin': xmins,
    'YMin': ymins,
    'XMax': xmaxs,
    'YMax': ymaxs,
    'File Name': file_names,
    'ImageUrls': imageurls,
    'Og_ImageUrls': imageurls_original,
    'Type of Data': type_of_data,
}, './output/data.pt')
torch.save({
    'ImageIds': imageids,
    'XMin': xmins,
    'YMin': ymins,
    'XMax': xmaxs,
    'YMax': ymaxs,
    'File Name': file_names,
    'ImageUrls': imageurls,
    'Og_ImageUrls': imageurls_original,
    'Type of Data': type_of_data,
}, './output/data.pth')
