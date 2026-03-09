import inspect

import matplotlib.pyplot as plt
from pathlib import Path

from src.paths import FIG_PATH


def prep_data(res):
    """
    Task: prepares data from a database into a form that python can use to plot.


    Inputs:
        * res (sqlite3.Cursor) - Cursor containing the results of an SQLite query. This must have only 2 columns.

    Outputs:
        * x (Array) - the first array of data to be plotted.
        * y (Array) - the second array of data to be plotted.
    """
    data = res.fetchall()

    if not data:
        raise ValueError("Query returned no rows.")

    num_cols = len(data[0])
    if num_cols != 2:
        raise ValueError(f"Expected exactly 2 columns, but query returned {num_cols} columns.")
    
    x,y = zip(*data)
    return x,y


def save_plot(folder_name, fig, title):
    """
    Task: Saves a plotted figure into the 'data/figs' folder.

    Inputs:
        * folder_name (String) - The folder that the figure will go into inside of '/figs'.
        * fig (matplotlib.figure.Figure) - The figure to be saved.
        * title (String) - The title of the figure and the name of the file.
    """
    fig.savefig(
        Path(FIG_PATH) / folder_name / f"{title}.png",
        dpi=300,
        bbox_inches="tight"
    )


def plot_bar_chart(
    x_values,
    y_labels,
    x_label="X axis",
    y_label="Y axis",
    title="Title",
    save=False,
    chunk_size=50
):
    """
    Tasks:
        * Generates a bar chart from x and y array data.
        * Simple horizontal bar charts: numeric x vs text y.
        * Splits into multiple figures if there are more than `chunk_size` items to plot.

    Inputs:
        * x_values (Array) - The values that will be mapped to the x-axis.
        * y_values (Array) - The values that will be mapped to the y-axis.
        * x_label and y_label (String) - Used to label their corresponding axes.
        * title (String) - Titles the plot.
        * Save (bool) - Allows you to either directly save the plot to 'data/figs/' or just display the result.
        * chunk_size (int) - The maximum number of y-axis items before a new plot is created.
    """

    total_items = len(y_labels)
    count = 0

    for start in range(0, total_items, chunk_size):
        count += 1
        end = min(start + chunk_size, total_items)

        x_chunk = x_values[start:end]
        y_chunk = y_labels[start:end]
        y_positions = list(range(len(y_chunk)))

        fig, ax = plt.subplots(figsize=(16, 10))

        ax.barh(y_positions, x_chunk)

        ax.set_yticks(y_positions)
        ax.set_yticklabels(y_chunk, fontsize=8)
        ax.set_ylim(-0.5, len(y_chunk) - 0.5)

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        if title and total_items > chunk_size:
            chunk_title = f"{title} ({start + 1}–{end} of {total_items})"
            ax.set_title(chunk_title)

        elif title:
            chunk_title = title
            ax.set_title(chunk_title)

        ax.grid(axis="x")
        fig.tight_layout()

        if save and chunk_title:
            caller_file = inspect.stack()[1].filename
            folder_name = Path(caller_file).name[0:-3]
            save_plot(folder_name, fig, chunk_title)

        else:
            plt.show()
        
        #close for next loop
        plt.close(fig)






