"""Manage the Moby Project's corpus"""
import os
import pathlib
import shutil
import sys
from os import path

import wget
import requests
from lxml import html

_URLS = {
    "word_list": "http://www.gutenberg.org/files/3201/"
}

_CORPUS_PATH = os.path.join(sys.prefix, 'moby_data/')


def _download_files(url, out, check_if_present=True):

    main_page = requests.get(url)
    if not check_if_present:
        shutil.rmtree(out)
    pathlib.Path(out).mkdir(parents=True, exist_ok=True)
    tree = html.fromstring(main_page.content)
    links = tree.xpath("//a/@href")
    for l in links:
        subpath = os.path.join(out, l)
        next_link = url + l
        # if it is a subdirectory
        if l[-1] == "/":
            _download_files(next_link, subpath)
        #  else,
        elif not check_if_present or not path.exists(subpath):
            wget.download(next_link, subpath)


def _download(corpus_name, force=False):
    if corpus_name not in _URLS:
        raise Exception("Corpus name not found or not supported.")
    url = _URLS[corpus_name]
    out = os.path.join(_CORPUS_PATH, corpus_name)
    _download_files(url, out, check_if_present=not force)


class CorpusReader:
    def __init__(self, corpus_name):
        self.corpus_name = corpus_name

    def download(self, force=False):
        _download(self.corpus_name, force=force)


class WordListCorpusReader(CorpusReader):
    """http://www.gutenberg.org/files/3201/3201.txt"""

    def __init__(self):
        super().__init__("word_list")

    def _readlines(self, name):
        """readlines from generic sub-corpus"""
        with open(os.path.join(_CORPUS_PATH, self.corpus_name, "files", name), encoding="utf8", errors='ignore') as f:
            return list(map(lambda x: x.strip(), f.readlines()))

    def single(self):
        """Get only single words"""
        return self._readlines("SINGLE.TXT")

    def names(self):
        """Get names"""
        return self._readlines("NAMES.TXT")

    def male_names(self):
        """Get male names"""
        return self._readlines("NAMES-M.TXT")

    def female_names(self):
        """Get female names"""
        return self._readlines("NAMES-F.TXT")

    def places(self):
        """Get places"""
        return self._readlines("PLACES.TXT")

    def crossword(self):
        """A list of words permitted in crossword games such as Scrabble(tm).
        Compatible with the first edition of the Official Scrabble Players
        Dictionary(tm).  Since this list has all forms: -ing, -ed, -s, and so
        on of words, it makes a good addition when building a custom spelling
        dictionary."""
        crosswords = self._readlines("CROSSWD.TXT")
        crosswords_delta = self._readlines("CRSWD-D.TXT")
        return crosswords + crosswords_delta

    def all(self):
        words = self.single() + self.names() + self.male_names() + self.female_names() +\
                self.places() + self.crossword()
        return set(words)
