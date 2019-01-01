import appex, ui
import os
import requests
from datetime import datetime

# Put your base58 or xpub address here
address = "xpub6CUGRUonZSQ4TWtTMmzXdrXDtypWKiKrhko4egpiMZbpiaQL2jkwSB1icqYh2cfDfVxdx4df189oLKnC5fSwqPfgyP3hooxujYzAu3fDVmz"

# Request blockchain.com API
response = requests.get("https://blockchain.info/multiaddr?active=" + address)

# Get transaction data
data = response.json() 

final_balance = str( data['wallet']['final_balance']*10**-8 )

txTimeUnix = data['txs'][0]['time']
txTime = datetime.utcfromtimestamp(txTime).strftime('%Y-%m-%d %H:%M:%S')

amount = str( data['txs'][0]['out'][0]['value'] )


# Create text
label = ui.Label(font=('Menlo', 15), alignment=ui.ALIGN_NATURAL)
label.number_of_lines = 0;
label.text = 'Final balance: ' + final_balance + ' btc' + '\n' + 'Last transaction: ' + txTime + '\n' + 'Amount: ' + amount + ' sat'

appex.set_widget_view(label)
