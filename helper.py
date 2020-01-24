import matplotlib.pyplot as plt

def plot_model(hist, size=(16,4)):
    plt.figure(figsize=size)
    x = range(1, len(hist.epoch)+1)

    metrics = [x for x in hist.history.keys() if not "val_" in x]
    for i in range(len(metrics)):
        plt.subplot(1,len(metrics),i+1)
        plt.plot(x, hist.history[metrics[i]],'m--')
        if "val_"+metrics[i] in hist.history.keys():
            plt.plot(x, hist.history["val_"+metrics[i]], 'b-')
            plt.legend([metrics[i],"val_"+metrics[i]])
        else:
            plt.legend([metrics[i]])
        plt.xlabel('epoch')
        plt.ylim()
        plt.grid()

    plt.show()
