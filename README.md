"# image" 

Program name: <b>image.py</b>

Born: August 13, 2018 

Updated: July 22, 2020

Author: Robert D. Schoening


OVERVIEW
--------
1. <b>Image.py</b> ("the program") has three features. All operate independently. (Detailed description below): 
  - <b>ADD TEXT WATERMARKS TO IMAGES</b>: 
adds a text watermark to all images in a directory (see Figures 1 and 2). 
  - <b>CONVERT COLOR IMAGES TO BLACK-AND-WHITE</b>: creates black-and-white copies of all images in a directory (see Figure 3). 
  - <b>SHRINK IMAGES</b>: shrinks all images in a directory (see Figure 4). (Creating smaller image files for attaching to emails was the inspiration for image.py.) 
2. The program prints on the screen the name of the original file, the name of the newly created file, and the time it took to create that file. Any non-image files that reside in the directory are ignored. Your original<sup>1</sup> images are unaltered. See the screen captures below.
3. A copy of image.py (the program) must reside in the same directory as your image files. (K.I.S.S.)
4. You can have different directories for different sets of images, but each directory must have a copy of image.py. To process images one-at-a-time, just put one image in the directory at a time.   
5. Image files in the directory can be numerous and of mixed format (.jpg, .png, .ppm, .gif, .tiff, etc.). The link to the Pillow library documentation below provides the entire list of supported formats. (Only .jpg and .png formats have been tested with this program so far.)
6. When shrinking, all images in the directory are shrunk by the same amount via command line arguments that you enter.  
7. Aspect ratios are preserved with all three features, even if the argument ratios you provide in the shrinking feature don't match the original's aspect ratio. For example, you can't crop or compress a rectangular image into a square image.
8. The program has a Help screen.<sup>2</sup>.
9. image.py is written in Python and uses the Pillow image processing library (see REQUIRED below).
10. image.py runs in a Windows 10 terminal (the black Command Prompt window). 
11. image.py was tested on Windows 10 and Python 3.6.3, and with .jpg and .png files. (It should also run on Linux.)

REQUIRED
--------
1. Windows 10
2. Python programming language: https://www.python.org/
3. Pillow library (a PIL fork): https://pillow.readthedocs.io/en/5.2.x/index.html

PROCEDURE:  
---------
1. Install Python 3.6.3 or higher on your Windows 10 machine. 
2. Install the Pillow library by using pip, a package manager written in Python. Pip should come with Python 3.6.3.
3. Create a new directory to contain the image files you want to process. 
4. Copy your image files into that directory.
5. Copy image.py into that directory. (NOTE: image.py only processes image files in the same directory.)  
6. Open a terminal window (Command Prompt) and navigate to your directory. Then enter one of the following commands.

FEATURE 1: ADD TEXT WATERMARKS TO IMAGES
--------------------------------------
In your Command Prompt window, first enter this command:  <pre>python  image.py  wm</pre> 

Then when prompted, enter the watermark text that you want to appear in the upper left corner, followed by your desired font size and color when prompted again. 

<p align="center">
  <img src="https://www.robertdschoening.com/images/shrink_wm_color.JPG" width="800" title="watermark">  
</p>
<p align="center"><b>Figure 1: The Watermark Feature</b></p>
For a 6000 x 4000 image, try a font size of 50 for starters. You'll have to experiment to see what size font looks good. As you can see from Figure 2, a font size of 50 on a 6000 x 4000 image is pretty inconspicuous, but much larger sizes are possible. This particular image went from 7.65MB before adding the watermark to 2.07MB afterwards, even though I didn't use the shrink feature! Why? Because it's a .jpg image.<sup>3</sup> 
<p></p>
<p align="center">
  <img src="https://www.robertdschoening.com/images/wm_DSC01668.JPG" width="800" title="watermark"> 
</p>
<p align="center"><b>Figure 2: Homemade Drone</b></p>
<p align="center"><em>Text watermark in upper left corner. Original image = 6000 x 4000 (24MB), font size = 50.</em></p>

Your new watermarketed images will be named <em>'wm_'+original_file_name</em>. The program does support watermarking on both color and black-and-white images that were taken with a camera, but it does not support watermarking on images that were converted to black-and-white using this program! Therefore, any files starting with 'bw_' are skipped when watermarking and a message to that effect is printed on your screen. A workaround is to watermark the color versions first, then convert them to black-and-white with the 'python image.py bw' command; the watermark will appear in the black-and-white images. Example uses of watermarks include displaying your name, your company name, your website, or descriptive information about the image. Watermarks also discourage unauthorized use of your images. 

FEATURE 2: CONVERT COLOR IMAGES TO BLACK-AND-WHITE
------------------------------------------------
In your Command Prompt window, enter this command. <pre>python  image.py  bw</pre>

<p align="center">
  <img src="https://www.robertdschoening.com/images/shrink_b_w.JPG" width="800" title="black-and-white">
 </p>
<p align="center"><b>Figure 3: Black-and-White Feature</b></p>
Your new black-and-white image files will be named <em>'bw_'+original_file_name</em>. 
Converting to black-and-white produces larger files, but you can shrink them later if needed. 

FEATURE 3: SHRINK IMAGES
----------------------
In your terminal window, enter your command in this format: <pre>python  image.py  x_dim  y_dim  prefix</pre>

THE SHRINK ARGUMENTS:
---------------------
<b>x_dim</b> is the maximum desired width of the resulting image in pixels

<b>y_dim</b> is the maximum desired height of the resulting image in pixels

<b>prefix</b> is the (required) text to be prepended to the original filename to create the filename of your shrunken image.  

A SHRINK EXAMPLE
----------------
Suppose you have a 6000 x 4000 (24MB) image file named DSC00609.JPG and you want to shrink it down to 600 x 400 for emailing purposes.
You want your new file to have additional text prepended<sup>4</sup> to their original file name. To accomplish this task, navigate in your terminal window to the image directory, then type this command in the Command Prompt window:

<pre>python  image.py  600  400  s_</pre>

<p align="center">
  <img src="https://www.robertdschoening.com/images/shrink_shrink.JPG" width="800" title="shrink">
</p>
<p align="center"><b>Figure 4: The Shrink Feature</b></p>
After running image.py, a new file named s_DSC00609.JPG is added to your directory. It is the shrunken version of your original image (DSC00609.JPG), which remains unchanged. (Groups of files as depicted will be named <em>'prefix'+original_file_name</em>.)

NOTES
-----
<sup>1</sup> The program considers "original" images to be the set of all images in the directory at the start of each program execution. That means any new files that you just created, if not relocated into a different directory, will themselves become "originals" the next time you run the program. Files reprocessed this way will start having duplicate prepended text, such as 'bw_bw_', 'bw_bw_bw', 'bw_bw_bw_bw', and your set of "originals" will grow and grow. So unless you want to do multiple things to your files, relocate newly created files into different directories after each program execution. 

One exception is with watermarking. As mentioned above, you can't watermark black-and-white images that were converted from color via this program (filenames beginning with 'bw_'), but you can achieve the same result by first watermarking their color versions with the command 'python image.py wm', then converting them to black-and-white with the command 'python image.py bw'. In that case, you will process the same files twice, and they will be labeled thusly: <em>bw_wm_XXXXX.JPG</em>. You might also want to shrink them, which creates yet another prefix. 

<sup>2</sup> Help Screen

<p align="center">
  <img src="https://www.robertdschoening.com/images/shrink_help.JPG" width="800" title="shrink">
 </p>
<p align="center"><b>Figure 5: The Help Screen</b></p>
<sup>3</sup> JPEG is a compression standard. Therefore, each time you process a '.jpg' image, it will get smaller, even without deliberately shrinking it. Exception: converting a color image to a black-and-white image (in this program) makes the file bigger!
<p></p>
<sup>4</sup> In our context, the word <em>prepend</em> means to attach extra text to the front of a filename. Prepending the original file name distinguishes your new files from the originals so they are not overwritten. Prepending also has the advantage of grouping your newly created images together in Windows File Explorer, which <em>appending</em> (attaching to the back of a filename) does not do.

