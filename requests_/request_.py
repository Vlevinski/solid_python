import requests

# from bs4 import BeautifulSoup

url = "http://www.blog.pythonlibrary.org/"


def get_articles():
    """
    Get the articles
    """
    response = requests.get(url)
    html = response.text

    return f" Length: {len(html)}"


if __name__ == "__main__":
    print(get_articles())
