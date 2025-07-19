# PyTorch Basics

Welcome to the **PyTorch Basics** repository! This README serves as a comprehensive and beautifully structured guide for beginners and intermediate learners to understand the core concepts of **PyTorch**, one of the most popular deep learning libraries.

---

## 📌 Table of Contents

1. [Introduction to PyTorch](#introduction-to-pytorch)
2. [Installing PyTorch](#installing-pytorch)
3. [Tensors](#tensors)
4. [Autograd](#autograd)
5. [Neural Networks](#neural-networks)
6. [Training a Model](#training-a-model)
7. [GPU Support](#gpu-support)
8. [Saving and Loading Models](#saving-and-loading-models)
9. [Useful Resources](#useful-resources)

---

## 🔍 Introduction to PyTorch

**PyTorch** is an open-source machine learning framework developed by Facebook's AI Research lab. It provides:

- Tensor computation with strong GPU acceleration
- Deep Neural Networks built on a tape-based autograd system
- Dynamic computation graphs

---

## ⚙️ Installing PyTorch

Install PyTorch via pip:

```bash
pip install torch torchvision torchaudio
```

Check installation:

```python
import torch
print(torch.__version__)
```

---

## 📐 Tensors

Tensors are the core building blocks in PyTorch.

```python
import torch

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0])
print(x)

# Tensor operations
print(x + 2)
print(x * 3)
```

Key features:

- N-dimensional arrays
- GPU support
- Broadcasting

---

## 🔁 Autograd

Autograd automatically computes gradients for tensors:

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
y.backward()
print(x.grad)  # dy/dx
```

---

## 🧠 Neural Networks

Use `torch.nn` to create models:

```python
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        return self.fc(x)
```

---

## 🏋️ Training a Model

Steps to train a model:

```python
model = Net()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Dummy training loop
for epoch in range(100):
    inputs = torch.randn(10, 2)
    targets = torch.randn(10, 1)

    outputs = model(inputs)
    loss = criterion(outputs, targets)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

## 🚀 GPU Support

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

---

## 💾 Saving and Loading Models

```python
# Save
torch.save(model.state_dict(), 'model.pth')

# Load
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

---

## 📚 Useful Resources

- [Official PyTorch Docs](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Deep Learning with PyTorch Book](https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf)

---

> ✨ This guide is beginner-friendly and suitable for quick revision or teaching material.

Feel free to fork, clone, and contribute to this repository!

---

### 🔗 License

MIT License. See `LICENSE` for more details.

---

Happy Learning! 🚀

