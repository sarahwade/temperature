from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self, parent):

        # formatting variables
        background_color = "light blue"

        # convert frame - main screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # temp conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font="Garamond 16 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                                  "converted and then push"
                                                  "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Ariel 14 bold")
        self.to_convert_entry.grid(row=2)

        # conversion button frame (row 3), khaki1=#c3b091 | orchid=#ff83fa
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  highlightbackground="Khaki1",
                                  text="To Centigrade", font="Arial 10 bold",
                                  padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Garamond 10 bold",
                                  highlightbackground="#ff83fa", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # answer label
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # history / help button (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15,
                                       padx=5, pady=5)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5,
                                  padx=5, pady=5)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (i.e. help box)
        self.help_box = Toplevel()

        # if user press cross at, top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg='orange', font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
