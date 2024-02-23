from discord import Client, Message
from get_response import get_response

class TTT:
    ' ' 'This is the TextTransformTool class' ' '

    #class variables
    uniqueid: int
    messageid:int
    initiator: str
    target: str
    time: int
    type: str
    client: Client
    content: Message

    def __init__(self, message_id:int, initiator:str, target:str, time:int, type: str, content: Message):
        print(str(content))
        
        self.uniqueid = 0
        self.message_id = message_id
        self.initiator = initiator
        self.target = target
        self.time = time
        self.type = type
        self.content = content

    
        

    def show_console_ticket(self, message: Message, client: Client):
        print(f'#######################################')
        print(f'#       on_message info               #')
        print(f'#######################################')
        print(f'# uniqueid {self.uniqueid}                         #')
        print(f'# message_id {self.message_id}             #')      
        print(f'# initiator {self.initiator}                #')
        print(f'# target {self.target}                     #')
        print(f'# time {self.time}                     #')
        print(f'# type {self.type}                     #')
        print(f'# message.content ::                     #')
    
        print(f'{message.content}')
        print(f'#######################################')
        print(f'#                SELF                 #')
        print(f'| self                                |')
        print(self)
        print(f'#######################################')
        print(f'#                MESSAGE              #')
        print(f'#######################################')
        print(f'| message                             |')
        print(f'|{message}                            |')
        print(f'| message.id                          |')
        print(f'|{message.id}                         |')
        print(f'| message.channel                     |')
        print(f'|{message.channel}                    |')
        print(f'| message.application                 |')
        print(f'|{message.application}                |')
        print(f'| message.content                     |')
        print(f'|{message.content}                    |')
        print(f'| message.components                     |')
        print(f'|{message.components}                    |')
        print(f'|                                     |')
        print(f'|                                     |')
        print(f'#######################################')
        print(f'#                CLIENT               #')
        print(f'#######################################')
        print(f'|  client.get_message(message.id)     |')
        print(f'|{client.get_message(message.id)}     |')
        print(f'|                                     |')
        print(f'|                                     |')
        '''
        print('#######################################')
        print('#                TICKET               #')
        print('#######################################')
        print(f'TICKET #:{self.uniqueid:_^21}')
        print(f'INITIATOR :{self.initiator:_^19}')
        print(f'TARGET :{self.target:_^22}')
        print(f'TIME:{self.time:_^25}')
        print(f'TYPE:          {self.type}')
        print('MESSAGE CONTENT:')
        print(self.content)
        print('NEW MESSAGE:')
        print('get_response(str(message), self.content)')
        print('#######################################')
        print(f'{self.messageid}')
        '''
        #self.increment_uniqueid()

    def deletemessage(self):
        messageid: int = self.message_id
        try:
            message.delete(messageid)
        except Exception as e:
            print(e)

    async def send_message(message: Message, user_message: str) -> None:
        if not user_message:
            print('Message empty, intents not enabled.')
            return
            
        # private check not wprking
        if is_private := user_message[0] == '?':
            user_message = user_message[1:]
        try:

            response: str = get_response(str(user_message)) #NOQA
            await message.author.send(response) if is_private else message.channel.send(response)
        except Exception as e:
            print(e)


    async def show_channel_message(self, message: Message, client: Client):
        if message.author == client.user:
            return

        username: str = str(message.author)
        user_message: str = message.content
        channel : str = str(message.channel)

        await client.send_message(message, user_message)

