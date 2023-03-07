import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
from pathlib import Path
import pandas as pd


def get_all_images(html):
    # Use BeautifulSoup to extract all image URLs from the HTML code
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.find_all("img")
    img_urls = []

    # Extract all URLs from src and srcset attributes
    for img in img_tags:
        img_urls.append(img['src'])
        if 'srcset' in img.attrs:
            srcset_urls = img['srcset'].split(',')
            for srcset_url in srcset_urls:
                img_urls.append(srcset_url.strip().split()[0])

    # Check the status code of each image URL
    invalid_urls = []
    for img_url in img_urls:
        # Check if the URL has a valid scheme
        if urlparse(img_url).scheme:
            response = requests.get(img_url)
            # if the status code is not 200, add it to the list of invalid URLs
            if response.status_code > 399: 
                invalid_urls.append(img_url)
            else:
                # Check if the URL is from the same domain
                if urlparse(img_url).netloc != test_site:
                    invalid_urls.append(img_url)

    if invalid_urls:
        for invalid_url in invalid_urls:
            # replace hostname with live_site
            parsed_url = urlparse(invalid_url)
            parsed_url = parsed_url._replace(netloc=live_site)
            modified_url = parsed_url.geturl()
            path = parsed_url.path

            invalid_filename = os.path.basename(path)
            invalid_data = requests.get(modified_url).content

            path = '.' + parsed_url.path.replace("%20", " ")
            # get the directory structure from the invalid URL
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)

            # write the file to the same relative path without the domain
            print(f"{directory}/{invalid_filename}")
            with open(f"{directory}/{invalid_filename}", 'wb') as f:
                f.write(invalid_data)


excel_name = 'Example Excel.xlsx' # change this to the name of the excel file
excel_sheet = 'Blogs' # change this to the name of the sheet
excel_column = 'F' # change this to the column letter

test_site = 'staging.example.com' # change this to the dev site
live_site = 'example.com' # change this to the live site

urls = pd.read_excel(excel_name,usecols = excel_column,sheet_name=excel_sheet,skiprows=[0],header=None).to_numpy()

print("Total URLs: ", len(urls))
i=0
for url in urls:

    i+=1
    print(f"Processing URL {i} of {len(urls)}")
    print(url[0])
    
    try:
        html = requests.get(url[0],stream=True)
        if html.status_code == 200 and html.content:
            get_all_images(html.content)
        
    except requests.exceptions.MissingSchema:
        pass