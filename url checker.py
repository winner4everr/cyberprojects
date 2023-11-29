import requests

def check_url_reputation(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"The URL '{url}' is accessible and considered trusted.")
        else:
            print(f"The URL '{url}' is not accessible or may be flagged as potentially unsafe.")
    except requests.exceptions.RequestException:
        print(f"An error occurred while trying to access the URL '{url}'.")

# Enter the URL you want to check
url = "https://lms.nu.edu.sa/webapps/collab-ultra/tool/collabultra?course_id=_70361_1&mode=view"

check_url_reputation(url)