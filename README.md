# retrobot
A minimalistic Discord server bot for my very own server.

## Sample
[![Clear-CHat.gif](https://i.postimg.cc/6p4bPDTP/Clear-CHat.gif)](https://postimg.cc/ZWZLBs8P)

## What can it do?
Well, at the moment it can:
* Clear the chat (also works as the purge command)
* Have a custom prefix (the default is r!)
* Have a custom status (although that's kind of strange)
* Update you when a user has joined/leaved (to make him happy/sad)
* Kick/Ban/Unban a user (you can also provide a reason)
* Tell you your crappy Internet connection latency in milliseconds
* Be an 8ball? Yes - it can. (just use r!8ball)
* Make announcements (r!announce #channel message message message)

## To-do
* On-join / on-leave direct messages.
* Music features (play, stop, clear the queue)

## How-to add it on your server
I created retrobot to give my a server a custom bot, although you can do whatever the GPLv3 license allows you to do, including creating your own version of it.
To begin, just open a terminal and type in:
```bash
git clone https://github.com/pasenidis/retrobot.git
cd retrobot
code .
# or
atom .
# or just use your favorite IDE!
```
Now, you should open bot.py and start modifying.
Also create a credentials.txt with your token inside, that's safer than having it in bot.py in case you upload it online.

## FAQ
* Q: Why do I have the token in a seperate file?
* A: For better open-sourcing. It takes time to have two seperate git repositories, one with a token and a second without a token. I just add credentials.txt to .gitignore and upload all the code to GitHub!
* Q: How can I contribute?
* A: There are two ways of contributing: you can either fork the repository (which won't really help because that will not be the original project) or just contribute to my own code! How? Just commit, you can even do this online! If your improvement/change/contribution seems right to the maintainer, he approves it and the project becomes a bit better, because of you! <3
* Q: How much time do you have for this project?
* A: Not much, I am doing this for fun and to learn the DiscordPy library, as I was making bots only in JavaScript, so I thought this would be a good try.
* Q: Can I join your server?
* A: Yes! Click this invite [link!](https://discord.gg/FtQ769f)
