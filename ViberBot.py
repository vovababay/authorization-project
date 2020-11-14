from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4c721f826bc00a41-cde61cf2e0862f5b-7b5080ab2cf79a9d'
)
viber = Api(bot_configuration)
viber.send_messages()