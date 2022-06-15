import torch
import math

model = torch.load('model.ckpt')
inputs = torch.tensor([[2, 4, 8]], dtype=torch.float)
predict = model(inputs)
print(f'predict={predict}')
