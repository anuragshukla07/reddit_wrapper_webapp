
# Reddit Wrapper WebApp

The Reddit Articles Web Application is a basic web application built using the Django framework that fetches the latest articles from a chosen subreddit using the "Reddit API". This documentation provides an overview of the application's structure, setup instructions, and usage details.

## Tech Stack & Libraries Used

-	Django : Used as the backend framework for this project as it simplifies the project building.
-	PRAW (Python Reddit API Wrapper) : Used as a wrapper for the Reddit API to interact with Reddit's data and retrieve articles from subreddits.

## Installation

Clone the repository to your local machine.

```bash
  git clone https://github.com/anuragshukla07/reddit_wrapper_webapp.git
```
Before starting it is a good practice to start the project in a separate isolated environment using 'venv'.

```bash
py -m venv venv
```
Activate the 'venv' using the following code for 'Windows'.

```bash
venv\Scripts\activate
```
Install all the dependencies using the requirements.txt file which contains all the dependencies that are required to run the project.

```bash
pip install -r requirements.txt
```

## Configuration
1.	Open the "reddit_wrapper_project/settings.py" file.
2.	Locate the following lines and replace the placeholders with your actual Reddit API credentials :

```bash
REDDIT_CLIENT_ID = 'YOUR_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDDIT_USER_AGENT = 'YOUR_USER_AGENT'
```

### NOTE : 
For security purposes for this app, I have hidden the Reddit Configs and Django Secret Key in the ".env" file and mentioned this in the ".gitignore" file so as to avoid pushing it on GitHub and keep the project secure.

## Running the Application
Navigate to the project's root directory and run the development server.

```bash
python manage.py runserver
```
You’ll see that the project is running successfully on your local server.

## NOTE :
You can change the name of the subreddit in the "views.py" file present in "reddit_wrapper_project\articles\views.py".

## Screenshots

![Homepage](https://github.com/anuragshukla07/reddit_wrapper_webapp/blob/master/ScreenShots/Original%20-%201.jpg) 
Original Subreddit Page
![Homepage](https://github.com/anuragshukla07/reddit_wrapper_webapp/blob/master/ScreenShots/Wrapper%20-1.jpg) 
Project Page
![Homepage](https://github.com/anuragshukla07/reddit_wrapper_webapp/blob/master/ScreenShots/Original%20-%202.jpg) 
Original Subreddit Page
![Homepage](https://github.com/anuragshukla07/reddit_wrapper_webapp/blob/master/ScreenShots/Wrapper%20-%202.jpg) 
Project Page

