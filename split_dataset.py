import os
import shutil
import random

# ==============================
# Configuration
# ==============================
RAW_DATASET_DIR = "raw_dataset"
OUTPUT_DATASET_DIR = "data"

TRAIN_SPLIT = 0.7
VAL_SPLIT = 0.15
TEST_SPLIT = 0.15

RANDOM_SEED = 42

# ==============================
# Helper Functions
# ==============================
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def split_and_copy(class_name):
    class_path = os.path.join(RAW_DATASET_DIR, class_name)
    images = os.listdir(class_path)

    images = [img for img in images if img.lower().endswith((".jpg", ".png", ".jpeg"))]

    random.shuffle(images)

    total_images = len(images)
    train_end = int(total_images * TRAIN_SPLIT)
    val_end = train_end + int(total_images * VAL_SPLIT)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    for split, split_images in zip(
        ["train", "val", "test"],
        [train_images, val_images, test_images]
    ):
        split_dir = os.path.join(OUTPUT_DATASET_DIR, split, class_name)
        create_dir(split_dir)

        for img in split_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(split_dir, img)
            shutil.copy(src, dst)

    print(
        f"{class_name}: "
        f"Train={len(train_images)}, "
        f"Val={len(val_images)}, "
        f"Test={len(test_images)}"
    )


# ==============================
# Main Execution
# ==============================
if __name__ == "__main__":
    random.seed(RANDOM_SEED)

    classes = os.listdir(RAW_DATASET_DIR)

    for class_name in classes:
        class_dir = os.path.join(RAW_DATASET_DIR, class_name)
        if os.path.isdir(class_dir):
            split_and_copy(class_name)

    print("\nDataset split completed successfully.")
