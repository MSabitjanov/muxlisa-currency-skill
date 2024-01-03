from mycroft import MycroftSkill, intent_file_handler


class MuxlisaCurrency(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('currency.muxlisa.intent')
    def handle_currency_muxlisa(self, message):
        self.speak_dialog('currency.muxlisa')


def create_skill():
    return MuxlisaCurrency()

