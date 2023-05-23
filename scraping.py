import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citation_tags)

count = get_citations_needed_count(url)
print(f"Number of citations needed: {count}\n")


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    report = ""
    for tag in citation_tags:
        passage = tag.find_parent('p')
        report += f"Citation needed for: {passage.text}\n"

    return report

report = get_citations_needed_report(url)
print(f'Citations needed report: {report}')
# print(report)


# convert to json
json_passages = json.dumps(report)

with open('passages.json', 'w') as file:
    file.write(json_passages)
