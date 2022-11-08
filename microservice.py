import pandas as pd
import zmq
import matplotlib.pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def create_table(df):
    """Create a table from the given JSON file."""

    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    # Create the table
    alternating_colors = ([['white'] * len(df.columns), ['lightgray'] * len(df.columns)] * len(df))
    alternating_colors = alternating_colors[:len(df)]
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     colColours=['lightblue']*len(df.columns),
                     cellColours=alternating_colors,
                     loc='center',
                     cellLoc='center')

    # Save figure as a PDF
    plt.savefig("./student_roster.pdf", format="pdf", bbox_inches="tight")
    plt.close()


while True:
    json_file = socket.recv_json()
    df = pd.DataFrame(json_file, columns=['First', 'Last', 'id'])
    create_table(df)
    pdf_location = f"/Users/timbobutler/PycharmProjects/CS361/Project/student_roster.pdf"
    socket.send_string(pdf_location)



