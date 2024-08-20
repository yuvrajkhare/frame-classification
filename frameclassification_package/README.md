
# Surgical Frame Classification 

This package provides tools for pretraining models using reverse contrastive learning and fine-tuning them on labeled datasets. It includes functionalities for data augmentation, custom datasets, model training, and evaluation.

## Installation

To install the package, use the following command:

```bash
pip install .
```

## Usage

### Pretraining

```python
from src.pretraining.train import train_pretraining_model

train_simclr_model('/path/to/unlabelled/images')
```

### Fine-tuning

```python
from src.finetuning.train import train_finetune_model

train_finetune_model(
    annotations_files=['/path/to/annotations1.xml', '/path/to/annotations2.xml','/path/to/annotations3.xml'],
    image_dirs=['/path/to/images1', '/path/to/images2','/path/to/images3'],
    augmented_images_dir='/path/to/augmented_frames',
    base_model_checkpoint='/path/to/pretrained/model.pth',
    results_path='/path/to/save/results.pkl',
    checkpoint_dir='/path/to/save/checkpoints'
)
```

## License

This project is licensed under the MIT License.
