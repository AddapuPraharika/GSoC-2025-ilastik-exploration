import tifffile
import nibabel as nib
import h5py
import os

def read_tiff_metadata(file_path):
    print(f"\n🔍 Reading TIFF metadata from: {file_path}")
    with tifffile.TiffFile(file_path) as tif:
        tags = {tag.name: tag.value for tag in tif.pages[0].tags.values()}
        for key, value in tags.items():
            print(f"{key}: {value}")

def read_nifti_metadata(file_path):
    print(f"\n🧠 Reading NIfTI metadata from: {file_path}")
    img = nib.load(file_path)
    print("Voxel size (pixdim):", img.header.get_zooms())
    print("Header info:\n", img.header)

def read_hdf5_metadata(file_path):
    print(f"\n📦 Reading HDF5 metadata from: {file_path}")
    with h5py.File(file_path, 'r') as hdf:
        def print_attrs(name, obj):
            if isinstance(obj, h5py.Dataset):
                print(f"\n📌 Dataset: {name}")
                for key, val in obj.attrs.items():
                    print(f" - {key}: {val}")
        hdf.visititems(print_attrs)

# 🔧 Replace with your own test files
test_files = {
    "tiff": "test_files/sample_image.tiff",
    "nifti": "test_files/sample_image.nii.gz",
    "hdf5": "test_files/sample_data.h5"
}

if __name__ == "__main__":
    for file_type, path in test_files.items():
        if not os.path.exists(path):
            print(f"❌ {file_type.upper()} file not found at {path}")
            continue
        if file_type == "tiff":
            read_tiff_metadata(path)
        elif file_type == "nifti":
            read_nifti_metadata(path)
        elif file_type == "hdf5":
            read_hdf5_metadata(path)
