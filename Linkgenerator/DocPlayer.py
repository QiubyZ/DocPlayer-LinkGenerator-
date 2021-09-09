from requests import Session
from bs4 import BeautifulSoup

class DocPlayer(Session):
    def __init__(self, url):
        super(DocPlayer, self).__init__()
        self.urls = url
        self.title = None
        self.doc_id = None
        self.doc_view = None
        self.file_name = None
        self.link_generator = None
        self.__parse_id()

    def __parse_id(self):
        element = BeautifulSoup(self.get(self.urls).text, "html.parser")
        self.title = element.find("title").text
        self.doc_id = element.find("span", {"id":"views_count"}).get("doc_id")
        self.doc_view = element.find("iframe", {"id":"player_frame"}).get("src")
        self.file_name = element.find("a", {"id":"download_link"}).get("download")
        self.link_generator = f"https://{self.urls.split('/')[2]}{self.doc_view.replace('docview', 'storage')}{self.doc_id}.{self.file_name.split('.')[-1]}"

    def getLink(self):
        return self.link_generator