# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 08:36:09 2024

@author: RS
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = 2 * x

# Legends
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()
plt.show()

# On the same graph we are drawing multiple plots

# For comparing 2 things we use subplots 
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-', label="x**2")     # blue line with dots
ax.plot(x, x**3, 'g--', label="x**3")     # green dashed line
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, x+1, color="blue", alpha=0.5)        # half-transparant
ax.plot(x, x+2, color="#880088")                # RGB hex code
#ax.plot(x, x+3, color="#12FF09")                # RGB hex code
ax.plot(x, x+3, color="#FF8C00")                # RGB hex code
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
# Use linewidth or lw
ax.plot(x, x-1, color="red", linewidth=0.25)
ax.plot(x, x-2, color="red", lw=0.50) 
ax.plot(x, x-3, color="red", lw=1)
ax.plot(x, x-4, color="red", lw=10)
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
# Use linestyle or ls
ax.plot(x, x-1, color="green", lw=3, linestyle = '-')   # solid
ax.plot(x, x-2, color="green", lw=3, ls = '-.')         # dash and dots
ax.plot(x, x-3, color="green", lw=3, ls = ':')          # dots
ax.plot(x, x-4, color="green", lw=3, ls = '--')         # dashed
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
# Use marker for string code
# Use markersize or ms for size
ax.plot(x, x-1, marker="+", markersize=20)
ax.plot(x, x-2, marker="o", ms=20)         # ms can be used for markersize
ax.plot(x, x-3, marker="s", ms=20, lw = 0)          # make linewidth 0 to see only markers
ax.plot(x, x-4, marker="1", ms=20)
plt.show()