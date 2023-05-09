# Slido-Bot
A bot for the audience interaction tool sli.do.
Since Slido blocks malicious access via the API very effectively, this bot was created as a new solution for voting up questions automatically. It works via Firefox or Chrome browser.
## Instalation
```
git clone https://github.com/4rts/slido-bot.git
python -m pip install -r requirements.txt
```
## Syntax
To use the bot, copy 
```
python slidobot.py -h "hash" -q "question" -d "driver" -s "number of scrolls" - v "amount of votes"
```
and paste it into your terminal. Next, replace
1. "hash" with the text between event/ and /live in the slido-link.
For example, the hash in ```"https://app.sli.do/event/1a2b3c4d5e/live/questions"```
would be ```"1a2b3c4d5e"```.
2. "question" is the full question you want to upvote.
3. "driver" with the path to the [chromedriver](https://chromedriver.chromium.org/) or [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) I r.ecommend to use Chrome, because the bot is more performant with it.
4. "number of scrolls" will scroll the page down that number of times, as the html for the question will not be loaded until the questions load.
5. "amount of votes" with the amount of votes you'd like to add to the question.

Have fun.
