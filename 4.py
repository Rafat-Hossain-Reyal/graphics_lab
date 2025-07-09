import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Clipping constants ---
LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

# --- Clipping window ---
clip_window = (1.5, 3.5, 2.5, 4.5)  # xmin, xmax, ymin, ymax

# --- Star polygon points (closed) ---
star = [
    (2.5, 5.0), (2.8, 3.6), (4.2, 3.6),
    (3.0, 2.6), (3.5, 1.2), (2.5, 2.0),
    (1.5, 1.2), (2.0, 2.6), (0.8, 3.6),
    (2.2, 3.6), (2.5, 5.0)
]

# --- Inside test ---
def inside(p, edge, bounds):
    x, y = p
    xmin, xmax, ymin, ymax = bounds
    if edge == LEFT:
        return x >= xmin
    elif edge == RIGHT:
        return x <= xmax
    elif edge == BOTTOM:
        return y >= ymin
    elif edge == TOP:
        return y <= ymax

# --- Find intersection point ---
def intersection(p1, p2, edge, bounds):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax, ymin, ymax = bounds

    if x1 == x2:
        m = float('inf')
    else:
        m = (y2 - y1) / (x2 - x1)

    if edge == LEFT:
        x = xmin
        y = y1 + m * (x - x1)
    elif edge == RIGHT:
        x = xmax
        y = y1 + m * (x - x1)
    elif edge == BOTTOM:
        y = ymin
        x = x1 + (y - y1) / m if m != 0 else x1
    elif edge == TOP:
        y = ymax
        x = x1 + (y - y1) / m if m != 0 else x1

    return (x, y)

# --- Clip polygon against one edge ---
def clip_polygon(polygon, edge, bounds):
    output = []
    prev = polygon[-1]
    for curr in polygon:
        if inside(curr, edge, bounds):
            if inside(prev, edge, bounds):
                output.append(curr)
            else:
                output.append(intersection(prev, curr, edge, bounds))
                output.append(curr)
        elif inside(prev, edge, bounds):
            output.append(intersection(prev, curr, edge, bounds))
        prev = curr
    return output

# --- Perform all four edge clipping steps ---
clip_steps = [star]
for edge in [LEFT, RIGHT, BOTTOM, TOP]:
    clipped = clip_polygon(clip_steps[-1], edge, clip_window)
    clip_steps.append(clipped)

# --- Titles for each subplot ---
titles = ["Original Polygon", "Clip Left", "Clip Right", "Clip Bottom", "Clip Top"]

# --- Plotting ---
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
xmin, xmax, ymin, ymax = clip_window

for i in range(5):
    ax = axes[i]
    polygon = clip_steps[i]
    if len(polygon) > 1:
        x, y = zip(*polygon)
        ax.plot(x, y, 'black')
        ax.fill(x, y, 'black', alpha=0.9)
    
    # Draw clipping window as dashed rectangle
    rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                             linewidth=1, edgecolor='gray', facecolor='none', linestyle='--')
    ax.add_patch(rect)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5.5)
    ax.set_title(titles[i], fontsize=10)
    ax.set_aspect('equal')
    ax.axis('off')

plt.tight_layout()
plt.show()
