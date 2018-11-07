# code description: This program takes in an exam schedule file and a course schedule file and outputs a file containing
#  the course and it's assigned exam period.


# Imports:
import pandas as pd  # pandas will be used to handle data conversion from excel file to matrix and then matrix to either excel file or csv
import os  # os will be used to open the file on the computer
import re  # re will be used to compare strings in course input
import tkinter as tk  # tkinter is used for making beautiful user interfaces
from tkinter import filedialog  # used for handling browsing files
from tkinter import ttk


# Global Variables
CSM = [[0][0]]  # CSM will be used to hold all important information from the course file
ESM = [[0][0]]  # ESM will be used to hold all the important information from the exam file
output = [[0][0]]  # output will be used to hold courses and their assigned exam times
name = ""  # name will be used to hold the file location of the output


# Display_output will open up the file on the computer for the user to view
def display_output():
    # This line brings in the global variable name
    global name
    # This if statement is true when name contains a file location and is not empty
    if (name != ""):
        # This line calls treatedSelectedAddress to translate the file location into one that can be used by the program
        treatedName = treatSelectedAddress(name)
        # This line opens the file on the computer
        os.startfile(treatedName)


# Used by course upload button to open a file browser
def upload_callback():
    # This line opens the file browser for the user to select the course schedule
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")))
    # This line calls the CLexcelToMatrix method to take in the course input and put the data into the CSM Matrix
    CLexcelToMatrix(name2)


# Used by exam schedule upload buttons to open a file browser
def upload_callback2():
    # This line opens the file browser for the user to select the exam schedule
    name2 = filedialog.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")))
    # This line calls the ESexcelToMatrix method to take in the exam schedule input and put the data into the ESM Matrix
    ESexcelToMatrix(name2)


# This is going to open a file browser
# and the user will specify where they want the output to be saved to.
def save_output():
    # This line brings in the global variable name
    global name
    # This line opens up a file browser and lets the user decide where the output file will be saved
    name = filedialog.asksaveasfile(mode='w', title='Save output',
                                    filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")))
    # This line calls on the exam_assignment method to use CSM and ESM matrixes to create the output data
    exam_assignment()
    # This line calls the output_writing method to output the data to the file location the user selected
    output_writing(name)


# Called when info button is pressed
# Prints the INFO section of the README file
# Someday, we will make it so this function causes a popup with the info printed onto it
def info_callback():
    global info_popup  # This must be global so we can check if it's open
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
    # msg_width = info_popup.winfo_width() - 40
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
                messages.append(tk.Message(help_popup, text=line, width=300, anchor='center', bg='white',
                                           font=('calibri', 10, 'bold'), bd=-7))
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


# The ESexcelToArray method will take in the information from the exam schedule file
#  and put the data into the ESM matrix
def ESexcelToMatrix(fa):
    # This line takes in the information from the exam schedule excel file and puts it into a pandas' data frame
    dfes = pd.read_excel(treatSelectedAddress(fa))
    # This line brings in the glabal matrix ESM
    global ESM
    # This line sets ESM as a matrix containing the data in the pandas dataframe
    ESM = dfes.as_matrix(columns=None)


# The ESexcelToArray method will take in the important information from the course schedule file
#  and put the data into the CSM matrix
def CLexcelToMatrix(fa):
    # This line takes in the information from the course schedule excel file and puts it into a pandas' data frame
    dfcl = pd.read_excel(treatSelectedAddress(fa))
    # This line creates a matrix dirtyCLM that contains all the information from the course excel file
    dirtyCLM = dfcl.as_matrix(columns=None)
    # This line defines the width and height as 7 and length of the course information dataframe
    w, h = 7, len(dfcl.index)
    # This line creates a matrix of size w, h
    CourseListMatrix = [[0 for x in range(w)] for y in range(h)]
    # This variable will be used to hold the current course location in the CourseListMatrix
    course_location = 0
    # This for loop goes through the dirtyCLM matrix
    for x in range(len(dfcl.index)):
        # This try/exempt block handles Atrribute and Type Errors
        try:
            # This variable will be used to check if the course time is not 0 or blank
            ct = dirtyCLM[x][9]
            # This line checks if the course time is not 0 or blank
            if (ct > 0 and ct != None):
                # This line gets the end date of the course
                ed = dirtyCLM[x][8]
                # This line gets the end date as a string in the Year-Month-Day format
                end_d = ed.strftime('%Y-%m-%d')
                # This line gets the month out of the end date of a course
                end_date = end_d[5:7]
                # These if statements check to see if the courses end on the last month of the semester
                # if they do, all important information is put into the CourseListMatrix
                # 0 - Course Number, 1 - Course Title, 2 - Section Title, 3 - Course Start Time, 4 -Course Meeting days
                # 5 - Building Code, 6 - Room Number
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
    # This line brings in the CSM matrix
    global CSM
    # This line sets CSM equal to CourseListMatrix
    CSM = CourseListMatrix


# The treatSelectedAddress method takes in a file address and cleans it up so it can be used in Python
def treatSelectedAddress(fileAddress):
    strFileAddress = fileAddress.name
    strFileAddress = strFileAddress.replace("/", "\\\\")
    return strFileAddress


# Method that takes user-provided course and exam schedules, and assigns
# courses exam times based on provided exam schedule
# Input: CSV files containing course information and exam information
# Output: Matrix containing exam information for every applicable course
def exam_assignment():
    global CSM
    global ESM
    global output
    output = []
    # output = [[0 for i in range(8)] for j in range(len(CSM))]
    for x in range(len(CSM)):  # for each course in course list:
        closest_time = None  # reset the closest exam time for each course

        # CSM[x][4] Course meeting days
        # CSM[x][3] Course start time
        # ESM[x][0] Exam course meeting days
        # ESM[x][1] Exam course start time

        for y in range(len(ESM)):  # for each exam time in exam schedule
            # if course meeting days match exam schedule course meeting days,
            # and course start time match exam schedule course start time
            if CSM[x][4] == ESM[y][0] and CSM[x][3] == ESM[y][1]:
                # output[x][0] = CSM[x][0]  # course number
                # output[x][1] = CSM[x][1]  # course title
                # output[x][2] = CSM[x][2]  # section number
                # output[x][3] = CSM[x][5]  # building code
                # output[x][4] = CSM[x][6]  # room number
                # output[x][5] = ESM[y][2]  # exam date
                # output[x][6] = ESM[y][3]  # exam start time
                # output[x][7] = ESM[y][4]  # exam end time
                output.append([CSM[x][0], CSM[x][1], CSM[x][2], CSM[x][5], CSM[x][6], ESM[y][2], ESM[y][3], ESM[y][4]])
                break  # perfect match found, break out of loop
            # perfect match hasn't been found yet, find the closest exam time
            elif (closest_time is None or closest_time > (CSM[x][3] - ESM[y][1])) and CSM[x][4] == ESM[y][0]:
                # new solution tracks the index of ESM which give the closest time
                # then appends a row with those indexed values if a perfect match is not found after loop has concluded
                # is this solution be better? It uses 2 more integer variables, but doesnt assign values in each pass
                closest_time = CSM[x][3] - ESM[y][1]
                closest_y = y  # index row of exam with the closest time
                # output[x][0] = CSM[x][0]  # course number
                # output[x][1] = CSM[x][1]  # course title
                # output[x][2] = CSM[x][2]  # section number
                # output[x][3] = CSM[x][5]  # building code
                # output[x][4] = CSM[x][6]  # room number
                # output[x][5] = ESM[y][2]  # exam date
                # output[x][6] = ESM[y][3]  # exam start time
                # output[x][7] = ESM[y][4]  # exam end time
            # if a match hasn't been found, append row of course information and exam time of closest normal course time
            if (y == len(ESM) - 1) and closest_time is not None:
                output.append(
                    [CSM[x][0], CSM[x][1], CSM[x][2], CSM[x][5], CSM[x][6], ESM[closest_y][2], ESM[closest_y][3],
                     ESM[closest_y][4]])

    # output: Course Number, Course Title, Section Number, Building code, Room Number, Exam Date, Exam Start Time, Exam End Time


# The output_writing method will output the data to the excel file selected by the user
def output_writing(name):
    # This line brings in the global matrix output
    global output
    # This line defines the headers for the output
    dataColumns = ['Course Number', 'Course Title', 'Section Number', 'Building Code', 'Room Number', 'Exam Date',
                   'Exam Start Time', 'Exam End Time']
    # This line creates a pandas dataframe with the data and header
    df = pd.DataFrame(data=output, columns=dataColumns)
    # This line calls the treatSelectedAddress method to clean up the output file location
    treatedName = treatSelectedAddress(name)
    # This line creates a writer to write to the excel file
    writer = pd.ExcelWriter(treatedName, engine='xlsxwriter')
    # This line puts the information from the dataframe to the excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    # This line saves the excel file and closes the writer
    writer.save()


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
    global seahawk_icon_path, README_path, info_popup, help_popup
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

    # Various icon formatting
    # print_icon = tk.PhotoImage(file=print_icon_path)
    # print_icon = print_icon.subsample(100, 100)

    about_icon = tk.PhotoImage(file=about_icon_path)
    about_icon = about_icon.subsample(18, 18)

    help_icon = tk.PhotoImage(file=help_icon_path)
    help_icon = help_icon.subsample(35, 35)

    # Separator that goes under the title
    sep = ttk.Separator(root, orient='horizontal')
    sep2 = ttk.Separator(root, orient='horizontal')

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

    upload_fschedule_button = tk.Button(root, text='Browse...', command=upload_callback2)

    # Output buttons
    save_output_button = tk.Button(root, text='Save Output...', command=save_output)

    display_output_button = tk.Button(root, text='Display/Print Output...', command=display_output)

    info_buttons_frame = tk.Frame(root)  # purely for the aesthetic

    about_button = tk.Button(info_buttons_frame, image=about_icon, width=15, height=15,
                             command=lambda: open_popup('info'))

    help_button = tk.Button(info_buttons_frame, image=help_icon, width=15, height=15,
                            command=lambda: open_popup('help'))

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
    sep2.grid(row=7, column=0, columnspan=2, pady=(20, 0), sticky='ew')
    save_output_button.grid(row=8, column=0, padx=12, pady=(20, 0), sticky='E')
    display_output_button.grid(row=8, column=1, pady=(20, 0), sticky='W')
    # print_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))  # rip :(
    info_buttons_frame.grid(row=10, column=1, pady=(30, 0), sticky="E")

    # These automatically pack into info_buttons_frame frame.
    about_button.pack(side="left")
    help_button.pack(side="right")

    # about_button.grid(row=9, column=1, columnspan=2, padx=(0, 12), sticky='E')
    # help_button.grid(row=9, column=2, columnspan=2, sticky='W')
    # root.rowconfigure(7, weight=2, minsize=45) # this is the stuff for moving buttons around when the window is resized

    # Make the window persistent
    root.mainloop()


GUI()
