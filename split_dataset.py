import os
import shutil
import random

def create_dir_structure(base_path):
    os.makedirs(os.path.join(base_path, 'train', 'images'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'train', 'labels'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'val', 'images'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'val', 'labels'), exist_ok=True)

def split_dataset(dataset_path, train_ratio=0.8):
    images = [f for f in os.listdir(dataset_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    labels = [f for f in os.listdir(dataset_path) if f.endswith('.txt')]

    data_pairs = [(img, img.replace(img.split('.')[-1], 'txt')) for img in images if img.replace(img.split('.')[-1], 'txt') in labels]

    random.shuffle(data_pairs)
    split_idx = int(len(data_pairs) * train_ratio)

    train_pairs = data_pairs[:split_idx]
    val_pairs = data_pairs[split_idx:]

    print(f"Total pairs: {len(data_pairs)}")
    print(f"Training pairs: {len(train_pairs)}")
    print(f"Validation pairs: {len(val_pairs)}")

    return train_pairs, val_pairs

def move_files(pairs, dataset_path, dest_path):
    for img, lbl in pairs:
        shutil.move(os.path.join(dataset_path, img), os.path.join(dest_path, 'images', img))
        shutil.move(os.path.join(dataset_path, lbl), os.path.join(dest_path, 'labels', lbl))

def main():
    dataset_path = 'dataset'
    create_dir_structure(dataset_path)

    train_pairs, val_pairs = split_dataset(dataset_path)

    move_files(train_pairs, dataset_path, os.path.join(dataset_path, 'train'))
    move_files(val_pairs, dataset_path, os.path.join(dataset_path, 'val'))

if __name__ == "__main__":
    main()