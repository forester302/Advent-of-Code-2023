import requests
import sys
import os
import dotenv

dotenv.load_dotenv()
sessionToken = os.environ["AoC_token"]
 
def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {'Cookie': 'session='+sessionToken}
    r = requests.get(url, headers=headers)
 
    if r.status_code == 200:
        return r.text 
    else:
        sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")

if __name__ == "__main__":
    print(get_input(2022,1)) # Test case