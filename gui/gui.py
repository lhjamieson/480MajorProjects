#################################################################
## GUI.PY
## This file is all about making windows, editing windows, and filling out windows.
## There are buttons that load, save, do popups, open, and print
##
##

import tempfile  # won't need this forever
import tkinter as tk
import win32api
import win32print
from tkinter import filedialog, ttk
import sys, os


# For test purposes
def empty_button():
    print("You pressed that button.")


# Takes output and sends it to a printer. details to come
def print_callback():
    filename = tempfile.mktemp(".txt")
    open(filename, 'w').write('Test!!!')
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )


# Used by upload buttons to open a file browser
def upload_callback():
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")))
    print(name2.read())


# This is going to open a file browser
# and the user will specify where they want the output to be saved to.
def save_output():
    name = filedialog.asksaveasfile(mode='w', title='Save output',
                                    filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")))
    name.write("hewwo?")


# Called when info button is pressed
# Prints the INFO section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def info_callback():
    global info_popup  #This must be global so we can check if it's open
    info_popup = tk.Toplevel()
    info_popup['padx'] = 20
    # popup['pady'] = 20
    info_popup.configure(bg='white')
    info_popup.iconbitmap(seahawk_icon_path)
    info_popup.wm_title("Information")

    popup_text = ""
    f = open(README_path, 'r')
    lines = f.readlines()
    for line in lines:
        if line.__contains__('HELP'):  # stop after reaching the help section
            break
        if not line.__contains__('====='):  # so it doesn't include the ===ABOUT=== line in the file.
            popup_text += line
    f.close()
    #msg_width = info_popup.winfo_width() - 40
    popup_message = tk.Message(info_popup, text=popup_text, width=400, anchor='center', bg='white')

    popup_message.grid()
    button1 = tk.Button(info_popup, text="Close", command=info_popup.destroy)
    button1.grid(pady=(0, 20))
    info_popup.focus()
    info_popup.rowconfigure(0, weight=2, minsize=45)
    info_popup.columnconfigure(0, weight=2, minsize=45)
    info_popup.mainloop()


# This function handles a pressed info or help button
# If the window indicated is open, it brings it to the front and focus
# If it's not open yet, it creates it. This is to prevent duplicate windows
def open_popup(pressed):
    if pressed == 'info':
        if (info_popup is not None) and info_popup.winfo_exists():
            # info popup is open
            info_popup.lift()
            info_popup.focus()
        else:
            # info popup isn't open
            info_callback()
    elif pressed == 'help':
        if (help_popup is not None) and help_popup.winfo_exists():
            # help_popup is open
            help_popup.lift()
            help_popup.focus()
        else:
            # help_popup isn't open
            help_callback()

# Called when help button is pressed
# Prints the HELP section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def help_callback():
    global help_popup
    help_popup = tk.Toplevel()
    help_popup['padx'] = 20
    help_popup.configure(bg='white')
    help_popup.iconbitmap(seahawk_icon_path)
    help_popup.wm_title("Help")

    popup_text = ""
    f = open(README_path, 'r')
    lines = f.readlines()
    HELP_flag = False
    messages = []
    for line in lines:
        if line.__contains__('HELP'):
            HELP_flag = True
        if HELP_flag and not line.__contains__('===='):
            popup_text += line
            if line.__contains__(':'):
                messages.append(tk.Message(help_popup, text=line, width=300, anchor='center', bg='white', font=('calibri', 10, 'bold'), bd=-7))
            else:
                messages.append(tk.Message(help_popup, text=line, width=300, anchor='center', bg='white', bd=-5))

    f.close()
    # popup_message = tk.Message(help_popup, text=popup_text, width=400, anchor='center', bg='white')

    # popup_message.grid()
    for m in messages:
        m.grid(sticky='w')
    button1 = tk.Button(help_popup, text="Close", command=help_popup.destroy)
    button1.grid(pady=(20, 20))
    help_popup.mainloop()


#################################################################
## SOME VARIABLES
## We are defining some stuff that will be used later
##

smcm_blue = '#1d285a'
logo_path = "images\\college-logo.gif"
print_icon_path = 'images\\print-icon.gif'
help_icon_path = 'images\\help-icon.gif'
about_icon_path = 'images\\info-icon.gif'
seahawk_icon_path = 'images\\seahawk-icon.ico'
README_path = 'README'
info_popup = None  # This is necessary for checking if the window is open
help_popup = None


#################################################################
## WINDOW STUFF
## We are defining and packing up some widgets.
##

# Window formatting
root = tk.Tk()  # The window object
# root.geometry("300x395") # Leaving this out makes the window resize itself
root.title("SMCM Exam Scheduler")
root['padx'] = 20
root['pady'] = 20
root.configure(bg='white')
root.iconbitmap(seahawk_icon_path)

# Logo formatting
logo = tk.PhotoImage(
    file=logo_path)
logo = logo.subsample(2, 2)
logo_widget = tk.Label(root, image=logo, bg='white')

# Print icon formatting
print_icon = tk.PhotoImage(file=print_icon_path)
print_icon = print_icon.subsample(100, 100)

about_icon = tk.PhotoImage(file=about_icon_path)
about_icon = about_icon.subsample(18, 18)

help_icon = tk.PhotoImage(file=help_icon_path)
help_icon = help_icon.subsample(35, 35)

# Separator that goes under the title
sep = ttk.Separator(root, orient='horizontal')

# Define title
title_text = "Exam Scheduler"
title = tk.Message(root, text=title_text, width=400, anchor='center')
title.config(font=('calibri', 14), foreground=smcm_blue, bg='white')

# Define the labels for upload buttons
text_1_str = "Upload course schedule .csv file:"
text_1 = tk.Message(root, text=text_1_str, width=1000, bg='white', font=('calibri', 10))

text_2_str = "Upload finals schedule .csv file:"
text_2 = tk.Message(root, text=text_2_str, width=1000, bg='white', font=('calibri', 10))

# Upload buttons
upload_cschedule_button = tk.Button(root, text='Browse...',
                                    command=upload_callback)  # , relief='flat', bg=smcm_blue, fg='white') #This stuff makes her pretty

upload_fschedule_button = tk.Button(root, text='Browse...', command=upload_callback)

# Output buttons
save_output_button = tk.Button(root, text='Save Output...', command=save_output)

display_output_button = tk.Button(root, text='Display Output...', command=empty_button)

print_button = tk.Button(root, image=print_icon, width=25, height=25, command=print_callback)

info_buttons_frame = tk.Frame(root)  # purely for the aesthetic

about_button = tk.Button(info_buttons_frame, image=about_icon, width=15, height=15,
                         command=lambda: open_popup('info'))

help_button = tk.Button(info_buttons_frame, image=help_icon, width=15, height=15, command=lambda: open_popup('help'))

################################
# Put all the widgets into the window with a whole bunch of formatting
#

logo_widget.grid(row=0, column=0, columnspan=2)
title.grid(row=1, column=0, columnspan=2)
sep.grid(row=2, column=0, columnspan=2, sticky='ew')
text_1.grid(row=3, column=0, columnspan=2, padx=0, pady=(20, 5), sticky="W")
upload_cschedule_button.grid(row=4, column=0, columnspan=2, padx=20)
text_2.grid(row=5, column=0, columnspan=2, padx=0, pady=(10, 5), sticky='W')
upload_fschedule_button.grid(row=6, column=0, columnspan=2, padx=20)
save_output_button.grid(row=7, column=0, padx=12, pady=(20, 0), sticky='E')
display_output_button.grid(row=7, column=1, pady=(20, 0), sticky='W')
print_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))
info_buttons_frame.grid(row=9, column=1, sticky="E")

# These automatically pack into info_buttons_frame frame.
about_button.pack(side="left")
help_button.pack(side="right")

# about_button.grid(row=9, column=1, columnspan=2, padx=(0, 12), sticky='E')
# help_button.grid(row=9, column=2, columnspan=2, sticky='W')
# root.rowconfigure(7, weight=2, minsize=45) # this is the stuff for moving buttons around when the window is resized

# Make the window persistent
root.mainloop()
