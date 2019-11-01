
import logging, sys, os
import matplotlib.pyplot as plt
import numpy as np
import heapq
import webbrowser
import web3
import json
import binascii
import pymysql.cursors

from web3 import Web3
from web3.contract import ConciseContract
from datetime import datetime
from matplotlib.widgets import Button

contract_json_name = 'contract_abi.json'

transfer_method_code = '0xa9059cbb'

#eth_host = "http://10.10.1.224:8545"
eth_host = "http://localhost:9545"

db_host = 'iotexdbdev2.cs4r6igeqju2.us-east-1.rds.amazonaws.com'
db_username = 'iotexadmin'
db_password = '6y3vPj4Sa6wAU'
db_name = 'eth'
db_port = 3306

contract_address = Web3.toChecksumAddress('0x6fb3e0a217407efff7ca062d46c26e5d60a14d69'.lower()) 
'''
walletsMonitored = [('PreAngel-1', '0x541E01962BD98EDcDC6cc11D85B052387C5DfCbC'),
						('PreAngel-2', '0x7EC6860e6C958CF3ca6e7176ae7082eA8F1E77C9'),
						('Thomas', '0x0c8e046870419A18ccBF90F49D44F73854420BC1'),
						('Victor Ye', '0x2aD8Aa4764700a0D17C3216DA1bd7B14eEF6d78A'),
						('8dCapital/yubo', '0x0049FAB7f5dD1F26F057BD5d972Ffc6ba3c349Dd'),
						('AlphaCoin', '0x350b6697d15CABE9A5117644aEDBD17e39Cf6aCe'),
						('Andrew(Danhua)', '0xdEc4d6b0ecf973f3f2D7B71D3ae1131B7669347F'),
						('ASBV', '0x85Ac9E682995ebeBDE8fF107fbBbfe7C40992E4A'),
						('Bay Lynx Capital Limited', '0x5102D0A855Bf5F0e72c06B311516c53e8e6D638A'),
						('BitsAngle', '0x4f48BB47B52737a2A7fef9D634706deeE38B178c'),
						('Block0', '0x8e36DD825390f40EF8bec7a722BFcECF7E05086b'),
						('Blockchange', '0xD8F150fEB4983f36Ab7bf83F0829c94A00471c1E'),
						('BlockSauce', '0x0079FE344F3fDec28956B39c8bbF5b5C31b926Bd'),
						('BlockVC', '0x839E60C3e6bcF714B00720746E9bBF9a3148a3ad'),
						('Bril Wang', '0x8b2eb4124c743314885509e79111BFE72E24F036'),
						('Bril Wang (I)', '0xdEdc3BBb6BA7da62C4114698eFEC9B7FEDe994EB'),
						('CEX', '0x5d09f2aaffe61c16985f7b5e96f35d764ea1929c'),
						('ceyuan', '0xE41Ac1289d1fcCCAF7Fb71D75e9b445fC881b645'),
						('Chance/Coefficient Group Holding Limited', '0xE8eA41F87Bbd365a3ec766e35ac4aC1d6A5E760a'),
						('Cherry', '0x00fe848d55d0a8bf20f876c9e2a4e7b8e2e5bcad'),
						('DFund', '0x27aB16A2fBA9F2f12bF1874bFbcD73f26267f9bB'),
						('DHVC', '0xe49EA0019414503ED62AE7647Fd6358944581Fa0'),
						('Distributed Global-1', '0x7f8df6723d41cad47866ac19717977947b873007'),
						('Distributed Global-2', '0x9E69Fae35b0FfcE1A5DfFF03154255A04433A00B'),
						('Distributed Global-3', '0xbF8d5Fc826792095bdED0633b7BD50196eC5BfaB'),
						('GBIC', '0x8A5e6837eDC4a17d2AC9873393c413af846E1055'),
						('Genesis Block', '0x609c4C3b56586444cbfc28CC01cfE828716EbC09'),
						('Hashed', '0xd6a2F7f94fDB83175FAb29d4976Bedf7C639ce47'),
						('Hofan', '0x653fBA50804DdA3aBF7B2189d70353A08e0fCF83'),
						('Hofan', '0xa7b5400973EE73d360F4aDC88a011D7Be388FD64'),
						('INB', '0x56270dedB43304783437D89902cC49cf2faEc736'),
						('Jack Lee', '0x2746c89457A11636CD0aadB0ba9DA48837eB3a83'),
						('Kenetic Capital', '0xE5C7716f9C508d008Ac2AFbED03E44Aaa6268331'),
						('LanHu', '0x8bbcA007D6743d8Bf260725049a95D805F4415ce'),
						('Larry', '0xf1C4cA28eC336af2Bd6542d87D1206b9d18682a9'),
						('Liaoliao', '0x412b364983Ef38e263a187EC4497592Ed047FA0e'),
						('LinkVC/OKEX', '0x906692908239030F5F1d348C03b6fC6081843F47'),
						('Mainnet Test', '0x4F20318DD98059D314874974737a99C102712176'),
						('Neo', '0xeef5A1F6cEd7E72d0c52f342fa1cB6e8cC5fd9A9'),
						('Node Capital', '0x1D3Ad91A2D7353D11cC981660225e3bB2F3542Fa'),
						('RedNova -Chi Fintech Global Limited', '0x1254F8522d55Eb1E687D5Bf1aAa6525bACf20A19'),
						('RedNova -Du Capital', '0x59F1a8893dA75E5041C946B08474DD3f5FF08815'),
						('Richard Wang (Draper)', '0x411fB4D77EDc659e9838C21be72f55CC304C0cB8'),
						('Roderik', '0xea09e2bca0550f731f500b566b2efba98158e370'),
						('Signal-1', '0xba0490B8f8960D966437705a26a101f913E6271B'),
						('Signal-2', '0xFa020e47c3621101B2CB7007BA1A0A56BecF4F88'),
						('Spark Land Venture Capital Fund LP', '0x1d689B042c99dA79256A1BA8Aff3172123c8Cd8b'),
						('Sparkland Crypto Fund', '0xe7eb7E7E6da4a68cBC0aE21ddD7E85314De2f7a7'),
						('Struck/Divergence Digital Currency LP', '0x46aBbc9fc9d8E749746B00865BC2Cf7C4d85C837'),
						('UBI', '0xAF8c006965bEC0C4a725DC32F586BDe34e72A60b'),
						('WanCoin', '0x3F19646E7D8069C5e75392cC0e27d44421789afc'),
						('Xiahong Lin', '0x3078F22015436d621062f7CC8334774EB5685E97'),
						('Zahi/Basel', '0xaFADCF85e0F39247840273f0c25D4C8B063d5750'),
						('ZH Capital-1', '0x2990968B2f60fB5116544850FC7C730638Ad7827'),
						('ZH Capital-2', '0x0DcF3748C085467eBc676e37611CC3332825FEFd'),
						('Zhang Fan', '0x708EFDF15cb02D7F4d694B379AcA160E9AdF0CE7'),
						('ZhenZhen', '0xb80E5158f894a11644cfc8CB34Ef6EA0259dF61A'),
						('ZMT Capital', '0xF4AF533C14d8C68AA2D5375526ec79876F9aDE98')
						]

walletsMonitoredDict = {v.lower(): k for (k,v) in walletsMonitored}
'''
'''
# skip for now. class will be available in js version.
class Cache:
	def __init__():
'''

class Transfer:
	def __init__(self, txhash, blockno, unixts, datetime, toAddr, fromAddr, quantity):
		self.txhash = txhash
		self.blockno = blockno
		self.unixts = unixts
		self.datetime = datetime
		self.fromAddr = fromAddr
		self.toAddr = toAddr
		self.quantity = float(quantity)

class User:
	def __init__(self, address, name, db, transfer={'in':[], 'out':[]}):
		self.address = address.lower()
		self.name = name
		self.transfer = transfer
		self.circle = Circle(address=address.lower(), db=db)
		self.updateBalance()
		self.db = db

	def getAddress(self):
		return self.address

	def getName(self):
		return self.name if self.name != '' else self.address[0:9] + '..'
		
	'''
	def setAddress(self, address):
		# check validity
		self.address = address.lower()
	'''
	
	def getCircle(self):
		return self.circle

	def getBalance(self):
		return self.balance

	def updateBalance(self):
		# TODO: Change to call api!!! Did not collect all transactions!!
		self.balance = sum([i.quantity for i in self.transfer['in']]) - sum([o.quantity for o in self.transfer['out']])

	# number of incoming transfers
	def getInNumber(self):
		return len(self.transfer['in'])

	# number of outgoing transfers
	def getOutNumber(self):
		return len(self.transfer['out'])

	def getTotalTransferNumber(self):
		return self.getInNumber() + self.getOutNumber()

	# outgoing
	def getTransfersOut(self):
		return self.transfer['out']
	
	# incoming
	def getTransfersIn(self):
		return self.transfer['in']

	def getTransfersToUserAddress(self, userAddr):
		return [t for t in self.transfer['out'] if t.toAddr.lower() == userAddr.lower()]

	def getTransfersFromUserAddress(self, userAddr):
		return [t for t in self.transfer['in'] if t.fromAddr.lower() == userAddr.lower()]

	def getTransfersToUser(self, user):
		return [t for t in self.transfer['out'] if t.toAddr.lower() == user.getAddress()]

	def getTransfersFromUser(self, user):
		return [t for t in self.transfer['in'] if t.fromAddr.lower() == user.getAddress()]

	# positive means receiving, negative means giving out
	def getTotalTransferQuantityBetween(self, userAddr):
		return sum([t.quantity for t in self.getTransfersFromUserAddress(userAddr)]) - sum([t.quantity for t in self.getTransfersToUserAddress(userAddr)])

	# incoming transfer amount
	def getTotalIn(self):
		return sum([t.quantity for t in self.transfer['in']])

	# outgoing transfer amount
	def getTotalOut(self):
		return sum([t.quantity for t in self.transfer['out']])

	# transfer out
	def addTransferTo(self, transfer):
		if type(transfer) is not Transfer:
			raise Exception("type of 'transfer' is wrong")
		if transfer not in self.transfer['out']:
			self.transfer['out'].append(transfer)
			self.balance -= transfer.quantity
			return True
		return False
	
	# transfer in
	def addTransferFrom(self, transfer):
		if type(transfer) is not Transfer:
			raise Exception("type of 'transfer' is wrong")
		if transfer not in self.transfer['in']:
			self.transfer['in'].append(transfer)
			self.balance += transfer.quantity
			return True
		return False


class Circle:
	def __init__(self, db, address):
		self.db = db
		self.conn = db.conn
		self.circle = set([])
		self.address = address

	def getOutgoing(self):
		curlist = self.db.getTransferRecordsFromAddr(self.address)
		og = []
		# TODO: get first 15 sorted by balance
		for data in curlist[:15]:
			og.append({
				'address': data['address'],
				'inAmount': data['transferIn'],
				'inNum': data['transferInNum'],
				'outAmount': data['transferOut'],
				'outNum': data['transferOutNum'],
				'name': self.db.getUserName(data['address']),
				'balance': data['balance'],
			})
		return og
	
	def getIncoming(self):
		curlist = self.db.getTransferRecordsToAddr(self.address)
		ic = []
		# TODO: get first 15 sorted by balance
		for data in curlist[:15]:
			ic.append({
				'address': data['address'],
				'inAmount': data['transferIn'],
				'inNum': data['transferInNum'],
				'outAmount': data['transferOut'],
				'outNum': data['transferOutNum'],
				'name': self.db.getUserName(data['address']),
				'balance': data['balance'],
			})
		return ic
	
	# incoming + outgoing combined is called circle
	def getCircle(self):
		curlist = self.db.getCircle(self.address)
		c = []
		for data in curlist[:20]:
			c.append({
				'address': data['address'],
				'inAmount': data['transferIn'],
				'inNum': data['transferInNum'],
				'outAmount': data['transferOut'],
				'outNum': data['transferOutNum'],
				'name': self.db.getUserName(data['address']),
				'balance': data['balance'],
			})
		return c

class DB():
	def __init__(self):
		print('Connection initiated.')

	def __enter__(self):
		self.conn = pymysql.connect(
			host=db_host,
            user=db_username,
            passwd=db_password,
            db=db_name,
			port=db_port,
			cursorclass=pymysql.cursors.DictCursor,
		)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.conn.close()

	def getUserName(self, address):
		qry = 'SELECT * from monitored where lower(address) = %s'
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			name = cur.fetchone()
			if name:
				return name['holder']
			else:
				return address[:10]

	# TODO: change implementation!!!
	def getUserBalance(self, address):
		qry = 'SELECT quantity from transfers where lower(fromAddr) = %s'
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			neg = sum([float(i['quantity']) for i in cur])
		
		qry = 'SELECT quantity from transfers where lower(toAddr) = %s'
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			pos = sum([float(i['quantity']) for i in cur])
			
		return pos - neg

	def getUserTransOut(self, address):
		qry = 'SELECT * from transfers where lower(fromAddr) = %s'
		transOut = []
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			for t in cur:
				transOut.append(
					Transfer(txhash=t['txhash'], blockno=t['blockno'],
					unixts=t['unixts'], datetime=t['datetime'], toAddr=t['toAddr'],
					fromAddr=t['fromAddr'], quantity=t['quantity']))
		return transOut

	# user Transfer-in records
	def getUserTransIn(self, address):
		qry = 'SELECT * from transfers where lower(toAddr) = %s'
		transIn = []
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			for t in cur:
				transIn.append(
					Transfer(txhash=t['txhash'], blockno=t['blockno'],
					unixts=t['unixts'], datetime=t['datetime'], toAddr=t['toAddr'],
					fromAddr=t['fromAddr'], quantity=t['quantity']))
		return transIn

	def getTransferRecordsFromAddr(self, address):
		qry = 'SELECT `address`, `transferInNum`, `transferIn`, `transferOutNum`, `transferOut`, (transferIn - transferOut) as balance from balance WHERE `address` IN ( SELECT DISTINCT `toAddr` from transfers WHERE `fromAddr` = %s );'
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			return [c for c in cur]

	def getTransferRecordsToAddr(self, address):
		qry = 'SELECT `address`, `transferInNum`, `transferIn`, `transferOutNum`, `transferOut`, (transferIn - transferOut) as balance from balance WHERE `address` IN ( SELECT DISTINCT `fromAddr` from transfers WHERE `toAddr` = %s );'
		with self.conn.cursor() as cur:
			cur.execute(qry, address)
			return [c for c in cur]

	def getCircle(self, address):
		qry = 'SELECT `address`, `transferInNum`, `transferIn`, `transferOutNum`, `transferOut`, (transferIn - transferOut) as balance from balance WHERE `address` IN ( SELECT DISTINCT `toAddr` from transfers WHERE `fromAddr` = %s ) UNION SELECT `address`, `transferInNum`, `transferIn`, `transferOutNum`, `transferOut`, (transferIn - transferOut) as balance from balance WHERE `address` IN ( SELECT DISTINCT `fromAddr` from transfers WHERE `toAddr` = %s );'
		with self.conn.cursor() as cur:
			cur.execute(qry, [address, address])
			return [c for c in cur]

class TransferDV:

	class Canvas(object):
		def __init__(self, tdv, addr):
			self.addr = addr	
			self.tdv = tdv
		
		def plot(self, event):
			self.tdv.plotOne(self.addr)
		'''
		def gotoCold(self, event):
			cold(self.users, self.transfers)

		def gotoTop19(self, event):
			top19(self.users)
		'''
		def gotoMonitored(self, event):
			self.tdv.plotMonitored()

	def __init__(self, uc):
		self.uc = uc
		self.start()

	def start(self):
		#ax1 = plt.axes([0.15, 0.6, 0.2, 0.1])
		ax2 = plt.axes([0.4, 0.6, 0.2, 0.1])
		#ax3 = plt.axes([0.65, 0.6, 0.2, 0.1])
		#btn1 = Button(ax1, 'Top 19')
		btn2 = Button(ax2, 'Monitored')
		#btn3 = Button(ax3, 'Exchange')
		#btn1.on_clicked(Canvas(None, users, transfers).gotoTop19)
		btn2.on_clicked(self.Canvas(self, None).gotoMonitored)
		#btn3.on_clicked(Canvas(None, users, transfers).gotoCold)
		plt.show()

	def rotate(self, theta, x, y, rate):
			c, s = np.cos(theta), np.sin(theta)
			R = np.array(((c,-s), (s, c)))
			# TODO: should be good but check this dot product later
			return np.dot(R, np.array([rate * x, rate * y]))

	# draw lines
	def connectPoints(self, centerUser, posx, posy, circleBasics):
		for i in range(0, len(posx)):
			user = circleBasics[i]
			transferQuantity = centerUser.getTotalTransferQuantityBetween(user['address'])
			textColor = 'green' if transferQuantity >= 0 else 'red'
			plt.plot([0, posx[i]], [0, posy[i]],'-', color=textColor, alpha=0.7, linewidth=2)
			plt.annotate('B: {}\nA: {}\nIn: {} (t: {})\nOut: {} (t: {})'.format(user['balance'], user['name'], user['inAmount'], user['inNum'], user['outAmount'], user['outNum']), xy=(posx[i],posy[i]), xytext=(0,0), textcoords="offset points",
						bbox=dict(boxstyle="round", fc="w"), zorder=30, size=9)
			plt.annotate('{}'.format(transferQuantity), xy=(posx[i]/2.0,posy[i]/2.0), xytext=(0,0), textcoords="offset points",
						bbox=dict(boxstyle="round", fc="w"), zorder=30, size=9, color=textColor)

	def plotByAddress(self, addr):
		user = self.uc.getUser(addr)
		if not user:
			return None, None
		circleBasics = user.getCircle().getCircle()
		coordinates = (self.rotate(i*np.pi*2/len(circleBasics), 30, 30, 1) for i in range(0, len(circleBasics)))
		posx = [0]
		posy = [0]
		for i in coordinates:
			posx.append(i[0])
			posy.append(i[1])
		colors = ['orange']+['blue']*(len(posx)-1)
		
		sc = plt.scatter(posx,posy,c=colors,s=2000,alpha=0.7,zorder=20)
		plt.axis('off')
		annot = plt.annotate('B: {}\nA: {}\nIn: {} (t: {})\nOut: {} (t: {})'.format(user.getBalance(), user.getName()[0:8], user.getTotalIn(), user.getInNumber(), user.getTotalOut(), user.getOutNumber()),xy=(0,0),xytext=(0,0),textcoords="offset points",
						bbox=dict(boxstyle="round", fc="w"),zorder=30,size=9)
		self.connectPoints(user, posx[1:], posy[1:], circleBasics)

		# TODO: this button not working
		class Web(object):
			def __init__(self, url):
				self.url = url

			def openWeb(self, event):
				print('It works!')
				webbrowser.open('https://etherscan.io/tokentxns%sa={}'.format(self.url))

		axbox = plt.axes([0.3, 0.03, 0.5, 0.065])
		text_box = Button(axbox, 'Eth: {}'.format(addr))
		text_box.on_clicked(Web(addr).openWeb)
		return sc, circleBasics

	def plotOne(self, addr):
		global sc, circleBasics
		fig, ax = plt.subplots()
		#ax.set_axis_off()
		sc, circleBasics = self.plotByAddress(addr)
		if not sc:
			return

		def onclick(event):
			global sc, circleBasics
			#print(event.inaxes)
			#print(ax)
			cont, ind = sc.contains(event)
			if cont:
				if ind["ind"][0] == 0:
					return
				else:
					fig.clear()
					ax.clear()
					sc, circleBasics = self.plotByAddress(circleBasics[ind["ind"][0] - 1]['address'])
					fig.canvas.draw()
						
		cid = fig.canvas.mpl_connect('button_press_event', onclick)
		plt.show()

	'''
	def top19(users):
		fig, ax = plt.subplots()
		plt.axis('off')
		top = users.getTopN(19)
		axes = [plt.axes([0.05+0.45*(i%2), 0.9-0.1*(i/2), 0.35, 0.075]) for i in range(19)]
		btns = [Button(axes[i], top[i].getName()) for i in range(19)]
		for i in range(19):
			btns[i].on_clicked(Canvas(top[i].getAddress(), users, None).plot)
		plt.show()
	'''
	def plotMonitored(self):
		monitored = self.uc.getMonitored()
		fig, ax = plt.subplots()
		plt.axis('off')
		axes = [plt.axes([0.05+0.17*(i%5), 0.92-0.1*(i/5), 0.16, 0.07]) for i in range(len(monitored))]
		btns = [Button(axes[i], list(monitored.values())[i]) for i in range(len(monitored))]
		for i in range(len(monitored)):
			btns[i].on_clicked(self.Canvas(self, list(monitored)[i]).plot)
		plt.show()
	'''
	def cold(users, transfers):
		fig, ax = plt.subplots()
		plt.axis('off')
		coldAddrs = getFirstLevelToColdWallets(transfers)
		#print(len(coldAddrs))
		coldUsersWithBalances = sorted([users.getUserByAddress(addr) for addr in coldAddrs], key=lambda x: x.getBalance(), reverse=True)[:28]
		#coldUsers = [users.getUserByAddress(addr) for addr in coldAddrs]
		axes = [plt.axes([0.05+0.3*(i%3), 0.9-0.1*(i/3), 0.29, 0.075]) for i in range(len(coldUsersWithBalances))]
		btns = [Button(axes[i], coldUsersWithBalances[i].getName()) for i in range(len(coldUsersWithBalances))]
		for i in range(len(coldUsersWithBalances)):
			btns[i].on_clicked(Canvas(coldUsersWithBalances[i].getAddress(), users, transfers).plot)
		plt.show()
	'''
	






class UserContainer:
	def __init__(self, db):
		self.db = db
		self.conn = db.conn

	'''
	def getUserList(self):
		return list(self.userdict.values())

	def getBalanceList(self):
		return [u.getBalance() for u in list(self.userdict.values())]

	def getAddresses(self):
		return [u.getAddress() for u in list(self.userdict.values())]

	def getUserByAddress(self, addr):
		if addr.lower() in self.userdict:
			return self.userdict[addr.lower()]
		else:
			print('no such user {} in data'.format(addr))
			# raise Exception('no such user in data')
	'''

	def hasUser(self, addr):
		addr = addr.lower()
		qry = 'SELECT * from users where lower(address) = %s'
		with self.conn.cursor() as cur:
			cur.execute(qry, addr)
			for o in cur:
				return True
		return False
	'''
	def hasUserAddress(self, userAddr):
		return userAddr.lower() in self.userdict
	'''

	def getUserNumber(self):
		qry = 'SELECT COUNT(*) FROM users'
		with self.conn.cursor() as cur:
			cur.execute(qry)
			return cur.fetchone()['COUNT(*)']

	def getTransferNumber(self):
		qry = 'SELECT COUNT(*) FROM transfers'
		with self.conn.cursor() as cur:
			cur.execute(qry)
			return cur.fetchone()['COUNT(*)']

	def getUser(self, address):
		address = address.lower()
		if not self.hasUser(address):
			return None
		#
		name = self.db.getUserName(address)
		transIn = self.db.getUserTransIn(address)
		transOut = self.db.getUserTransOut(address)
		user = User(address=address, name=name, transfer={'in':transIn, 'out':transOut}, db=self.db)
		return user

	def getMonitored(self):
		qry = 'SELECT * from monitored'
		monitored = {}
		with self.conn.cursor() as cur:
			cur.execute(qry)
			for o in cur:
				monitored[o['address'].lower()] = o['holder']
		return monitored

	'''
	def getTopN(self, n):
		return sorted(list(self.userdict.values()), key=lambda u: u.getBalance(), reverse=True)[:n]

	def update(self, transfer):
		if type(transfer) is not Transfer:
			raise Exception("type of 'transfer' is wrong")

		if not self.hasUserAddress(transfer.fromAddr) :
			self.addUserByAddr(transfer.fromAddr)

		if not self.hasUserAddress(transfer.toAddr):
			self.addUserByAddr(transfer.toAddr)
		
		try:
			fromUser = self.getUserByAddress(transfer.fromAddr)
			fromUser.addTransferTo(transfer)
			toUser = self.getUserByAddress(transfer.toAddr)
			toUser.addTransferFrom(transfer)

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno, str(e))
	'''
	# TODO: add remove user method
'''
def updateUsers(users, transfer):
	if type(users) is not Users:
		raise Exception("type of 'users' is wrong")

	if type(transfer) is not Transfer:
		raise Exception("type of 'transfer' is wrong")

	if not users.hasUserAddress(transfer.fromAddr) :
		users.addUserByAddr(transfer.fromAddr)
	
	if not users.hasUserAddress(transfer.toAddr):
		users.addUserByAddr(transfer.toAddr)

	try:
		fromUser = users.getUserByAddress(transfer.fromAddr)
		fromUser.addTransferTo(transfer)
		toUser = users.getUserByAddress(transfer.toAddr)
		toUser.addTransferFrom(transfer)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno, str(e))
'''
def parseTransfer(web3, transaction):
    txhash = '0x' + binascii.hexlify(transaction['hash']).decode('ascii').lower()
    blockno = str(transaction['blockNumber'])
    unixts = '' # TODO
   #getting date time
    block_number = transaction.blockNumber
    datetime = str(web3.eth.getBlock(block_number).timestamp)
    fromAddr = transaction['from'].lower()
    toAddr = '0x' + transaction['input'][34:74].lower()
    quantity = float(web3.fromWei(int(transaction['input'][98:], 16), 'ether')) # convert hex to decimal then wei to ether
    transfer = Transfer(txhash, blockno, unixts, datetime, toAddr, fromAddr, quantity)
    return transfer

def insertDb(transfers, conn):
	for transfer in transfers:
		with conn.cursor() as cur:
			qry = 'INSERT IGNORE INTO transfers (txhash, blockno, datetime, fromAddr, toAddr, quantity) VALUES (%s, %s, %s, %s, %s, %s)'
			cur.execute(qry, [transfer.txhash, transfer.blockno, transfer.datetime, transfer.fromAddr, transfer.toAddr, transfer.quantity])
	conn.commit()
	print('Transfers data done.')

def fetchBlockData(conn, web3, fromBlock, toBlock, contract_address):
	logFilter = web3.eth.filter({'fromBlock': fromBlock, 'toBlock': toBlock, 'address': contract_address})

	transfers = set([])
	print('Fetching data...')
	total = len(logFilter.get_all_entries())
	print('{} new transaction records found from block {} to {}.'.format(total, fromBlock, toBlock))
	for block_hash in logFilter.get_all_entries():
		#print(block_hash)
		transId = '0x' + binascii.hexlify(block_hash['transactionHash']).decode('ascii')
		transaction = web3.eth.getTransaction(transId)
		#print(transaction)
		if transaction['input'][:10] == transfer_method_code:
			transfer = parseTransfer(web3, transaction)
			if transfer not in transfers:
				transfers.add(transfer)
	print('Updating to db...')
	insertDb(transfers, conn)
	return transfers
'''				
def getTransactions(web3, contract_address, abi):
    myContract = web3.eth.contract(address=contract_address, abi=abi)
    # current block as of 2:40PM June 4 5734000
    logFilter = web3.eth.filter({'fromBlock': 5652744, 'toBlock': 5734000, 'address': contract_address})
    transactionIds = []
    transactions = []
    transfers = []
    for block_hash in logFilter.get_all_entries():
        transId = '0x' + binascii.hexlify(block_hash['transactionHash']).decode('ascii')
        transactionIds.append(transId)
        transaction = web3.eth.getTransaction(transId)
        transactions.append(transaction)
        if transaction['input'][:10] == transfer_method_code:
            transfer = parseTransfer(web3, transaction)
            if transfer not in transfers:
                transfers.append(transfer)
                print(transfer.quantity)
    return transfers

def initUsers(transfers=[]):
    users = Users()
    for tf in transfers:
        users.update(tf)
    return users

def parseTransfersFromCsv(filename):
	#logger = logging.getLogger(__name__)
	with open(filename, "r") as f:
		users = Users()
		transfers = []
		f.readline() # skip first line
		for line in f:
			data = [x.replace('"', '') for x in line.split(',')]
			txhash = data[0]
			blockno = data[1]
			unixts = data[2]
			# TODO nonzero padded month date
			# datetime = datetime.strptime(data[3], '%m/%d/%Y %I:%M:%S %p')
			datetime = data[3]
			fromAddr = data[4]
			toAddr = data[5]
			quantity = float(data[6])
			transfer = Transfer(txhash, blockno, unixts, datetime, toAddr, fromAddr, quantity)
			if transfer not in transfers:
				transfers.append(transfer)
			try:
				updateUsers(users, transfer)
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(exc_type, fname, exc_tb.tb_lineno, str(e))
				#logger.error(sys.exc_info())
	return users, transfers

	# identify cold a wallet by its transferring decimal amount
	# TODO: i dont think these are cold wallets. these are transferring out to cold wallets.
def getFirstLevelToColdWallets(transfers):
	return list(set([t.toAddr for t in transfers if not t.quantity.is_integer()]))
'''


def eth_connect():
	web3 = Web3(Web3.HTTPProvider(eth_host))
	with open(contract_json_name, "r") as abi_definition:
		contract_abi = json.load(abi_definition)
	myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
	return web3, myContract, contract_abi
'''
def updateUserBalance(conn, myContract, users):
	for addr in users:
		addr = addr.lower()
		balanceOf = myContract.functions['balanceOf']
		result = myContract.functions.balanceOf(addr).call()
		if result:
			balance = web3.fromWei(result, 'ether') # Change the string to be in Ether not Wei, and show it in the console
			with conn.cursor() as cur:
				qry = 'UPDATE users SET balance = %s where lower(address) = %s'
				cur.execute(qry, [str(balance), addr])
	conn.commit()
'''	

def sync(conn):
	web3, myContract, contract_abi = eth_connect()
	# REACHED 6164985
	# start: 6164985
	# TODO: how to get latest block number
	for i in range(6000000,6164985,1000):
		# TODO: DIDNT CATCH multisendToken!!!!!
		# dig these!
		# e.g. https://etherscan.io/tx/0x4888ce4cc4368c332b6190f91894a016607fcf2468b6ee434ceb5ce43882da76
		# adminWithdraw!
		# e.g. https://etherscan.io/tx/0x990f5483d965c081172b04c7b5974627e1fca1e3c5a0ce9a6e8894365e4a77ef
#contract_address
		transfers = fetchBlockData(conn, web3, i, i + 1000, contract_address)
	#updateUserBalance(conn, myContract, users)


def main():
	#filename = "export-token-0x6fb3e0a217407efff7ca062d46c26e5d60a14d69.csv"
	#users, transfers = parseTransfersFromCsv(filename)
	with DB() as db:
		sync(db.conn)
		#uc = UserContainer(db)
		#tdv = TransferDV(uc)


	#transfers = getTransactions(web3, contract_address, contract_abi)
	#users = initUsers(transfers)
	#fltcw = getFirstLevelToColdWallets(transfers)
	#start(users, transfers)
	#plotOne(users, 'ETH ADDRESS')
	
if __name__ == '__main__':
	main()




'''
def connectOutGoingPoints(posx, posy, users_trans_to):
	for i in range(0, len(posx)):
		user = users_trans_to[i]
		plt.plot([0, posx[i]], [0, posy[i]],'k-', color='red', alpha=0.7, linewidth=2)
		plt.annotate('B: {}\nA: {}\nIn: {}\nOut: {}'.format(user.getBalance(), user.getName()[0:8], user.getTotalIn(), user.getTotalOut()),xy=(posx[i],posy[i]),xytext=(0,0),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),zorder=3,size=6)

def connectIncomingPoints(posx, posy, users_trans_from):
	for i in range(0, len(posx)):
		user = users_trans_from[i]
		plt.plot([0, posx[i]], [0, posy[i]],'k-', color='green', alpha=0.7, linewidth=3)
		plt.annotate('B: {}\nA: {}\nIn: {}\nOut: {}'.format(user.getBalance(), user.getName()[0:8], user.getTotalIn(), user.getTotalOut()),xy=(posx[i],posy[i]),xytext=(0,0),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),zorder=3,size=6)

def plot(users):
	def rotate(theta, x, y, rate):
		c, s = np.cos(theta), np.sin(theta)
		R = np.array(((c,-s), (s, c)))
		# TODO: should be good but check this dot product later
		return np.dot(R, np.array([rate * x, rate * y]))

	coordinates = (rotate(np.radians(np.random.rand()*i), i, i, 1) for i in range(1, 1 + users.getLength()))

	#np.random.seed(19680801)
	
	posx = []
	posy = []
	for i in coordinates:
		posx.append(i[0])
		posy.append(i[1])
	#print(posx)
	balanceList = users.getBalanceList()
	balances = [10 * np.log(i) if i > 0 else 10 * np.log(-i) if i < 0 else 1 for i in balanceList]
	colors = ['blue' if i > 0 else 'r' if i < 0 else 'g' for i in balanceList]
	#print(balances)
	fig, ax = plt.subplots()
	sc = plt.scatter(posx, posy, c=colors, s=balances, alpha=0.5)
	annots = []
	annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
	annot.set_visible(False)

	def connectOutGoingPoints(x, y, users, i):
		addresses = users.getAddresses()
		p1 = i
		for trans in users.getUserList()[i].getTransfersOut():
			toAddr = trans.toAddr
			if toAddr not in addresses:
				return
			p2 = addresses.index(toAddr)
			x1, x2 = x[p1], x[p2]
			y1, y2 = y[p1], y[p2]
			plt.plot([x1,x2], [y1,y2],'k-', color='orange', linewidth=np.log(trans.quantity)/2)
			annots.append(ax.annotate('{}pts,\n from {}'.format(trans.quantity, trans.toAddr),
				xy=((x1 + x2)/2, (y1 + y2)/2),xytext=(20, 20)))

	def connectIncomingPoints(x, y, users, i):
		addresses = users.getAddresses()
		p1 = i
		for trans in users.getUserList()[i].getTransfersIn():
			fromAddr = trans.fromAddr
			if fromAddr not in addresses:
				return
			p2 = addresses.index(fromAddr)
			x1, x2 = x[p1], x[p2]
			y1, y2 = y[p1], y[p2]
			plt.plot([x1,x2], [y1,y2],'k-', color='green', linewidth=np.log(trans.quantity)/2)
			annots.append(ax.annotate('{}pts,\n from {}'.format(trans.quantity, trans.fromAddr), xy=(0, 0),
				xytext=((x1 + x2)/2, (y1 + y2)/2)))
				
	def update_annot(ind):
		pos = sc.get_offsets()[ind["ind"][0]]
		annot.xy = pos
		text = "{},\n {}".format(users.getUserList()[ind["ind"][0]].getBalance(), users.getUserList()[ind["ind"][0]].getAddress())
		annot.set_text(text)
		annot.get_bbox_patch().set_alpha(0.4)

	def hover(event):
		vis = annot.get_visible()
		lines = plt.gca().lines
		if event.inaxes == ax:
			cont, ind = sc.contains(event)
			if cont:
				update_annot(ind)
				connectOutGoingPoints(posx, posy, users, ind["ind"][0])
				connectIncomingPoints(posx, posy, users, ind["ind"][0])
				annot.set_visible(True)
				fig.canvas.draw_idle()
			else:
				if vis:
					annot.set_visible(False)
					for a in annots:
						a.remove()
					annots[:] = []
					fig.canvas.draw_idle()
				if lines:
					for artist in lines:
						artist.remove()

	fig.canvas.mpl_connect("motion_notify_event", hover)
	plt.show()
'''
