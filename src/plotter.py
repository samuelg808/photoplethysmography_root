import matplotlib.pyplot as plt

class Plot():
    @staticmethod
    def plot(**kwargs): 
        """ 
        Plots the data on a graph

        :type **kwargs: dict, arbitrary keyword arguments.
        :rtype: plt.figure.Figure
        """
        
        fig = plt.Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        ax.plot(kwargs["xvals"], kwargs["signal"])

        if "xticks" in kwargs:
            ax.set_xticks(kwargs["xticks"])

        ax.set_xlabel(kwargs["xlabel"])
        ax.set_ylabel(kwargs["ylabel"])

        if kwargs["save"] is True:
            fig.savefig("../output/" + kwargs["filename"] + ".png")

        return fig
