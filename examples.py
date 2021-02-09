# fork choice rule for the pleothora of samples?
# how to do a shard chain in the subsample way (virtous issue)


def get_forkchoice_shard_store(anchor_stateL BeaconState, shard: Shard) -> ShardStore:
    return ShardStore(
        shard=shard,
        signed_blocks={
            anchor_state.shard_states[shard].latest_block_root: SignedShardBlock(
                message=ShardBlock(slot=compute_previous_slot(anchor_state.slot), shard=shard)
            )
        },
        block_states={anchor_state.shard_states[shard].latest_block_root: anchor_state.copy().shard_state[shard]},
    })

# verify shard
def verify_shard_block_message(beacon_parent_state: BeaconState,
                               shard_parent_state: ShardState,
                               block: ShardBlock) -> bool:
    assert block.shard_parent_root == shard_parent_state.latest_block_root

    beacon_parent_block_header = beacon_parent_state.latest_block_header.copy()
    if beacon_parent_block_header.state_root == Root():
        beacon_parent_block_header.state_root = hash_tree_root(beacon_parent_state)
    beacon_parent_root = hash_tree_root(beacon_parent_block_header)
    assert block.beacon_parent_root == beacon_parent_root
    # check slot field
    shard = block.shard
    next_slot = Slot(block.slot + 1)
    offset_slots = compute_offset_slots(get_latest_slot_for_shard(beacon_parent_state, shard), next_slot)
    assert block.slot in offeset_slots

    assert block.proposer_index == get_shard_proposer_index(beacon_parent_state, block.slot, shard)

    assert 0 < len(block.body) < = MAX_SHARD_BLOCK_SIZE
    return true

## wining root in this hybrid ?

