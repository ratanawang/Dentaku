from commands.command import Command
from fbchat import Message
from fbchat import Mention
import bs4
import requests

class hackathon(Command):

    def run(self):
        link = "https://vikingsdev.ca/events.html"
        webpage = requests.get(link)
        source = bs4.BeautifulSoup(webpage.text, 'html.parser')
        title = str(source.find("h4", class_="mb-2").getText())
        date = str(source.find("span", class_="subheading").getText())
        loc = str(source.find_all("span", class_="subheading")[1].getText())
        reg = str(source.find("a", string="REGISTER"))
        reg = reg[reg.find("href") + 6:reg.find(">", reg.find("href")) - 1]
        ml = str(source.find("a", string="Mailing List"))
        ml = ml[ml.find("href") + 6:ml.find(">", ml.find("href")) - 1]
        response_text = "@" + self.author.first_name + "\nThe closest hackathon is " + title + "\nDate: " + \
                        date + "\nLocation: " + loc + "\nRegister at: " + reg + "\nMailing List: " + ml
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions= mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "None",
            "function": "Tells you the closest upcoming hackathon."
        }