import requests
from .models import TeleSettings


def send_telegram_message(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_text)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.find('{') and text.find('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.find('{')]
            part_3 = text[text.find('}'):-1]
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slice = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Send error')
            elif req.status_code == 500:
                print('Error 500')
            else:
                print('OK. Message is sent!')
