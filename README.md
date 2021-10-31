# FlamingTranslationMonkeys

To Run the project, you will first need to install some dependencies.

# Instructions for Windows
Setting up the front end (from top level dir):

``` 
cd frontend
npm install
npm start 
```

Setting up the backend (from top level dir):

```
cd backend
python3 -m venv venv
. \venv\Script\activate
pip install -r requirements.txt
python app.py
```

Now that both the back-end and front-end are up and running, you can
experiment with the software. On the website, navigate to the service
tab. For now, you will need SRT (subtitle) files for the files you want
dubbed. Upload the srt, mp4, select appropriate options, and watch the magic!

# Errors:
Male voice config error

Sync drop down doesn't change anything, you only receive ratio-synced audios

The audio and video sliders aren't synced. To reset, you need to reload the page
