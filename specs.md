We can divide some specs in:

### Table of content
<!-- TOC -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
- [1] State
- [2] Shooter
- [3] Samples
- [4] Leader section
- [5] Leaderless section
- [6] Samples (Snowball - epidemic samples)
- [7] Gossip
- [8] Hybrids 

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- /TOC -->
Introduction:
We include basics specifications of maya.

Hint: the inmutability of the leader (shooter - beacon) in the center of the matrix
and the edges - execute the n samples in a sort random to get shard-samplers leaderless
the attestation of the shard give the leader election of the leader 
**posible needs more states than cristallized 

Specs of others blockchains:
Zilliqa -- can support 24 shards at max.
Avalanche -- can support 1 sample and only leaderless
Elrond --- 
Solana --
Ethereum --- *Hint: any pool of any shard could be any attestation of the leader state( a kind of hibryd beacon with sa shooter)
**threshold always: if (numNodesForSharding < shardSizeValues[0]) ?
###  Slasher? of samplers
```python
def Slash_of_samples(state, shooter) -> None:
    
    


```
### Slasher of validator 

```python
def Slasher() 
```
### Shooter of samples (in the edges?)
```python
def Shooter_of_samples(state, sample1, sample2, sample3) -> None:
   
```


### snowball 
```python
class snowball
```


### sample of election of leader 
```python
def election_of_leader(state, sample_of_election) -> None:

 # election of leader based in the number of number of samples that shoter?
```

### Fork choice rule of shooter?  to avoid bizantine fault 
```python
def fork_choice_shooter():

```
### 


### Another Epidemic Sample 
```python
def AnotherSample() -> None: 

```




### Validator 
```
def Validator() {
    // A duty approach

    Attestation_sample

    // A Store approach 

    sign_block() 

    sign_attestation_sample() 


    }
```
