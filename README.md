[English](README.md) | [中文](README_CN.md)
# 🎲 Rotating 3D Cube
**Pure Python implementation with Tkinter (no third-party dependencies)**

---

### 📖 Project Overview
This project implements a smooth rotating 3D cube animation using only the built-in `tkinter` library from Python's standard library. It reproduces the classic 3D perspective projection effect based on the pinhole imaging principle of geometric optics, and realizes the spatial rotation of the cube through 3D coordinate transformation formulas.

> Reference Tutorial: [One Formula That Demystifies 3D Graphics](https://youtu.be/qjWkNZ0SXfo?si=xNpgccAyyMGSGiR-)

---

### ✨ Features
- 📦 **Zero Dependencies**: Runs directly with the standard Python environment, no need to install any third-party packages
- 🎯 **Classic Perspective Projection**: Implemented strictly based on pinhole imaging and similar triangle principles, restoring the real perspective effect of "near big, far small"
- 🔄 **Smooth 3D Rotation**: Driven by linear algebra transformation formulas to achieve real-time and smooth spatial rotation animation
- 🧩 **Lightweight & Easy to Learn**: Minimal code structure, perfect for beginners to learn the fundamentals of 3D graphics

---

### 🔍 Implementation Principle
#### 1. Perspective Projection Principle
The core of mapping 3D space coordinates to a 2D screen is perspective projection, which is derived from the **pinhole imaging model** of geometric optics and the mathematical principle of similar triangles.
- We set the camera at the origin of the 3D space `(0, 0, 0)`, with the line of sight along the positive direction of the Z-axis
- Only points with `z > 0` (located in front of the camera) can be captured and displayed on the screen
- The farther the point is from the camera (the larger the z value), the smaller the projected coordinate on the 2D screen, which achieves the "near big, far small" perspective effect

#### 2. 3D Spatial Rotation Implementation
The rotation animation of the cube is realized by the 3D coordinate rotation formula of linear algebra. By updating the rotation angle in real time and recalculating the coordinates of each vertex of the cube, we can achieve a continuous and smooth rotation effect.

---

### 📐 Core Formulas
#### 1. Perspective Projection Formula
Map 3D space coordinates `(x, y, z)` to 2D screen coordinates `(x', y')`:
$$
x' = \frac{x}{z}
$$
$$
y' = \frac{y}{z}
$$
*Where `z` is the distance between the spatial point and the camera*

#### 2. Spatial Rotation Formula
Core 2D plane rotation formula (the basis for 3D multi-axis composite rotation):
$$
x' = x \cdot \cos\beta - y \cdot \sin\beta
$$
$$
y' = x \cdot \sin\beta + y \cdot \cos\beta
$$
*Where $\beta$ is the rotation angle around the axis*

---

### 🚀 Quick Start
#### Prerequisites
- Python 3.6+ (built-in `tkinter` included, pre-installed in most Python distributions)
- Optional: uv (for virtual environment management, consistent with the project configuration)

#### Run Steps
1. Clone this repository
```bash
git clone https://github.com/Lightouch9/Rotating_3d_object.git
cd Rotating_3d_object
```

2. (Optional) Sync virtual environment with uv
```bash
uv sync
```

3. Run the program
```bash
python main.py
```

After running, you will see the rotating 3D cube animation in the pop-up window!

---

### 🙏 References & Acknowledgements
This project is inspired and referenced from the tutorial of [Tsoding](https://www.youtube.com/@TsodingDaily): *One Formula That Demystifies 3D Graphics*
Video link: https://youtu.be/qjWkNZ0SXfo?si=xNpgccAyyMGSGiR-