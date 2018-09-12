#
import itchat

# login wechat
def login():
    itchat.auto_login(hotReload=True)

# gain all friends
def get_all_friends():
    return itchat.get_friends()


def send_msg_bomb():
    print('------------------------------------------------------')
    itchat.send("bomb ------------->>>",toUserName='Onny')

login()
friends = get_all_friends()
itchat.send_msg('bomb')
i=0
for i in range(4):
    send_msg_bomb()
for friend in friends:
    i=i+1
   # print(friend)
   # itchat.send("测试消息，无需理会！！！",toUserName=friend.UserName)
print("count: "+str(len(friends)))
