#!/bin/python
import socket, string, time, random, sys, subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("insomnia247.nl", 5010))
nickname = "AlphaBot"
password = "" # Bot's NickServ password goes here
adminpass = "authpl0x" # Bot's auth password
channels = ["#main"]
public = ["!auth","!ninja","#hashtag","!time","!say","PING","PONG",nickname + "!","XD",nickname + ": you suck"]
log = 1
grant = []
chan1 = ""
chan2 = ""
word1 = ""
word2 = ""
chanset = channels[0]
admins = ["zsoltisawesome","WindHero"]
readbuffer = ""
s.send("USER %s %s %s %s \n" % (nickname, nickname, nickname, nickname))
s.send("NICK %s \n" % nickname)
s.send("PRIVMSG NickServ :IDENTIFY %s \n" % password)
for i in channels:
    s.send("JOIN %s \n" % i)
#########################
class irc(object):
    def join(self, channel):
        s.send("JOIN %s\n" % channel)
    def part(self, channel):
        s.send("PART %s :HEY, Who turned out the lights?\n" % channel)
    def say(self, target, message):
        s.send("PRIVMSG %s : %s\n" % (target, message))
        irc.logger(message)
    def saynick(self, target, message):
        s.send("PRIVMSG %s :" % (target) + nick + ": %s\n" % (message))
        irc.logger(nick + ": %s\n" % (message))
    def notice(self, target, message):
        s.send("NOTICE %s :%s\n" % (target, message))
    def kick(self, nickname, reason=nickname):
        s.send("KICK %s :%s\n" % (nickname, reason))
    def op(self, target, nickname):
        s.send("MODE %s +o %s\n" % (target, nickname))
    def deop(self, target, nickname):
        s.send("MODE %s -o %s\n" % (target, nickname))
    def voice(self, target, nickname):
        s.send("MODE %s +v %s\n" % (target, nickname))
    def devoice(self, target, nickname):
        s.send("MODE %s -v %s\n" % (target, nickname))
    def ban(self, target, nickname):
        s.send("MODE %s +b %s\n" % (target, nickname))
    def unban(self, target, nickname):
        s.send("MODE %s -b %s\n" % (target, nickname))
    def nick(self, newnick):
        s.send("NICK %s\n" % newnick)
    def quit(self):
        s.send("QUIT :HEY, Who turned out the lights?\n")
    def logger(self, loggable):
        print("["+nickname+"]: "+loggable+"\n")
        f = open("log", "a")
        f.write("["+nickname+"]: "+loggable+"\n")
        f.close()
irc = irc()
#########################
while 1:
 try:    
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop()
    rndm = float("0." + str(random.randint(1,99999999999999999)))

    for msg in temp:
        msg=string.rstrip(msg)

    if msg.find('PING') != -1:
        s.send('PONG ' + msg.split() [1] + '\r\n')

    if msg.split(' ')[1] == "PRIVMSG" or msg.split(' ')[1] == "NOTICE":
        message = ' '.join(msg.split(' ')[3:])[1:]
        nick = msg.split('!')[0][1:]
        target = msg.split(' ')[2]
        #print message, nick, target
        if target == nickname:
            target = nick
        split = message.split()
        if len(split) > 0:
            cmd = split[0]
        if log == 1:
            print("[Message from "+target+"]: "+nick+": "+message+"\n")
            f = open("log", "a")
            f.write("[Message from "+target+"]: "+nick+": "+message+"\n")
            f.close()

    #########################
        def gen(number):
            if auth() and wordc(number):
                return True

        def wordc(num):
            if len(split) == num:
                return True

        def auth():
            if nick in admins:
                return True
            if nick+":"+cmd in grant:
                return True
            if cmd in public:
                return True
    #########################
    #    hmm = str(sys.stdin.readlines())
    #    s.send("PRIVMSG "+target+" :"+hmm)
    #########################

        if cmd == "!notice" and len(split) > 1 and auth():
             irc.notice(chanset, " ".join(split[1:]))
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!join" and gen(2):
             irc.join(split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!part" and gen(2):
             irc.part(split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        
        if cmd == "!op" and gen(2):
             irc.op(chanset, split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")
        elif cmd == "!op" and gen(1):
             irc.op(chanset, nick)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!deop" and gen(2):
             irc.deop(chanset, split[1])
             irc.logger(nick+" used the '"+cmd+"' command!")

        elif cmd == "!deop" and gen(1):
             irc.deop(chanset, nick)
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!voice" and gen(2):
            irc.voice(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!devoice" and gen(2):
            irc.devoice(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!ban" and gen(2):
            irc.ban(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")
        if cmd == "!unban" and gen(2):
            irc.unban(chanset, split[1])
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!say" and len(split) > 1 and auth():
             irc.saynick(chanset, " ".join(split[1:]))
             irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!bfg" and gen(1):
            irc.say(chanset, nickname+" fired a big freaking gun at no one in particular...")

        elif cmd == "!bfg" and gen(2):
            irc.say(chanset, split[1]+" was shot with a big freaking gun by "+nickname+".")

        if cmd == "!kick" and auth():
            irc.kick(chanset, split[1])

        if cmd == "!auth" and wordc(2) and split[1] == adminpass:
            admins.append(nick)
            irc.saynick(target, "Congrats! You are now a tempadmin!")
            irc.logger(nick+" used the '"+cmd+"' command!")

        if cmd == "!quit" and gen(1):
            irc.logger(nick+" used the '"+cmd+"' command!")            
            irc.quit()
            time.sleep(5)
            exit()

 except KeyboardInterrupt:
    irc.quit()
    sys.exit()
