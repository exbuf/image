'''
Program name: image.py
Born: August 13, 2018 
Updated: August 26, 2018 16:30 (added prompt to wm() for text color so it stands out against any background color) 

Author: Robert D. Schoening, https://www.robertdschoening.com
Code and documentation: https://github.com/exbuf/Shrink
'''

# Functions-----------------------------------------------------------------------------------------
def printErrMsg(error):  # Display input error messages and Help screen 
    print(" ")
    print("       * * * * * * * * * * * * ERROR: "+error+ " * * * * * * * * * * * * * * * ")
    print(" ")
    print("       1.                                 TO SHRINK IMAGES:")    
    print("       =============================================================================================")
    print("       EXAMPLE.......  python  image.py    600     400      s_")
    print("                                        arg[1]  arg[2]  arg[3]")
    print("       where... ")
    print("       - arg[1] is the maximum desired horizontal size in pixels, in this example 600.")
    print("       - arg[2] is the maximum desired vertical size in pixels, in this example 400.")
    print("       - arg[3] is the text you want prepended to your shunken filename, in this example s_")
    print("         Do not use these illegal Windows filename characters in arg[3]: \ / : * ? < > | ")
    print(" ")
    print(" ")
    print("       2.                       TO CONVERT IMAGES TO BLACK AND WHITE (bw):")
    print("       ============================================================================================")
    print("       EXAMPLE.......> python  image.py    bw   ( ... Converted files will be prepended with 'bw_')")
    print(" ")
    print(" ")
    print("       3.                  TO ADD WATERMARK (wm) TEXT IN UPPER LEFT HAND CORNER:")
    print("       ============================================================================================")
    print("       EXAMPLE.......> python  image.py    wm   ( ... then enter your text when prompted. ")
    print("                                                      Converted files will be prepended with 'wm_')")
    print(" ")
    print(" ") 
    print("       Please read the program documentation: https://github.com/exbuf/Shrink/blob/master/README.md")
    print(" ")
    print("       To get this Help screen anytime, type:  'python  image.py  help'     OR     'python  image.py'")
    print(" ")

def black_white(fileList):
    count = 0
    notCount = 0
    print("")
    # process all files
    for fileName in fileList:
        start_time = time.time()
        try:
            im = Image.open(fileName) 
            print(fileName, im.format, im.size, im.mode)
            im = im.convert('1')  
            outFile = 'bw_'+fileName
            im.save(outFile)  
            print(outFile, im.format, im.size, im.mode)
            count=count+1
            print("--- %s seconds ---" % round((time.time() - start_time),3))
            print("")
        except IOError:
            notCount=notCount+1
        
    # summarize results of processing          
    print(str(count)+" files processed and "+str(notCount)+" files ignored.")

    if(count==0):
        print("0 files processed can be caused by illegal characters  \ / : * ? < > |  in the prefix argument.")

    print("To get the Help screen, type this-----------> python    image.py    help")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    #print("--- %s seconds ---" % (time.time() - start_time))

def shrink(fileList, prefix, size):
    count = 0
    notCount = 0
    print("")
    # process all files
    for fileName in fileList:
        try:
            # start timer
            start_time = time.time()
            im = Image.open(fileName) 
            print(fileName, im.format, im.size, im.mode)
            im.thumbnail(size)   # thumbnail function maintains aspect ratio
            outFile = prefix+fileName
            im.save(outFile)  # save shrunken file
            print(outFile, im.format, im.size, im.mode)
            count=count+1
            print("--- %s seconds ---" % round((time.time() - start_time),3))
            print("")

        except IOError:
            notCount=notCount+1

    # summarize results of processing          
    print(str(count)+" files processed and "+str(notCount)+" files ignored.")

    if(count==0):
        print("")
        print("0 files processed can be caused by illegal characters  \ / : * ? < > |  in the prefix argument.")
    
    print("To get the Help screen, type this-----------> python    image.py    help")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

def checkInputs():
    
    if ( len(sys.argv) != 4):
        printErrMsg("Wrong number of arguments ("+str(len(sys.argv)-1)+")")
        exit()

    try:
        value = int(sys.argv[1])
    except ValueError:
        printErrMsg("arg[1] is not an integer")
        exit()

    try:
        value = int(sys.argv[2])
    except ValueError:
        printErrMsg("arg[2] is not an integer")
        exit()

    if(int(sys.argv[1]) < 1 or int(sys.argv[2]) < 1):
        printErrMsg("arg[1] and arg[2] must be integers 1 or greater")
        exit()

# This works for .jpg and .png but not on black and white. So disallow images beginning with 'wm_'. 
def wm(fileList):
    
    pos=(10, 0)
    
    wm_text = input("Enter your watermark text: ")
    print("You entered: "+wm_text)
    
    wm_font = input("Enter the font size: ")
    print("You entered: "+wm_font)
    
    wm_color = input("Enter the font color: ")        
    print("You entered: "+wm_color)

    count = 0
    notCount = 0
    prefix = "wm_"
    print(" ")

    for fileName in fileList: 
        start_time = time.time()
        if('bw_' in fileName):
            print("Skipping "+fileName+" because 'wm' does\'t work on B/W images yet. Run 'wm' on color image first, then run 'bw'.")
            continue
        
        ext = os.path.splitext(fileName)[-1].lower()
        if(ext == '.JPG' or ext == '.jpg' or ext == '.PNG' or ext == '.png'):
            print(fileName)
            photo = Image.open(fileName)
 
            # make image editable
            drawing = ImageDraw.Draw(photo)
            black = (3, 8, 12)
            font = ImageFont.truetype("arial.ttf", int(wm_font)) 
            drawing.text(pos, wm_text, fill=wm_color, font=font)
            outFile = 'wm_'+fileName
#           photo.show()
            photo.save(outFile)
            count=count+1
            print(outFile, photo.format, photo.size, photo.mode)
            print("--- %s seconds ---" % round((time.time() - start_time),3))
            print(" ")
        else:
            notCount=notCount+1
            
    # summarize results of processing          
    print(str(count)+" files processed and "+str(notCount)+" files ignored.")

    if(count==0):
         print("0 files processed can be caused by illegal characters  \ / : * ? < > |  in the prefix argument.")

    print("To get the Help screen, type this-----------> python    image.py    help")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    exit()
    

    
# End Functions--------------------------------------------------------------------------------

# Main program---------------------------------------------------------------------------------
# imports
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os, sys, time
from sys import exit  # fixes bug in pyinstaller (for making standalone executable)

# start timer
#start_time = time.time()

# fileList is common to all functions()
fileList = os.listdir(os.getcwd())

# check for zero arguments (empty arguments causes checkIntegers() to get 'out of range' error)
if(len(sys.argv) == 1):
     printErrMsg("Wrong number of arguments (0).")
     exit()

# check for one argument--'help', so show help screen
if(str(sys.argv[1]) == 'HELP' or str(sys.argv[1]) == 'help'):
   printErrMsg("None. This is the Help screen.")
   exit()

# check for one argument--'bw', so call black_white() function
if(str(sys.argv[1]) == "bw" or str(sys.argv[1]) == "BW"):
    black_white(fileList)
    exit()

# check for one argument--'wm', so call wm() function
if(str(sys.argv[1]) == "wm" or str(sys.argv[1]) == "WM"):
    wm(fileList)
    exit()

# neither of the two legal one-argument inputs were found, so default to the shrink() function which requires 3 arguments
# first check for argument input errors:
checkInputs()

# no argument input errors found, so prepare the shrink() function arguments
size_x = int(sys.argv[1])
size_y = int(sys.argv[2])
prefix = str(sys.argv[3])
size = (size_x, size_y)

# call the shrink() function
shrink(fileList, prefix, size)

# exit program
#print("--- %s seconds ---" % round((time.time() - start_time),3))
exit()
