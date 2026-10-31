# Signature-Verification

Handwritten signature classification across four people (Akbar, Anny, Parvez, Shirina) using CNNs (VGG19 and ResNet).

## Structure
- `raw_data/` – original scans, cropped signatures (`splited_data/`) and augmented images
- `preprocessing_codes/`
  - `resize.py` – resizes images while keeping aspect ratio
  - `augment.py` – random rotation and flip augmentation
  - `data_split.py` – splits data into train/val/test (80/10/10)
- `dataset/` – final `train`, `val` and `test` sets
- `metrics.csv` – per-epoch accuracy, precision, recall and F1 (train/val)
- `plots/` – loss/accuracy curves and confusion matrix

## Results
After 200 epochs the model reaches **~93.5% training accuracy** and **~98% validation accuracy** (see `metrics.csv` and `plots/`).

> Note: the preprocessing scripts use hard-coded paths; edit them before running.
