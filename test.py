import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    original_text = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    translate_text = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    for i in range(len(original_text)):
        print(original_text[i], translate_text)

def main():
    parse('https://www.amalgama-lab.com/songs/a/avicii/hey_brother.html')

if __name__ == "__main__":
    main()