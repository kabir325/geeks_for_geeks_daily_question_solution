import requests
from selenium import webdriver
from bs4 import BeautifulSoup




def scrape():
    # Initialize a headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    
    url = 'https://practice.geeksforgeeks.org/explore?page=1&sortBy=submissions&utm_source=auth&utm_medium=profile&utm_campaign=empty-data'
    browser.get(url)
    
    main_window = browser.current_window_handle
    
    js_script = """
    var element = document.querySelector('.explore_problem__XatX9');
    if (element) {
        element.target = "_blank";
        element.click();
    }
    """
    browser.execute_script(js_script)
    
    new_window = [window for window in browser.window_handles if window != main_window][0]
    browser.switch_to.window(new_window)
    
    new_url = browser.current_url
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    # Navigate to the page
    browser.get(new_url)

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

    # Find the element with class 'problems_problem_content__Xm_eO'
    example_div = soup.find('div', class_='problems_problem_content__Xm_eO')

    # Check if the element was found
    if example_div is not None:
        # Get the text content from the element
        content_string = example_div.text
    else:
        content_string = ""

    # Print or use the content_string

    output = {
        "folder_name": string,  # Use the extracted string for folder name
        "file_name": string + ".txt",  # Append '.txt' to the folder name for the file name
        "content": content_string  # Use the content string as the file content
    }

    return output
if __name__ == "__main__":
    inp=scrape()
    print(inp)
    
        
