#!/usr/bin/python
import requests
def print_urls(file):
    #Each line is of the form: GET /foo/bar/a.jpg
    #remove the GET and print only /foo/bar/a.jpg

    #use a for-loop to iterate through each line of `file'
    #split the line and print second part

    for line in f:
        print line.split()[1]


f = open('1.txt')
print_urls(f)

 

def eliminate_duplicates_and_sort(file):
    #remove duplicate lines from `file'
    r = sorted(set(file))
    for line in r:
        print line,

if __name__ == '__main__':
    eliminate_duplicates_and_sort(open('2.txt'))
    

def save_image(url, filename):
    print url
    r = requests.get(url)
    f = open(filename, 'w')
    f.write(r.content)
    f.close()


def main():

    filename = 1
    url_base = 'http://code.google.com'

    #open file 3.txt

    #using a for loop, save each url to a file
    #you can use the save_image function for doing 
    #this.
    #The files to which you are saving the urls should
    #be called 0.jpg, 1.jpg, 2.jpg etc.
    
    for url in open('3.txt'):
        save_image(url_base + url.strip(), "images/" + str(filename) + ".jpg")
        print 'saved file %d' % filename
        filename += 1

main()


print """<html>
         <head><title>Images</title></head>
         <body>
      """

for i in range(0,21):
    print '<img src="%s">' % (str(i) + ".jpg")


print """</body></html>"""
