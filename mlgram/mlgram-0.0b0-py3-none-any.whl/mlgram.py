# Assuming function is f(a, b, c=..., *args, **kwargs)

# TODO defaults comprehension
# TODO list and shit comprehension


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import Bot as Bota, ReplyKeyboardRemove, ReplyKeyboardMarkup
import os, stat

# For function analysis

import inspect

def test_func(a, b, c=3, d=4):
    return a * b + c

CHOOSING_PARAMETER, ENTERING_VALUE, EXECUTING = range(3)

class Bot:
    def __init__(self, token, path='user_ids.txt'):
        self.token = token
        self.variable = 0
        
        self.path = path

        # ID list initializing

        try:
            with open(path) as f:
                self.id_list = [ line.strip() for line in f ]
        except FileNotFoundError:
            f = open(path, 'w')
            f.close()

        # Hiding ID file
        
        if os.name == 'nt':
            os.system("attrib +H " + path)
        else:
            st = os.stat(path)
            os.chflags(path, st.st_flags ^ stat.UF_HIDDEN)

    def start(self):

        self.bot = Bota(token=self.token)

        self.updater = Updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        
        self.dispatcher.add_handler(CommandHandler('start', self.start_msg))
        self.dispatcher.add_handler(CommandHandler('register', self.register))

        self.updater.start_polling()

        #self.updater.idle() # IDK yet what is this yet it does not let functions after bot.send to be used. #TODO fix this somehow
    
    def stop(self):
        self.updater.stop()

    def start_msg(self, update, context):
        update.message.reply_text(update.message.from_user.id)

    def parameter_keyboard(self):

        reply_keyboard = []

        for x, y in zip(self.parameters_list[::2], self.parameters_list[1::2]):
            reply_keyboard.append([x, y])

        if len(self.parameters_list) % 2 == 1:
            reply_keyboard.append([self.parameters_list[-1]])

        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

        return markup



    # Send commands
    
    def send_all(self, message):
        try:
            self.id_list

            for user_id in self.id_list:
                self.bot.sendMessage(chat_id=user_id, text=message)

        except AttributeError:
            print('There are no users yet')

    def send_privately(self, message, users, reply_keyboard=None):
        try:
            for _ in users:
                break
        except TypeError:
            users = (users, )

        for user_id in users:
            self.bot.sendMessage(chat_id=user_id, text=message, reply_markup=reply_keyboard)

    # Ways to add users

    def add_user(self, user_id):
        try:
            self.id_list
        except AttributeError:
            self.id_list = []
        if str(user_id) not in self.id_list:
            self.id_list.append(user_id)

            if os.stat(self.path).st_size == 0:
                with open(self.path, 'a') as f:
                    f.write(str(user_id))
            else:
                with open(self.path, 'a') as f:
                    f.write('\n' + str(user_id))

    def register(self, update, context):

        new_user_id = update.message.from_user.id

        self.add_user(new_user_id)
        message = 'User {} has been successfully registered in the network.'.format(new_user_id)

        self.send_all(message)

    # Function comprehending

    def ask_parameters(self, update, context, function, users):
        
        markup = self.parameter_keyboard()

        self.send_privately('Choose one of the parameters', users=users, reply_keyboard=markup)
        return CHOOSING_PARAMETER

    def choice(self, update, context, users):

        if self.analysis_flag:
            for key in self.defaults:
                context.user_data[key] = self.defaults[key]


        text = update.message.text
        context.user_data['choice'] = text

        self.send_privately(
            'Parameter \'{}\' is chosen. Please enter the value for it.'.format(context.user_data['choice']), users=users
        )

        return ENTERING_VALUE

    def memorize(self, update, context, users):

        user_data = context.user_data
        text = update.message.text

        parameter_name = user_data['choice']

        if parameter_name not in user_data:
            self.nof_unassigned -= 1

        user_data[parameter_name] = text
        del user_data['choice']

        if self.nof_unassigned != 0:

            if len(user_data) == 1:
                msg = 'Value for parameter ' + ', '.join('\'' + str(x) + '\'' for x in user_data) + ' is now registered. Please enter ones which remain.'
            else:
                msg = 'Values for parameters ' + ', '.join('\'' + str(x) + '\'' for x in user_data) + ' are now registered. Please enter ones which remain.'

            msg += '\nCurrent parameters are:'
            for x in context.user_data:
                msg += ('\n' + str(x) + ': ' + str(context.user_data[x]))

            markup = self.parameter_keyboard()

            self.send_privately(msg, users=users, reply_keyboard=markup)

            return CHOOSING_PARAMETER
        else:
            msg = 'All parameters are now registered, would you like to execute?\nCurrent parameters are:'

            for x in context.user_data:
                msg += ('\n' + str(x) + ': ' + str(context.user_data[x]))

            reply_keyboard = [
                ['Yes'],
                ['No']
            ]
            markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

            self.send_privately(msg, users=users, reply_keyboard=markup)
            return EXECUTING

    def regect(self, update, context, users):
        msg = 'Choose the parameter you would like to modify.'

        markup = self.parameter_keyboard()

        self.send_privately(msg, users=users, reply_keyboard=markup)

        return CHOOSING_PARAMETER

    def execute(self, update, context, function, users):
        user_data = context.user_data

        parameters = ', '.join(str(x) + '=' + str(user_data[x]) for x in user_data)

        self.send_privately('The function ' + function.__name__ + ' is now processing.', users=users, reply_keyboard=ReplyKeyboardRemove())

        self.result = eval('function(' + parameters + ')')

        self.ready = True

        return ConversationHandler.END

    def call(self, function, users):

        # TODO User is still able to access the function typing 'yes' once the execution stage is done. 

        ## Function analysis phase

        signature = inspect.signature(function)
        self.analysis_flag = True

        self.defaults = {
            k: v.default
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }

        self.parameters_list = list(inspect.signature(function).parameters.keys())
        self.nof_unassigned = len(self.parameters_list) - len(self.defaults)
        self.parameters_filter = '^(' + '|'.join(str(x) for x in self.parameters_list) + ')$'

        ## Call phase

        self.ready = False

        msg = 'Function {} with parameters {} has been called and requires your parameters. Would you like to enter them?'.format(function.__name__, self.parameters_list)

        if len(self.defaults) != 0:
            msg += '\nThe defaults are:'
            
            for key in self.defaults:
                msg += '\n' + str(key) + ': ' + str(self.defaults[key])

        reply_keyboard = [
            ['Yes'],
            ['No']
        ]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

        self.send_privately(msg, users=users, reply_keyboard=markup)

        conv_handler = ConversationHandler(
            entry_points=[MessageHandler(
                        Filters.regex('^(Yes|yes)$'), lambda update, context: self.ask_parameters(update, context, function, users)
                    )],
            states={
                CHOOSING_PARAMETER: [
                    # User chooses the parameter they want to modify
                    MessageHandler(
                        Filters.regex(self.parameters_filter), lambda update, context: self.choice(update, context, users)
                    )
                ],
                ENTERING_VALUE: [
                    # User enters the value for the chosen parameter
                    MessageHandler(
                        Filters.text & ~(Filters.command | Filters.regex('^a$')), lambda update, context: self.memorize(update, context, users)
                    )
                ],
                # TODO: Handler shall die once the execution is finished.
                EXECUTING: [
                    MessageHandler(
                        Filters.regex('^(Yes|yes)$'), lambda update, context: self.execute(update, context, function, users)
                    ),
                    MessageHandler(
                        Filters.regex('^(No|no)$'), lambda update, context: self.regect(update, context, users)
                    ),
                    MessageHandler(
                        Filters.text & ~(Filters.regex('^(Yes|yes)') | Filters.regex('^(No|no)$')), lambda update, context: EXECUTING
                    )
                ]
            },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), lambda update, context: ConversationHandler.END)],
        )
        
        self.dispatcher.add_handler(conv_handler)