import block.Block as Block
import chain

# Create the blockchain and the genesis block
blockchain = [chain.create_genesis_block()]
previous_block = blockchain[0]

num_blocks = 20
for i in range(0, num_blocks):
    block_to_add = chain.next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added".format(block_to_add.index))
    print("Hash: {}".format(block_to_add.hash))