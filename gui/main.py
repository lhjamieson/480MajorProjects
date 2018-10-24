# code description: The below code incorperates the front end GUI with back end input functionallity

# if everything works the two browse buttons should be configured for a user to select an xlsx file,
# have the contents brought into a python matrix, and then printed to console

# indexing issues might occur - length and width are not fully dynamic with varrying xlsx file format
# do not forget to configure the image file paths to your local machine

# Things to consider:

# as a user i will want to see the file path and the selected file before i tell the program to continue
# for the user this ensures their selection was received by the program and confirms the file selected is the one they
# intend to work with

# i think the display output should show the file contents within the GUI and if the user wishes to save the file
# and open it in excel they have that option. i think the user should be able to preview content before saving it

# currently the print icon is cut off at the bottom of the gui - maybe allow for resizing of window

import pandas as pd
import tkinter as tk
import re
from tkinter import filedialog
from tkinter.ttk import Separator

CSM = [[0][0]]
ESM = [[0][0]]
output = [[0][0]]

# For test purposes
def empty_button():
    print("You pressed that button.")


# Used by exam schedule upload button to open a file browser
def upload_callback():
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")))
    print(name2)
    CLexcelToMatrix(name2)

# Used by course upload buttons to open a file browser
def upload_callback2():
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")))
    ESexcelToMatrix(name2)


# This is going to open a file browser
# and the user will specify where they want the output to be saved to.
def save_output():
    name = filedialog.asksaveasfile(mode='w', title='Save output',
                                    filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")))
    exam_assignment()
    output_writing(name)


# Called when info button is pressed
# Prints the INFO section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def info_callback():
    README_path = 'README'
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
    README_path = 'README'
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

def ESexcelToMatrix(fa):
    print('Converting Exam Schedual to Python Matrix')
    fileAddress = fa
    dfes = pd.read_excel(treatSelectedAddress(fileAddress))
    dirtyESM = dfes.as_matrix(columns=None)
    global ESM
    ESM = dirtyESM



def CLexcelToMatrix(fa):
    print('Converting Course List to Python Matrix')
    fileAddress = fa
    dfcl = pd.read_excel(treatSelectedAddress(fileAddress))
    dirtyCLM = dfcl.as_matrix(columns=None)
    w, h = 7, len(dfcl.index)
    CourseListMatrix = [[0 for x in range(w)] for y in range(h)]
    CourseListMatrix[0] = [['Course Number'], ['Course Title'], ['Section Number'], ['Class Meeting Time'],
                           ['Class Meeting Days'], ['Building Code'], ['Room Number']]
    course_location = 1
    for x in range(len(dfcl.index)):
        try:
            ct = dirtyCLM[x][9]
            if(ct > 0):
                ed = dirtyCLM[x][8]
                end_d = ed.strftime('%Y-%m-%d')
                end_date = end_d[5:7]
                if re.match(r'12', end_date):
                    CourseListMatrix[course_location][0] = dirtyCLM[x][0]
                    CourseListMatrix[course_location][1] = dirtyCLM[x][1]
                    CourseListMatrix[course_location][2] = dirtyCLM[x][5]
                    CourseListMatrix[course_location][3] = dirtyCLM[x][9]
                    CourseListMatrix[course_location][4] = dirtyCLM[x][13]
                    CourseListMatrix[course_location][5] = dirtyCLM[x][14]
                    CourseListMatrix[course_location][6] = dirtyCLM[x][15]
                    course_location += 1
                elif re.match(r'11', end_date):
                    CourseListMatrix[course_location][0] = dirtyCLM[x][0]
                    CourseListMatrix[course_location][1] = dirtyCLM[x][1]
                    CourseListMatrix[course_location][2] = dirtyCLM[x][5]
                    CourseListMatrix[course_location][3] = dirtyCLM[x][9]
                    CourseListMatrix[course_location][4] = dirtyCLM[x][13]
                    CourseListMatrix[course_location][5] = dirtyCLM[x][14]
                    CourseListMatrix[course_location][6] = dirtyCLM[x][15]
                    course_location += 1
                elif re.match(r'04', end_date):
                    CourseListMatrix[course_location][0] = dirtyCLM[x][0]
                    CourseListMatrix[course_location][1] = dirtyCLM[x][1]
                    CourseListMatrix[course_location][2] = dirtyCLM[x][5]
                    CourseListMatrix[course_location][3] = dirtyCLM[x][9]
                    CourseListMatrix[course_location][4] = dirtyCLM[x][13]
                    CourseListMatrix[course_location][5] = dirtyCLM[x][14]
                    CourseListMatrix[course_location][6] = dirtyCLM[x][15]
                    course_location += 1
                elif re.match(r'05', end_date):
                    CourseListMatrix[course_location][0] = dirtyCLM[x][0]
                    CourseListMatrix[course_location][1] = dirtyCLM[x][1]
                    CourseListMatrix[course_location][2] = dirtyCLM[x][5]
                    CourseListMatrix[course_location][3] = dirtyCLM[x][9]
                    CourseListMatrix[course_location][4] = dirtyCLM[x][13]
                    CourseListMatrix[course_location][5] = dirtyCLM[x][14]
                    CourseListMatrix[course_location][6] = dirtyCLM[x][15]
                    course_location += 1
        except AttributeError:
            cl = 0
        except TypeError:
            cl = 0
    global CSM
    CSM = CourseListMatrix


def treatSelectedAddress(fileAddress):
    strFileAddress = fileAddress.name
    strFileAddress = strFileAddress.replace("/", "\\\\")
    return strFileAddress

def exam_assignment():
    global CSM
    global ESM
    global output
    output_location = 0
    output = [[0 for i in range(8)] for j in range(len(CSM))]
    for x in range(len(CSM)):  # for each course in course list:
        # get course meeting days and time
        # based on a course's meeting days and time, assign it to the matching exam time and date
        # CSM[x][4] Course meeting days; course meeting days has 7 slots,
        # CSM[x][3] Course start time
        # ESM[x][0] Exam course meeting days; exam course meeting days has 6
        # ESM[x][1] Exam course start time

        # if the 4th index in CSM is a string, remove the first character
        # This is because the meeting days in CSM and ESM are different length
        # CSM is 7 characters and starts with Sunday, while ESM is 6 characters and starts with Monday
        if isinstance(CSM[x][4], str):
            # remove first character in string
            CSM[x][4] = CSM[x][4][1:7]
        # Check if course has a meeting time
            for y in range(len(ESM)):  # for each exam time in exam schedule
                # if course meeting days match exam schedule course meeting days,
                # and Course start time match exam schedule course start time
                if CSM[x][4] == ESM[y][0] and CSM[x][3] == ESM[y][1]:
                    output[output_location][0] = CSM[x][0]  # course number
                    output[output_location][1] = CSM[x][1]  # course title
                    output[output_location][2] = CSM[x][2]  # section number
                    output[output_location][3] = CSM[x][5]  # building code
                    output[output_location][4] = CSM[x][6]  # room number
                    output[output_location][5] = ESM[y][2]  # exam date
                    output[output_location][6] = ESM[y][3]  # exam start time
                    output[output_location][7] = ESM[y][4]  # exam end time
                    output_location += 1

    # output: Course Number, Course Title, Section Number, Building code, Room Number, Exam Date, Exam Start Time, Exam End Time


def output_writing(name):
    global output
    dataColumns = ['Course Number', 'Course Title', 'Section Number', 'Building Code', 'Room Number', 'Exam Date', 'Exam Start Time', 'Exam End Time']
    df = pd.DataFrame(data = output, columns = dataColumns)
    df.to_csv(name, index=False, header=dataColumns)


def GUI():
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

    #################################################################
    ## WINDOW STUFF
    ## We are defining and packing up some widgets.
    ##

    # Window formatting
    root = tk.Tk()  # The window object
    root.geometry("300x395")
    root.resizable(False, True)
    root.title("SMCM Exam Scheduler")
    root['padx'] = 30
    root['pady'] = 30
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

    upload_fschedule_button = tk.Button(root, text='Browse...', command=upload_callback2)

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


GUI()
