import os
import requests

# Get API key from environment variable
API_KEY = os.getenv("PIXABAY_API_KEY")

if not API_KEY:
    raise ValueError("Please set the PIXABAY_API_KEY environment variable.")

# Define API base URL
BASE_URL = "https://pixabay.com/api/"

# Parameters
query = "yellow flowers"  # Search term
lang = "en"  # Language code
image_type = "photo"  # Image type
orientation = "horizontal"  # Orientation
category = "nature"  # Category
min_width = 800  # Minimum image width
min_height = 600  # Minimum image height
colors = "yellow"  # Color filter
editors_choice = True  # Editor's choice filter
safesearch = True  # Safe search filter
order = "popular"  # Order by
page = 1  # Page number
per_page = 10  # Results per page
pretty = True  # Pretty JSON output

# Construct the query parameters
params = {
    "key": API_KEY,
    "q": query,
    "lang": lang,
    "image_type": image_type,
    "orientation": orientation,
    "category": category,
    "min_width": min_width,
    "min_height": min_height,
    "colors": colors,
    "editors_choice": str(editors_choice).lower(),  # Convert boolean to lowercase string
    "safesearch": str(safesearch).lower(),  # Convert boolean to lowercase string
    "order": order,
    "page": page,
    "per_page": per_page,
    "pretty": str(pretty).lower(),  # Convert boolean to lowercase string
}

# Make the API request
response = requests.get(BASE_URL, params=params)

# Check for successful response
if response.status_code == 200:
    print(response.json())  # Pretty print the JSON response
else:
    print(f"Error: {response.status_code}, {response.text}")
