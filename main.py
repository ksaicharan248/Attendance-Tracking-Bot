import time
import threading
import telegram.ext
from telegram.ext import CommandHandler
from telegram.ext import *
from allop import altho, altho_2
from webser import keep_alive
from todaypk import today
from tmrpk import tommaro
from replit import db
import io
import base64

tokenn = "5751283716:AAGHgB6P15DPNyaV7Kr_FGQpbX0DjuUT0gc"
#       Create the Updater and pass it your bot's token
updater = telegram.ext.Updater(tokenn, use_context=True)
#
#            Get the dispatcher to register handlers
dispatcher = updater.dispatcher

#         memory uint

attendanc = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0])
roshitt = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0])




#     A function dispcription

#15 MIN UPDATER CODE inside the threadings 2


def update_attendance():
  while True:
    global attendanc, roshitt
    attendanc = altho()
    time.sleep(10)
    roshitt = altho_2()
    time.sleep(60)


# Define a command handler function


def start(update, context):
  update.message.reply_text('Hi! /help')


def updaters(update, context):
  chat_id = update.message.chat_id
  useridd = update.message.from_user
  full_name = str(useridd.first_name) + str(useridd.last_name)
  if chat_id == 1746861239 or full_name == "saicharan":
    update.message.reply_text('Updating.....')
    t = threading.Thread(target=update_attendance)
    t.start()
    time.sleep(20)
    try:
      context.bot.delete_message(chat_id=update.message.chat_id,
                                 message_id=update.message.message_id)
      context.bot.delete_message(chat_id=update.message.chat_id,
                                 message_id=update.message.message_id + 1)
    except telegram.error.BadRequest:
      update.message.reply_text(
        'Due to some techincal issuse update have not done')

    update.message.reply_text('Updated succesfully............😒')
    time.sleep(10)
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id + 2)
  else:
    update.message.reply_text(
      "This command can ony be used by sai charan only")


def clear(update, context):
  chat_id = update.message.chat_id
  useridd = update.message.from_user
  full_name = str(useridd.first_name) + str(useridd.last_name)
  if chat_id == 1746861239 or full_name == "saicharan":
    for i in range(0, 50):
      try:
        context.bot.delete_message(chat_id=update.message.chat_id,
                                   message_id=update.message.message_id - i)
      except telegram.error.BadRequest:
        pass
  else:
    update.message.reply_text(
      "This command can ony be used by sai charan only")


def help(update, context):
  update.message.reply_text(
    "/attendance---->attandance visit\n/allattendance-------->show all\n/pic---attendance pic\n/more"
  )


def more(update, context):
  update.message.reply_text(
    "/today_attendance------> show todays\n/yesterdays----->show yesterday")
  try:
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id)
  except telegram.error.BadRequest:
    pass


def attendance(update, context):
  chat_id = update.message.chat_id
  useridd = update.message.from_user
  full_name = str(useridd.first_name) + str(useridd.last_name)
  global attendanc, roshitt

  if chat_id == 1746861239 or full_name == "saicharan":
    t2 = attendanc
    update.message.reply_text("your attendance is : " + str(t2[1][11]) + " %")
  else:
    t2 = roshitt
    update.message.reply_text("Your attendance is: " + str(t2[1][11]) + " %")


def pic(update, context):
  global attendanc, roshitt
  useridd = update.message.from_user
  full_name = str(useridd.first_name) + str(useridd.last_name)
  if full_name == "saicharan":
    encoded_string = attendanc[2]
    decoded_bytes = base64.b64decode(encoded_string)
    photo_file = io.BytesIO(decoded_bytes)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=photo_file)
  else:
    encoded_string = roshitt[2]
    decoded_bytes = base64.b64decode(encoded_string)
    photo_file = io.BytesIO(decoded_bytes)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=photo_file)
  try:
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id - 1)
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id - 2)
  except telegram.error.BadRequest as e:
    pass


def allattendance(update, context):
  useridd = update.message.from_user
  full_name = str(useridd.first_name) + str(useridd.last_name)
  global attendanc
  global roshitt
  if full_name == "saicharan":
    t2 = attendanc
    update.message.reply_text("subject" + " " * (16 - len("subject")) + " " +" " * (7 - len(str("percentage"))) +
                              "percentage " + "\n" + "\n".join([
                                str(t2[0][i]) + " " *
                                (16 - len(str(t2[0][i]))) + ":" + " " *(7 - len(str(t2[1][i]))) + str(t2[1][i])for i in range(0, 12)]))
  else:
    t2 = roshitt
    update.message.reply_text("\n".join([
      str(t2[0][i]) + " " * (16 - len(str(t2[0][i]))) + ":" + " " *
      (7 - len(str(t2[1][i]))) + str(t2[1][i]) for i in range(0, 12)
    ]))
  try:
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id - 1)
    context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id - 2)
  except telegram.error.BadRequest:
    pass


def today_attendance(update, context):

  t2 = today()
  update.message.reply_text("CS           :" + str(t2[0]) + "\n" +
                            "EMTL      :" + str(t2[1]) + "\n" +
                            "VLSI         :" + str(t2[2]) + "\n" +
                            "EMI          :" + str(t2[3]) + "\n" +
                            "IR             :" + str(t2[4]) + "\n" +
                            "MAP        :" + str(t2[5]) + "\n" +
                            "CS LAB    :" + str(t2[6]) + "\n" + "VL LAB    :" +
                            str(t2[7]) + "\n" + "COI          :" + str(t2[8]) +
                            "\n" + "CONS      :" + str(t2[9]) + "\n" +
                            "LIB           :" + str(t2[10]) + "\n" +
                            "TOTAL     :" + str(t2[11]) + "%")


def yesterdays(update, context):

  t2 = tommaro()
  update.message.reply_text("CS           :" + str(t2[0]) + "\n" +
                            "EMTL      :" + str(t2[1]) + "\n" +
                            "VLSI         :" + str(t2[2]) + "\n" +
                            "EMI          :" + str(t2[3]) + "\n" +
                            "IR             :" + str(t2[4]) + "\n" +
                            "MAP        :" + str(t2[5]) + "\n" +
                            "CS LAB    :" + str(t2[6]) + "\n" + "VL LAB    :" +
                            str(t2[7]) + "\n" + "COI          :" + str(t2[8]) +
                            "\n" + "CONS      :" + str(t2[9]) + "\n" +
                            "LIB           :" + str(t2[10]) + "\n" +
                            "TOTAL     :" + str(t2[11]) + "%")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('clear_history', clear))
dispatcher.add_handler(CommandHandler('updaters', updaters))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('more', more))
dispatcher.add_handler(CommandHandler('attendance', attendance))
dispatcher.add_handler(CommandHandler('pic', pic))
dispatcher.add_handler(CommandHandler('allattendance', allattendance))
dispatcher.add_handler(CommandHandler('today_attendance', today_attendance))
dispatcher.add_handler(CommandHandler('yesterdays', yesterdays))

t = threading.Thread(target=update_attendance)
t.start()

keep_alive()
#run the bot
updater.start_polling()
updater.idle()
