package _go

import "sync"

///##### start avalanche paradimg leaderless


// Validator is the minimal description of someone that can be sampled.


type validator interface {
	weights()
}

// validator is a struct that contains the base values required by the validator
// interface.
type validator struct {
	nodeID ids.ShortID
	weight uint64
}

////#######   Start Ethereum paradigm
type validator struct {

	// first idea of to be a validator
	//ticker      slotticker.SlotTicker
	///assignments map[uint64]pb.ValidatorRole

	/// the second way..
	logValidatorBalances               bool
	useWeb                             bool
	emitAccountMetrics                 bool
	domainDataLock                     sync.Mutex
	attLogsLock                        sync.Mutex
	aggregatedSlotCommitteeIDCacheLock sync.Mutex
	prevBalanceLock                    sync.RWMutex
	attesterHistoryByPubKeyLock        sync.RWMutex
	walletInitializedFeed              *event.Feed
	genesisTime                        uint64
	domainDataCache                    *ristretto.Cache
	aggregatedSlotCommitteeIDCache     *lru.Cache
	ticker                             *slotutil.SlotTicker
	attesterHistoryByPubKey            map[[48]byte]*slashpb.AttestationHistory
	prevBalance                        map[[48]byte]uint64
	duties                             *ethpb.DutiesResponse
	startBalances                      map[[48]byte]uint64
	attLogs                            map[[32]byte]*attSubmitted
	node                               ethpb.NodeClient
	keyManagerV2                       v2keymanager.IKeymanager
	beaconClient                       ethpb.BeaconChainClient
	validatorClient                    ethpb.BeaconNodeValidatorClient
	protector                          slashingprotection.Protector
	db                                 vdb.Database
	//graffiti                           []byte
	//voteStats                          voteStats

}
