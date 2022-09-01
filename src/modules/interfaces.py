import os
import requests
from bs4 import BeautifulSoup


class Module:
    def __init__(self):
        """Retrieves username and password from environment secrets."""

        self.name = self.__class__.__name__.upper()
        self.user = os.environ[self.name + '_USER']
        self.password = os.environ[self.name + '_PASSWORD']
        self.session = requests.Session()
        self.initialized = False

    def login(self):
        """Logs into the online classroom webpage."""

        raise NotImplementedError

    def run(self, assignments):
        if self.initialized:
            self._main(assignments)

    def _main(self, assignments):
        """Parses the webpage for assignments and adds them to ASSIGNMENTS."""

        raise NotImplementedError

    def finish(self):
        """Any final clean up steps."""

        pass

    #################################
    #       Helper Functions        #
    #################################
    @staticmethod
    def parse_html(html):
        return BeautifulSoup(html, 'html.parser')
