import os
import cv2
import PIL
from functools import partial
import torch
from torch.vision import VisionDataset
from torch.utils import verify_str_arg
import pandas as pd


class CustomDataset(VisionDataset):
    base_folder="images"
    file_list = ["list_eval_partition.txt"]
    def __init__(self, root_dir, split, transform):
        super(CustomDataset, self).__init__(root_dir, transform)
        self.split=split
        self.root_dir=root_dir
        split_map = {
            "train": 0,
            "valid": 1,
            "test": 2, 
            "all": None,
        }
        split_ = split_map[verify_str_arg(split.lower(), "split", ("train", "valid", "test", "all"))]
        fn = partial(os.path.join, self.root_dir)
        splits = pd.read_csv(fn("list_eval_partition.txt"), delim_whitespace=True, header=None, index_col=0)
        mask = slice(None) if split_ is None else (splits[1] == split_)
        self.filename = splits[mask].index.values

    def __len__(self):
        return len(self.filename)

    def __getitem__(self, idx):
        X = PIL.Image.open(os.path.join(self.root_dir, self.base_folder, self.filename[idx]))
        if self.transform is not None:
            X = self.transform(X)
        return X


