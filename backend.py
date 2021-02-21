'''
1. using the backend, once an image of an unfurnished room is received, I have written a function to compare it to pictures of furnished rooms, and pick which one it is the most simliar to

2. once that is done, using the vision API the furniture in the picture can be determined

3. and then specific products of that type of furniture can be recommended from amazon using the get_product function


2. is incomplete currently and this backend still needs to be linked to the frontend
'''
import numpy as np 
import cv2
import os
from requests_html import HTMLSession

def mse(imageA, imageB):
    '''return the mean squared error of 2 images, the lower the error the more similar they are'''
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def most_similar_image(img, type):
    '''
    returns the most similar image to the inputted img which is the room of type type
    img is a file location for the actual image
    '''
    input_img = cv2.imread(img) #might need to do this each time, inside the loop
    input_img = cv2.resize(input_img, (500, 500))
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    similarities = {}
    if type == "bedroom":
        for image in os.listdir('bedroom'):
            location = 'bedroom/' + image
            comparing_img = cv2.imread(location)
            comparing_img = cv2.resize(comparing_img, (500, 500))
            comparing_img = cv2.cvtColor(comparing_img, cv2.COLOR_BGR2GRAY)
            similarities[location] = mse(input_img, comparing_img)
        return min(similarities, key=similarities.get)
    if type == "dining room":
        for image in os.listdir('dining_room'):
            location = 'dining_room/' + image
            comparing_img = cv2.imread(location)
            comparing_img = cv2.resize(comparing_img, (500, 500))
            comparing_img = cv2.cvtColor(comparing_img, cv2.COLOR_BGR2GRAY)
            similarities[location] = mse(input_img, comparing_img)
        return min(similarities, key=similarities.get)
    if type == "living room":
        for image in os.listdir('living_room'):
            location = 'living_room/' + image
            comparing_img = cv2.imread(location)
            comparing_img = cv2.resize(comparing_img, (500, 500))
            comparing_img = cv2.cvtColor(comparing_img, cv2.COLOR_BGR2GRAY)
            similarities[location] = mse(input_img, comparing_img)
        return min(similarities, key=similarities.get)
#print (most_similar_image('diningroomtest.jpg', 'dining room'))   #it works quite well!

def get_product(query):
    '''returns the link for the best product for a certain query from amazon'''
    query = query.split()
    string = ""
    for i in range(len(query)):
        string += query[i]
        if i < len(query) - 1:
            string += "+"
    link = "https://www.amazon.com/s?k=" + string + "&ref=nb_sb_noss_2"
    s = HTMLSession()
    r = s.get(link)
    r.html.render()
    links = r.html.links
    for j in links:
        if j[:2] != '/s' and j[:2] != 'ht' and "UTF" not in j:
            if "#customerReviews" in j:
                return "https://amazon.com" + j[:len(j)-16]
            if "?dchild" in j:
                return "https://amazon.com" + j[:j.find("?dchild")]
            return "https://amazon.com" + j
