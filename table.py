import pandas as pd


# SearchResults = HTMLSource.find('table', id="SearchResult")
# ResultsContents = (SearchResults.prettify())

df = pd.read_html('table.html')
print(df)