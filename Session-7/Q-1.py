class InstaStory:
    def share(self):
        print("Sharing an image story")

class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

obj1 = InstaStory()
obj2 = WhatsAppStory()

obj1.share()
obj2.share()