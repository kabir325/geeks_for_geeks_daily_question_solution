import requests

# Define your repository information
owner = "kabir325"
repo = "geeks_for_geeks_question_solution"
folder_name = "new_folder"
file_name = "new_file.txt"
file_content = "Hello, this is the content of the new file."

# Set your Personal Access Token (PAT)
token = "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"

# Define API endpoints
base_url = f"https://api.github.com/repos/{owner}/{repo}"
contents_url = f"{base_url}/contents"
commit_url = f"{base_url}/git/commits"

# Create folder
folder_data = {
    "path": f"{folder_name}/",
    "message": f"Create {folder_name}",
    "content": "",
    "branch": "main"
}
response = requests.put(contents_url, headers={"Authorization": f"token {token}"}, json=folder_data)
response.raise_for_status()

# Create file
file_data = {
    "path": f"{folder_name}/{file_name}",
    "message": f"Add {file_name}",
    "content": file_content.encode("base64").decode(),  # Encode content to base64
    "branch": "main"
}
response = requests.put(contents_url, headers={"Authorization": f"token {token}"}, json=file_data)
response.raise_for_status()

# Create commit
commit_data = {
    "message": "Create new folder and add file",
    "content": file_content,
    "tree": response.json()["commit"]["tree"]["sha"],
    "parents": [response.json()["commit"]["sha"]]
}
response = requests.post(commit_url, headers={"Authorization": f"token {token}"}, json=commit_data)
response.raise_for_status()

print("Folder and file created successfully!")
