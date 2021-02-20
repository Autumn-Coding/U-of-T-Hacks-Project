from requests_html import HTMLSession
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
    #links = r.html.absolute_links
    links = r.html.links
    for j in links:
        if j[:2] != '/s' and j[:2] != 'ht' and "UTF" not in j:
            if "#customerReviews" in j:
                return "https://amazon.com/" + j[:len(j)-16]
            if "?dchild" in j:
                return "https://amazon.com/" + j[:j.find("?dchild")]
            return "https://amazon.com/" + j
