import telebot
from datetime import datetime

API_TOKEN = '7610827979:AAF8Bx-WSvXFQO4E0bya236puM-KrtO1qME'

bot = telebot.TeleBot(API_TOKEN)

# Command: /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! This is your PV Operations Bot. How can I assist you today?")

# Command: /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """
    Available commands:
    /start - Welcome message
    /help - Display this help message
    /dailyupdate - Submit your daily update
    /leave - Mark yourself as on leave
    /hubstaff - Link your Hubstaff account
    /addtask - Add a new task
    /listtask - List all tasks
    /stats - Display stats
    /feedback - Provide feedback
    /mydetails - Submit your employment information
    /cancel - Cancel the current operation
    """)

# Command: /dailyupdate
@bot.message_handler(commands=['dailyupdate'])
def daily_update(message):
    bot.reply_to(message, "Please submit your daily update:")
    # Expect a follow-up message with the daily update

# Command: /leave
@bot.message_handler(commands=['leave'])
def mark_leave(message):
    bot.reply_to(message, "You are now marked as on leave.")

# Command: /hubstaff
@bot.message_handler(commands=['hubstaff'])
def link_hubstaff(message):
    bot.reply_to(message, "Please follow the steps to link your Hubstaff account.")

# Command: /addtask
@bot.message_handler(commands=['addtask'])
def add_task(message):
    bot.reply_to(message, "Please provide the details for the new task:")

# Command: /listtask
@bot.message_handler(commands=['listtask'])
def list_task(message):
    bot.reply_to(message, "Here are the active tasks:")

# Command: /stats
@bot.message_handler(commands=['stats'])
def show_stats(message):
    bot.reply_to(message, "Here are your current stats:")

# Command: /feedback
@bot.message_handler(commands=['feedback'])
def provide_feedback(message):
    bot.reply_to(message, "Please provide your feedback:")

# Command: /mydetails
@bot.message_handler(commands=['mydetails'])
def submit_details(message):
    bot.reply_to(message, "Please submit your employment details:")

# Command: /cancel
@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.reply_to(message, "The operation has been canceled.")

if __name__ == '__main__':
    print("Bot is running...")
    bot.polling()
