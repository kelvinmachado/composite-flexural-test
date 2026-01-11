import matplotlib.pyplot as plt

def plot_response(P, delta, label):
    plt.plot(delta * 1e3, P, marker='o', label=label)
    plt.xlabel("Mid-span displacement [mm]")
    plt.ylabel("Load [N]")
    plt.grid(True)
