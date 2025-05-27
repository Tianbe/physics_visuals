from pathlib import Path

import matplotlib.pyplot as plt


def set_plot_style(stylename):
    plot_style_path = Path(__file__).parent / (stylename + ".mplstyle")
    plt.style.use(plot_style_path)
