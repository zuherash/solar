import matplotlib.pyplot as plt
from matplotlib import animation

# Constants
G = 6.67e-11
Mb = 4.0e30
Ms = 2.0e30
Me = 5.972e24
Mm = 6.39e23
Mc = 6.39e20
AU = 1.5e11
daysec = 24.0 * 60 * 60

e_velocity = 29290
m_velocity = 21970
comet_velocity = 7000

gravconst_e = G * Me * Ms
gravconst_m = G * Mm * Ms
gravconst_c = G * Mc * Ms

# Initial conditions
xe, ye, ze = 1.0167 * AU, 0, 0
xve, yve, zve = 0, e_velocity, 0

xm, ym, zm = 1.666 * AU, 0, 0
xvm, yvm, zvm = 0, m_velocity, 0

xc, yc, zc = 2 * AU, 0.3 * AU, 0
xvc, yvc, zvc = 0, comet_velocity, 0

xs, ys, zs = 0, 0, 0
xvs, yvs, zvs = 0, 0, 0

t = 0.0
dt = 0.20 * daysec

# Lists to store positions
xelist, yelist, zelist = [], [], []
xslist, yslist, zslist = [], [], []
xmlist, ymlist, zmlist = [], [], []
xclist, yclist, zclist = [], [], []  # Initialize empty lists for xclist and yclist

# Simulation loop
while t < 5 * 365 * daysec:
    # Earth
    rx, ry, rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5
    fx_e = -gravconst_e * rx / modr3_e
    fy_e = -gravconst_e * ry / modr3_e
    fz_e = -gravconst_e * rz / modr3_e
    
    xve += fx_e * dt / Me
    yve += fy_e * dt / Me
    zve += fz_e * dt / Me
    
    xe += xve * dt
    ye += yve * dt
    ze += zve * dt
    
    xelist.append(xe)
    yelist.append(ye)
    zelist.append(ze)
    
    # Mars
    rx_m, ry_m, rz_m = xm - xs, ym - ys, zm - zs
    modr3_m = (rx_m ** 2 + ry_m ** 2 + rz_m ** 2) ** 1.5
    fx_m = -gravconst_m * rx_m / modr3_m
    fy_m = -gravconst_m * ry_m / modr3_m
    fz_m = -gravconst_m * rz_m / modr3_m
    
    xvm += fx_m * dt / Mm
    yvm += fy_m * dt / Mm
    zvm += fz_m * dt / Mm
    
    xm += xvm * dt
    ym += yvm * dt
    zm += zvm * dt
    
    xmlist.append(xm)
    ymlist.append(ym)
    zmlist.append(zm)
    
    # Comet
    rx_c, ry_c, rz_c = xc - xs, yc - ys, zc - zs
    modr3_c = (rx_c ** 2 + ry_c ** 2 + rz_c ** 2) ** 1.5
    fx_c = -gravconst_c * rx_c / modr3_c
    fy_c = -gravconst_c * ry_c / modr3_c
    fz_c = -gravconst_c * rz_c / modr3_c
    
    xvc += fx_c * dt / Mc
    yvc += fy_c * dt / Mc
    zvc += fz_c * dt / Mc
    
    xc += xvc * dt
    yc += yvc * dt
    zc += zvc * dt
    
    xclist.append(xc)
    yclist.append(yc)
    zclist.append(zc)
    
    # Sun
    xvs += -(fx_e + fx_m) * dt / Ms
    yvs += -(fy_e + fy_m) * dt / Ms
    zvs += -(fz_e + fz_m) * dt / Ms
    
    xs += xvs * dt
    ys += yvs * dt
    zs += zvs * dt
    
    xslist.append(xs)
    yslist.append(ys)
    zslist.append(zs)
    
    t += dt

print('simulation ready')

# Create animation figure
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.grid()

# Create initial empty lines and points
line_e, = ax.plot([], [], '-g', lw=1)
point_e, = ax.plot([AU], [0], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_e = ax.text(AU, 0, 'Earth')

line_m, = ax.plot([], [], '-g', lw=1)
point_m, = ax.plot([1.666 * AU], [0], marker="o", markersize=3, markeredgecolor="red", markerfacecolor="red")
text_m = ax.text(1.666 * AU, 0, 'Mars')

line_c, = ax.plot([], [], '-g', lw=1)
point_c, = ax.plot([2 * AU], [0], marker="o", markersize=2, markeredgecolor="black", markerfacecolor="black")
text_c = ax.text(2 * AU, 0, 'Comet')

point_s, = ax.plot([0], [0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s = ax.text(0, 0, 'Sun')

exdata, eydata = [], []
sxdata, sydata = [], []
mxdata, mydata = [], []
cxdata, cydata = [], []

def update(i):
    exdata.append(xelist[i])
    eydata.append(yelist[i])
    sxdata.append(xslist[i])
    sydata.append(yslist[i])
    mxdata.append(xmlist[i])
    mydata.append(ymlist[i])
    cxdata.append(xclist[i])
    cydata.append(yclist[i])
    
    line_e.set_data(exdata, eydata)
    point_e.set_data(xelist[i], yelist[i])
    text_e.set_position((xelist[i], yelist[i]))
    
    line_m.set_data(mxdata, mydata)
    point_m.set_data(xmlist[i], ymlist[i])
    text_m.set_position((xmlist[i], ymlist[i]))
    
    line_c.set_data(cxdata, cydata)
    point_c.set_data(xclist[i], yclist[i])
    text_c.set_position((xclist[i], yclist[i]))
    
    point_s.set_data(sxdata[i], sydata[i])
    
    ax.axis('equal')
    ax.set_xlim(-3 * AU, 3 * AU)
    ax.set_ylim(-3 * AU, 3 * AU)
    
    return line_e, point_s, point_e, line_m, point_m, text_e, text_m, text_s, line_c, point_c, text_c

# Create animation
anim = animation.FuncAnimation(fig, func=update, frames=len(xelist), interval=1, blit=True)
plt.show()
