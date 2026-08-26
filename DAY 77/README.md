<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2077/day77banner.png" alt="Day 77 - NumPy and N-Dimensional Arrays Banner" width="100%">
</p>

# Day 77 - Computation with NumPy & N-Dimensional Arrays 🔢🖼️

A hands-on tour of NumPy's `ndarray` — from basic 1D/2D/3D array indexing, through slicing challenges and linear algebra, to treating real images as numerical arrays and manipulating them directly.

## 🗂️ Project Structure

```
DAY 77/
├── numpy_n_dimensional_array.ipynb
├── yummy_macarons.jpg
└── README.md
```

## ⚙️ What's Inside the Notebook

### Understanding `ndarray`
- **1D arrays (vectors):** creating arrays from scratch, checking `.shape` and `.ndim`, indexing elements.
- **2D arrays (matrices):** creating a matrix, understanding shape as (rows, columns), indexing individual values and full rows with `[row, :]` slicing.
- **N-D arrays (tensors):** working with a 3-dimensional array, indexing specific values across all three axes, and slicing to extract 1D vectors or 2D sub-matrices from within a higher-dimensional array.

### NumPy Mini-Challenges
A set of hands-on exercises: generating a range with `.arange()`, slicing (last N values, middle ranges, every-other-value), reversing an array two different ways (`np.flip()` vs. `[::-1]`), finding non-zero indices with `.nonzero()`, generating random 3D arrays, and creating evenly-spaced values with `.linspace()` — including plotting two `linspace()`-generated vectors against each other, and visualizing a random noise array as an image with `.imshow()`.

### Linear Algebra with Vectors
- Element-wise addition and multiplication of NumPy vectors — contrasted directly against Python lists, where `+` **concatenates** instead of adding element-wise, and `*` isn't defined at all for two lists.
- **Broadcasting:** adding/multiplying a 2D array by a scalar, where NumPy automatically applies the operation to every element.
- **Matrix multiplication:** using both `np.matmul()` and the `@` operator to multiply matrices of compatible shapes, verifying the resulting shape matches the expected (m×n)·(n×p) = (m×p) rule.

### Manipulating Images as ndarrays
- Loads a sample image (`scipy.misc.face()`, a raccoon photo) and inspects its type, shape, and dimensions — revealing that a color image is just a 3D array of RGB pixel values.
- **Grayscale conversion:** normalizes pixel values to 0–1 (sRGB), then uses `@` (matrix multiplication) against a luminance-weighting vector (`[0.2126, 0.7152, 0.0722]`) to properly convert to grayscale — a real application of the matrix math practiced earlier.
- **Image transformations via array operations:** flipping the grayscale image upside down (`np.flip()`), rotating the color image (`np.rot90()`), and inverting/solarizing colors by computing `255 - img`.
- **Working with a custom image:** loads a personal JPG (`yummy_macarons.jpg`) via `PIL.Image`, converts it to a NumPy array, and applies the same solarize-style inversion technique.

## 🧠 Concepts Practiced

- NumPy `ndarray` fundamentals: shape, dimensions, indexing, slicing across multiple axes
- Vector/matrix arithmetic and how it differs from plain Python lists
- Broadcasting scalars across arrays
- Matrix multiplication (`matmul`/`@`) and verifying result dimensions
- Treating images as multi-dimensional numerical data
- Practical image manipulation (grayscale conversion, flipping, rotating, inverting) purely through array math

## 🚀 Run It

```bash
pip install numpy matplotlib scipy pillow jupyter
jupyter notebook numpy_n_dimensional_array.ipynb
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
