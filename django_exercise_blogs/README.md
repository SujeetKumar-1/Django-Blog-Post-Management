# Project Overview
This Django project demonstrates an efficient blogging platform with features like detect the country, country-based blog filtering, dynamic frontend interaction, and a CSV import feature for blog posts. The project showcases backend and frontend integration with modern design principles.

# Features

### Country Detection
Detects the user's country based on their IP address using a third-party API.
Displays the detected country dynamically on the frontend.

### Blog Post Management
Ability to import blog posts from a CSV file into the database using a custom Django management command.
Blog posts include title, content, and an optional country.

### Dynamic Filtering
Users can filter blog posts dynamically by country using a dropdown and button interaction on the frontend.
Filtering is implemented with JavaScript for a smooth, no-refresh experience.

### Pagination
Blog posts are displayed in a paginated format for improved readability and navigation.

### Styling and Responsiveness
Clean and responsive frontend design.
Compatible with all devices and browsers.

## Setup Instructions
1. Prerequisites
Python 3.8+
Django 3.2+

## A virtual environment tool (optional but recommended)
2. Installation Steps
Clone the repository:

   git clone <repository-link>
   cd django_blog_project

## Create and activate a virtual environment:
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate      # For Windows

## Install dependencies:
   pip install -r requirements.txt
   
## Run database migrations:
   python manage.py makemigrations
   python manage.py migrate

## Start the development server:
   python manage.py runserver

## Usage
1. Detect User's Country
The application detects the user's country using an external API and displays it on the blog post page.

2. Filter Posts by Country
Use the dropdown on the frontend to filter posts by country dynamically.

3. View Posts
Visit the homepage to view all blog posts with pagination. Filter them using the detected country or the dropdown.

## CSV Format for Importing Posts
The CSV file must have the following structure:

title,content,country
Post Title 1,Content for the post,India
Post Title 2,Another post content,USA

## API Integration
This project uses the ip-api to fetch the user's country based on IP. Ensure an active internet connection and proper API keys (if required).

## Frontend Functionality
The filtering mechanism is implemented using custom JavaScript. The posts are dynamically filtered and displayed or hidden based on the selected country from the dropdown.

## Screenshots
Blog posts with detected country displayed.
Pagination and filtering feature.
Enhanced UI with modern design.

# Views

## 1. post_list View
The post_list view fetches and displays blog posts in a paginated format while detecting the user's country.

** Workflow **
### Country Detection:

Uses the get_user_country utility to determine the user's country based on their IP address.
The detected country is passed to the template to enable filtering.

### Post Retrieval:
Retrieves all blog posts from the database (BlogPost.objects.all()).

### Pagination:
Implements pagination using Django's Paginator class.
Displays 12 posts per page (paginator = Paginator(posts, 12)).
The page_number query parameter allows navigation between pages.

### Template Rendering:
Renders the posts along with pagination and detected country to blog/post_list.html.

## 2. upload_csv View
The upload_csv view enables users to upload a CSV file and store its data in the database.

** Workflow **

### File Upload:
Accepts a POST request with a CSV file attached as csv_file.

### Validation:
Ensures the uploaded file has a .csv extension.
If not, returns a JSON response with an error message.

### CSV Parsing:
Reads the uploaded CSV file line by line using Python's built-in csv module.
Assumes each row in the file corresponds to a blog post with columns for title, content, and country.

### Database Storage:
Iterates through the rows and creates BlogPost entries in the database.

### Success/Error Handling:
On success, returns a JSON response indicating the data was uploaded successfully.
Catches exceptions and returns an appropriate error message.

### Template Rendering:
Renders the upload form (blog/upload_file.html) for GET requests.
CSV File Format

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.