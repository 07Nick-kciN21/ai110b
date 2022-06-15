import torch
import math

# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = 0+1*x+2*x**2+3*x**3 # torch.sin(x)

# Prepare the input tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)
'''
xx 為 tensor (x, x^2, x^3) 的陣列，如下
PS D:\pmedia> python
Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import math
>>> x = torch.linspace(-math.pi, math.pi, 2000)
>>> x
tensor([-3.1416, -3.1384, -3.1353,  ...,  3.1353,  3.1384,  3.1416])
>>> p = torch.tensor([1, 2, 3])
>>> p
tensor([1, 2, 3])
>>> x.unsqueeze(-1)            
tensor([[-3.1416],
        [-3.1384],
        [-3.1353],
        ...,
        [ 3.1353],
        [ 3.1384],
        [ 3.1416]])
>>> x.unsqueeze(-1).pow(p)
tensor([[ -3.1416,   9.8696, -31.0063],
        [ -3.1384,   9.8499, -30.9133],
        [ -3.1353,   9.8301, -30.8205],
        ...,
        [  3.1353,   9.8301,  30.8205],
        [  3.1384,   9.8499,  30.9133],
        [  3.1416,   9.8696,  31.0063]])
'''
# Use the nn package to define our model and loss function.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)

def loss_fn(output, target):
    loss = torch.mean((output - target)**2)
    return loss
# loss_fn = torch.nn.MSELoss(reduction='sum')

def GD(inputs, outputs, model, loss_fn, loop_max = 10000, learning_rate = 1e-3):
	# Use the optim package to define an Optimizer that will update the weights of
	# the model for us. Here we will use RMSprop; the optim package contains many other
	# optimization algorithms. The first argument to the RMSprop constructor tells the
	# optimizer which Tensors it should update.
	# 註 參考 hinton https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf
	# rmsprop: Divide the learning rate for a weight by a running average of the magnitudes of recent gradients for that weight.
	optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
	for t in range(loop_max):
		# Forward pass: compute predicted y by passing x to the model.
		predicats = model(inputs)

		# Compute and print loss.
		loss = loss_fn(predicats, outputs)
		if t % 100 == 99:
			print(t, loss.item())

		# Before the backward pass, use the optimizer object to zero all of the
		# gradients for the variables it will update (which are the learnable
		# weights of the model). This is because by default, gradients are
		# accumulated in buffers( i.e, not overwritten) whenever .backward()
		# is called. Checkout docs of torch.autograd.backward for more details.
		optimizer.zero_grad()

		# Backward pass: compute gradient of the loss with respect to model
		# parameters
		loss.backward()

		# Calling the step function on an Optimizer makes an update to its
		# parameters
		optimizer.step()

GD(inputs=xx, outputs=y, model=model, loss_fn=loss_fn)
linear_layer = model[0]
# 為何以下這行用 linear_layer.weight[:, 0].item() ? 這是甚麼意思?
# 猜測:因為 .weight 是個 torch 物件，而非 list，透過 weight[:] 先轉為 list 之後，再取出第 i 個...
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')
torch.save(model, 'model.ckpt')