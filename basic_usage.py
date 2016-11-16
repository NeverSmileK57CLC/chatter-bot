from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
  "Bach Van Ngoc",
  silence_performance_warning=True,
  trainer="chatterbot.trainers.ChatterBotCorpusTrainer"
)

chatbot.train("chatterbot.corpus.english")

response = chatbot.get_response("Hello, how old are you?")

print chatbot.get_response("I have a question.")

conversation = [
  "Hello",
  "Hi there!",
  "How are you doing?",
  "I'm doing great.",
  "That is good to hear",
  "Thank you",
  "You're welcome."
]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

print chatbot.get_response("Good morning")
print chatbot.get_response("What's your name?")
