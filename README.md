<html>
<h1> Image Editor </h1>
<br>
<p1>This Python code allows you to edit a image stored locally on your device.</p1>


<h2>Before Running the code</h2>
<br>
<p1> Make sure you have Python installed on your device.<br><br>To check if Python is installed correctly Go to your terminal and type the following command and hit enter</p1>
<pre><b>python</b></pre>
<p1>The output will be the following type-:</p1>
<pre>Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.</pre>
<p1>Otherwise first install Python correctly from its official site</p1>
<br>
<br>
<p1> Now clone the project by directly using github or by using git bash</p1><br><br>
<p1>Open your preferred IDE ( VS Code , PyCharm etc. ) and in the terminal run the following command to install the required python packages. Note that "requirements.txt"  file will be saved to a directory where you have cloned or downloaded this project</p1>
<pre><b>pip install "<i>requirements.txt file path</i></b>" without the double quotes</pre>
<p1>The above step will install the required python libraries</p1><br><br>
<p1>That's it Now you are ready to use this image editor directly from your terminal<p1>

<h2>Using the editor</h2><br>
<p1>Run the image.py file from your IDE</p1><br><br>
<p1>Now in your terminal or output window you will be asked to enter the image path for the image you want to edit, so go for it and press enter key</p1><br>
<pre>Format for a image path -: <b><i>"C:\Users\prath\OneDrive\Pictures\image 10.jpg" </i></b>without the double quotes</pre>
<p1>Note -: It is always advised to enter the full image path with using two backslashes [ " \\ " ] and with proper image extension [" .png , .jpg "]. Otherwise the code will not run properly.</p1>
<p1>After hitting enter you will be offered a drop-down of options there itself in the terminal to edit a image and asked to enter one of them</p1><br><br>
<p1>Type the name of operation you want to perform as it is in the dropdown and hit enter<br></p1>
<h2>Saving and Exiting</h2>
<p1>After one operation is performed on the image you will be asked to "continue editing the image or exit" <br>type your required choice and hit enter</p1>
<br><br>
<p1>If you chose "exit" then you will be asked about "the location you want to save your image" or to "leave without submitting the image".Depending upon your choice if you chose to save your image then you will be asked to enter full path to save the image to a particular location . Be sure you enter the full and correct path.</p1>
  <h2>Operations for a Image</h2>
  <dl>
    <pre><dt><h3>Resize - <b>"resize"</b></h3></dt></pre>
        <dd>For Resize you need to enter the width and height of the image in pixels for the final image.<br> At first you will be shown your original image and the width and height of the original image will be printed on the screen</dd>
    <pre/><dt><h3>Crop - <b>"crop"</b></h3></dt></pre>
        <dd>For crop you need to enter the coordinates for the required portion of the image which you want to keep.This operation is a little hectic in the terminal but it's usually fun to play with it</dd>
  <pre><dt><h3>Thumbnail - <b>"thumbnail"</b></h3></dt></pre>
      <dd>For Thumbnail you need to enter the size of thumbnail you need</dd>
  <p1>Tip-: In the above three operations which involves chanzing the size of the image , At first the original image will be shown to the user and then the user can apply the operation and also the user can go back to his original image rejecting the operation.</p1>
  <pre><dt><h3>Rotate - <b>"rotate"</b></h3></dt></pre>
  <dd>For Rotate user will be asked to enter the the amount of rotation ( in degrees clockwise ) and the image will be rotated by that amount</dd>
  <pre><dt><h3>Flip Image - <b>"flip_image"</b></h3></dt></pre>
  <dd>User will be provided with two set of options (Flip Horizontal and Flip Vertical) and then after typing the name of the flip choices the image will be flipped.
    <pre><ul><li>Flip Horizontally - <b>"horizontal"</b> </li> <li>Flip Vertically - <b>"vertical"</b>  </li></ul></pre></dd>
  <dd>Horizantal flipping will flip the image as left <-> right and Vertical Flipping will flip the image as Top <-> Bottom</dd>
  <pre><dt><h3>Mirror - <b>"mirror"</b></h3></dt></pre>
  <dd>Your Image will be Mirrored or flipped horizontally</dd>
  </dl>
</html>
