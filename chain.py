import datetime as dt
import block.Block as Block

def create_genesis_block():
    return Block(0, dt.datetime.now(), "Genesis block", "0")

def next_block(previous_block):
    this_index = previous_block.index + 1
    this_timestamp = dt.datetime.now()
    this_data = "I'm block index " + str(this_index)
    this_hash = previous_block.hash
    return block.Block(this_index, this_timestamp, this_data, this_hash)
