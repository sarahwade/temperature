from tkinter import *
from functools import partial  # To prevent unwanted windows
import re


class Converter:
    def __init__(self, parent):

        # formatting variables
        background_color = "light blue"

        # initialise list to hold calculation history
        self.all_calc_list = []

        # convert frame - main screen GUI
        self.converter_frame = Frame(bg=background_color, width=300, height=300,
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
                                             font="Arial 10 italic",
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
                                  text="To Centigrade", font="Garamond 12 bold",
                                  padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Garamond 12 bold",
                                  highlightbackground="#ff83fa", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # answer label
        self.converted_label = Label(self.converter_frame, font="arial 12 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # history / help button (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=15,
                                  padx=10, pady=10, command=self.help)
        # command help button set for history command for now, change later
        self.help_button.grid(row=0, column=0)

        # history button (column 1)
        self.history_button = Button(self.hist_help_frame, text="History",
                                     width=15, font="Arial 12 bold",
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)

    def temp_convert(self, low):

        error = "#ffafaf"
        # pale pink background for when entry box has errors

        # retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # check and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert} degrees C is {fahrenheit} degrees F"

            # check and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert * 5/9) - 32
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert} degrees F is {celsius} degrees C"

            else:
                # Input is invalid (too cold)
                answer = "Too Cold!"
                has_errors = "yes"

            # display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
                print(answer)
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # add answer to list of history
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                print(self.all_calc_list)
                self.history_button.config(state=NORMAL)

        except ValueError:
            print("oops")
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

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

        # set up heading (row 0)
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


class History:
    def __init__(self, partner, calc_history):
        background = "#98FB98"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # set up child window (i.e. history box)
        self.history_box = Toplevel()

        # if user press cross at, top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="History / Instructions",
                                 font="Arial 12 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use the "
                                                           "export button to create a text for "
                                                           "file of all your calculations for"
                                                           "this session", wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # history output goes (here row 2)
        # generate string from list of calculations...
        history_string = ""

        if len(calc_history) > 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history, You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # label to display calculation history user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg="#6bfa6b", font="arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # frame for export and dismiss buttons (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button (row 3)
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    padx=5, pady=5, font="arial 10 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # dismiss button (row 3)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  width=10, bg='orange', font="arial 10 bold", padx=5, pady=5,
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):
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
                                 font="Garamond 14 bold", bg=background)
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

        # error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="#ffafaf",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # save / cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel buttons (row 0 of save_cancel frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 14 bold", padx=5, pady=5,
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 14 bold",
                                    padx=5, pady=5,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):
        # get filename, can't be blank or invalid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        # retrieve input entered into Entry field
        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
                has_error = "yes"

            else:
                problem = ("(no {}'s allowed)".format(letter))
                has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        # check that there are no errors before saving the file
        if has_error == "yes":
            # display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            print("you entered a valid filename")

            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")
                
            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
