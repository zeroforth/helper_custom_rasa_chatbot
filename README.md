# helper_custom_rasa_chatbot
Custom Rasa Chatbot for Django -  Currently fetches Bible Verse from API

**To install RASA opensource and intializing the bot**
https://rasa.com/docs/rasa/installation/installing-rasa-open-source

**Setting up the bot**
After installation and Init , train the bot for the first time using
```
rasa train
```
this will set up the intial training data , now use this repo to change the relevant files of your rasa bot directiory 
- The custom actions are in actions/actions.py
- The intent recognition and conversations(stories) are in data directory (all are YAML files , syntax sensitive)
- The domain.yml is realllyreallly important - endpoints.yml is used to define API endpoints - will need it to connect to django

**Any changes you do to data - make sure to re-train your chatbot on that data**

**Django files**
The custom views , models and urls are given here , just create a new app inside your existing Django project using
```
pyhton3 manage.py startapp helperbot
```
and replace the code inside the views.py , models.py , urls.py from this repo
also the templates , just paste them inside the directory of your app 

**Did all of it , did runserver and nothing worked?**
It wont yet 
First make sure you made all migrations after you created a new app and then do
````
python3 manage.py runserver
```

open another terminal and start the rasa chatbot
```
rasa run -m models --enable-api --cors "*" --debug
```

and another terminal(exhausting i know) and start the action server
```
rasa run action
```
(Or just write a script to do this )

The current actions fetched Bible Verses from https://bolls.life/api/ API

