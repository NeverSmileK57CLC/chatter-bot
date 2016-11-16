from chatterbot import ChatBot
import logging

bot = ChatBot(
  "Bach Ngoc",
  storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
  login_adapters=[
    "chatterbot.adapters.logic.MathematicalEvaluation",
    "chatterbot.adapters.logic.TimeLogicAdapter",
    "chatterbot.adapters.logic.ClosestMatchAdapter",
  ],
  input_adapter="chatterbot.adapters.input.TerminalAdapter",
  output_adapter="chatterbot.adapters.output.TerminalAdapter",
  database="./database.json",
)

print "Type something to begin..."

while True:
  try:
    bot_input = bot.get_response(None)

  except(KeyboardInterrupt, EOFError, SystemExit):
    break
