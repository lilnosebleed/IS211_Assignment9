import requests
from bs4 import BeautifulSoup

def main():
        print("Running scrapper two...")
         ## url: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions
        url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

  ## again, adding another user agent so the script isnt blocked when accessing
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        print("Super Bowl Champions")
        print("-" * 40)

        ## beautifulsoup actually has a wikitable class
        tables = soup.find_all('table', class_='wikitable')

        if len(tables) < 2:
              print("Error: Could not find the expected tables on Wikipedia.")
              return

    ## looping through the tables to find the main one
        for table in tables:
            rows = table.find_all('tr')
    
        ## actual champions table will have over 50 rows. 
        ## skips the top of page table if it is too short
            if len(rows) > 20:
        
            ## grabs the first 20 games, having a clean output 
                for row in rows[1:21]:
                    cols = row.find_all(['td', 'th'])
            
                    if len(cols) >= 3:
                        game = cols[0].text.strip()
                        year = cols[1].text.strip()
                        winning_team = cols[2].text.strip()
                        print(f"Game: {game} | Year: {year} | Winner: {winning_team}")

if __name__ == "__main__":
    main()
   
