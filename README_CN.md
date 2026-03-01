[English](README.md) | [中文](README_CN.md)
# 🎲 3D旋转立方体动画
**基于Python标准库Tkinter实现，无任何第三方依赖**

---

### 📖 项目简介
本项目仅使用Python标准库内置的`tkinter`库，实现了流畅的3D立方体旋转动画。项目基于几何光学的小孔成像原理复现了经典的3D透视投影效果，并通过3D坐标变换公式实现立方体的空间旋转。

> 参考教程: [One Formula That Demystifies 3D Graphics](https://youtu.be/qjWkNZ0SXfo?si=xNpgccAyyMGSGiR-)

---

### ✨ 项目特性
- 📦 **零外部依赖**: 仅需Python标准环境即可直接运行，无需安装任何第三方包
- 🎯 **经典透视投影**: 严格基于小孔成像与相似三角形原理实现，还原真实的近大远小透视效果
- 🔄 **流畅3D旋转**: 基于线性代数变换公式驱动，实现实时、流畅的空间旋转动画
- 🧩 **轻量易读**: 极简代码结构，非常适合新手入门学习3D图形学基础原理

---

### 🔍 实现原理
#### 1. 透视投影原理
3D空间坐标到2D屏幕坐标映射的核心是透视投影，该效果基于几何光学的**小孔成像模型**与相似三角形数学原理推导得出。
- 约定相机位于3D空间原点`(0, 0, 0)`，视线沿Z轴正方向
- 只有`z > 0`（位于相机前方）的点才能被相机捕捉，最终渲染到屏幕上
- 空间点距离相机越远（z值越大），在2D屏幕上的投影坐标就越小，以此实现近大远小的透视效果

#### 2. 3D空间旋转实现
立方体的旋转动画通过线性代数的3D坐标旋转公式实现。通过实时更新旋转角度，重新计算立方体每个顶点的空间坐标，最终实现连续流畅的旋转效果。

---

### 📐 核心公式
#### 1. 透视投影核心公式
将3D空间坐标`(x, y, z)`映射为2D屏幕坐标`(x', y')`：

$$
x' = \frac{x}{z}
$$

$$
y' = \frac{y}{z}
$$

*其中`z`为空间点与相机的距离*

#### 2. 空间坐标旋转公式
核心2D平面旋转公式（3D多轴复合旋转的基础）：

$$
x' = x \cdot \cos\beta - y \cdot \sin\beta
$$

$$
y' = x \cdot \sin\beta + y \cdot \cos\beta
$$

*其中$\beta$为绕轴旋转的角度*

---

### 🚀 快速开始
#### 环境要求
- Python 3.6及以上版本（已内置`tkinter`，绝大多数Python发行版默认预装）
- 可选: uv（用于虚拟环境管理，与本项目配置一致）

#### 运行步骤
1. 克隆本仓库
```bash
git clone https://github.com/Lightouch9/Rotating_3d_object.git
cd Rotating_3d_object
```

2. （可选）使用uv同步虚拟环境
```bash
uv sync
```

3. 运行程序
```bash
python main.py
```

运行后即可在弹出的窗口中看到旋转的3D立方体动画！

---

### 🙏 参考与致谢
本项目灵感与核心实现参考自[Tsoding](https://www.youtube.com/@TsodingDaily)的教程：《One Formula That Demystifies 3D Graphics》
视频链接：https://youtu.be/qjWkNZ0SXfo?si=xNpgccAyyMGSGiR-