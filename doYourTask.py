import wikipedia #pip install wikipedia

def searchInWikipedia(query):
    listWikiQuery = query.split(" ")[1:-2]
    stringWikiQuery = " ".join(listWikiQuery)
    try:
        results = wikipedia.summary(stringWikiQuery, sentences=2)
        print(results)
    except Exception as e:
        print("sorry! i couldn't find anything")