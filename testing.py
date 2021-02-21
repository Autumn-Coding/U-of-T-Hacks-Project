from requests_html import HTMLSession
import requests
import os 
from bs4 import BeautifulSoup as bs 
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

def is_valid(url):
    '''checks if url is valid'''
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def get_first_image(url):
    '''returns the url of the first valid image contained in a url'''
    soup = bs(requests.get(url).content, "html.parser")
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            return img_url
def download(url, pathname):
    '''downloads a file given a URL and puts it in the folder 'pathname' '''
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join(pathname, url.split("/")[-1])  #maybe make this a custom filename as well, that can be input into the function too maybe?
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))

link = 'https://www.google.com/search?hl=en&gl=ar&tbm=isch&sxsrf=ALeKk02JaYFUOlH9E4F8nZ9l9pH8J981Ow%3A1613898773493&source=hp&biw=1536&bih=754&ei=FSQyYKjvG5GZlwSezJmYDw&q=bedroom&oq=bedroom&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzoHCCMQ6gIQJ1CoE1jjGmC-H2gBcAB4AIABkAKIAb8NkgEDMi03mAEAoAEBqgELZ3dzLXdpei1pbWewAQQ&sclient=img&ved=0ahUKEwjozeG40fruAhWRzIUKHR5mBvMQ4dUDCAc&uact=5'
#generalize this link when putting it in a function, and make sure to accoutn for multiple words, like living room and not just single ones like bedroom
s = HTMLSession()
r = s.get(link)
r.html.render()
links = r.html.links
print (links)
for i in links:
    if i[:4] == "http":
        print (i)
        image_url = get_first_image(i)
        print (image_url)
        download(image_url, 'test_images')


#functionize this too if it works
'''
given an image of the room and the type of the room, 
the code should compare the given image with other images from google search (maybe like the top 10 iamges)
and choose which one is the most similar
and detect the furniture in that
and recommend that
might need to use getty images or sth if google doesn't work
'''