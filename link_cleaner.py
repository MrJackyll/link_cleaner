import re

def trim_url(url):
    trimmed_url = re.sub(r'\?.*$', '', url)
    return trimmed_url

if __name__ == "__main__":
    user_input = input("Enter your link: ")
    result = trim_url(user_input)
    print(\nClear link:", result)
