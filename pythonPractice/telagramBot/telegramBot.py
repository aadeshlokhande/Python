from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import constants as key
import Responses as Res


help_text = '''
| <π> | <π> | <π> | <π> | <π> |\n
πππMAIN FEATURESπππ\n
π1) π» Wikipedia search \ntype: wiki <anytopic>\nExample:- wiki tajmahal\n
π2) π€ Search a meaning of word \ntype: mean <anyword>\nExample:- mean World\n
π3) π Convert number to words \ntype: word in <any number>\nExample:- word in 12\n
π4) π Instagram ID details \ntype: insta <username>\nExample:- insta aadesh_lokhande\n
π5) π± Translate to Hindi\ntype: trans <sentense>\nExample:- trans I love India\n
π6) π URL shortener\ntype: url <url/link>\nExample:- url t.me/AadeshLokhandeBot \n
π7) π¦  Covid updated cases\ntype: covid <country name>\nExample:- \na) covid India\nb) covid world\n
π8) Calculator\ntype: calc <Equation>\nExample:- calc 3+2-1*2\\6\n
π9) Bitoin Price\ntype: Bitcoin\n
π10) calender\nTypr: month <month number> <year>\nExample:- month 9 1997

πππBASIC FEATURESπππ\n
π1) βοΈ Time \ntype: time\n
π2) ποΈ Date \ntype: date\n
π3) π Instagram ID \ntype: instagram\n
π4) π°οΈ Big word \ntype: big <any word>\nexample:- big Aadesh\n
π5) π Reverse sentense\ntype: rev <any sentense>\nExample:- rev Aadesh Lokhande\n
π6) π  Capitalize sentense\ntype: cap <any sentense>\nExample:- cap Aadesh Lokhande\n
π7) π‘ Small letters\ntype: small <any sentense>\nExample:- small Aadesh Lokhande\n
π8) π Emoji\ntype: emoji <emoji>\nExample: emoji moon\n
π9) π£οΈ Table\ntype: table <number>\nExample: table 12\n
π10) π£οΈ You can do small talk also (Beta Version)\n
| <π> | <π> | <π> | <π> | <π> |
'''


def start_command(update, context):
    update.message.reply_text("Welcome to Aadesh Lokhande's Bot.\nHow can I help you \n/help")

def help_command(update, context):
    update.message.reply_text(help_text)

def handle_command(update,context):
    text = str(update.message.text).lower()
    response = Res.sample_responses(text,update)
    helpmsg = Res.navigat(text)
    update.message.reply_text(response+"\n"+helpmsg)
    


def error(update, context):
    # errortxt = f"Update:- {update}\n\ncaused error:- {context.error}"
    # print(errortxt)
    update.message.reply_text(f"\ncaused error:- {context.error}")
    # pass

def main():
    print("Start BOT...")
    updater = Updater(key.API_KEY, use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_command))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

a = 0
while(a==0):
    try:
        main()
        a+=1
    except:
        print("No Internet Connection")