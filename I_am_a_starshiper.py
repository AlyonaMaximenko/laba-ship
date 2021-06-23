import matplotlib.pyplot as plt

H = float(input ('Начальная высота H = '))
H_finish = float(input ('Конечная высота H_fin = '))
M=3150
m=1000
g=1.62
U=3660
a_m=29.43
V_m_x=3
V_m_y=1
V_x=0
V_y=0
a_x=0
a_y=0
t=0
rasxod=0
L=0
Y = []
VT = []
AT = []
Time = []
Dlina = []

while ((V_y*V_y + V_x*V_x)/g + L <= 250000 - L):
    t += 0.1
    a_x = 17.3982
    rasxod = M*a_x/(U/2**0.5)
    a_y = (U*rasxod/2**0.5-M*g)/M
    M = M - rasxod*0.1
    m = m - rasxod*0.1
    V_x = V_x + a_x*0.1
    V_y = V_y + a_y*0.1
    H = H + V_y*0.1
    L = L + V_x*0.1
    VT.append((V_x*V_x+V_y*V_y)**0.5)
    AT.append((a_x*a_x+a_y*a_y)**0.5)
    Y.append(H)
    Dlina.append(L)
    Time.append(t)
print ('V_x = ', V_x, 'V_y = ', V_y, 'H = ', H, 'L = ', L, 'a = ', 45, 'Расход = ', rasxod,'t = ', t,)


H_dvig = H
while H >= H_dvig:
    rasxod = 0
    alpha = 0
    t += 0.1
    a_x = 0
    a_y = -1*g
    M = M - rasxod*0.1
    m = m - rasxod*0.1
    V_x = V_x + a_x*0.1
    V_y = V_y + a_y*0.1
    H = H + V_y*0.1
    L = L + V_x*0.1
    VT.append((V_x*V_x+V_y*V_y)**0.5)
    AT.append((a_x*a_x+a_y*a_y)**0.5)
    Y.append(H)
    Dlina.append(L)
    Time.append(t)
print ('V_x = ', V_x, 'V_y = ', V_y, 'H = ', H, 'L = ', L, 'a = ',alpha, 'Расход = ', rasxod,'t = ', t,)
       
while V_x >= 0:
    t += 0.1
    a_x = -18.025
    rasxod = -M*a_x/(U/2**0.5)
    a_y = (U*rasxod/2**0.5-M*g)/M
    M = M - rasxod*0.1
    m = m - rasxod*0.1
    V_x = V_x + a_x*0.1
    V_y = V_y + a_y*0.1
    H = H + V_y*0.1
    L = L + V_x*0.1
    VT.append((V_x*V_x+V_y*V_y)**0.5)
    AT.append((a_x*a_x+a_y*a_y)**0.5)
    Y.append(H)
    Dlina.append(L)
    Time.append(t)
print ('V_x = ', V_x, 'V_y = ', V_y, 'H = ', H, 'L = ', L, 'a = ',-45, 'Расход = ', rasxod,'t = ', t,)

V_x = 0
while H > H_finish + 56:
    rasxod = 0
    alpha = 0
    t += 0.1
    a_x = 0
    a_y = -1*g
    M = M - rasxod*0.1
    m = m - rasxod*0.1
    V_x = V_x + a_x*0.1
    V_y = V_y + a_y*0.1
    H = H + V_y*0.1
    L = L + V_x*0.1
    VT.append((V_x*V_x+V_y*V_y)**0.5)
    AT.append((a_x*a_x+a_y*a_y)**0.5)
    Y.append(H)
    Dlina.append(L)
    Time.append(t)
print ('V_x = ', V_x, 'V_y = ', V_y, 'H = ', H, 'L = ', L, 'a = ',-45, 'Расход = ', rasxod,'t = ', t,)

while (V_y < 0):
    t += 0.1
    a_x = 0
    a_y = 5
    rasxod = M*(g+a_y)/U
    M = M - rasxod*0.1
    m = m - rasxod*0.1
    V_x = V_x + a_x*0.1
    V_y = V_y + a_y*0.1
    H = H + V_y*0.1
    L = L + V_x*0.1
    VT.append((V_x*V_x+V_y*V_y)**0.5)
    AT.append((a_x*a_x+a_y*a_y)**0.5)
    Y.append(H)
    Dlina.append(L)
    Time.append(t)
print ('V_x = ', V_x, 'V_y = ', V_y, 'H = ', H, 'L = ', L, 'a = ',-45, 'Расход = ', rasxod,'t = ', t,)

fig = plt.figure()

ax_1 = fig.add_subplot(323)
ax_1.plot(Dlina, Y)
ax_1.set_title('График зависимости y(x)')
plt.grid()

ax_2 = fig.add_subplot(324)
ax_2.plot(Time, AT)
ax_2.set_ylim([0, 50])
ax_2.set_title('График зависимости a(t)')
plt.grid()

ax_3 = fig.add_subplot(311)
ax_3.plot(Time, VT)
ax_3.set_title('График зависимости V(t)')
plt.grid()


plt.tight_layout()
plt.show()
