# %%
!nvidia-smi

# %%
from numpy import *
from math import pi as pi
from math import sin, cos
import matplotlib as plt
from pylab import *
%pylab inline

# %%
x = linspace(-pi,pi,201)

x,y = meshgrid (x,x)
z = sin(5*x)
for i in range (5000):
    y = sin(5*z)

# x = np.arange(-pi, pi, pi/4)
# y = np.arange(-pi, pi, pi/4) 
# xx, yy = np.meshgrid(x, y, sparse=True)
# z = sin(5 *xx)

# plt.figure(figsize=(10,8)) 
# # plt.contourf(x, y, z)
# plt.axis('scaled')

plt.figure(figsize=(10,8))
imshow(y)

# %%
x = linspace(-pi,pi,201)

x,y = meshgrid (x,x)
for i in range (5000):
    z = ((sin(5*x)**2) + (sin(3*y)**2))/2

# x = np.arange(-pi, pi, pi/4)
# y = np.arange(-pi, pi, pi/4) 
# xx, yy = np.meshgrid(x, y, sparse=True)
# z = sin(5 *xx)

# plt.figure(figsize=(10,8)) 
# # plt.contourf(x, y, z)
# plt.axis('scaled')

plt.figure(figsize=(10,8))
imshow(z)

# %%
def Plasma(n,m):
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)
    for i in range (5000):
        z = ((sin(5*x)**n) + (sin(3*y)**n))/m

    # x = np.arange(-pi, pi, pi/4)
    # y = np.arange(-pi, pi, pi/4) 
    # xx, yy = np.meshgrid(x, y, sparse=True)
    # z = sin(5 *xx)

    # plt.figure(figsize=(10,8)) 
    # # plt.contourf(x, y, z)
    # plt.axis('scaled')

    plt.figure(figsize=(10,8))
    imshow(z)

# %%
def PlasmaN(n,m):
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)
    for i in range (n):
        z = ((sin(5*x)**n) + (sin(3*y)**n))/m

    # x = np.arange(-pi, pi, pi/4)
    # y = np.arange(-pi, pi, pi/4) 
    # xx, yy = np.meshgrid(x, y, sparse=True)
    # z = sin(5 *xx)

    # plt.figure(figsize=(10,8)) 
    # # plt.contourf(x, y, z)
    # plt.axis('scaled')

    plt.figure(figsize=(10,8))
    imshow(z)

# %%
Plasma(3,2)

# %%
Plasma(8,9)

# %%
Plasma(10,100)


# %%
Plasma(100,10)

# %%
PlasmaN(4, 20000)

# %%
PlasmaN(4,8)

# %%
PlasmaN(9,4)

# %%
from numpy import sin, cos, ceil
x = linspace(-pi,pi,201)
x,y = meshgrid (x,x)
a = cos(20*x)**2
b = sin(20*y)**2
z = cos((20*(a)) + (b))

    # x = np.arange(-pi, pi, pi/4)
    # y = np.arange(-pi, pi, pi/4) 
    # xx, yy = np.meshgrid(x, y, sparse=True)
    # z = sin(5 *xx)

    # plt.figure(figsize=(10,8)) 
    # # plt.contourf(x, y, z)
    # plt.axis('scaled')
plt.figure(figsize=(10,8))
imshow(z)

# %%
def Plasma2(n):
    from numpy import sin, cos, ceil
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)
    a = cos(20*x)**n
    b = sin(20*y)**n
    z = cos((20*(a)) + (b))

        # x = np.arange(-pi, pi, pi/4)
        # y = np.arange(-pi, pi, pi/4) 
        # xx, yy = np.meshgrid(x, y, sparse=True)
        # z = sin(5 *xx)

        # plt.figure(figsize=(10,8)) 
        # # plt.contourf(x, y, z)
        # plt.axis('scaled')
    plt.figure(figsize=(10,8))
    imshow(z)

# %%
for i in range(10):
    Plasma2(i)

# %%
def PlasDoc(n):
    from numpy import sin, cos, ceil
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)
    a = cos(20*x)**n
    b = sin(20*y)**n
    z = cos((20*(a)) + (b))

        # x = np.arange(-pi, pi, pi/4)
        # y = np.arange(-pi, pi, pi/4) 
        # xx, yy = np.meshgrid(x, y, sparse=True)
        # z = sin(5 *xx)

        # plt.figure(figsize=(10,8)) 
        # # plt.contourf(x, y, z)
        # plt.axis('scaled')
    plt.figure(figsize=(10,8))
    imshow(abs(z))

# %%
for i in range(11):
    PlasDoc(i)

# %%
def PlasDoc2(n, p):
    from numpy import sin, cos, ceil
    x = linspace(-n,n,201)
    x,y = meshgrid (x,x)
    a = cos(20*x)**p
    b = sin(20*y)**p
    z = cos((20*(a)) + (b))

        # x = np.arange(-pi, pi, pi/4)
        # y = np.arange(-pi, pi, pi/4) 
        # xx, yy = np.meshgrid(x, y, sparse=True)
        # z = sin(5 *xx)

        # plt.figure(figsize=(10,8)) 
        # # plt.contourf(x, y, z)
        # plt.axis('scaled')
    plt.figure(figsize=(10,8))
    imshow(abs(z))

# %%
for i in range(8):
    PlasDoc2(i,i-1)

# %%
for i in range(6):
    PlasDoc2(0.2, i)

# %%
from numpy import sin, cos, dstack
x = linspace(-pi,pi,201)
x,y = meshgrid (x,x)
r = cos(x) + sin(y)
red = cos(r*y)
green = cos(r*y*x)
blue = sin(r*x)
z = dstack((red, green,blue))

plt.figure(figsize=(10,8))
imshow(z)


# %%
def RGBPlas(n,p):
    from numpy import sin, cos, dstack
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)
    r = cos(x)**n + sin(y)**n
    red = cos(r*y)**p
    green = cos(r*y*x)**p
    blue = sin(r*x)**p
    z = dstack((red, green,blue))

    plt.figure(figsize=(10,8))
    imshow(z)


# %%
for i in range(9):
    RGBPlas(i,i-1)

# %%
for i in range(10):
    RGBPlas(i,i*3)

# %%
from numpy import sqrt, hstack
def AniPlas(t):
    x = linspace(-pi,pi,201)
    x,y = meshgrid (x,x)

    v1 = sin(10*x + 5*t)
    v2 = sin(10*(x*sin(t/2)) + y*cos(t/3)+ 5*t)
    cx = x + 5*sin(t/5)
    cy = y + 5*cos(t/3)
    v3 = sin(sqrt(100*(cx**2 + cy**2)+1)+t)
    v = v1+v2+v3


    g = cos(pi*v)
    b = sin(pi*v)
    r = ones_like(b)
    z = dstack((r,g,b))

    plt.figure(figsize=(10,8))
    imshow(z)

# %%
for t in range(7): 
    x = linspace(-pi, pi, 201)
    x, y = meshgrid(x, x)

    v1 = sin(10*x + 5*t)
    v2 = sin(10*(x*sin(t/2)) + y*cos(t/3) + 5*t)
    cx = x + 5*sin(t/5)
    cy = y + 5*cos(t/3)
    v3 = sin(sqrt(100*(cx**2 + cy**2)+1)+t)
    v = v1+v2+v3

    g = cos(pi*v)
    b = sin(pi*v)
    r = ones_like(g)
    z = dstack((r, g,b))

    plt.figure(figsize=(10, 9))
    imshow(z)


# %%
for i in range(12):
    AniPlas(1)

# %%
for i in range(9):
    AniPlas(2*i)

# %%
def ConCir(n):
    from numpy import sin
    x = linspace(-pi,pi,100)
    x,y = meshgrid (x,x)
    z = sin(n*sqrt(x**2 + y**2))

    plt.figure(figsize=(10,8))
    imshow(abs(z))

# %%
for i in range(12):
    ConCir(2*i)

# %%
for i in range(10):
    ConCir(5*i)

# %%
for i in range(10):
    ConCir(0.4*i)

# %%
for i in range(10):
    ConCir(100*i)

# %%
for i in range(10):
    ConCir(abs(i*1j))

# %%
def ConCirN(i,n):
    from numpy import sin
    x = linspace(-pi,pi,n*50)
    x,y = meshgrid (x,x)
    z = sin(i*sqrt(x**2 + y**2))
    imshow(abs(z))

# %%
plt.figure(figsize=(50,20))
ax = plt.figure(figsize=(8,5))
for i in range(25):
    # plt.subplot(5,5,i+1, ax)
    f, axs = plt.subplots(figsize=(10,10), sharex=True)
    plt.title('S' + str(i) ,color='m')
    ConCirN(6*i,i)

# %%



