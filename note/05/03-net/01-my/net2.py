from net import Net
net = Net()

x = net.variable(1)
y = net.variable(3)
x2 = net.mul(x, x)
y2 = net.mul(y, y)
o  = net.add(x2, y2)

net.gradient_descendent()
print('x=', x.v, 'y=', y.v)
