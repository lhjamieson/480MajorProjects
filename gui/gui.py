import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Separator


# For test purposes
def empty_button():
    print("You pressed that button.")


# Used by upload buttons to open a file browser
def upload_callback():
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    print(name2.read())


# This is going to open a file browser
# and the user will specify where they want the output to be saved to.
def save_output():
    name = filedialog.asksaveasfile(mode='w', title='Save output',
                                    filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    name.write("hewwo?")


# Called when info button is pressed
# Prints the INFO section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def info_callback():
    f = open(README_path, 'r')
    lines = f.readlines()
    for line in lines:
        if line.__contains__('HELP'):
            break
        print(line)
    f.close()
    print('info button was successfully pressed')


# Called when help button is pressed
# Prints the HELP section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def help_callback():
    f = open(README_path, 'r')
    lines = f.readlines()
    HELP_flag = False
    for line in lines:
        if line.__contains__('HELP'):
            HELP_flag = True
        if HELP_flag:
            print(line)
    f.close()
    print('help button was successfully pressed')


#################################################################
## SOME VARIABLES
## We are defining some stuff that will be used later
##

smcm_blue = '#1d285a'
logo_path = "images\\college-logo.gif"
print_icon_path = 'images\\print-icon.gif'
help_icon_path = 'images\\print-icon.gif'
about_icon_path = 'images\\info-icon.gif'
README_path = 'README'

#################################################################
## WINDOW STUFF
## We are defining and packing up some widgets.
##

# Window formatting
root = tk.Tk()  # The window object
root.geometry("300x395")
root.resizable(False, False)
root.title("SMCM Exam Scheduler")
root['padx'] = 30
root['pady'] = 30
root.configure(bg='white')

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
help_icon = help_icon.subsample(110, 110)

# Separator that goes under the title
sep = Separator(root, orient='horizontal')

# Define title
title_text = "Exam Scheduler"
title = tk.Message(root, text=title_text, width=400, anchor='center')
title.config(font=('calibri', 14), foreground=smcm_blue, bg='white')

# Define the labels for upload buttons
text_1_str = "Upload course schedule .csv file:"
text_1 = tk.Message(root, text=text_1_str, width=1000, bg='white')

text_2_str = "Upload finals schedule .csv file:"
text_2 = tk.Message(root, text=text_2_str, width=1000, bg='white')

# Upload buttons
upload_cschedule_button = tk.Button(root, text='Browse...', command=upload_callback)

upload_fschedule_button = tk.Button(root, text='Browse...', command=upload_callback)

# Output buttons
save_output_button = tk.Button(root, text='Save Output...', command=save_output)

display_output_button = tk.Button(root, text='Display Output...', command=empty_button)

print_button = tk.Button(root, image=print_icon, width=25, height=25, command=empty_button)

about_button = tk.Button(root, image=about_icon, width=15, height=15, command=info_callback)

help_button = tk.Button(root, image=help_icon, width=15, height=15, command=help_callback)

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
about_button.grid(row=9, column=1, columnspan=2, padx=(0, 12), sticky='E')
help_button.grid(row=9, column=2, columnspan=2, sticky='W')

# Make the window persistent
root.mainloop()
