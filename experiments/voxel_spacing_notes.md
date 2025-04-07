# 🧠 Understanding Voxel Spacing & Pixel Resolution Metadata

## 📌 What is Voxel Spacing?
In 3D or volumetric imaging, each pixel or voxel represents a real-world measurement. The **voxel spacing** (or pixel resolution) tells us how much **physical space** (e.g., in mm or microns) a voxel occupies in each axis (X, Y, Z).

Knowing this is **critical** in medical imaging for accurate measurements, segmentation, and 3D visualization.

---

## 🔍 File Formats Explored

### 🖼️ TIFF
- Stores resolution using `XResolution` and `YResolution` tags.
- Some metadata embedded in `ImageDescription`.
- Used `tifffile` library for parsing.
- ✅ Simple and direct, but not always standardized.

---

### 🧠 NIfTI (.nii / .nii.gz)
- Used heavily in neuroscience and medical imaging.
- Pixel spacing stored in the **`pixdim`** array within the header.
- Used `nibabel` for metadata extraction.
- ✅ Supports 3D + 4D data, good voxel detail.

---

### 🔬 HDF5 (.h5)
- Hierarchical format — metadata can be stored as **custom attributes**.
- Used `h5py` to access dataset-level attributes.
- Flexible but no strict standard for voxel spacing.
- ✅ Powerful, but requires understanding of dataset structure.

---

## 💡 ilastik-Specific Observations (Work in Progress)
- ilastik supports many file types via `lazyflow` and `volumina`.
- It may use internal project files (`.ilp`) to store resolution metadata.
- Likely interacts with voxel spacing during:
  - Data import
  - Feature extraction
  - Segmentation overlays

---

## 🔍 Code Snippet for TIFF Metadata
```python
import tifffile

with tifffile.TiffFile('sample.tiff') as tif:
    tags = tif.pages[0].tags
    x_res = tags.get('XResolution').value
    y_res = tags.get('YResolution').value
    print("X Resolution:", x_res, "Y Resolution:", y_res)
