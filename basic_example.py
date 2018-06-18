import time

#Import crypto lib to generate identities
from bigchaindb_driver.crypto import generate_keypair

# import BigchainDB and create an object
from bigchaindb_driver import BigchainDB
bdb_root_url = 'http://localhost:9985'

#Example without authentication tokens
bdb = BigchainDB(bdb_root_url)

#Asset Definition
bicycle_asset = {
	'data': {
		'bicycle': {
			'serial_number' : '123',
			'manufacturer' : 'mybike'
		}
	}
}

#Metadata definition
bicycle_metadata = {'color' : 'blue'}

#Generate identities
alice, bob = generate_keypair(), generate_keypair()

#Asset creation
asset_creation_tx = bdb.transactions.prepare(
	operation = 'CREATE',

	#asset signed by the owner
	signers = alice.public_key,
	asset = bicycle_asset,
	metadata = bicycle_metadata
)

#Transaction signed by the sender
fulfilled_creation_tx = bdb.transactions.fulfill(
	asset_creation_tx, private_keys = alice.private_key
)

#Send the Tx to the BigchainDB node
sent_creation_tx = bdb.transactions.send_commit(
	fulfilled_creation_tx
)

# CHECK IF SENT
#####################################
#print(sent_creation_tx == fulfilled_creation_tx)

txid = fulfilled_creation_tx['id']

#print(txid)
#block_height = bdb.blocks.get(txid=signed_tx['id'])
#block = bdb.transactions.retrieve(txid)
#####################################

#Asset transfer
#creation_tx = bdb.transactions.retrieve(txid)

#print(creation_tx)
