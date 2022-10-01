# How it works

There are two options to run the script, option 1 is with a discord bot command, Option 2 is to run it on a timer.

## Option 1

A server containing a discord bot with the commannd `run` will have the following sub commands

- [ ] timer - Takes date and time as arguments and runs the script at that time
- [ ] now - runs the script in the next 10 seconds
- [ ] cancel - cancels the execution of the script

## Option 2

- [ ] A timer that runs the script on a predefined schedule, example:
  - [ ] Tuesday - 7:50 AM - 9:45 AM
  - [ ] Thursday - 10:00 AM - 12:00 PM

### How the discord bot works

The python script will be listening on port 42069 for websocket messages and the discord bot will send a websocket message to the python script with the date and time
