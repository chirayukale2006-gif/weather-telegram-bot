from dotenv import load_dotenv
load_dotenv()
import requests
import os
from bs4 import BeautifulSoup
import telebot
url="https://www.timeanddate.com/weather/india/pune"
BOT_TOKEN=os.environ.get("BOT_TOKEN")
# chat_id=""
# print(BOT_TOKEN)


bot=telebot.TeleBot(BOT_TOKEN )
# print(BOT_TOKEN)

# def send(msg):
#     requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
#         data={
#             "chat_id":msg.chat.id,
#             "text":msg
#         }

#     )


def Getweather(city,chat_id):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response=requests.get(f"https://www.timeanddate.com/weather/india/{city}", headers=headers)

    if(response.status_code!=200):
        bot.send_message(chat_id, "City not Found please Enter valid city ")
        return 
    


    soup=BeautifulSoup(response.text, "html.parser")

    # print(soup.prettify())
    firstday=soup.select_one('div#qlook')
    now=firstday.find(class_='h1').string
    # print(now)
    temperature=soup.select_one('div.h2').string
    # print(temperature)

    weather=soup.select('p')[0].string
    # print(weather)
    # print(soup.find_all('p')[1].get_text(separator='\n'))

    message=f"{city}\n{now}\nTemperature: {temperature}\nWether:{weather}"
    # print(message)

    # print("\n\n\n")

    for line in soup.find_all('p')[1].stripped_strings:
        message+='\n'+(line)

    # print(soup.find_all('tbody')[0].get_text(separator='\n'))
    # print(message)

    # requests.post(
    #     f"https://api.telegram.org/bot{Bot_token}/sendMessage",
    #     data={
    #         "chat_id":chat_id,
    #         "text":message
    #     }
    # )
    bot.send_message(chat_id,message)




    meassage2=""

    for line in soup.find_all('tbody')[0].stripped_strings:
        meassage2+=line+"\n"

    # print(meassage2)
    # requests.post(
    #     f"https://api.telegram.org/bot{Bot_token}/sendMessage",
    #     data={
    #         "chat_id":chat_id,
    #         "text":meassage2
    #     }
    # )
    bot.send_message(chat_id,meassage2)


    time=soup.select_one('tr.h2').get_text(separator="\n").split()


    i=0
    meassage3="Upcoming temperature \n "
    for line in soup.find(class_="h2 soft") :
        meassage3+=(time[i]+"-> " +line.string)+'\n'
        i+=1

    # requests.post(
    #     f"https://api.telegram.org/bot{Bot_token}/sendMessage",
    #     data={
    #         "chat_id":chat_id,
    #         "text":meassage3
    #     }
    # )

    bot.send_message(chat_id,meassage3)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id=message.chat.id
    bot.send_message(message.chat.id,"""welcome to the ck`s wheather bot\n
                 Usase:\n
                 /weather <city_name> & get current weather\n
                 Example:\n
                 /weather pune """)
   
    
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "📖 Available Commands:\n\n" "/weather <city> — Current weather for any Indian city\n" "/start — Welcome message\n" "/help — Show this message")

@bot.message_handler(commands=['weather'])
def weather(message):
    part=message.text.split()
    if(len(part)<2):
        bot.send_message(message.chat.id, "Please Enter The city")
        return 
    
    city=part[1]
    bot.send_chat_action(message.chat.id,"typing")
    result=Getweather(city,message.chat.id)

    
    
bot.infinity_polling()
