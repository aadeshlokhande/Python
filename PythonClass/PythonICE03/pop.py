import requests
import bs4
import os 

# This function gets the HTML of a web page.
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Error getting HTML for URL: {}".format(url))

# This function parses the HTML of a web page and returns a list of all the links on the page.
def get_links(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return links

# This function indexes the pages in a directory.
def index_pages(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            html = get_html(os.path.join(directory, filename))
            links = get_links(html)
            for link in links:
                url = link["href"]
                if url not in indexed_pages:
                    indexed_pages[url] = []
                indexed_pages[url].append(filename)

# This function searches for a keyword in the indexed pages.
def search(keyword):
    results = []
    for url, filenames in indexed_pages.items():
        for filename in filenames:
            with open(os.path.join(directory, filename), "r") as f:
                content = f.read()
                if keyword in content:
                    results.append((url, content))
    return results

# This function starts the search engine.
if __name__ == "__main__":
    directory = "/path/to/directory/with/html/files"
    indexed_pages = {}
    index_pages(directory)
    keyword = input("Enter a keyword to search for: ")
    results = search(keyword)
    for url, content in results:
        print("URL: {}".format(url))
        print("Content: {}".format(content))
