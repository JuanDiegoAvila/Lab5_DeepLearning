import torch

print("Versión de PyTorch:", torch.__version__)
print("Versión de CUDA:", torch.version.cuda)
print("CUDA disponible:", torch.cuda.is_available())
