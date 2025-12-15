import matplotlib.pyplot as plt

def set_publication_style():
plt.rcParams.update({
"font.family": "serif",
"font.serif": ["Times New Roman"],
"font.size": 11,
"axes.labelsize": 11,
"axes.titlesize": 12,
"xtick.labelsize": 10,
"ytick.labelsize": 10,
"legend.fontsize": 10,
"lines.linewidth": 1.8,
"lines.markersize": 6,
"figure.dpi": 300,
"savefig.dpi": 300,
"axes.linewidth": 1.0
})
