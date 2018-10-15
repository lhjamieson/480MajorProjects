# TODO drop classes without meeting days/room numbers? not sure how to reference empty matrix cell
# if dirtyCLM[x][15] == '':
#   print('skipped class with no room number')
# else:
#   CourseListMatrix[x][6] = dirtyCLM[x][15]
# TODO figure out why column titles on the es iteration are overwritten

# import pandas a powerful data science module for python
import pandas as pd

# fill a data frame with the CourseList(cl) and ExamSchedule(es)
# user will feed program this address
dfcl = pd.read_excel('C:\\Programming Software\\Pycharm\\480MajorProjects\\Input Test Files\\cl.xlsx')
dfes = pd.read_excel('C:\\Programming Software\\Pycharm\\480MajorProjects\\Input Test Files\\es.xlsx')

# print to make sure data is good
# print(dfcl)
# print(dfes)

dirtyCLM = dfcl.as_matrix(columns=None)

# in our matrix the important data can be found in the columns as follows
# Course Number      - Column 0
# Course Title       - Column 1
# Course Number      - Column 5
# Class Meeting Time - Column 9
# Class Meeting Days - Column 13
# Building Code      - Column 14
# Room Number        - Column 15
# every row is new class

# munge
w, h = len(dfcl.columns), len(dfcl.index);
CourseListMatrix = [[0 for x in range(w)] for y in range(h)]

# starting with header row because we know that data
CourseListMatrix[0] = [['Course Number'], ['Course Title'], ['Section Number'], ['Class Meeting Time'], ['Class Meeting Days'], ['Building Code'], ['Room Number']]

# now have to iterate through the dirty matrix on proper columns to fill CourseListMatrix
for x in range(len(dfcl.index)):
    CourseListMatrix[x][0] = dirtyCLM[x][0]  # Course Number
    CourseListMatrix[x][1] = dirtyCLM[x][1]  # Course title
    CourseListMatrix[x][2] = dirtyCLM[x][5]  # Course Number
    CourseListMatrix[x][3] = dirtyCLM[x][9]  # Class Meeting Time
    CourseListMatrix[x][4] = dirtyCLM[x][13]  # Class Meeting Days
    CourseListMatrix[x][5] = dirtyCLM[x][14]  # Building Code
    CourseListMatrix[x][6] = dirtyCLM[x][15]  # Room number
    print(CourseListMatrix[x][0], CourseListMatrix[x][1], CourseListMatrix[x][2], CourseListMatrix[x][3], CourseListMatrix[x][4], CourseListMatrix[x][5], CourseListMatrix[x][6])
print()
print()
print()
# now for ExamSchedule(es)
dirtyESM = dfes.as_matrix(columns=None)
w, h = len(dfes.columns), len(dfes.index);

ExamScheduleMatrix = [[0 for x in range(w)] for y in range(h)]
ExamScheduleMatrix[0] = [['Course Meeting Time'], ['Course Meeting Days'], ['Exam Date'], ['Exam Begin Time'], ['Exam End Time']]
# not sure why the column titles are overwritten on es iterations but not cl iterations ¯\_(ツ)_/¯
# for now just hard coding a print of the first row before it gets overwritten by for loop
# print(CourseListMatrix[0])
for x in range(len(dfes.index)):
    # also need to get which exam times correspond to course meeting days
    ExamScheduleMatrix[x][0] = dirtyESM[x][0]  # Course meeting days
    ExamScheduleMatrix[x][1] = dirtyESM[x][1]  # Course meeting times
    ExamScheduleMatrix[x][2] = dirtyESM[x][2]  # Exam date
    ExamScheduleMatrix[x][3] = dirtyESM[x][3]  # Exam start time
    ExamScheduleMatrix[x][4] = dirtyESM[x][4]  # Exam end date
    print(ExamScheduleMatrix[x])

