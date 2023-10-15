from selenium import webdriver

# Initialize a headless browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

# Navigate to the page
url = 'https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1'
browser.get(url)

# Wait for some time to let the content load (you might need to adjust this)
browser.implicitly_wait(10)

# Get the page source after it's fully loaded
page_source = browser.page_source

# Close the browser
browser.quit()

# Now you can create a BeautifulSoup object with the page source
soup = BeautifulSoup(page_source, 'html.parser')

#to get the title of the file

example_div = soup.find('title')
string=example_div.text 
len=string.find('|')
string=string[:len-1]
string=string.replace(' ','_')
print(string)

# Find the element with class 'problems_problem_content__Xm_eO'
example_div = soup.find('div', class_='problems_problem_content__Xm_eO')

# Check if the element was found
if example_div is not None:
    # Get the text content from the element
    content_string = example_div.text
else:
    content_string = ""

# Print or use the content_string
print(content_string)


import github_interaction

github_interaction.create_folder_and_add_file()
