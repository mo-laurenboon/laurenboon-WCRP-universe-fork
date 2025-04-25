import json
import os
from urllib.parse import urljoin

import requests

# GitHub repository information
repo_owner = "znichollscr"
repo_name = "CMIP7_DReq_Content"
branch = "extract-branded-variables"
path = "branded-variables"

# Local directory where the modified JSON files will be saved
local_dir = "known_branded_variable/"

# Create the local directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)


def get_github_directory_contents(owner, repo, branch, path):
    """Fetch the contents of a directory in a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def download_and_modify_json(file_url):
    """Download a JSON file, modify it, and save it locally."""
    response = requests.get(file_url)
    response.raise_for_status()

    # Parse the original JSON
    original_json = json.loads(response.text)

    # Extract the filename from the URL
    filename = file_url.split("/")[-1]

    # Modify the JSON according to requirements
    modified_json = {
        "@context": "000_context.jsonld",
        "id": original_json.get(
            "branded_variable", ""
        ).lower(),  # Use branded_variable as id
        "description": original_json.get("description", ""),
        "dimensions": original_json.get("dimensions", []),
        "type": "known_branded_variable",
        "cell_methods": original_json.get("cell_methods", ""),
        "variable": original_json.get("variableRootDD", ""),
        "label": original_json.get("branded_variable"),
        "drs_name": original_json.get("branded_variable"),
    }

    # Save the modified JSON
    save_path = os.path.join(local_dir, filename)
    with open(save_path, "w") as f:
        json.dump(modified_json, f, indent=2)

    return filename


# Main execution
try:
    # Get the directory contents
    contents = get_github_directory_contents(repo_owner, repo_name, branch, path)

    # Process each JSON file
    for item in contents:
        if item["type"] == "file" and item["name"].endswith(".json"):
            print(f"Processing {item['name']}...")
            download_and_modify_json(item["download_url"])

    print(f"All files have been downloaded and modified. Saved to {local_dir}")

except requests.exceptions.RequestException as e:
    print(f"Error accessing GitHub: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
