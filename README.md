# IAP1 Homework: Web-based steganography tool

Name: Alin-Ioan Alexandru

Group: 312CA

Series: CA

Some of the information in this file can also be found in the about section on the web-site :)

## 1. The steganography:
 * The steganography implementation is very simple:
    * The encoding is done by extracting the pixels from the image with the help of the PIL library. The input text is turned into an array of ints based on the ascii code. For each value in a pixel the last bit is set to zero. At the same time we go through the bits of a letter and after setting the pixel to zero we set it to the bit in the letter. The First bit of the letter is represented in the first value of the first pixel. At the end if the image is not fully encoded we add 8 zeros (aka the null string terminator).
    * The decoding is done in a similar fashion. After extracting the pixels from the image we make a list with the last bit from each value in the pixel, then, while counting the bits so we don't have more than 8, we shift each one to the left with its coresponding position and add them together to get the value for the letter. The decoding is done until we reach a null string terminator or the end of the image.
 * There is also a command line version of the script that can be run like this, where the \<command\> is "encode" that requires both argumnets or "decode" that requires only the filename argument

```console
foo@bar:~$ python3 steganography.py <command> --filename --text
```
## 2. The website:
 * The website has 4 pages which all have some common elements:
   * The menu bar, which was done with the help of bootsrap. In the top left you can also see our cute mascot, The Fat Racoon.
   * The right-side box which has links to the last image and text saved.
   * The copyright handle at the bottom of the page.
 * The main content box is done by using a wrapper that contains both the main content box and the right-side box.
 * The html files use jinja templating and so there are very few lines of "code" in each file.

## 3. Docker:
 * The Dockerfile uses alpine as the base image and it requires flask and pillow.
 * The folders are copied using the ADD command.
 * The port that is exposed is 5000

## 4. Other:
 * I had a lot of fun while working on this project and researching and learing about html, css, flask, and even python. This was one of the best homework that I had this semester.
 * PS: I hope you like the racoon. 

