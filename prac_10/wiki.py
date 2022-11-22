"""
CP1404/CP5632 Practical
Use wikipedia python API
"""

import wikipedia
from wikipedia import DisambiguationError, PageError

search_phrase = input("Search phrase: ")
while search_phrase != "":
    wikipedia.search(search_phrase)
    try:
        summary = wikipedia.summary(search_phrase)
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary: {summary}")
        print(f"URL: {page.url}")
    except DisambiguationError as e:
        print("Disambiguation page")
        print(e.options)
    except PageError:
        print("The page doesn't exist")
    search_phrase = input("Search phrase: ")
