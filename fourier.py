import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(-2,2,5000)
n = 10000
k = 0
ft = 49

ck = np.zeros(int(n))
bk = np.zeros(int(n))
Ak = np.ones(int(n))
phik = np.zeros(int(n))

for k in range(1, n):
    if k%2 == 1:
        ck[k] = 2/(k*np.pi)
        bk[k] = ck[k]**2


def quad(x, f, ft, s=False):
    if s == True:
        shark(f, ft)
    else:
        for i in range(n):
            Ak[i] = 1
            phik[i] = 0
    q = 0
    for i in range(n):
        q += (Ak[i]*ck[i]*np.sin(2*np.pi*f*i*x+phik[i]))
    return q


def shark(f, ft):
    for i in range(n):
        Ak[i] = 1/np.sqrt(1+(((f*i)/ft)**2))
        phik[i] = np.arctan(-(f*i)/ft) + np.pi

def tr(x, f, ft):
    t = 0
    for i in range(n):
        t += (bk[i]*np.cos(2*np.pi*f*i*x))
    return t


# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
plt.figure(1)
plt.title('Onda quadra')
plt.plot(t, quad(t,1, ft,), color='blue')
plt.xlabel('Tempi [s]')
plt.ylabel('$Simulazione$ [a.u.]')
plt.grid(color = 'gray')

plt.figure(2)
plt.title('Onda triangolare')
plt.plot(t, tr(t,1, ft), color='red')
plt.xlabel('Tempi [s]')
plt.ylabel('Simulazione [a.u.]')
plt.grid(color = 'gray')

bbox_props = dict(boxstyle="square", fc="w", lw=1)

x, y = np.loadtxt('data_gen\datiql10.txt', unpack=True)
tt = np.linspace(0,200,1000)
x = x/1000
f=10

x_max=197.4
y_max=640

x2=x[y<y_max]
y2=y[y<y_max]

x1=x2[x2<x_max]
y1=y2[x2<x_max]

plt.figure(3)
plt.title('Andamento dati 1')
plt.plot(x, y, color='red')
plt.xlabel('Tempi [s]')
plt.ylabel('Volt [a.u.]')
plt.grid(color = 'gray')

fig = plt.figure(6)
ax = fig.add_subplot(frameon=False)
ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)

ax1 = fig.add_subplot(311)
ax1.yaxis.set_major_locator(plt.MultipleLocator(200.))
ax1.xaxis.set_major_locator(plt.MultipleLocator(50))
ax1.grid(color = 'gray')
ax1.plot(tt, 320*quad(tt, f, ft, s=True)+479, color='blue', zorder=10)
ax1.errorbar(x1, y1, None, None, '.', color='r', zorder=5)
ax1.text(175, 500,"$f$ = 10 Hz", bbox=bbox_props, zorder =20)

x, y = np.loadtxt('data_gen\datiql50.txt', unpack=True)
tt2 = np.linspace(0,100,1000)
x = x/1000
f=50

x_max=100
y_max=640

x2=x[y<y_max]
y2=y[y<y_max]

x1=x2[x2<x_max]
y1=y2[x2<x_max]


plt.figure(4)
plt.title('Andamento dati 2')
plt.plot(x, y, color='red')
plt.xlabel('Tempi [s]')
plt.ylabel('Volt [a.u.]')
plt.grid(color = 'gray')

ax2 = fig.add_subplot(312)
ax2.yaxis.set_major_locator(plt.MultipleLocator(200))
ax2.xaxis.set_major_locator(plt.MultipleLocator(25))
ax2.grid(color = 'gray')
ax2.plot(tt2, 320*quad(tt2, f, ft, s=True)+479, color='blue', zorder=10)
ax2.errorbar(x1, y1, None, None, '.', color='r', zorder=5)
ax2.text(88, 500,"$f$ = 50 Hz", bbox=bbox_props, zorder =20)

x, y = np.loadtxt('data_gen\datiql250.txt', unpack=True)
tt2 = np.linspace(0,20,1000)
x = x/1000
f=250

x_max=20
y_max=640000

x2=x[y<y_max]
y2=y[y<y_max]

x1=x2[x2<x_max]
y1=y2[x2<x_max]

y1 -= 4.5

plt.figure(5)
plt.title('Andamento dati 2')
plt.plot(x, y, color='red')
plt.xlabel('Tempi [s]')
plt.ylabel('Volt [a.u.]')
plt.grid(color = 'gray')



ax3 = fig.add_subplot(313)
ax3.yaxis.set_major_locator(plt.MultipleLocator(50.))
ax3.xaxis.set_major_locator(plt.MultipleLocator(5))
ax3.grid(color = 'gray')
ax3.plot(tt2, 320*quad(tt2, f, ft, s=True)+479, color='blue', label='Simulazione', zorder=10)
ax3.errorbar(x1, y1, None, None, '.', color='r', label='Dati', zorder=5)
ax3.text(17, 500,"$f$ = 250 Hz", bbox=bbox_props, zorder =20)

ax.set_xlabel('$Tempi$ [ms]')
ax.set_ylabel('$d.d.p.$ [a.u.]')

plt.show()