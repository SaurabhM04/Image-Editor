import os
from PIL import Image,ImageDraw,ImageFont
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, GaussianBlur, SMOOTH, SMOOTH_MORE, SHARPEN)

def main():
    ask_file_name()

def ask_file_name():
    file_name= input("\n \nPlease enter your image full path/location : ")
    original_image=Image.open(file_name)
    continuos_ask(original_image,"start")

def continuos_ask(o_image,i):
    continue_ask="continue"
    if i != "start":
        continue_ask= input('\nEnter " continue " to do operations on image or press "exit" to save the image and exit : \n')
    if continue_ask == "continue":
        pass_choice(o_image)
    if continue_ask=="exit":
        save_or_exit=input("Do you want to save your image before exitting .Enter 'yes' or 'no' : ")
        if save_or_exit=="yes":
            save_image(o_image)
        else:
            print("\nHOPE YOU ENJOYED .THANK YOU :)")

def pass_choice(image):
    choice=ask_choice()
    if choice=="rotate": 
        rotate_image(image)
    if choice=="text": 
        add_text(image)
    elif choice == "filter":
        filter(image)
    elif choice=="flip_image":
        flip_image(image)
    elif choice =="blur":
        blur(image)
    elif choice =="mirror":
        mirror_image(image)
    elif choice=="colour_modes":
        colour_mode(image)
    elif choice=="crop":
        crop_image(image)
    elif choice=="resize":
        resize_image(image)
    elif choice =="thumbnail":
        image_thumbnail(image)
    elif choice=="grayscale":
        to_grayscale(image)
    elif choice=="bw":
        to_blackWhite(image)

def ask_choice():
    print("*****************Image Operations**********************\n")
    operations=['text','rotate','blur','colour_modes','mirror','filter','crop','thumbnail','resize','grayscale','black & white']
    [print(x) for x in operations]
    choice = input("\nEnter the name of the operation which you want to make on your image : ")
    return choice

def rotate_image(im):
    rotate=float(input("enter no. of degrees to rotate the image clockwise : "))
    im=im.rotate(rotate)
    show_image(im)
    continuos_ask(im,"not_start") 

def crop_image(im_crop):
    size= im_crop.size
    want_show = input("Enter 'yes' if you want to see the original image before cropping : ")
    if want_show=="yes":
        show_image(im_crop)
    print("The width and height of the image are",size[0],size[1],"respectively.\n")
    l,t,r,b =map(int,input("Enter the left, top, right, bottom line of rectangle to crop your image").split(","))
    im=im_crop.crop((l,t,r,b))
    show_image(im)
    satisfied= input("Enter 'continue' to move with this cropped image or enter 'crop' to crop again")
    while satisfied != "continue":
        l,t,r,b =map(int,input("Enter the left, top, right, bottom coordinates line of rectangle to crop your image"))
        im=im_crop.crop((l,t,r,b))
        show_image(im)
        satisfied= input("Enter 'continue' to move with this cropped image or enter 'crop' to crop again")
    continuos_ask(im,"not_start")

def resize_image(image_resize):
    size= image_resize.size
    want_show = input("Enter 'yes' if you want to see the original image before resizing : ")
    if want_show=="yes":
        show_image(image_resize)

    print("The width and height of the image are",size[0],size[1],"respectively.\n")
    print("Enter the no. of times with respect original width or height to make the image of desired size.")
    print("Note that entering 2,2 will make the new image of double width and height of original image")
    new_width,new_height=map(float,input("Enter the times width and height separated by ','").split(','))

    im=image_resize.resize((round(new_width*size[0]),round(new_height*size[1])))
    show_image(im)
    satisfied= input("Enter 'continue' to move with this new image or enter 'resize' to resize again")
    while satisfied != "continue":
        new_width,new_height=map(float,input("Enter the times width and height separated by ','").split(','))
        im=image_resize.resize((round(size[0]*new_width),round(size[1]*new_height)))
        show_image(im)
        satisfied= input("Enter 'continue' to move with this new image or enter 'resize' to resize again")
    continuos_ask(im,"not_start")

def image_thumbnail(image):
    print("It is always advised to first edit the image and at last create the thumbnail of it\n")
    ask_caution=input("Do you still want to proceed. 'yes' or 'no'")
    if ask_caution == "yes":
        th_width,th_height=map(int,input("Enter the required size of the thumbnail you want in width,height format separated by ','").split(","))
        image.thumbnail((th_width,th_height))
        im=image
        show_image(im)
        continuos_ask(im,"not_start")
    else:
        print("Fine! proceed with your editing\n")
        im=image
        continuos_ask(im,"not_start")
    
def filter(im):
    filters=["blur","enhance","smooth","contour","detail","find_edge","sharpen"]
    print("list of filter available are")
    [print(x) for x in filters]
    filter_type=input("Enter the type of filter to apply to your image from the list: ")
    apply_filter(filter_type,im)

def apply_filter(filter_style,im):
    if filter_style=="enhance":
        enhance_image(im)
    if filter_style=="smooth":
        smooth_image(im)
    if filter_style=="contour":
        contour_image(im)
    if filter_style=="detail":
        detail_image(im)
    if filter_style=="find_edge":
        find_edge_image(im)
    if filter_style=="sharpen":
        sharp_image(im)

def blur(im):
    print("Enter normal_blur and custom_blur")
    blur_type=input("Enter the type of blur : ")
    if blur_type == "normal_blur":
        im=im.filter(BLUR)
        show_image(im)
        continuos_ask(im,"not_start") 
    elif blur_type == "custom_blur":
        blur_amount=int(input("Enter the amount of blur -\n 5-little blur\n10-medium blur\n15-intense blur"))
        im=im.filter(GaussianBlur(radius=blur_amount))
        show_image(im)
        continuos_ask(im,"not_start") 

def mirror_image(im):
    mirror=Image.new('RGB',(im.width,im.height),'white')
    #accessing the pixel of image
    for x in range(im.width):
        for y in range(im.height):
            pixel = im.getpixel((x,y))
            mirror.putpixel((im.width-(1+x),y),(pixel[0],pixel[1],pixel[2]))
    combine_mirror(im,mirror)

def combine_mirror(image1,image2):
    im=Image.new('RGB',(2*image1.width,image1.height),'white')
    im.paste(image1,(0,0))
    im.paste(image2,(image1.width,0))
    show_image(im)
    continuos_ask(im,"not_start")

def enhance_image(im):
    enhance_type=input("Enter'normal' for normal enhance and 'intense' for intense enhance")
    if enhance_type=="normal":
        im=im.filter(EDGE_ENHANCE)
        show_image(im)
        continuos_ask(im,"start") 
    elif enhance_type=="intense":
        im=im.filter(EDGE_ENHANCE_MORE)
        show_image(im)
        continuos_ask(im,"not_start") 

def smooth_image(im):
    smooth_type=input("Enter'normal' for normal smooth and 'intense' for intense smooth")
    if smooth_type=="normal":
        im=im.filter(SMOOTH)
        show_image(im)
        continuos_ask(im,"start") 
    elif smooth_type=="intense":
        im=im.filter(SMOOTH_MORE)
        continuos_ask(im,"not_start") 

def sharp_image(im):
    im=im.filter(SHARPEN)
    show_image(im)
    continuos_ask(im,"start") 

def find_edge_image(im):
    im=im.filter(FIND_EDGES)
    show_image(im)
    continuos_ask(im,"not_start") 

def contour_image(im):
    im=im.filter(CONTOUR)
    continuos_ask(im,"not_start") 

def embossy_image(im):
    im=im.filter(EMBOSS)
    show_image(im)
    continuos_ask(im,"not_start") 

def detail_image(im):
    im=im.filter(DETAIL)
    show_image(im)
    continuos_ask(im,"not_start") 

def flip_image(im):
    flip_value=input("enter 'h' for horizontally flipping and 'v' for vertically flipping : ")
    if flip_value=="h":
        im=im.FLIP_LEFT_RIGHT
        show_image(im)
        continuos_ask(im,"not_start") 
    elif flip_value=="v":
        im=im.FLIP_TOP_BOTTOM
        show_image(im)
        continuos_ask(im,"not_start") 

def colour_mode(im):
    print("colour modes available are :\n1- *built_in_colours*\n2-*special_mix*\n3-*custom*")
    colour_option= int(input("Enter the given no. of your choice as 1 or 2 or 3"))
    if colour_option==1:
        colours =['red','blue','green']
        print(colours,"\n")
        your_colour= input("Enter colour from the above list : ")
        pixel_change(im,your_colour)
    elif colour_option==2:
        colours=["black_white"]
        for i in range(1,12):
            colours.append("special_"+str(i))
        [print(x,end=" ") for x in colours]
        your_colour=input("Enter colour from the above list : ")
        special_colour(im,your_colour)
    elif colour_option==3:
        r,g,b=map(float,input("Enter the value of red,green,blue component separated by ','.\nEntering 1.5 for red means 1.5*original_red_value.").split(","))
        custom(im,r,g,b)

def custom(im,red,blue,green):
    for x in range(im.width):
        for y in range(im.height):
            pixel=im.getpixel((x,y))
            im.putpixel((x,y),(round(pixel[0]*red),round(pixel[1]*green),round(pixel[2]*blue)))        
    im.show()
    continuos_ask(im,"not_start")

def pixel_change(im,colour):
    for x in range(im.width):
        for y in range(im.height):
            pixel=im.getpixel((x,y))
            if colour =="red":
                im.putpixel((x,y),(pixel[0],0,0))
            elif colour =="green":
                im.putpixel((x,y),(0,pixel[1],0))
            elif colour =="blue":
                im.putpixel((x,y),(0,0,pixel[2]))
    im.show()
    continuos_ask(im,"not_start")
    
#  0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue

def to_grayscale(im):
    for x in range(im.width):
        for y in range(im.height):
            pixel=im.getpixel((x,y))
            gray=round(pixel[0]*0.299)+round(pixel[1]*0.587)+round(pixel[2]*0.114)
            im.putpixel((x,y),(gray,gray,gray))            
    im.show()
    continuos_ask(im,"not_start")

def to_blackWhite(im):
    for x in range(im.width):
        for y in range(im.height):
            pixel=im.getpixel((x,y))
            gray=round(pixel[0]*0.299)+round(pixel[1]*0.587)+round(pixel[2]*0.114)
            if gray>=127:
                im.putpixel((x,y),(255,255,255))  
            else:
                im.putpixel((x,y),(0,0,0))  
    im.show()
    continuos_ask(im,"not_start")

def special_colour(im,colour):         
    r,g,b=im.split()
    if colour=="black_white":
        im=Image.merge(("RGB"),(r,r,r))
        continuos_ask(im,"not_start")
    elif colour=="special_1":
        im=Image.merge(("RGB"),(r,b,g))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_2":
        im=Image.merge(("RGB"),(b,r,g))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_3":
        im=Image.merge(("RGB"),(r,g,r))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_4":
        im=Image.merge(("RGB"),(g,r,b))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_5":
        im=Image.merge(("RGB"),(g,b,r))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_6":
        im=Image.merge(("RGB"),(r,g,r))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_7":
        im=Image.merge(("RGB"),(b,g,b))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_8":
        im=Image.merge(("RGB"),(g,r,g))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_9":
        im=Image.merge(("RGB"),(b,r,b))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_10":
        im=Image.merge(("RGB"),(r,b,r))
        show_image(im)
        continuos_ask(im,"not_start")
    elif colour=="special_11":
        im=Image.merge(("RGB"),(g,b,g))
        show_image(im)
        continuos_ask(im,"not_start")

def add_text(text_image):
    show_image(text_image)
    size_image=text_image.size
    print("The width and height of the image are",size_image[0],size_image[1],"respectively.\n")
    draw=ImageDraw.Draw(text_image)
    x,y=map(int,input("Enter x,y coordinates of point on the image for text to appear separated by ',': ").split(","))
    os.startfile('Font_Family.pdf')
    font = input("Enter font file name with first letter of every word in capital (Times New Roman) ")
    size= int(input("Enter the font size : "))
    my_font=ImageFont.truetype("C:/Windows/Fonts/"+font+".ttf", size)
    text=input("Enter the text to be showb on your image\n")
    r,g,b=map(int,input("Enter the font colour in r,g,b format separated by ','").split(","))
    draw.text((x,y), text, font=my_font, fill=(r,g,b))
    show_image(text_image)
    satisfied= input("Enter 'continue' to move with this new image or enter 'change' only to change the position and font of the text")
    while satisfied != "continue":
        x,y=map(int,input("Enter x,y coordinates of point on the image for text to appear separated by ',': ").split(","))
        font = input("Enter font name with first letter of every word in capital (Times New Roman) ")
        size= int(input("Enter the font size : "))
        my_font=ImageFont.truetype("C:/Windows/Fonts/"+font+".ttf", size)
        draw.text((x,y), text, font=my_font, fill=(r,g,b))
        show_image(text_image)
        satisfied= input("Enter 'continue' to move with this new image or enter 'change' to edit  again")
    im=text_image
    continuos_ask(im,"not_start")
    
def show_image(image):
    image.show()


def save_image(new):
    location=input("Please enter the location to save your image")
    new.save(location,"JPEG")


if __name__ == "__main__":
    main()
