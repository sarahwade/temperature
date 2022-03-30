from tkinter import *
from functools import partial  # To prevent unwanted windows
import re
import random

data = ['Hi', 'is', 'this', 'working?']


class Converter:
    def __init__(self, parent):

        # formatting variables
        background_color = "light blue"

        # convert main screen GUI
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # temp conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # export button (row 1)
        self.export_button = Button(self.converter_frame, text="export",
                                    font=("Arial", "14"),
                                    padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        print("You asked for export")
        get_export = Export(self)


class Export:
    def __init__(self, partner):
        background = "purple"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # set up child window (i.e. export box)
        self.export_box = Toplevel()

        # if user press cross at, top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file",
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        # export text (label, row 1)
        self.export = Label(self.export_frame, text="If the filename "
                                                    "you enter below "
                                                    "already exists, "
                                                    "its contents will "
                                                    "be replaced with "
                                                    "your calculation"
                                                    "history",
                            justify=LEFT, bg="#FFAFAF",
                            fg="maroon", wrap=225, padx=10, pady=10,
                            font="arial 10 italic")
        self.export_text.grid(row=1)

        # file name entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # save / cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel buttons (row 0 of save_cancel frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel")
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

        # get filename, can't be blank or invalid
        # assume valid data for now

        has_error = "yes"
        while has_error == "yes":
            has_error = "no"
            # retrieve amount entered into Entry field
            filename = self.filename_entry.get()

            valid_char = "[A-Za-z0-9_]"
            for letter in filename:
                if re.match(valid_char, letter):
                    continue

                elif letter == "":
                    problem = "(no spaces allowed)"

                else:
                    problem = f"(no {letter}'s allowed"
                has_error = "yes"

                if filename == "":
                    problem = "can't be blank"
                    has_error = "yes"

                if has_error == "yes":
                    print(f"Invalid filename - {problem}")
                else:
                    print("you entered a valid filename")

        # add .txt suffix!
        filename = filename + ".txt"

        # create file to hold data
        f = open(filename, "w+")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()



