# -*- coding: utf-8 -*-
"""test_finetuning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SRaS0u-ddU9ULvV96WZSop4zXNmk0_YL
"""

import unittest
from src.finetuning.dataset import SurgicalImagesDataset
from src.finetuning.model import create_classifier

class TestFinetuning(unittest.TestCase):
    def test_dataset_loading(self):
        dataset = SurgicalImagesDataset(annotations_file='path/to/annotations.xml', image_dir='path/to/images')
        self.assertTrue(len(dataset) > 0)

    def test_model_initialization(self):
        model = create_classifier()
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()