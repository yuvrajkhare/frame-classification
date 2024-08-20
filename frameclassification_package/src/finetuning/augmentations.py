# -*- coding: utf-8 -*-
"""augmentations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SRaS0u-ddU9ULvV96WZSop4zXNmk0_YL
"""

from torchvision import transforms

def get_finetune_transforms():
    """
    Returns the data augmentation pipeline for fine-tuning.
    """
    train_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    return train_transforms, val_transforms