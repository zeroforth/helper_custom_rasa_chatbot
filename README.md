# helper_custom_rasa_chatbot
Custom Rasa Chatbot for Django -  Currently fetches Bible Verse from API

**To install RASA opensource and intializing the bot**
https://rasa.com/docs/rasa/installation/installing-rasa-open-source

**Setting up the bot :**
After installation and Init , train the bot for the first time using

```
rasa train
```

this will set up the intial training data , now use this repo to change the relevant files of your rasa bot directiory 
- The custom actions are in actions/actions.py
- The intent recognition and conversations(stories) are in data directory (all are YAML files , syntax sensitive)
- The domain.yml is realllyreallly important - endpoints.yml is used to define API endpoints - will need it to connect to django

**Any changes you do to data - make sure to re-train your chatbot on that data**

**Django files :**
The custom views , models and urls are given here , just create a new app inside your existing Django project using
<br>
```
pyhton3 manage.py startapp helperbot
```

<br>and use the views and urls to render your templates properly -  the chatbot render from the templates
<br>also the templates , just paste them inside the directory of your app 

**Did all of it , did runserver and nothing worked?**
<br>It wont yet
<br>First make sure you made all migrations after you created a new app and then do

```
python3 manage.py runserver
```

<br>open another terminal and start the rasa chatbot<br>

```
rasa run -m models --enable-api --cors "*" --debug
```

<br>and another terminal(exhausting i know) and start the action server<br>

```
rasa run action
```

<br>(Or just write a script to do this )

<br>The current actions fetched Bible Verses from https://bolls.life/api/ API<br>

