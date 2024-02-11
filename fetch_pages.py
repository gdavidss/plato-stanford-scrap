import requests

# Function to fetch HTML content for each letter and save it to a file
def fetch_and_save_html():
    # open output_list.txt and put entries into a list, removing \n
    with open("output_list.txt", "r") as file:
        output_list = file.read().splitlines()
    
    with open("entries", "r") as file:
        entries = file.read().splitlines()

    print(output_list)
    # Base URL before the letter
    base_url = "https://plato.stanford.edu/"

    # access the URL by concatenating the base URL and the entrie
    for i, entry in enumerate(output_list):
        url = base_url + entry
        response = requests.get(url)
        # Save the HTML content to a file
        with open(entries[i] + ".html", "w") as file:
            file.write(response.text)
        print("Saved " + entries[i] + " to file")    

# Call the function
fetch_and_save_html()

