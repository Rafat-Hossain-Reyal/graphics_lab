import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots()

# Draw green rectangle (flag background)
ax.add_patch(plt.Rectangle((0, 0), 10, 6, color='#006a4e'))  # green

# Draw red circle (centered slightly to the left)
#ax.add_patch(plt.Circle((4.5, 3), 2, color='#f42a41'))  # red
ax.add_patch(plt.Circle((5, 3), 2, color='#f42a41'))
# Set limits and turn off axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
plt.axis('off')

# Show flag
plt.show()
