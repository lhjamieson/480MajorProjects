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

import tkinter as tk
import pandas as pd
from tkinter import filedialog as fd
from tkinter.ttk import Separator

def callback():
    fileAddress = fd.askopenfile(mode='rb', initialdir='/', title='Select a file',
                                   filetypes=(("Excel Files", "*.xlsx"), ("All files", "*.*")))

def ESexcelToMatrix():
    print('Converting Exam Schedual to Python Matrix')
    fileAddress = fd.askopenfile(mode='rb', initialdir='/', title='Select a file', filetypes=(("Excel Files", "*.xlsx"), ("All files", "*.*")))
    dfes = pd.read_excel(treatSelectedAddress(fileAddress))
    dirtyESM = dfes.as_matrix(columns=None)
    w, h = 3, len(dfes.index);
    ExamScheduleMatrix = [[0 for x in range(w)] for y in range(h)]
    for x in range(len(dfes.index)):
        ExamScheduleMatrix[x][0] = dirtyESM[x][2]
        ExamScheduleMatrix[x][1] = dirtyESM[x][3]
        ExamScheduleMatrix[x][2] = dirtyESM[x][4]
    printExamSchedual(ExamScheduleMatrix)


def CLexcelToMatrix():
    print('Converting Course List to Python Matrix')
    fileAddress = fd.askopenfile(mode='rb', initialdir='/', title='Select a file', filetypes=(("Excel Files", "*.xlsx"), ("All files", "*.*")))
    dfcl = pd.read_excel(treatSelectedAddress(fileAddress))
    dirtyCLM = dfcl.as_matrix(columns=None)
    w, h = 7, len(dfcl.index);
    CourseListMatrix = [[0 for x in range(w)] for y in range(h)]
    CourseListMatrix[0] = [['Course Number'], ['Course Title'], ['Section Number'], ['Class Meeting Time'], ['Class Meeting Days'], ['Building Code'], ['Room Number']]
    for x in range(len(dfcl.index)):
        CourseListMatrix[x][0] = dirtyCLM[x][0]
        CourseListMatrix[x][1] = dirtyCLM[x][1]
        CourseListMatrix[x][2] = dirtyCLM[x][5]
        CourseListMatrix[x][3] = dirtyCLM[x][9]
        CourseListMatrix[x][4] = dirtyCLM[x][13]
        CourseListMatrix[x][5] = dirtyCLM[x][14]
        CourseListMatrix[x][6] = dirtyCLM[x][15]
    printCourseList(CourseListMatrix)

def printCourseList(CourseListMatrix):
    for row in CourseListMatrix:
        print(row)

def printExamSchedual(ExamScheduleMatrix):
    print('Exam Date , Exam Begin Time , Exam End Time')
    for row in ExamScheduleMatrix:
        print(row)

def treatSelectedAddress(fileAddress):
    strFileAddress = fileAddress.name
    strFileAddress = strFileAddress.replace("/", "\\\\")
    return strFileAddress

def GUI():
    smcm_blue = '#1d285a'
    logo_path = 'LOCAL MACHINE IMAGE FILE PATH'
    print_icon_path = 'LOCAL MACHINE IMAGE FILE PATH'

    root = tk.Tk()  # The window object
    root.geometry("300x400")
    root.resizable(False,False)
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
    print_icon = tk.PhotoImage(
        file=print_icon_path)
    print_icon = print_icon.subsample(100, 100)

    # Separator that goes under the title
    sep = Separator(root, orient='horizontal')

    # Define title
    title_text = "Exam Scheduler"
    title = tk.Message(root, text=title_text, width=400, anchor='center')
    title.config(font=('calibri', 14), foreground=smcm_blue, bg='white')

    # Define the labels for upload buttons
    text_1_str = "Upload course schedule .xlsx file:"
    text_1 = tk.Message(root, text=text_1_str, width=1000, bg='white')

    text_2_str="Upload exams schedule .xlsx file:"
    text_2 = tk.Message(root, text=text_2_str, width=1000, bg='white')

    # Upload buttons
    upload_cschedule_button = tk.Button(root, text='Browse...', command=CLexcelToMatrix)
    upload_fschedule_button = tk.Button(root, text='Browse...', command=ESexcelToMatrix)

    # Output buttons
    save_output_button = tk.Button(root, text='Save Output', command=callback)
    display_output_button = tk.Button(root, text='Display Output', command=callback)

    print_button = tk.Button(root, image=print_icon, width=25, height=25, command=callback)

    logo_widget.grid(               row=0, column=0, columnspan=2)
    title.grid(                     row=1, column=0, columnspan=2)
    sep.grid(                       row=2, column=0, columnspan=2,                       sticky='ew')
    text_1.grid(                    row=3, column=0, columnspan=2, padx=0,  pady=(20,5), sticky="W")
    upload_cschedule_button.grid(   row=4, column=0, columnspan=2, padx=20)
    text_2.grid(                    row=5, column=0, columnspan=2, padx=0,  pady=(10,5), sticky='W')
    upload_fschedule_button.grid(   row=6, column=0, columnspan=2, padx=20)
    save_output_button.grid(        row=7, column=0,               padx=12, pady=(20,0), sticky='E')
    display_output_button.grid(     row=7, column=1,                        pady=(20,0), sticky='W')
    print_button.grid(              row=8, column=0, columnspan=2,          pady=(10,0))

    # Make the window persistent
    root.mainloop()

GUI()

