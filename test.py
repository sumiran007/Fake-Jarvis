import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
print("CUDA available:", torch.cuda.is_available())

if device.type == "cuda":
    print("GPU count:", torch.cuda.device_count())
    print("Current GPU index:", torch.cuda.current_device())
    try:
        print("GPU name:", torch.cuda.get_device_name(0))
    except Exception:
        pass

# Tensor check
x = torch.randn(2, 3).to(device)
print("Tensor device:", x.device, "is_cuda:", x.is_cuda)

# Model check
model = torch.nn.Linear(3, 2).to(device)
print("Model params device:", next(model.parameters()).device)

# Example: verify moving a batch (use non_blocking with pinned memory in DataLoader)
batch = torch.randn(4, 3)
batch_gpu = batch.to(device, non_blocking=True)
print("Batch device:", batch_gpu.device)