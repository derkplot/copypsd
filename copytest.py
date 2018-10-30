import shutil
import os
import openpyxl

# define source and destination folders for converted files and excel file with names of specific files #
source = '/Volumes/Seagate Bac/AH NEW MACFILES/VIDEOS/PRIMARY/Currently Editing/test'
dest = '/Volumes/Seagate Bac/AH NEW MACFILES/VIDEOS/PRIMARY/JPG'
exFile = '/Users/ryanstout/Desktop/python/parts3.xlsx'

# Open up the right sheet #
wb = openpyxl.load_workbook('parts3.xlsx')
ws = wb['Sheet1']

# File names are in first row, copy them to new dir if found in source dir ###
for row in ws.iter_rows('A1:B1'):
    if row[0].value == "Yes":
        file = source+row[1].value
        fileDst = dest+row[1].value
        shutil.copyfile(file, fileDst)

### to be followed with psdtojpg module to convert all folders in tree ###