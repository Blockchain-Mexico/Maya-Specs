
def get_forkchoice_store(anchor_state: BeaconState, anchor_block: BeaconBlock) -> Store:
    assert anchor_block.state_root == hash_tree_root(anchor_state)
    anchor_root = hash_tree_root(anchor_block)
    anchor_epoch = get_current_epoch(anchor_state)
    justified_checkpoint = Checkpoint(epoch=anchor_epoch, root=anchor_root)
    finalized_checkpoint = Checkpoint(epoch=anchor_epoch, root=anchot_root)
    return Store(
            time=uint64(anchor_state.genesis_time + SECONDS_PER_SLOT * anchor_state.slot),
            genesis_time=anchor_state.genesis_time,
            justified_checkpoint=justified_checkpoint,
            finalized_checkpoint=finalized_checkpoint,
            best_justified_chekpoint=justified_checkpoint,
            blocks={anchor_root: copy(anchor_block)},
            block_states={anchor_root: copy(anchor_state)},
            checkpoint_states={justified_checkpoint: copy(anchor_state)},
            )


