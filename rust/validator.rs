





pub struct Validator {



    pub Validator_pubkey: PublicKey,

    pub validator_index: Option<u64>,

    pub attestation_sample_slot: Option<SlotSample>,

    pub attestation_committee_position: Option<usize>,

    pub comitte_count_at_slot: Option<u64>,

    pub block_proposal_slots: Option<Vec<Slot>>,


}

// ignoring some proposals slot boolean 
// subcription stuff 
// store approach for the validator 

pub struct ValidatorStore {
    pub fn num_voting_validators() {

    }

    pub fn randao_reveal() {

    }

    pub fn sing_block() {

    }

    pub fn  sign_attestation() {

    }


}
