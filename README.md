# Django Gallery
## This is a django gallery application where users can upload their photos and store according to different locations taken and different category
 
 ## Author
## By **[JOSEPHAT OTIENO](https://github.com/josphat-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user and writer.

* User loads the application using the url provided
* The user sees various photos posted
* The user clicks on the photo; photos details page is loaded
* user searches for images by category
* different photos are loaded according to that category
* User filters photos by location and different photos are loaded according to that location
* user clicks on the copy button to copy the link to download images


## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| users loads the application | *On page load* | user sees various photos posted on the application |
| user clicks on the photo | *On  click* | photo's details page is loaded showing the description, name , location and category |
| user searches for category on the search bar | *on page load* | different photos are loaded according to that category |
| user clicks on the loaction | *On page load* | different photos are loaded according to that location |
| user clicks on the copy button  |  | image link is copied to the clipboard |


## Prerequisites
* Python3.8

## Setup/Installation Requirements
* Clone [this repository]( https://github.com/josphat-otieno/Django-Gallery.git)  using the following commamnd  in the terminal: `git clone  https://github.com/josphat-otieno/Django-Gallery.git`. 
* Note:<em>You will need  git installed in your machine. You can install using the following comman: `$ sudo apt-get install git.`</em>
* After cloning, navigate to the folder where the repo was cloned and open it with your favorite code editor. 
* Create a vitual environment using the following command `python3 -m venv --without-pip virtual`
* Activate the virtual environment using the following command `source virtual/bin/activate`
* Run thefollowing command  to interact with the application `$python3.8 manage.py runserver`
* 
* Run tests units using the following command `$python3.8 manage.py test`

## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Django
- Heroku

## Contacts
# Tel: +254717878813
Email: josephat.otieno@student.moringaschool.com