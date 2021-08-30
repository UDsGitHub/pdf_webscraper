import requests
from bs4 import BeautifulSoup

# URL
url = 'https://dyysg.org.uk/docs.php'

# make HTTP ger request to url
response = requests.get(url)

# parse content
content = BeautifulSoup(response.text, 'lxml')

# extract PDF URLs
all_urls = content.find_all('a')

# loop over all urls
for url in all_urls:
    # try URLs containing 'href' attribute
    try:
        # collect only those with pdf in them
        if 'pdf' in url['href']:
            # init PDF url
            pdf_url = ''
            # append base URL if 'https' not in URL
            if 'https' not in url['href']:
                pdf_url = 'https://dyysg.org.uk/docs.php' + url['href']
            # use bare URL otherwise
            else:
                pdf_url = url['href']
            # make HTTP request to fetch pdf bytes
            pdf_response = requests.get(pdf_url)

            # extract PDF file names
            filename = pdf_response.url.split('/')[-1].replace('%20', '_')

            # write pdf file to local file
            with open('./PDFs/' + filename, 'wb') as f:
                # write pdf to local file
                f.write(pdf_response.content)
    # skip all other URLs
    except:
        pass
