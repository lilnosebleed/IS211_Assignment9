import requests
from bs4 import BeautifulSoup

def main():
  
    print("Running scrapper one...")

  ## url: https://finance.yahoo.com/quote/AAPL/history?p=AAPL
  url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

  ## have to make a useragent so Yahoo doesnt block out the request ( returning a error 404)
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'html.parser')

  ## finds the first table on the page
  table = soup.find('table')
  if not table:
        print("Error: Yahoo blocked the request or no table was found.")
        return
  rows = table.find_all('tr')

  print("Apple Stock - Fiscal Year Days Close")
  print("-" * 40)

  ## skips the first row (index 0) because it just contains the headers 
  for row in rows[1:]:
      cols = row.find_all('td')
    
      ## standard rows have 7 columns and dividend rows only have 2. 
      ## this check prevents the script from crashing on dividend days.
      if len(cols) >= 5:
          date = cols[0].text.strip()
          ## column 4 is the Close price column
          close_price = cols[4].text.strip()
          print(f"Date: {date} | Close: {close_price}")
        


if __name__ == "__main__":
    main()
