# whatsapp-broadcaster

![main screen lol](https://i.imgur.com/EN2krD7.jpg)

Mass WhatsApp message broadcaster for a list of phone numbers. Provides interval delay functionality between messages.

## Running on local
### Requirements

- python3 (i used 3.8.3 but 3.6 and above should work fine)
- Google Chrome on your pc
- Chrome webdriver
- selenium (install via pip): `pip install selenium`
- tkinter for GUI (linux: install via `sudo apt-get install python3-tk`)

Just run `python WhatsappBroadcaster.py` in the root directory.

## Building into executable

[pyinstaller](https://www.pyinstaller.org/) can be used to compile it to a distributable exe with the following command.

```
pyinstaller --add-data "./wa.ico;./" ./WhatsappBroadcaster.py
```

## Distributed executable

If you do not know how to compile this or run it, check out the Releases section for precompiled versions of this. You need to get your own Chromedriver.exe file from https://chromedriver.chromium.org/downloads. Make sure the version of chromedriver you're downloading is the same as your computer's Google Chrome version (click on the three-dots menu > `Help` > `About Google Chrome` to find out your version).


