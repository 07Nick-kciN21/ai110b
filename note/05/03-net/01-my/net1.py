from net import Net
net = Net()

x = net.variable(1)
y = net.variable(3)
x2 = net.mul(x, x)
y2 = net.mul(y, y)
o  = net.add(x2, y2)

print('net.forward()=', net.forward())
print('net.backwward()')
net.backward()
print('x=', x, 'y=', y, 'o=', o)
print('gfx = x.g/o.g = ', x.g/o.g, 'gfy = y.g/o.g=', y.g/o.g)
