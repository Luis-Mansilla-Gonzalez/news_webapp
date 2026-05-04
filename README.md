#Overview
This program displays news headlines using the gdelt project api, hosted on a docker based local webapp

The news articles are as recent as the api refreshes, getting information through JSON file format

The webapp also displays the news article headline, as well as providing the link to the article (using Firefox, links on edge are not clickable at present)

#Structure

The folder contains the yml file

The backend folder contains: dockerfile, main.py, and requirements.txt

the dockerfile creates the python environment, installs from the requirements.txt file, and runs the api
main.py contains the main operations for the backend work

The frontend folder contains: dockerfile, frontend.html

the frontend docker sets up the web server for the html file 
frontend html file allows interaction (readable headlines and clickable links) for the user

#usage

to build docker container, run: 

docker compose up --build

Frontend: http://localhost:3000

Backend: http://localhost:5000/api/news

#improvements

For better user experience, providing a link preview displaying the news organization and article thumbnail
Additionally, including a language and article category filter would be in the works
