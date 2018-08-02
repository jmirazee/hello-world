
import urllib
def read_text():
    text = open(r"C:\Users\mgmirazee\Documents\MATEEN\text\Williamson thank you letter, Justin Mirazee.txt")
    contents_of_file=text.read()
    print(contents_of_file)
    text.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("You have a curse word")
    elif "false" in output:
        print("No curse words")

read_text()

         
