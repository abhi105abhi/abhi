import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters
from django.core.management import BaseCommand
from django.conf import settings
from django.apps import apps

class Command(BaseCommand):
    help = 'Run Telegram Bot'

    def handle(self, *args, **options):
        bot_token = '<your_bot_token>'
        updater = telegram.Updater(token=bot_token, use_context=True)

        def start(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I am your tutor agency bot. You can type /help to see available commands.')

        def help(update, context):
            commands = [
                '/start - Start the bot',
                '/help - See available commands',
                '/stats - See statistics',
            ]
            text = 'Available commands:\n' + '\n'.join(commands)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

        def stats(update, context):
            lead_count = apps.get_model('tutor_agency', 'Lead').objects.count()
            tutor_count = apps.get_model('tutor_agency', 'Tutor').objects.count()
            text = f'Total leads: {lead_count}\nTotal tutors: {tutor_count}'
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

        def unknown(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Please type /help to see available commands.")

        start_handler = CommandHandler('start', start)
        help_handler = CommandHandler('help', help)
        stats_handler = CommandHandler('stats', stats)
        unknown_handler = MessageHandler(Filters.command, unknown)

        updater.dispatcher.add_handler(start_handler)
        updater.dispatcher.add_handler(help_handler)
        updater.dispatcher.add_handler(stats_handler)
        updater.dispatcher.add_handler(unknown_handler)

        updater.start_polling()
        updater.idle()
if __name__ == '__main__':
    telegram_bot.polling(none_stop=True)
