import os
import pyignite
import uuid
from pyignite import Client, GenericObjectMeta
from pyignite.datatypes import *

IGNITE_IP = os.environ['IGNITE_SQL'].split(':')[1][2:]
IGNITE_PORT = int(os.environ['IGNITE_SQL'].split(':')[2])

print("connecting to", IGNITE_IP, IGNITE_PORT)

client = Client()
client.connect(IGNITE_IP, IGNITE_PORT)

PRESENCE_TABLE = '''
CREATE TABLE IF NOT EXISTS presence (
    subkey VARCHAR,
    channel VARCHAR,
    uuid VARCHAR,
    metadata BINARY,
    PRIMARY KEY (subkey, channel, uuid)
)'''

DROP_PRESENCE_TABLE = '''
DROP TABLE IF EXISTS presence
'''

INSERT_PRESENCE_TABLE = '''
INSERT INTO presence(
 subkey, channel, uuid, metadata
    ) VALUES (?, ?, ?, ?)
    '''


args = ["somekey", "somechannel", str(uuid.uuid4()), None]
client.sql(DROP_PRESENCE_TABLE)
client.sql(PRESENCE_TABLE)
client.sql(INSERT_PRESENCE_TABLE,query_args=args)

results = client.sql('select * from presence')

print([result for result in results])
