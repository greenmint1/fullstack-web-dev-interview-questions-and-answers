# Blockchain Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 blockchain interview questions and answers for full stack web developers: 150 easy, 150 moderate and 150 advanced. Most answers use Ethereum as the main example (after the Fusaka upgrade of December 2025), with Solidity 0.8.x for contracts and ethers.js v6 or viem v2 for JavaScript code. Bitcoin and other chains come up where the difference matters.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a blockchain?](#1-what-is-a-blockchain)
- [2: What problem does a blockchain solve?](#2-what-problem-does-a-blockchain-solve)
- [3: What is a block?](#3-what-is-a-block)
- [4: What is a hash function and why does a blockchain need one?](#4-what-is-a-hash-function-and-why-does-a-blockchain-need-one)
- [5: What is the genesis block?](#5-what-is-the-genesis-block)
- [6: What is a node?](#6-what-is-a-node)
- [7: What is the difference between a full node and a light node?](#7-what-is-the-difference-between-a-full-node-and-a-light-node)
- [8: What is an archive node?](#8-what-is-an-archive-node)
- [9: What does decentralized mean in blockchain?](#9-what-does-decentralized-mean-in-blockchain)
- [10: What is a distributed ledger?](#10-what-is-a-distributed-ledger)
- [11: What does immutable mean for a blockchain?](#11-what-does-immutable-mean-for-a-blockchain)
- [12: What is a transaction?](#12-what-is-a-transaction)
- [13: What is a cryptocurrency?](#13-what-is-a-cryptocurrency)
- [14: What is the difference between a coin and a token?](#14-what-is-the-difference-between-a-coin-and-a-token)
- [15: What is Bitcoin?](#15-what-is-bitcoin)
- [16: What is Ethereum?](#16-what-is-ethereum)
- [17: What is a smart contract?](#17-what-is-a-smart-contract)
- [18: What is Solidity?](#18-what-is-solidity)
- [19: What is the EVM?](#19-what-is-the-evm)
- [20: What is gas?](#20-what-is-gas)
- [21: What are gwei and wei?](#21-what-are-gwei-and-wei)
- [22: What is a wallet?](#22-what-is-a-wallet)
- [23: What is a private key?](#23-what-is-a-private-key)
- [24: What is a public key?](#24-what-is-a-public-key)
- [25: What is a blockchain address?](#25-what-is-a-blockchain-address)
- [26: What is a seed phrase?](#26-what-is-a-seed-phrase)
- [27: What is the difference between a custodial and a non-custodial wallet?](#27-what-is-the-difference-between-a-custodial-and-a-non-custodial-wallet)
- [28: What is a hot wallet versus a cold wallet?](#28-what-is-a-hot-wallet-versus-a-cold-wallet)
- [29: What is a consensus mechanism?](#29-what-is-a-consensus-mechanism)
- [30: What is proof of work?](#30-what-is-proof-of-work)
- [31: What is proof of stake?](#31-what-is-proof-of-stake)
- [32: What is mining?](#32-what-is-mining)
- [33: What is a validator?](#33-what-is-a-validator)
- [34: What is staking?](#34-what-is-staking)
- [35: What is a block reward?](#35-what-is-a-block-reward)
- [36: What is the Bitcoin halving?](#36-what-is-the-bitcoin-halving)
- [37: What is a transaction fee?](#37-what-is-a-transaction-fee)
- [38: What is the mempool?](#38-what-is-the-mempool)
- [39: What is block time?](#39-what-is-block-time)
- [40: What is a block explorer?](#40-what-is-a-block-explorer)
- [41: What is a public blockchain?](#41-what-is-a-public-blockchain)
- [42: What is a private blockchain?](#42-what-is-a-private-blockchain)
- [43: What is a consortium blockchain?](#43-what-is-a-consortium-blockchain)
- [44: What is the difference between permissioned and permissionless blockchains?](#44-what-is-the-difference-between-permissioned-and-permissionless-blockchains)
- [45: What is a fork in blockchain?](#45-what-is-a-fork-in-blockchain)
- [46: What is a hard fork?](#46-what-is-a-hard-fork)
- [47: What is a soft fork?](#47-what-is-a-soft-fork)
- [48: What is a dApp?](#48-what-is-a-dapp)
- [49: What is Web3?](#49-what-is-web3)
- [50: What is an NFT?](#50-what-is-an-nft)
- [51: What does fungible mean?](#51-what-does-fungible-mean)
- [52: What is an ERC-20 token?](#52-what-is-an-erc-20-token)
- [53: What is an ERC-721 token?](#53-what-is-an-erc-721-token)
- [54: What is an ERC-1155 token?](#54-what-is-an-erc-1155-token)
- [55: What is an EIP?](#55-what-is-an-eip)
- [56: What is a stablecoin?](#56-what-is-a-stablecoin)
- [57: What is DeFi?](#57-what-is-defi)
- [58: What is a DEX?](#58-what-is-a-dex)
- [59: What is a CEX?](#59-what-is-a-cex)
- [60: What is a DAO?](#60-what-is-a-dao)
- [61: What is a governance token?](#61-what-is-a-governance-token)
- [62: What is an oracle in blockchain?](#62-what-is-an-oracle-in-blockchain)
- [63: What is a layer 1?](#63-what-is-a-layer-1)
- [64: What is a layer 2?](#64-what-is-a-layer-2)
- [65: What is a rollup?](#65-what-is-a-rollup)
- [66: What is a sidechain?](#66-what-is-a-sidechain)
- [67: What is a bridge?](#67-what-is-a-bridge)
- [68: What is a wrapped token?](#68-what-is-a-wrapped-token)
- [69: What is an account on Ethereum?](#69-what-is-an-account-on-ethereum)
- [70: What is an externally owned account (EOA)?](#70-what-is-an-externally-owned-account-eoa)
- [71: What is a contract account?](#71-what-is-a-contract-account)
- [72: What is a nonce on Ethereum?](#72-what-is-a-nonce-on-ethereum)
- [73: What is a transaction hash?](#73-what-is-a-transaction-hash)
- [74: What is a transaction receipt?](#74-what-is-a-transaction-receipt)
- [75: What is a confirmation?](#75-what-is-a-confirmation)
- [76: What is finality?](#76-what-is-finality)
- [77: What is the double spending problem?](#77-what-is-the-double-spending-problem)
- [78: What is a 51% attack?](#78-what-is-a-51-attack)
- [79: What is a Merkle tree?](#79-what-is-a-merkle-tree)
- [80: What is a Merkle root?](#80-what-is-a-merkle-root)
- [81: What is a digital signature?](#81-what-is-a-digital-signature)
- [82: What is public key cryptography?](#82-what-is-public-key-cryptography)
- [83: What is a hardware wallet?](#83-what-is-a-hardware-wallet)
- [84: What is MetaMask?](#84-what-is-metamask)
- [85: What is a testnet?](#85-what-is-a-testnet)
- [86: What is a mainnet?](#86-what-is-a-mainnet)
- [87: What is a faucet?](#87-what-is-a-faucet)
- [88: What is a chain ID?](#88-what-is-a-chain-id)
- [89: What is an ABI?](#89-what-is-an-abi)
- [90: What is bytecode?](#90-what-is-bytecode)
- [91: What is an RPC node or provider?](#91-what-is-an-rpc-node-or-provider)
- [92: What is JSON-RPC in Ethereum?](#92-what-is-json-rpc-in-ethereum)
- [93: What is ethers.js?](#93-what-is-ethersjs)
- [94: What is viem?](#94-what-is-viem)
- [95: What is web3.js?](#95-what-is-web3js)
- [96: What is Hardhat?](#96-what-is-hardhat)
- [97: What is Foundry?](#97-what-is-foundry)
- [98: What is Remix?](#98-what-is-remix)
- [99: What is IPFS?](#99-what-is-ipfs)
- [100: Why is storing large data on-chain a bad idea?](#100-why-is-storing-large-data-on-chain-a-bad-idea)
- [101: What is a token allowance?](#101-what-is-a-token-allowance)
- [102: What is a smart contract event?](#102-what-is-a-smart-contract-event)
- [103: What is msg.sender?](#103-what-is-msgsender)
- [104: What is msg.value?](#104-what-is-msgvalue)
- [105: What does payable mean in Solidity?](#105-what-does-payable-mean-in-solidity)
- [106: What are the main data types in Solidity?](#106-what-are-the-main-data-types-in-solidity)
- [107: What is a mapping in Solidity?](#107-what-is-a-mapping-in-solidity)
- [108: What is a struct in Solidity?](#108-what-is-a-struct-in-solidity)
- [109: What are the function visibility types in Solidity?](#109-what-are-the-function-visibility-types-in-solidity)
- [110: What is the difference between view and pure functions?](#110-what-is-the-difference-between-view-and-pure-functions)
- [111: What is a constructor in Solidity?](#111-what-is-a-constructor-in-solidity)
- [112: What does require do in Solidity?](#112-what-does-require-do-in-solidity)
- [113: What does revert mean?](#113-what-does-revert-mean)
- [114: What is a modifier in Solidity?](#114-what-is-a-modifier-in-solidity)
- [115: What is OpenZeppelin?](#115-what-is-openzeppelin)
- [116: Can a smart contract be changed after deployment?](#116-can-a-smart-contract-be-changed-after-deployment)
- [117: What does deploying a contract mean?](#117-what-does-deploying-a-contract-mean)
- [118: What is contract verification?](#118-what-is-contract-verification)
- [119: What is a public ledger?](#119-what-is-a-public-ledger)
- [120: Is blockchain anonymous?](#120-is-blockchain-anonymous)
- [121: What is a cryptocurrency exchange?](#121-what-is-a-cryptocurrency-exchange)
- [122: What is market capitalization in crypto?](#122-what-is-market-capitalization-in-crypto)
- [123: What is tokenomics?](#123-what-is-tokenomics)
- [124: What is a token burn?](#124-what-is-a-token-burn)
- [125: What is an airdrop?](#125-what-is-an-airdrop)
- [126: What is a smart contract wallet?](#126-what-is-a-smart-contract-wallet)
- [127: What is a multisig wallet?](#127-what-is-a-multisig-wallet)
- [128: What is a seed phrase used for when you get a new device?](#128-what-is-a-seed-phrase-used-for-when-you-get-a-new-device)
- [129: What is an ENS name?](#129-what-is-an-ens-name)
- [130: What is a token decimals value?](#130-what-is-a-token-decimals-value)
- [131: What is a liquidity pool?](#131-what-is-a-liquidity-pool)
- [132: What is an automated market maker (AMM)?](#132-what-is-an-automated-market-maker-amm)
- [133: What is slippage?](#133-what-is-slippage)
- [134: What is a proof of stake validator's stake on Ethereum?](#134-what-is-a-proof-of-stake-validators-stake-on-ethereum)
- [135: What is slashing?](#135-what-is-slashing)
- [136: What was the Merge?](#136-what-was-the-merge)
- [137: What is the Beacon Chain?](#137-what-is-the-beacon-chain)
- [138: What are execution and consensus clients?](#138-what-are-execution-and-consensus-clients)
- [139: What is client diversity and why does it matter?](#139-what-is-client-diversity-and-why-does-it-matter)
- [140: What is a slot and an epoch on Ethereum?](#140-what-is-a-slot-and-an-epoch-on-ethereum)
- [141: What is the Bitcoin UTXO model?](#141-what-is-the-bitcoin-utxo-model)
- [142: What is the account model?](#142-what-is-the-account-model)
- [143: What is Satoshi?](#143-what-is-satoshi)
- [144: What is the Lightning Network?](#144-what-is-the-lightning-network)
- [145: What is Solana?](#145-what-is-solana)
- [146: What are some well-known EVM-compatible chains?](#146-what-are-some-well-known-evm-compatible-chains)
- [147: What is a smart contract audit?](#147-what-is-a-smart-contract-audit)
- [148: What is a rug pull?](#148-what-is-a-rug-pull)
- [149: What is a phishing attack in crypto?](#149-what-is-a-phishing-attack-in-crypto)
- [150: What are some real uses of blockchain besides cryptocurrency?](#150-what-are-some-real-uses-of-blockchain-besides-cryptocurrency)

### Moderate Questions (151-300)

- [151: How does EIP-1559 change how transaction fees work?](#151-how-does-eip-1559-change-how-transaction-fees-work)
- [152: How do you set gas fees for a transaction with ethers.js?](#152-how-do-you-set-gas-fees-for-a-transaction-with-ethersjs)
- [153: What is the gas limit of a transaction versus the block gas limit?](#153-what-is-the-gas-limit-of-a-transaction-versus-the-block-gas-limit)
- [154: How do you estimate gas for a transaction?](#154-how-do-you-estimate-gas-for-a-transaction)
- [155: What happens to the fee if a transaction reverts?](#155-what-happens-to-the-fee-if-a-transaction-reverts)
- [156: How do you connect a web app to MetaMask?](#156-how-do-you-connect-a-web-app-to-metamask)
- [157: What is EIP-1193?](#157-what-is-eip-1193)
- [158: What is EIP-6963 and what problem does it solve?](#158-what-is-eip-6963-and-what-problem-does-it-solve)
- [159: What is wagmi?](#159-what-is-wagmi)
- [160: What is WalletConnect?](#160-what-is-walletconnect)
- [161: How do you read data from a smart contract with ethers.js?](#161-how-do-you-read-data-from-a-smart-contract-with-ethersjs)
- [162: How do you send a transaction to a contract with viem?](#162-how-do-you-send-a-transaction-to-a-contract-with-viem)
- [163: How do you listen to contract events in JavaScript?](#163-how-do-you-listen-to-contract-events-in-javascript)
- [164: How do you query past events?](#164-how-do-you-query-past-events)
- [165: What are indexed event parameters?](#165-what-are-indexed-event-parameters)
- [166: What are the topics in an Ethereum log?](#166-what-are-the-topics-in-an-ethereum-log)
- [167: What is a function selector?](#167-what-is-a-function-selector)
- [168: How does ABI encoding work?](#168-how-does-abi-encoding-work)
- [169: What is the difference between abi.encode and abi.encodePacked?](#169-what-is-the-difference-between-abiencode-and-abiencodepacked)
- [170: What are custom errors in Solidity?](#170-what-are-custom-errors-in-solidity)
- [171: What is the difference between require, revert and assert?](#171-what-is-the-difference-between-require-revert-and-assert)
- [172: How does Solidity 0.8 handle integer overflow?](#172-how-does-solidity-08-handle-integer-overflow)
- [173: What are storage, memory and calldata in Solidity?](#173-what-are-storage-memory-and-calldata-in-solidity)
- [174: What are constant and immutable variables?](#174-what-are-constant-and-immutable-variables)
- [175: How does inheritance work in Solidity?](#175-how-does-inheritance-work-in-solidity)
- [176: What is an interface in Solidity?](#176-what-is-an-interface-in-solidity)
- [177: What is an abstract contract?](#177-what-is-an-abstract-contract)
- [178: What is a library in Solidity?](#178-what-is-a-library-in-solidity)
- [179: What are receive and fallback functions?](#179-what-are-receive-and-fallback-functions)
- [180: What are the ways to send ETH from a contract and which should you use?](#180-what-are-the-ways-to-send-eth-from-a-contract-and-which-should-you-use)
- [181: How does the Ownable pattern work?](#181-how-does-the-ownable-pattern-work)
- [182: What is role-based access control in smart contracts?](#182-what-is-role-based-access-control-in-smart-contracts)
- [183: How do you pause a contract in an emergency?](#183-how-do-you-pause-a-contract-in-an-emergency)
- [184: How do you write a basic test with Foundry?](#184-how-do-you-write-a-basic-test-with-foundry)
- [185: What are Foundry cheatcodes?](#185-what-are-foundry-cheatcodes)
- [186: What is fuzz testing in smart contracts?](#186-what-is-fuzz-testing-in-smart-contracts)
- [187: What is invariant testing?](#187-what-is-invariant-testing)
- [188: What is mainnet forking in testing?](#188-what-is-mainnet-forking-in-testing)
- [189: How do you deploy a contract with Foundry?](#189-how-do-you-deploy-a-contract-with-foundry)
- [190: How do you deploy a contract with Hardhat Ignition?](#190-how-do-you-deploy-a-contract-with-hardhat-ignition)
- [191: How should you manage private keys in a development project?](#191-how-should-you-manage-private-keys-in-a-development-project)
- [192: How do you handle big numbers in JavaScript blockchain code?](#192-how-do-you-handle-big-numbers-in-javascript-blockchain-code)
- [193: What is the difference between a provider and a signer?](#193-what-is-the-difference-between-a-provider-and-a-signer)
- [194: How do you sign a message and verify it?](#194-how-do-you-sign-a-message-and-verify-it)
- [195: What is EIP-712 typed data signing?](#195-what-is-eip-712-typed-data-signing)
- [196: What is Sign-In with Ethereum (SIWE)?](#196-what-is-sign-in-with-ethereum-siwe)
- [197: What is ERC-2612 permit?](#197-what-is-erc-2612-permit)
- [198: What is Permit2?](#198-what-is-permit2)
- [199: How do you switch the user's wallet to the right network?](#199-how-do-you-switch-the-users-wallet-to-the-right-network)
- [200: How do you handle a user rejecting a transaction?](#200-how-do-you-handle-a-user-rejecting-a-transaction)
- [201: How do you decode a revert reason in the front end?](#201-how-do-you-decode-a-revert-reason-in-the-front-end)
- [202: How do you wait for a transaction and handle it being replaced?](#202-how-do-you-wait-for-a-transaction-and-handle-it-being-replaced)
- [203: How do you speed up or cancel a pending transaction?](#203-how-do-you-speed-up-or-cancel-a-pending-transaction)
- [204: What does a stuck transaction mean and how does it affect later ones?](#204-what-does-a-stuck-transaction-mean-and-how-does-it-affect-later-ones)
- [205: How do you manage nonces when sending many transactions from a back end?](#205-how-do-you-manage-nonces-when-sending-many-transactions-from-a-back-end)
- [206: What are transaction types on Ethereum?](#206-what-are-transaction-types-on-ethereum)
- [207: What is an access list transaction?](#207-what-is-an-access-list-transaction)
- [208: What is the difference between call, staticcall and delegatecall?](#208-what-is-the-difference-between-call-staticcall-and-delegatecall)
- [209: How does the proxy pattern work?](#209-how-does-the-proxy-pattern-work)
- [210: What is the difference between a transparent proxy and a UUPS proxy?](#210-what-is-the-difference-between-a-transparent-proxy-and-a-uups-proxy)
- [211: Why can't upgradeable contracts use constructors?](#211-why-cant-upgradeable-contracts-use-constructors)
- [212: What is a storage collision in upgradeable contracts?](#212-what-is-a-storage-collision-in-upgradeable-contracts)
- [213: What is the beacon proxy pattern?](#213-what-is-the-beacon-proxy-pattern)
- [214: What is a minimal proxy (clone)?](#214-what-is-a-minimal-proxy-clone)
- [215: How does CREATE2 work?](#215-how-does-create2-work)
- [216: How does an ERC-20 transfer work under the hood?](#216-how-does-an-erc-20-transfer-work-under-the-hood)
- [217: Why do some ERC-20 tokens not return a boolean?](#217-why-do-some-erc-20-tokens-not-return-a-boolean)
- [218: What is the approve front-running issue in ERC-20?](#218-what-is-the-approve-front-running-issue-in-erc-20)
- [219: What is safeTransferFrom in ERC-721?](#219-what-is-safetransferfrom-in-erc-721)
- [220: How is NFT metadata stored?](#220-how-is-nft-metadata-stored)
- [221: What is ERC-2981?](#221-what-is-erc-2981)
- [222: What is ERC-4626?](#222-what-is-erc-4626)
- [223: What is ERC-165?](#223-what-is-erc-165)
- [224: What is a merkle airdrop and why use it?](#224-what-is-a-merkle-airdrop-and-why-use-it)
- [225: What is a reentrancy attack?](#225-what-is-a-reentrancy-attack)
- [226: How do you prevent reentrancy?](#226-how-do-you-prevent-reentrancy)
- [227: What is the checks-effects-interactions pattern?](#227-what-is-the-checks-effects-interactions-pattern)
- [228: What is front-running?](#228-what-is-front-running)
- [229: What is MEV?](#229-what-is-mev)
- [230: What is a sandwich attack?](#230-what-is-a-sandwich-attack)
- [231: What is a private mempool or private RPC?](#231-what-is-a-private-mempool-or-private-rpc)
- [232: What is a commit-reveal scheme?](#232-what-is-a-commit-reveal-scheme)
- [233: Why is block.timestamp not a good source of randomness?](#233-why-is-blocktimestamp-not-a-good-source-of-randomness)
- [234: What is Chainlink VRF?](#234-what-is-chainlink-vrf)
- [235: How do you get a price feed in a smart contract?](#235-how-do-you-get-a-price-feed-in-a-smart-contract)
- [236: Why is using a DEX spot price as an oracle dangerous?](#236-why-is-using-a-dex-spot-price-as-an-oracle-dangerous)
- [237: What is a flash loan?](#237-what-is-a-flash-loan)
- [238: What is impermanent loss?](#238-what-is-impermanent-loss)
- [239: How does lending work in DeFi protocols like Aave?](#239-how-does-lending-work-in-defi-protocols-like-aave)
- [240: What is a liquidation in DeFi?](#240-what-is-a-liquidation-in-defi)
- [241: What is a health factor in lending protocols?](#241-what-is-a-health-factor-in-lending-protocols)
- [242: What is a time lock in smart contracts?](#242-what-is-a-time-lock-in-smart-contracts)
- [243: How does on-chain governance usually work?](#243-how-does-on-chain-governance-usually-work)
- [244: What is ERC20Votes and why use checkpoints?](#244-what-is-erc20votes-and-why-use-checkpoints)
- [245: How do you build a subgraph with The Graph?](#245-how-do-you-build-a-subgraph-with-the-graph)
- [246: Why do dApps need an indexer?](#246-why-do-dapps-need-an-indexer)
- [247: How would you build your own event indexer in Node.js?](#247-how-would-you-build-your-own-event-indexer-in-nodejs)
- [248: What is a chain reorganization (reorg) and how should apps handle it?](#248-what-is-a-chain-reorganization-reorg-and-how-should-apps-handle-it)
- [249: What are the "latest", "safe" and "finalized" block tags?](#249-what-are-the-latest-safe-and-finalized-block-tags)
- [250: How do you call a read function at a past block?](#250-how-do-you-call-a-read-function-at-a-past-block)
- [251: How do you make many contract reads in one request?](#251-how-do-you-make-many-contract-reads-in-one-request)
- [252: How do you handle RPC rate limits and failures?](#252-how-do-you-handle-rpc-rate-limits-and-failures)
- [253: Should you put your RPC API key in the front end?](#253-should-you-put-your-rpc-api-key-in-the-front-end)
- [254: What is a gas optimization you can make with storage?](#254-what-is-a-gas-optimization-you-can-make-with-storage)
- [255: Why is reading the same storage variable many times in a loop expensive?](#255-why-is-reading-the-same-storage-variable-many-times-in-a-loop-expensive)
- [256: What is the cost of writing to storage?](#256-what-is-the-cost-of-writing-to-storage)
- [257: Why should you avoid unbounded loops in smart contracts?](#257-why-should-you-avoid-unbounded-loops-in-smart-contracts)
- [258: What is the pull over push payment pattern?](#258-what-is-the-pull-over-push-payment-pattern)
- [259: What is a denial of service attack in smart contracts?](#259-what-is-a-denial-of-service-attack-in-smart-contracts)
- [260: What is tx.origin and why shouldn't you use it for authorization?](#260-what-is-txorigin-and-why-shouldnt-you-use-it-for-authorization)
- [261: What is signature replay and how do you prevent it?](#261-what-is-signature-replay-and-how-do-you-prevent-it)
- [262: How do you verify a signature in Solidity?](#262-how-do-you-verify-a-signature-in-solidity)
- [263: What is ERC-1271?](#263-what-is-erc-1271)
- [264: What is account abstraction?](#264-what-is-account-abstraction)
- [265: How does ERC-4337 work?](#265-how-does-erc-4337-work)
- [266: What is a paymaster?](#266-what-is-a-paymaster)
- [267: What is EIP-7702?](#267-what-is-eip-7702)
- [268: What are session keys?](#268-what-are-session-keys)
- [269: How do passkeys work with blockchain wallets?](#269-how-do-passkeys-work-with-blockchain-wallets)
- [270: What is an optimistic rollup?](#270-what-is-an-optimistic-rollup)
- [271: What is a ZK rollup?](#271-what-is-a-zk-rollup)
- [272: What is the difference between optimistic and ZK rollups?](#272-what-is-the-difference-between-optimistic-and-zk-rollups)
- [273: What is data availability?](#273-what-is-data-availability)
- [274: What are blobs (EIP-4844)?](#274-what-are-blobs-eip-4844)
- [275: What did the Fusaka upgrade bring?](#275-what-did-the-fusaka-upgrade-bring)
- [276: What was the Pectra upgrade?](#276-what-was-the-pectra-upgrade)
- [277: What is the next planned Ethereum upgrade?](#277-what-is-the-next-planned-ethereum-upgrade)
- [278: How do you bridge tokens between layer 1 and a rollup?](#278-how-do-you-bridge-tokens-between-layer-1-and-a-rollup)
- [279: What is a cross-chain messaging protocol?](#279-what-is-a-cross-chain-messaging-protocol)
- [280: What is the difference between a lock-and-mint bridge and a burn-and-mint bridge?](#280-what-is-the-difference-between-a-lock-and-mint-bridge-and-a-burn-and-mint-bridge)
- [281: How do you deploy the same contract on multiple chains?](#281-how-do-you-deploy-the-same-contract-on-multiple-chains)
- [282: What is a token vesting contract?](#282-what-is-a-token-vesting-contract)
- [283: How do you implement an NFT allowlist mint?](#283-how-do-you-implement-an-nft-allowlist-mint)
- [284: What are soulbound tokens?](#284-what-are-soulbound-tokens)
- [285: What is the difference between on-chain and off-chain data in a dApp?](#285-what-is-the-difference-between-on-chain-and-off-chain-data-in-a-dapp)
- [286: How do you store and pin files on IPFS from Node.js?](#286-how-do-you-store-and-pin-files-on-ipfs-from-nodejs)
- [287: What is Arweave and how is it different from IPFS?](#287-what-is-arweave-and-how-is-it-different-from-ipfs)
- [288: How do you show token balances for a user in a dApp?](#288-how-do-you-show-token-balances-for-a-user-in-a-dapp)
- [289: How do you handle account and network changes in a dApp?](#289-how-do-you-handle-account-and-network-changes-in-a-dapp)
- [290: What is optimistic UI in a dApp?](#290-what-is-optimistic-ui-in-a-dapp)
- [291: How do you show transaction status to users?](#291-how-do-you-show-transaction-status-to-users)
- [292: How do you protect users from approving unlimited allowances?](#292-how-do-you-protect-users-from-approving-unlimited-allowances)
- [293: What is transaction simulation and why do wallets show it?](#293-what-is-transaction-simulation-and-why-do-wallets-show-it)
- [294: How do you debug a failed transaction?](#294-how-do-you-debug-a-failed-transaction)
- [295: What is Etherscan's API useful for?](#295-what-is-etherscans-api-useful-for)
- [296: How do you write a Hardhat test in TypeScript?](#296-how-do-you-write-a-hardhat-test-in-typescript)
- [297: What is gas reporting and snapshotting?](#297-what-is-gas-reporting-and-snapshotting)
- [298: What is Slither?](#298-what-is-slither)
- [299: What should a smart contract code review checklist include?](#299-what-should-a-smart-contract-code-review-checklist-include)
- [300: What are fee-on-transfer and rebasing tokens, and why do they cause bugs?](#300-what-are-fee-on-transfer-and-rebasing-tokens-and-why-do-they-cause-bugs)

### Advanced Questions (301-450)

- [301: What is the blockchain trilemma?](#301-what-is-the-blockchain-trilemma)
- [302: How does Ethereum's proof of stake reach consensus?](#302-how-does-ethereums-proof-of-stake-reach-consensus)
- [303: What is the difference between justification and finalization on Ethereum?](#303-what-is-the-difference-between-justification-and-finalization-on-ethereum)
- [304: What is an inactivity leak?](#304-what-is-an-inactivity-leak)
- [305: How are block proposers chosen on Ethereum and why does it matter that the choice is unpredictable?](#305-how-are-block-proposers-chosen-on-ethereum-and-why-does-it-matter-that-the-choice-is-unpredictable)
- [306: What does PREVRANDAO give you in Solidity and how safe is it?](#306-what-does-prevrandao-give-you-in-solidity-and-how-safe-is-it)
- [307: How does Bitcoin's difficulty adjustment work?](#307-how-does-bitcoins-difficulty-adjustment-work)
- [308: What is the longest chain rule in Bitcoin, and why is "most work" more accurate?](#308-what-is-the-longest-chain-rule-in-bitcoin-and-why-is-most-work-more-accurate)
- [309: What is a selfish mining attack?](#309-what-is-a-selfish-mining-attack)
- [310: What is a long range attack in proof of stake and how is it prevented?](#310-what-is-a-long-range-attack-in-proof-of-stake-and-how-is-it-prevented)
- [311: What is the nothing at stake problem?](#311-what-is-the-nothing-at-stake-problem)
- [312: How do BFT-style consensus protocols differ from Nakamoto consensus?](#312-how-do-bft-style-consensus-protocols-differ-from-nakamoto-consensus)
- [313: What is the CAP theorem's relevance to blockchains?](#313-what-is-the-cap-theorems-relevance-to-blockchains)
- [314: What is proposer-builder separation (PBS)?](#314-what-is-proposer-builder-separation-pbs)
- [315: How does MEV-Boost work?](#315-how-does-mev-boost-work)
- [316: What are the centralization concerns with MEV?](#316-what-are-the-centralization-concerns-with-mev)
- [317: What is the Ethereum state and how is it stored?](#317-what-is-the-ethereum-state-and-how-is-it-stored)
- [318: What is a Merkle Patricia Trie?](#318-what-is-a-merkle-patricia-trie)
- [319: What are Verkle trees and why does Ethereum want them?](#319-what-are-verkle-trees-and-why-does-ethereum-want-them)
- [320: What is state growth and why is it a problem?](#320-what-is-state-growth-and-why-is-it-a-problem)
- [321: What is history expiry (EIP-4444)?](#321-what-is-history-expiry-eip-4444)
- [322: How does the EVM work at a low level?](#322-how-does-the-evm-work-at-a-low-level)
- [323: What are warm and cold storage accesses (EIP-2929)?](#323-what-are-warm-and-cold-storage-accesses-eip-2929)
- [324: What is transient storage and how is it used?](#324-what-is-transient-storage-and-how-is-it-used)
- [325: What happened to SELFDESTRUCT?](#325-what-happened-to-selfdestruct)
- [326: How is memory expansion charged in the EVM?](#326-how-is-memory-expansion-charged-in-the-evm)
- [327: What is the 63/64 rule for gas?](#327-what-is-the-6364-rule-for-gas)
- [328: What is the contract size limit?](#328-what-is-the-contract-size-limit)
- [329: What is the diamond pattern (EIP-2535)?](#329-what-is-the-diamond-pattern-eip-2535)
- [330: How does the Solidity optimizer "runs" setting work?](#330-how-does-the-solidity-optimizer-runs-setting-work)
- [331: What is the via-IR pipeline?](#331-what-is-the-via-ir-pipeline)
- [332: What is the "stack too deep" error and how do you fix it?](#332-what-is-the-stack-too-deep-error-and-how-do-you-fix-it)
- [333: What is inline assembly in Solidity and when should you use it?](#333-what-is-inline-assembly-in-solidity-and-when-should-you-use-it)
- [334: How are dynamic arrays and mappings laid out in storage?](#334-how-are-dynamic-arrays-and-mappings-laid-out-in-storage)
- [335: Can private variables be read by anyone?](#335-can-private-variables-be-read-by-anyone)
- [336: What is read-only reentrancy?](#336-what-is-read-only-reentrancy)
- [337: What is cross-function and cross-contract reentrancy?](#337-what-is-cross-function-and-cross-contract-reentrancy)
- [338: What are ERC-777 and ERC-721 hooks, and why are they reentrancy risks?](#338-what-are-erc-777-and-erc-721-hooks-and-why-are-they-reentrancy-risks)
- [339: What is a price manipulation attack, step by step?](#339-what-is-a-price-manipulation-attack-step-by-step)
- [340: What is a TWAP oracle and its limits?](#340-what-is-a-twap-oracle-and-its-limits)
- [341: What is an ERC-4626 inflation (donation) attack?](#341-what-is-an-erc-4626-inflation-donation-attack)
- [342: How should you handle rounding in DeFi math?](#342-how-should-you-handle-rounding-in-defi-math)
- [343: How does Uniswap V3 concentrated liquidity work?](#343-how-does-uniswap-v3-concentrated-liquidity-work)
- [344: What are Uniswap V4 hooks and the singleton design?](#344-what-are-uniswap-v4-hooks-and-the-singleton-design)
- [345: How would you design a stablecoin and what are the main risks?](#345-how-would-you-design-a-stablecoin-and-what-are-the-main-risks)
- [346: What is a governance attack and how can you defend against it?](#346-what-is-a-governance-attack-and-how-can-you-defend-against-it)
- [347: How do you secure admin keys for a protocol?](#347-how-do-you-secure-admin-keys-for-a-protocol)
- [348: What did the Bybit hack in 2025 teach about multisig security?](#348-what-did-the-bybit-hack-in-2025-teach-about-multisig-security)
- [349: What is blind signing and how do you avoid it?](#349-what-is-blind-signing-and-how-do-you-avoid-it)
- [350: What is address poisoning?](#350-what-is-address-poisoning)
- [351: What are common bridge vulnerabilities?](#351-what-are-common-bridge-vulnerabilities)
- [352: How do ZK proofs work at a high level?](#352-how-do-zk-proofs-work-at-a-high-level)
- [353: What is the difference between SNARKs and STARKs?](#353-what-is-the-difference-between-snarks-and-starks)
- [354: What is a trusted setup ceremony?](#354-what-is-a-trusted-setup-ceremony)
- [355: What is a zkVM?](#355-what-is-a-zkvm)
- [356: What is a ZK coprocessor?](#356-what-is-a-zk-coprocessor)
- [357: What are KZG commitments and how are they used for blobs?](#357-what-are-kzg-commitments-and-how-are-they-used-for-blobs)
- [358: How does data availability sampling (PeerDAS) work?](#358-how-does-data-availability-sampling-peerdas-work)
- [359: How does an optimistic rollup's fraud proof actually work?](#359-how-does-an-optimistic-rollups-fraud-proof-actually-work)
- [360: What are the "stages" of rollup decentralization?](#360-what-are-the-stages-of-rollup-decentralization)
- [361: What is a sequencer and what are the risks of a centralized one?](#361-what-is-a-sequencer-and-what-are-the-risks-of-a-centralized-one)
- [362: What is a based rollup?](#362-what-is-a-based-rollup)
- [363: What are preconfirmations?](#363-what-are-preconfirmations)
- [364: How do layer 2 fees work?](#364-how-do-layer-2-fees-work)
- [365: What is the difference between EVM equivalence and EVM compatibility?](#365-what-is-the-difference-between-evm-equivalence-and-evm-compatibility)
- [366: How do you make an app work across several layer 2s safely?](#366-how-do-you-make-an-app-work-across-several-layer-2s-safely)
- [367: What is a sequencer uptime feed and why do lending protocols use it?](#367-what-is-a-sequencer-uptime-feed-and-why-do-lending-protocols-use-it)
- [368: What are intents and solvers?](#368-what-are-intents-and-solvers)
- [369: How does a Bitcoin transaction get validated?](#369-how-does-a-bitcoin-transaction-get-validated)
- [370: What is Bitcoin Script?](#370-what-is-bitcoin-script)
- [371: What were SegWit and Taproot?](#371-what-were-segwit-and-taproot)
- [372: What are Schnorr signatures and their advantages?](#372-what-are-schnorr-signatures-and-their-advantages)
- [373: What are Ordinals and inscriptions?](#373-what-are-ordinals-and-inscriptions)
- [374: How do HTLCs and the Lightning Network route payments?](#374-how-do-htlcs-and-the-lightning-network-route-payments)
- [375: What is the UTXO model's advantage for parallelism and privacy?](#375-what-is-the-utxo-models-advantage-for-parallelism-and-privacy)
- [376: How does Solana achieve high throughput?](#376-how-does-solana-achieve-high-throughput)
- [377: How is writing a Solana program different from writing a Solidity contract?](#377-how-is-writing-a-solana-program-different-from-writing-a-solidity-contract)
- [378: What is Move and how do Sui and Aptos use it?](#378-what-is-move-and-how-do-sui-and-aptos-use-it)
- [379: What is Cosmos and the IBC protocol?](#379-what-is-cosmos-and-the-ibc-protocol)
- [380: What is restaking?](#380-what-is-restaking)
- [381: What is liquid staking and what are its risks?](#381-what-is-liquid-staking-and-what-are-its-risks)
- [382: What is distributed validator technology (DVT)?](#382-what-is-distributed-validator-technology-dvt)
- [383: What are BLS signatures and why does Ethereum's consensus use them?](#383-what-are-bls-signatures-and-why-does-ethereums-consensus-use-them)
- [384: What are precompiled contracts?](#384-what-are-precompiled-contracts)
- [385: How does ecrecover work and what are its pitfalls?](#385-how-does-ecrecover-work-and-what-are-its-pitfalls)
- [386: How do HD wallets (BIP-32 and BIP-44) derive keys?](#386-how-do-hd-wallets-bip-32-and-bip-44-derive-keys)
- [387: What is MPC wallet technology?](#387-what-is-mpc-wallet-technology)
- [388: What is social recovery?](#388-what-is-social-recovery)
- [389: How would you design a secure custodial deposit system for an exchange?](#389-how-would-you-design-a-secure-custodial-deposit-system-for-an-exchange)
- [390: How do you monitor smart contracts in production?](#390-how-do-you-monitor-smart-contracts-in-production)
- [391: What should an incident response plan for a hacked protocol include?](#391-what-should-an-incident-response-plan-for-a-hacked-protocol-include)
- [392: What is formal verification for smart contracts?](#392-what-is-formal-verification-for-smart-contracts)
- [393: What is symbolic execution?](#393-what-is-symbolic-execution)
- [394: What is differential fuzzing?](#394-what-is-differential-fuzzing)
- [395: How do you test upgrades safely?](#395-how-do-you-test-upgrades-safely)
- [396: What is the risk of uninitialized implementation contracts?](#396-what-is-the-risk-of-uninitialized-implementation-contracts)
- [397: What is a function selector clash in proxies?](#397-what-is-a-function-selector-clash-in-proxies)
- [398: How would you design a gas-efficient NFT mint for 10,000 tokens?](#398-how-would-you-design-a-gas-efficient-nft-mint-for-10000-tokens)
- [399: What causes "nonce too low" and "replacement transaction underpriced" errors?](#399-what-causes-nonce-too-low-and-replacement-transaction-underpriced-errors)
- [400: How do you handle chain reorgs in a payment system?](#400-how-do-you-handle-chain-reorgs-in-a-payment-system)
- [401: How would you design a back end that sends many on-chain transactions reliably?](#401-how-would-you-design-a-back-end-that-sends-many-on-chain-transactions-reliably)
- [402: How do you keep private keys safe on a server that signs transactions?](#402-how-do-you-keep-private-keys-safe-on-a-server-that-signs-transactions)
- [403: How do you build a gasless transaction experience?](#403-how-do-you-build-a-gasless-transaction-experience)
- [404: What is ERC-2771 and what are its risks?](#404-what-is-erc-2771-and-what-are-its-risks)
- [405: How do you build a token-gated website?](#405-how-do-you-build-a-token-gated-website)
- [406: How do you design a smart contract system for upgrades and long-term maintenance?](#406-how-do-you-design-a-smart-contract-system-for-upgrades-and-long-term-maintenance)
- [407: When should you not use a blockchain?](#407-when-should-you-not-use-a-blockchain)
- [408: How do you handle personal data and GDPR with blockchains?](#408-how-do-you-handle-personal-data-and-gdpr-with-blockchains)
- [409: What are tokenized real-world assets (RWAs) and their technical challenges?](#409-what-are-tokenized-real-world-assets-rwas-and-their-technical-challenges)
- [410: How do stablecoin issuers freeze funds and what does that mean for your contracts?](#410-how-do-stablecoin-issuers-freeze-funds-and-what-does-that-mean-for-your-contracts)
- [411: How would you design a decentralized exchange order book on-chain?](#411-how-would-you-design-a-decentralized-exchange-order-book-on-chain)
- [412: How does Ethereum's EIP-1559 base fee formula work exactly?](#412-how-does-ethereums-eip-1559-base-fee-formula-work-exactly)
- [413: What determines a validator's rewards on Ethereum?](#413-what-determines-a-validators-rewards-on-ethereum)
- [414: How are ETH withdrawals and exits handled for validators?](#414-how-are-eth-withdrawals-and-exits-handled-for-validators)
- [415: What is the churn limit and why does it exist?](#415-what-is-the-churn-limit-and-why-does-it-exist)
- [416: What is the difference between a light client in proof of work and in proof of stake?](#416-what-is-the-difference-between-a-light-client-in-proof-of-work-and-in-proof-of-stake)
- [417: How do ZK light client bridges improve on multisig bridges?](#417-how-do-zk-light-client-bridges-improve-on-multisig-bridges)
- [418: What is the role of the Engine API?](#418-what-is-the-role-of-the-engine-api)
- [419: How do you run your own Ethereum node and when is it worth it?](#419-how-do-you-run-your-own-ethereum-node-and-when-is-it-worth-it)
- [420: What are trace and debug APIs and when do you need them?](#420-what-are-trace-and-debug-apis-and-when-do-you-need-them)
- [421: How would you detect internal ETH transfers to a deposit address?](#421-how-would-you-detect-internal-eth-transfers-to-a-deposit-address)
- [422: What is a reorg-safe way to build real-time notifications for users?](#422-what-is-a-reorg-safe-way-to-build-real-time-notifications-for-users)
- [423: What is EOF and what happened to it?](#423-what-is-eof-and-what-happened-to-it)
- [424: How would you reduce gas costs for a high-traffic contract?](#424-how-would-you-reduce-gas-costs-for-a-high-traffic-contract)
- [425: Why are gas refunds limited?](#425-why-are-gas-refunds-limited)
- [426: How do you protect a DeFi protocol from oracle failure?](#426-how-do-you-protect-a-defi-protocol-from-oracle-failure)
- [427: What is economic security, and how do you estimate it for a protocol?](#427-what-is-economic-security-and-how-do-you-estimate-it-for-a-protocol)
- [428: How would you design an on-chain auction that resists front-running?](#428-how-would-you-design-an-on-chain-auction-that-resists-front-running)
- [429: How do you make a contract work with both EOAs and smart contract wallets?](#429-how-do-you-make-a-contract-work-with-both-eoas-and-smart-contract-wallets)
- [430: Why is checking extcodesize to block contracts unreliable?](#430-why-is-checking-extcodesize-to-block-contracts-unreliable)
- [431: How do you design a token with a fixed supply that's safe from admin abuse?](#431-how-do-you-design-a-token-with-a-fixed-supply-thats-safe-from-admin-abuse)
- [432: What is a time-weighted voting or vote-escrow (veToken) model?](#432-what-is-a-time-weighted-voting-or-vote-escrow-vetoken-model)
- [433: What is a sybil attack and how do apps resist it?](#433-what-is-a-sybil-attack-and-how-do-apps-resist-it)
- [434: How do privacy tools like mixers work and what are the legal concerns?](#434-how-do-privacy-tools-like-mixers-work-and-what-are-the-legal-concerns)
- [435: What are stealth addresses?](#435-what-are-stealth-addresses)
- [436: What is fully homomorphic encryption (FHE) in blockchains?](#436-what-is-fully-homomorphic-encryption-fhe-in-blockchains)
- [437: How might quantum computers threaten blockchains?](#437-how-might-quantum-computers-threaten-blockchains)
- [438: How does Ethereum's roadmap plan to scale layer 1 itself?](#438-how-does-ethereums-roadmap-plan-to-scale-layer-1-itself)
- [439: What would you check before integrating a third-party DeFi protocol?](#439-what-would-you-check-before-integrating-a-third-party-defi-protocol)
- [440: Walk through what happens when a user clicks "Swap" on a DEX front end.](#440-walk-through-what-happens-when-a-user-clicks-swap-on-a-dex-front-end)
- [441: How would you debug "execution reverted" with no reason?](#441-how-would-you-debug-execution-reverted-with-no-reason)
- [442: How do you test a contract that depends on time?](#442-how-do-you-test-a-contract-that-depends-on-time)
- [443: How do you write an invariant test in Foundry?](#443-how-do-you-write-an-invariant-test-in-foundry)
- [444: What makes a good bug bounty program for a protocol?](#444-what-makes-a-good-bug-bounty-program-for-a-protocol)
- [445: How would you migrate users from an old contract to a new one?](#445-how-would-you-migrate-users-from-an-old-contract-to-a-new-one)
- [446: How do you design an NFT marketplace's order matching securely?](#446-how-do-you-design-an-nft-marketplaces-order-matching-securely)
- [447: What are the trade-offs between app-specific chains and deploying on a general-purpose chain?](#447-what-are-the-trade-offs-between-app-specific-chains-and-deploying-on-a-general-purpose-chain)
- [448: How do you choose which chain to build on?](#448-how-do-you-choose-which-chain-to-build-on)
- [449: How would you design a cross-chain token?](#449-how-would-you-design-a-cross-chain-token)
- [450: What's a sensible end-to-end architecture for a production dApp?](#450-whats-a-sensible-end-to-end-architecture-for-a-production-dapp)

---

# Easy Questions (1-150)

## 1: What is a blockchain?

A blockchain is a list of records (blocks) that many computers keep a copy of. Each block holds a batch of transactions and the hash of the block before it, so the blocks form a chain. If someone changes an old block, its hash changes and every block after it no longer matches. Because thousands of nodes hold the same data and agree on new blocks with a set of rules, no single party can quietly rewrite history.

## 2: What problem does a blockchain solve?

It lets people who don't trust each other agree on a shared record without a middleman like a bank. The classic example is money: without a central party, how do you stop someone from spending the same coin twice? Bitcoin solved this by having all nodes agree on one order of transactions. The same idea works for any shared state that several parties need to trust.

## 3: What is a block?

A block is a container of data added to the chain. It has a header and a body. The header holds things like the hash of the previous block, a timestamp, and a root hash that sums up all transactions in the block. The body holds the transactions themselves.

## 4: What is a hash function and why does a blockchain need one?

A hash function takes any input and returns a fixed-size output, like a fingerprint. A good cryptographic hash is fast to compute, gives a totally different output if one bit of input changes, and makes it practically impossible to find the input from the output or to find two inputs with the same output. Blockchains use hashes to link blocks, to identify transactions, and to detect any change in the data. Bitcoin uses SHA-256 and Ethereum uses Keccak-256.

```js
import { keccak256, toUtf8Bytes } from "ethers";

console.log(keccak256(toUtf8Bytes("hello")));
// 0x1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8
```

## 5: What is the genesis block?

The genesis block is the first block of a chain. It has no previous block, so its "previous hash" field is empty or all zeros. It is usually hardcoded into the node software, and every other block traces back to it. Bitcoin's genesis block was mined on January 3, 2009.

## 6: What is a node?

A node is a computer running the blockchain software. It keeps a copy of the chain (full or partial), checks new transactions and blocks against the rules, and passes them on to other nodes. Some nodes also produce blocks. The more independent nodes there are, the harder it is for anyone to censor or change the chain.

## 7: What is the difference between a full node and a light node?

A full node downloads and checks every block and keeps the current state, so it trusts nobody. A light node only downloads block headers and asks full nodes for the specific data it needs, along with proofs that the data is in the chain. Light nodes use much less disk and bandwidth, which makes them fit for phones and browsers, but they depend on full nodes being around to answer.

## 8: What is an archive node?

An archive node is a full node that also keeps every past state, not just the current one. It can answer questions like "what was this account's balance at block 15,000,000?" right away. Archive nodes need a lot more disk space, so most people run normal full nodes and use a provider when they need historical state.

## 9: What does decentralized mean in blockchain?

It means no single company or person controls the system. Many independent parties run nodes, produce blocks and hold copies of the data. Decentralization is a range, not a yes or no: you can ask how many parties would have to collude to censor a transaction or change the rules, and the higher that number, the more decentralized the chain is.

## 10: What is a distributed ledger?

A distributed ledger is a database of records that is copied across many computers, often in different places and owned by different parties. A blockchain is one type of distributed ledger where records are grouped into hash-linked blocks. Not every distributed ledger is a blockchain; some use other structures like a directed acyclic graph (DAG).

## 11: What does immutable mean for a blockchain?

It means that once data is in a block that is deep enough in the chain, it can't be changed in practice. Changing it would mean redoing the work or stake behind that block and every block after it, and convincing the rest of the network to accept the new version. Strictly speaking it is "tamper evident and very costly to change", not physically impossible.

## 12: What is a transaction?

A transaction is a signed message from an account that asks the network to do something, such as send coins or call a smart contract. Nodes check that the signature is valid and that the sender can pay, then a block producer puts it into a block. Once in a block, it changes the shared state for everyone.

## 13: What is a cryptocurrency?

A cryptocurrency is digital money whose ownership is tracked on a blockchain instead of by a bank. You prove ownership with a private key, and the network rules decide how new coins are created. Bitcoin (BTC) and Ether (ETH) are the best-known examples. A native cryptocurrency is also used to pay transaction fees on its chain.

## 14: What is the difference between a coin and a token?

A coin is the native asset of a blockchain, like BTC on Bitcoin or ETH on Ethereum, and it is used to pay fees. A token is an asset created by a smart contract on top of an existing chain, like USDC or UNI on Ethereum. The chain itself knows about coin balances, while token balances live inside the token contract's storage.

## 15: What is Bitcoin?

Bitcoin is the first cryptocurrency, launched in 2009 by someone using the name Satoshi Nakamoto. It is a peer-to-peer payment network with a fixed supply cap of 21 million BTC. It uses proof of work to agree on blocks, and new blocks come about every 10 minutes. Its scripting language is kept simple on purpose, so it is mainly used for payments and storing value.

## 16: What is Ethereum?

Ethereum is a blockchain that can run programs called smart contracts. Its native currency is Ether (ETH), used to pay for computation (gas). Since the Merge in September 2022 it uses proof of stake. It is the largest platform for tokens, DeFi, NFTs and layer 2 networks.

## 17: What is a smart contract?

A smart contract is a program stored on a blockchain. It has code and its own storage, and it runs when someone sends a transaction to it. Every node runs the same code and gets the same result, so nobody can change the outcome. Once deployed, the code usually can't be edited, which is why bugs in contracts are such a big deal.

## 18: What is Solidity?

Solidity is the most popular language for writing smart contracts on Ethereum and other EVM chains. It looks a bit like JavaScript and C++, has static types, and compiles to EVM bytecode. A minimal contract looks like this:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Counter {
    uint256 public count;

    function increment() external {
        count += 1;
    }
}
```

## 19: What is the EVM?

The EVM (Ethereum Virtual Machine) is the runtime that executes smart contract bytecode on Ethereum. It is a stack-based machine where every instruction (opcode) has a gas cost. Every node runs the same EVM, so every node gets the same result for the same transaction. Many other chains, like Polygon, BNB Chain, Arbitrum and Base, also run the EVM, which is why the same Solidity code often works on all of them.

## 20: What is gas?

Gas is the unit that measures how much computation and storage a transaction uses on Ethereum. Each EVM operation costs a set amount of gas; a simple ETH transfer costs 21,000 gas. You pay for gas in ETH, so the fee is roughly gas used times the gas price. Gas stops infinite loops and makes people pay for the load they put on the network.

## 21: What are gwei and wei?

Wei is the smallest unit of ETH: 1 ETH = 10^18 wei. Gwei is 10^9 wei, and gas prices are usually shown in gwei because the numbers are easier to read. In code you should always work in wei with big integers, and only convert to ETH for display.

```js
import { parseEther, formatUnits } from "ethers";

const wei = parseEther("0.5"); // 500000000000000000n
console.log(formatUnits(wei, "gwei")); // "500000000.0"
```

## 22: What is a wallet?

A wallet is software or hardware that holds your private keys and lets you sign transactions. It does not actually "store" coins; the coins are on the chain, and the wallet holds the keys that prove you own them. Examples are MetaMask, Rabby, Coinbase Wallet, and hardware wallets like Ledger and Trezor.

## 23: What is a private key?

A private key is a large secret number that controls an account. Anyone who has it can sign transactions and move the funds, and if you lose it, nobody can recover it for you. On Ethereum and Bitcoin it is a 256-bit number. It should never be shared, put in source code, or sent to a server.

## 24: What is a public key?

The public key is derived from the private key with elliptic curve math, and it can be shared safely. Others use it to check that a signature was made by the matching private key. Going from the public key back to the private key is not practically possible. On Ethereum, the address is made from the public key.

## 25: What is a blockchain address?

An address is a short public identifier for an account, like an account number. On Ethereum it is the last 20 bytes of the Keccak-256 hash of the public key, written as 40 hex characters with a 0x prefix. Bitcoin addresses come in several formats; modern ones start with bc1. You share your address so people can send you funds.

## 26: What is a seed phrase?

A seed phrase (mnemonic) is a list of 12 or 24 common words that encodes the master secret of a wallet, following the BIP-39 standard. From that one phrase, the wallet can derive many private keys. Writing the words down on paper is the usual backup. Whoever has the seed phrase controls every account in that wallet.

## 27: What is the difference between a custodial and a non-custodial wallet?

In a custodial wallet, a company like an exchange holds the keys for you, so you log in with a password and they can freeze or lose your funds. In a non-custodial wallet, you hold the keys yourself, so you have full control and full responsibility. The common saying is "not your keys, not your coins".

## 28: What is a hot wallet versus a cold wallet?

A hot wallet keeps keys on a device connected to the internet, like a browser extension or phone app. It is handy for daily use but more exposed to hacks. A cold wallet keeps keys offline, like a hardware wallet or a paper backup, and is used for larger amounts. Many people keep a small balance hot and the rest cold.

## 29: What is a consensus mechanism?

A consensus mechanism is the set of rules nodes use to agree on which blocks are valid and in what order. Since there is no central server, the network needs a way to pick who adds the next block and to settle conflicts. The two main families are proof of work and proof of stake.

## 30: What is proof of work?

In proof of work (PoW), miners compete to find a number (nonce) that makes the block's hash lower than a target. The only way is to try billions of guesses, which costs electricity and hardware. The first miner to find one gets to add the block and earn a reward. Bitcoin uses PoW; attacking it would require more computing power than the rest of the network combined.

## 31: What is proof of stake?

In proof of stake (PoS), validators lock up coins as a deposit (stake) instead of burning electricity. The protocol picks validators to propose and vote on blocks, and those who break the rules can lose part of their stake (slashing). Ethereum has used PoS since the Merge in 2022, which cut its energy use by about 99.9%.

## 32: What is mining?

Mining is the process of creating new blocks in a proof of work chain. Miners gather pending transactions, build a block, and keep hashing it with different nonces until they hit the target. The winner gets the block reward plus the fees in that block. Today Bitcoin mining is done with special chips called ASICs.

## 33: What is a validator?

A validator is a participant in a proof of stake chain that stakes coins and runs software to propose blocks and vote on (attest to) blocks made by others. On Ethereum, running a validator needs at least 32 ETH. Validators earn rewards for doing their job and lose some stake for being offline or acting dishonestly.

## 34: What is staking?

Staking means locking up coins to help secure a proof of stake network and earn rewards in return. You can run your own validator, use a staking service, or use liquid staking protocols like Lido that give you a token (stETH) you can still use elsewhere. The risk is that the stake can be slashed and, depending on the method, you may have to wait to withdraw.

## 35: What is a block reward?

A block reward is the new coins a miner or validator gets for producing a block. In Bitcoin it started at 50 BTC and is cut in half every 210,000 blocks (about every 4 years). After the April 2024 halving it is 3.125 BTC. Producers also collect the transaction fees in their block.

## 36: What is the Bitcoin halving?

The halving is the event, about every four years, when the Bitcoin block reward is cut in half. It is built into the code and makes new supply shrink over time until it reaches the 21 million cap around the year 2140. After that, miners will be paid only through fees. The latest halving happened in April 2024.

## 37: What is a transaction fee?

A transaction fee is what you pay to get your transaction included in a block. It pays block producers for their work and protects the network from spam. When many people want to transact, fees rise because space in each block is limited. On Ethereum the fee depends on gas used and the gas price; on Bitcoin it depends on the transaction's size in bytes.

## 38: What is the mempool?

The mempool (memory pool) is where pending transactions wait before they get into a block. Each node keeps its own mempool, so they can differ a little. Block producers usually pick the transactions that pay the highest fees. If the network is busy, a low-fee transaction can sit there for a long time or be dropped.

## 39: What is block time?

Block time is the average time between two blocks. Bitcoin targets 10 minutes and adjusts mining difficulty to stay near it. Ethereum has fixed slots of 12 seconds. Many layer 2 networks and newer chains produce blocks in under a second.

## 40: What is a block explorer?

A block explorer is a website that lets you search and read blockchain data: blocks, transactions, addresses, token transfers and contract code. Etherscan is the best known for Ethereum, and mempool.space is popular for Bitcoin. Developers use explorers to check if a transaction went through, read events, and verify contract source code.

## 41: What is a public blockchain?

A public blockchain is open to everyone. Anyone can read the data, send transactions, and run a node or become a validator without asking permission. Bitcoin and Ethereum are public blockchains. They are also called permissionless.

## 42: What is a private blockchain?

A private blockchain is run by one organization that decides who can join, read and write. It is faster and gives more control, but it loses most of the trust benefits because one party is in charge. Some people argue that in many cases a normal database would do the same job.

## 43: What is a consortium blockchain?

A consortium blockchain is run by a group of known organizations, like several banks, that share control. Only approved members run nodes and validate blocks. It sits between public and private chains. Hyperledger Fabric and R3 Corda are often used for this kind of setup.

## 44: What is the difference between permissioned and permissionless blockchains?

In a permissionless chain, anyone can join, validate and transact without approval. In a permissioned chain, an authority or group controls who can take part and in what role. Permissionless chains are more open and resistant to censorship; permissioned chains are easier to make fast and compliant with regulations.

## 45: What is a fork in blockchain?

A fork happens when the chain splits into two paths. It can be a short accidental split, when two blocks are made at almost the same time, which sorts itself out quickly. Or it can be a change to the protocol rules, which is called a soft fork or a hard fork depending on whether old nodes still accept the new blocks.

## 46: What is a hard fork?

A hard fork is a rule change that old nodes don't accept. Every node must upgrade, or it ends up on a separate chain. Ethereum's network upgrades, like Dencun, Pectra and Fusaka, are planned hard forks that almost everyone upgrades for. A contested hard fork can create two lasting chains, like Ethereum and Ethereum Classic in 2016.

## 47: What is a soft fork?

A soft fork is a rule change that makes the rules stricter, so blocks made by upgraded nodes are still valid for old nodes. Old nodes can keep running, though they don't fully check the new rules. Bitcoin prefers soft forks; SegWit (2017) and Taproot (2021) were both soft forks.

## 48: What is a dApp?

A dApp (decentralized application) is an app whose main logic or data lives in smart contracts on a blockchain. Usually it has a normal web front end that talks to the contracts through the user's wallet. Uniswap is a well-known example. The front end is often still hosted on a regular server, so "decentralized" mostly applies to the back end.

## 49: What is Web3?

Web3 is a loose term for apps built on blockchains where users hold their own assets and identity through wallets, instead of having accounts stored by a company. In Web2, the platform owns your data; in Web3, you own your keys and can take your assets to any app. In practice, Web3 apps still mix centralized and decentralized parts.

## 50: What is an NFT?

An NFT (non-fungible token) is a token where each unit is unique and has its own ID. It proves who owns a specific item, like a piece of digital art, a game item, a domain name, or a ticket. On Ethereum, NFTs usually follow the ERC-721 or ERC-1155 standard. The token records ownership; the file it points to is usually stored somewhere else, like IPFS.

## 51: What does fungible mean?

Fungible means every unit is the same and can be swapped one for one. One dollar is as good as any other dollar, and one USDC is as good as any other USDC. Non-fungible items are each different, like concert seats or pieces of art. ERC-20 tokens are fungible; ERC-721 tokens are not.

## 52: What is an ERC-20 token?

ERC-20 is the standard interface for fungible tokens on Ethereum. It defines functions like `balanceOf`, `transfer`, `approve`, `transferFrom` and `allowance`, plus the `Transfer` and `Approval` events. Because every ERC-20 token has the same interface, wallets and exchanges can support any new token without custom code. USDC, DAI and LINK are ERC-20 tokens.

## 53: What is an ERC-721 token?

ERC-721 is the standard for non-fungible tokens. Each token has a unique `tokenId` and exactly one owner. Key functions are `ownerOf`, `transferFrom`, `safeTransferFrom`, `approve` and `setApprovalForAll`. Most NFT collections, like profile picture projects, use ERC-721.

## 54: What is an ERC-1155 token?

ERC-1155 is a multi-token standard: one contract can hold many token types, and each type can be fungible or non-fungible. It supports batch transfers, so moving 10 different items costs much less gas than 10 separate transfers. It is popular in games, where you have both currencies and unique items.

## 55: What is an EIP?

An EIP (Ethereum Improvement Proposal) is a design document that proposes a change to Ethereum. Core EIPs change the protocol and ship in hard forks, like EIP-1559 (fee market) or EIP-4844 (blobs). ERCs are the subset that define application standards, like ERC-20. Bitcoin has a similar process called BIPs.

## 56: What is a stablecoin?

A stablecoin is a token designed to keep a stable price, usually 1 US dollar. Fiat-backed stablecoins like USDC and USDT hold cash and bonds in a bank. Crypto-backed ones like DAI (now also USDS) are backed by more crypto than they issue. Stablecoins are used for payments, trading, and as a safe place to park value inside DeFi.

## 57: What is DeFi?

DeFi (decentralized finance) is financial services built with smart contracts instead of banks: lending, borrowing, trading, savings and derivatives. Anyone with a wallet can use them, and the rules are visible in the code. Well-known protocols are Uniswap (trading), Aave (lending) and Maker/Sky (stablecoins). The risks are smart contract bugs, hacks and market swings.

## 58: What is a DEX?

A DEX (decentralized exchange) lets users swap tokens directly from their wallets through smart contracts, without handing funds to an exchange. Most DEXs use liquidity pools and a pricing formula instead of an order book. Uniswap, Curve and PancakeSwap are examples. You keep custody of your funds until the trade happens.

## 59: What is a CEX?

A CEX (centralized exchange) is a company like Coinbase, Binance or Kraken that holds users' funds and matches buy and sell orders on its own servers. It is fast and easy to use, and it handles fiat deposits. The downside is that you trust the company with your money; failures like FTX in 2022 showed what can go wrong.

## 60: What is a DAO?

A DAO (decentralized autonomous organization) is a group that makes decisions through smart contracts and token votes instead of a board. Members propose changes, vote with governance tokens, and approved actions can run on-chain automatically. Many DeFi protocols are governed by DAOs. In practice, voting power is often concentrated in a few large holders.

## 61: What is a governance token?

A governance token gives holders voting rights in a protocol or DAO. Holders can vote on things like fee changes, treasury spending, or contract upgrades. UNI (Uniswap) and AAVE are examples. Voting power is usually proportional to the number of tokens held or delegated.

## 62: What is an oracle in blockchain?

An oracle is a service that brings outside data, like prices, weather, or sports results, onto the blockchain so smart contracts can use it. Contracts can't call web APIs themselves because every node must get the same result. Chainlink is the most used oracle network. If an oracle reports wrong data, contracts that rely on it can be exploited.

## 63: What is a layer 1?

A layer 1 is a base blockchain that handles its own security and consensus, like Bitcoin, Ethereum or Solana. It is the final source of truth for its transactions. Scaling a layer 1 directly is hard without giving up decentralization, which is why layer 2 networks were built on top.

## 64: What is a layer 2?

A layer 2 is a network that runs on top of a layer 1 to make transactions faster and cheaper. It processes many transactions off the main chain and posts compressed data or proofs back to it, so it borrows the layer 1's security. Arbitrum, Optimism, Base, zkSync and Starknet are Ethereum layer 2s. Bitcoin's Lightning Network is also a layer 2.

## 65: What is a rollup?

A rollup is a layer 2 that runs transactions off-chain, then "rolls up" many of them into a batch and posts the data to the layer 1. Because the data is on layer 1, anyone can rebuild the rollup's state and users can always get their funds out. There are two main types: optimistic rollups and zero-knowledge (ZK) rollups.

## 66: What is a sidechain?

A sidechain is a separate blockchain that runs alongside a main chain and is connected by a bridge. It has its own validators and security, so it does not inherit the main chain's security the way a rollup does. Polygon PoS started as a sidechain to Ethereum. Sidechains are cheaper but you trust their validator set.

## 67: What is a bridge?

A bridge moves assets or messages between two blockchains. A common design locks tokens on chain A and mints a wrapped version on chain B. Bridges hold large amounts of locked funds, so they are a big target; some of the largest hacks, like Ronin and Wormhole, were bridge hacks.

## 68: What is a wrapped token?

A wrapped token represents another asset on a different chain or in a different format. WBTC is Bitcoin represented as an ERC-20 on Ethereum, backed by BTC held by a custodian. WETH is ETH wrapped into an ERC-20 so it can be used by contracts that only speak ERC-20. You can usually unwrap back one to one.

## 69: What is an account on Ethereum?

An account is an entity with an address and an ETH balance. There are two kinds: externally owned accounts (EOAs), controlled by a private key, and contract accounts, controlled by their code. Each account also has a nonce, and contract accounts have code and storage.

## 70: What is an externally owned account (EOA)?

An EOA is an Ethereum account controlled by a private key, like a normal MetaMask account. Only EOAs could start transactions in the original design. It has a balance and a nonce but no code of its own. Since the Pectra upgrade (May 2025, EIP-7702), an EOA can also point to contract code so it can act like a smart wallet.

## 71: What is a contract account?

A contract account is an Ethereum account controlled by the code deployed at its address. It has no private key. It runs when it receives a transaction or a call from another contract, and it can hold ETH, tokens and its own storage. Its address is computed from the deployer's address and nonce (or from a salt with CREATE2).

## 72: What is a nonce on Ethereum?

For an account, the nonce is a counter of how many transactions it has sent. Each new transaction must use the next nonce, which keeps transactions in order and stops the same signed transaction from being replayed. In proof of work, "nonce" also means the number miners change while searching for a valid block hash.

## 73: What is a transaction hash?

A transaction hash is the unique ID of a transaction, computed by hashing the signed transaction data. You get it right after you send a transaction, and you use it to look the transaction up on a block explorer or to wait for its receipt. It looks like 0x followed by 64 hex characters.

## 74: What is a transaction receipt?

A receipt is the record created after a transaction is mined. It includes the status (1 for success, 0 for failure), gas used, the block number, the logs (events) emitted, and the contract address if a contract was deployed. Front ends read the receipt to know if an action worked.

```js
const tx = await signer.sendTransaction({ to, value: parseEther("0.01") });
const receipt = await tx.wait();
console.log(receipt.status, receipt.gasUsed);
```

## 75: What is a confirmation?

A confirmation is a block added on top of the block that has your transaction. One confirmation means it is in the latest block; each extra block makes it harder to undo. Bitcoin users often wait for 6 confirmations for large payments. On Ethereum, people usually look at whether the block is "finalized", which takes about 13 minutes.

## 76: What is finality?

Finality is the point after which a transaction can't be reversed. In proof of work, finality is probabilistic: the deeper the block, the less likely a reorg. Ethereum's proof of stake gives economic finality: after two epochs (about 12.8 minutes), reversing a block would require burning at least a third of all staked ETH. Some chains, like those using BFT consensus, finalize in one block.

## 77: What is the double spending problem?

Double spending is trying to spend the same money twice. With digital files, copying is easy, so a digital coin needs a way to make sure each unit is only spent once. Blockchains solve this by having everyone agree on a single order of transactions; once one spend is confirmed, the second one is invalid.

## 78: What is a 51% attack?

A 51% attack is when one party controls most of the mining power (PoW) or stake (PoS). They could then reorder or censor transactions and reverse their own recent payments to double spend. They still can't steal coins from other people's addresses or create coins outside the rules. Big chains like Bitcoin make this very expensive; small chains have been hit by it.

## 79: What is a Merkle tree?

A Merkle tree is a tree of hashes. Each leaf is the hash of a piece of data (like a transaction), and each parent is the hash of its two children, up to a single root hash. The root sums up all the data. You can prove that one item is in the set by giving just a few hashes along its path, instead of the whole set.

## 80: What is a Merkle root?

The Merkle root is the single hash at the top of a Merkle tree. A block header stores the Merkle root of its transactions, so the header alone commits to every transaction in the block. If any transaction changes, the root changes too.

## 81: What is a digital signature?

A digital signature proves that a message was approved by the holder of a private key and was not changed after signing. Anyone can check it with the public key. In blockchains, every transaction is signed by the sender. Bitcoin and Ethereum use ECDSA on the secp256k1 curve, and Bitcoin's Taproot also uses Schnorr signatures.

## 82: What is public key cryptography?

Public key (asymmetric) cryptography uses a key pair: a private key you keep secret and a public key you can share. You sign with the private key and others verify with the public key. It is the base of blockchain ownership: whoever can sign for an address controls it.

## 83: What is a hardware wallet?

A hardware wallet is a small device that keeps private keys inside a secure chip. When you send a transaction, the device shows the details on its own screen and signs inside the device, so the key never touches your computer. Ledger and Trezor are common brands. It protects you from malware, but you still need to check what you are signing.

## 84: What is MetaMask?

MetaMask is a popular non-custodial wallet, available as a browser extension and mobile app. It stores keys, shows balances, and lets websites ask the user to connect and sign transactions. It injects a provider at `window.ethereum` that dApps use to talk to it.

## 85: What is a testnet?

A testnet is a copy of a blockchain used for testing, where the coins have no real value. Developers deploy and test contracts there before going to mainnet. For Ethereum, the main testnets today are Sepolia (for apps) and Hoodi (for validators and staking). You get test ETH from faucets.

## 86: What is a mainnet?

Mainnet is the real production network where transactions use real money. When a project "launches on mainnet", its contracts are live and users risk real funds. Ethereum mainnet has chain ID 1.

## 87: What is a faucet?

A faucet is a website or service that gives out small amounts of free testnet coins so developers can pay for gas while testing. Many faucets ask you to log in or hold a small mainnet balance to stop abuse.

## 88: What is a chain ID?

A chain ID is a number that identifies a network, like 1 for Ethereum mainnet, 11155111 for Sepolia, 8453 for Base and 42161 for Arbitrum One. It is included in signed transactions (EIP-155), so a transaction signed for one chain can't be replayed on another. Wallets also use it to know which network the user is on.

## 89: What is an ABI?

An ABI (Application Binary Interface) is a JSON description of a contract's functions, events and errors, with their names and types. Libraries use it to encode your function calls into bytes the EVM understands and to decode the results. The compiler generates it for you.

```js
const abi = [
  "function balanceOf(address owner) view returns (uint256)",
  "event Transfer(address indexed from, address indexed to, uint256 value)",
];
```

## 90: What is bytecode?

Bytecode is the compiled form of a smart contract: a list of EVM opcodes in hex. There is creation bytecode, which runs once at deploy time and returns the runtime bytecode, and runtime bytecode, which is what's stored on-chain and runs on each call. You can see a contract's bytecode with `eth_getCode`.

## 91: What is an RPC node or provider?

An RPC provider is a node that your app talks to through the JSON-RPC API to read chain data and send transactions. You can run your own node or use a hosted provider like Alchemy, Infura or QuickNode. Your front end or back end uses its URL to make calls like `eth_blockNumber` or `eth_call`.

## 92: What is JSON-RPC in Ethereum?

JSON-RPC is the standard API that every Ethereum node exposes. You send a JSON object with a method name and parameters, and get a JSON response. Libraries like ethers.js and viem wrap it for you.

```js
const res = await fetch(RPC_URL, {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "eth_blockNumber",
    params: [],
  }),
});
console.log(BigInt((await res.json()).result));
```

## 93: What is ethers.js?

ethers.js is a JavaScript library for working with Ethereum. It gives you providers (to read the chain), signers (to sign and send), contract objects built from an ABI, and helpers for units, hashing and ABI encoding. Version 6 uses native `BigInt` for numbers.

```js
import { JsonRpcProvider, formatEther } from "ethers";

const provider = new JsonRpcProvider(process.env.RPC_URL);
const balance = await provider.getBalance(
  "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
);
console.log(formatEther(balance));
```

## 94: What is viem?

viem is a newer TypeScript library for Ethereum, often used as an alternative to ethers.js. It splits functionality into a public client (read), a wallet client (write), and plain functions, has strong type inference from ABIs, and is small and fast. It is the base of wagmi, the popular React hooks library.

```js
import { createPublicClient, http } from "viem";
import { mainnet } from "viem/chains";

const client = createPublicClient({ chain: mainnet, transport: http() });
console.log(await client.getBlockNumber());
```

## 95: What is web3.js?

web3.js was the original JavaScript library for Ethereum. It was widely used for years, and you will still see it in older projects and tutorials. The project was sunset in March 2025, so new projects should use viem or ethers.js instead.

## 96: What is Hardhat?

Hardhat is a JavaScript/TypeScript development environment for Ethereum. It compiles contracts, runs a local network, runs tests, and has plugins for deployment and verification. Hardhat 3, released in 2025, added Solidity tests next to the TypeScript ones and uses Hardhat Ignition for deployments.

## 97: What is Foundry?

Foundry is a fast toolkit for smart contract development written in Rust. It includes `forge` (build and test, with tests written in Solidity), `cast` (command line calls to the chain), `anvil` (a local node), and `chisel` (a Solidity REPL). It is very popular for testing because it is fast and supports fuzzing out of the box.

```bash
forge init my-project
forge build
forge test -vvv
```

## 98: What is Remix?

Remix is a browser-based IDE for Solidity at remix.ethereum.org. You can write, compile, deploy and debug contracts without installing anything. It is great for learning and quick experiments, but real projects usually move to Foundry or Hardhat.

## 99: What is IPFS?

IPFS (InterPlanetary File System) is a peer-to-peer network for storing and sharing files. Files are addressed by a hash of their content (a CID), not by a server location, so the same file always has the same address. NFTs often store metadata and images on IPFS. Files only stay available if someone keeps "pinning" them.

## 100: Why is storing large data on-chain a bad idea?

Every byte you store is kept by every full node forever, so it is very expensive. On Ethereum, writing a new 32-byte storage slot costs about 20,000 gas. The usual pattern is to store the file in IPFS, Arweave or a normal server and store only its hash or ID on-chain, so you can still prove the file wasn't changed.

## 101: What is a token allowance?

An allowance is permission you give a contract (or another address) to spend up to a set amount of your ERC-20 tokens. You call `approve(spender, amount)`, and later the spender calls `transferFrom`. This is how a DEX takes your tokens during a swap. Old unused allowances are a risk, so it is good practice to revoke them.

## 102: What is a smart contract event?

An event is a log entry a contract writes during a transaction. Events are stored in the transaction receipt, not in contract storage, so they are cheap but contracts can't read them. Front ends and indexers listen to events to know what happened.

```solidity
event Deposited(address indexed user, uint256 amount);

function deposit() external payable {
    emit Deposited(msg.sender, msg.value);
}
```

## 103: What is msg.sender?

`msg.sender` is the address that called the current function. If a user calls contract A directly, it is the user's address. If contract A calls contract B, then inside B `msg.sender` is A. It is the main value used for access control in Solidity.

## 104: What is msg.value?

`msg.value` is the amount of ETH, in wei, sent with the current call. A function can only receive ETH if it is marked `payable`; otherwise the call reverts when value is attached.

## 105: What does payable mean in Solidity?

`payable` marks a function or an address that can receive ETH. A `payable` function accepts `msg.value`. An `address payable` has `transfer` and `send` methods, and you can turn an address into one with `payable(addr)`.

```solidity
function buy() external payable {
    require(msg.value == 0.1 ether, "wrong price");
}
```

## 106: What are the main data types in Solidity?

Value types include `bool`, signed and unsigned integers (`int8` to `int256`, `uint8` to `uint256`), `address`, fixed-size `bytes1` to `bytes32`, and `enum`. Reference types are arrays, `bytes`, `string`, `struct` and `mapping`. `uint256` is the most common integer type because the EVM works in 32-byte words.

## 107: What is a mapping in Solidity?

A mapping is a key-value store, like a hash map. Every possible key exists and returns the default value (zero) if never set. You can't loop over a mapping or get its length, so if you need that, keep a separate array of keys.

```solidity
mapping(address => uint256) public balances;

function credit(address user, uint256 amount) external {
    balances[user] += amount;
}
```

## 108: What is a struct in Solidity?

A struct is a custom type that groups several fields together, like an object.

```solidity
struct Order {
    address buyer;
    uint256 amount;
    bool paid;
}

mapping(uint256 => Order) public orders;
```

## 109: What are the function visibility types in Solidity?

`public` functions can be called from outside and inside. `external` functions can only be called from outside (or with `this.f()`). `internal` functions can be called from the contract and contracts that inherit it. `private` functions can only be called from the contract that defines them. Note that `private` does not hide data: everything on-chain is readable.

## 110: What is the difference between view and pure functions?

A `view` function reads state but does not change it. A `pure` function neither reads nor changes state; it only works with its inputs. Both are free when called off-chain with `eth_call`, because no transaction is needed. If called from inside a transaction, they still cost gas.

## 111: What is a constructor in Solidity?

The constructor is a special function that runs once when the contract is deployed. It is used to set initial values, like the owner. Its code is part of the creation bytecode and is not stored on-chain afterwards.

```solidity
address public owner;

constructor() {
    owner = msg.sender;
}
```

## 112: What does require do in Solidity?

`require(condition, message)` checks a condition and reverts the whole call if it is false, undoing all state changes. It is used to validate inputs and permissions. Since Solidity 0.8.26 you can also pass a custom error instead of a string.

```solidity
error NotOwner();

function withdraw() external {
    require(msg.sender == owner, NotOwner());
}
```

## 113: What does revert mean?

A revert stops execution and rolls back all state changes made in the current call. The caller gets an error message or custom error data, and the gas already used is still paid. You trigger it with `require`, `revert`, failed `assert`, or errors like a failed external call.

## 114: What is a modifier in Solidity?

A modifier is reusable code that runs before (and optionally after) a function body, often to check permissions. The `_` marks where the function body goes.

```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "not owner");
    _;
}

function pause() external onlyOwner {
    paused = true;
}
```

## 115: What is OpenZeppelin?

OpenZeppelin Contracts is a widely used library of audited Solidity code: ERC-20, ERC-721 and ERC-1155 implementations, access control (`Ownable`, `AccessControl`), security helpers (`ReentrancyGuard`, `Pausable`) and upgradeable proxies. Using it saves time and avoids common mistakes. You install it with `npm install @openzeppelin/contracts` or as a Foundry dependency.

```solidity
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor() ERC20("My Token", "MTK") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }
}
```

## 116: Can a smart contract be changed after deployment?

Not directly: the code at an address can't be edited. To allow changes, developers use the proxy pattern, where users call a proxy contract that forwards calls to an implementation contract whose address can be swapped. This adds flexibility but also means someone holds the power to change the code, which users have to trust.

## 117: What does deploying a contract mean?

Deploying means sending a transaction with no `to` address whose data is the contract's creation bytecode (plus constructor arguments). The EVM runs it, stores the resulting runtime code at a new address, and the receipt shows that address. Deployment costs gas like any other transaction, and more for bigger contracts.

## 118: What is contract verification?

Verification means uploading your contract's source code and compiler settings to a block explorer like Etherscan or to Sourcify. The service compiles it and checks that the bytecode matches what's on-chain. After that, anyone can read the source and use the "Read/Write Contract" tabs. Users trust unverified contracts much less.

## 119: What is a public ledger?

A public ledger is a record that anyone can read. On public blockchains, every transaction, balance and contract is visible to everyone. This gives transparency but also means privacy is weak: addresses are pseudonymous, not anonymous.

## 120: Is blockchain anonymous?

Most blockchains are pseudonymous, not anonymous. Your address isn't tied to your name by default, but every transaction is public forever. Once your address is linked to you, for example through an exchange with identity checks, your whole history can be traced. Privacy coins like Monero and tools using zero-knowledge proofs try to fix this.

## 121: What is a cryptocurrency exchange?

An exchange is a place where you trade crypto for other crypto or for fiat money. It can be centralized (a company like Coinbase) or decentralized (smart contracts like Uniswap). Centralized exchanges are usually how people first turn dollars or euros into crypto.

## 122: What is market capitalization in crypto?

Market cap is the current price times the circulating supply of a coin or token. It gives a rough idea of a project's size. It can be misleading for tokens where only a small part of the supply is circulating, so people also look at fully diluted valuation (price times max supply).

## 123: What is tokenomics?

Tokenomics is how a token's supply and use are designed: total supply, how new tokens are issued, who got tokens at launch, vesting schedules, burns, and what the token is used for. Good tokenomics give people a real reason to hold and use the token. Bad tokenomics often mean early insiders sell to later buyers.

## 124: What is a token burn?

Burning means sending tokens to an address nobody controls, or calling a burn function, so they are removed from supply for good. Some projects burn to reduce supply. Ethereum burns the base fee of every transaction under EIP-1559, which can make ETH supply shrink when the network is busy.

## 125: What is an airdrop?

An airdrop is a free distribution of tokens to many addresses, often to reward early users or to spread out governance power. Users usually have to claim the tokens through a website. Scammers also send fake "airdrop" tokens that lead to phishing sites, so you should never interact with tokens you didn't expect.

## 126: What is a smart contract wallet?

A smart contract wallet is a wallet whose account is a contract, not a plain key pair. Because it's code, it can do things a normal EOA can't: multiple signers, spending limits, social recovery, paying gas in tokens, and batching several actions. Safe (formerly Gnosis Safe) is the best-known one. ERC-4337 made them work without changing the core protocol.

## 127: What is a multisig wallet?

A multisig wallet needs approval from several keys to move funds, like 3 out of 5 owners. It protects against a single lost or stolen key and is the standard for team and DAO treasuries. On Ethereum, Safe is the most used multisig; on Bitcoin, multisig is built into the scripting system.

## 128: What is a seed phrase used for when you get a new device?

You enter the seed phrase into a new wallet app and it derives all the same private keys and addresses again, so your funds show up. This works across different wallet apps because the derivation follows standards (BIP-39, BIP-32 and BIP-44). That's also why anyone who sees your phrase can take everything.

## 129: What is an ENS name?

ENS (Ethereum Name Service) maps readable names like `vitalik.eth` to addresses and other data. Instead of copying a long hex address, users can send funds to a name. ENS names are NFTs that you own and renew. Libraries can resolve them for you.

```js
const address = await provider.resolveName("vitalik.eth");
```

## 130: What is a token decimals value?

ERC-20 balances are stored as whole integers, and `decimals` tells you where to put the decimal point for display. Most tokens use 18, but USDC and USDT use 6. A balance of `1500000` for USDC means 1.5 USDC. Always read `decimals` from the contract instead of assuming 18.

```js
import { formatUnits } from "ethers";
const pretty = formatUnits(rawBalance, await token.decimals());
```

## 131: What is a liquidity pool?

A liquidity pool is a smart contract holding two (or more) tokens that people can trade against. Liquidity providers deposit both tokens and get a share of trading fees. The price comes from the ratio of tokens in the pool, using a formula. Pools are what make most DEXs work.

## 132: What is an automated market maker (AMM)?

An AMM is a DEX that prices trades with a formula instead of matching buyers and sellers. Uniswap V2 uses `x * y = k`: the product of the two token reserves stays the same after a trade (before fees). Buying token X removes X and adds Y, which makes X more expensive. Anyone can trade at any time as long as the pool has liquidity.

## 133: What is slippage?

Slippage is the difference between the price you expected and the price you actually got. It happens because the pool's price moves as your trade goes through, or because other trades land before yours. DEX interfaces let you set a slippage tolerance, like 0.5%, and the trade reverts if the price moves more than that.

## 134: What is a proof of stake validator's stake on Ethereum?

To run a validator on Ethereum you deposit at least 32 ETH into the deposit contract. Since the Pectra upgrade, a single validator can have an effective balance of up to 2,048 ETH if it uses the newer withdrawal credentials, so big stakers can run fewer validators. Rewards and penalties are applied to this balance.

## 135: What is slashing?

Slashing is a penalty for a validator that breaks the rules in a way that could harm the chain, such as signing two different blocks for the same slot or making conflicting votes. Part of the stake is burned and the validator is forced to exit. Being offline is not slashing; it only leads to small penalties.

## 136: What was the Merge?

The Merge was the switch of Ethereum from proof of work to proof of stake on September 15, 2022. The original execution chain joined the Beacon Chain, which had been running proof of stake since December 2020. Mining ended, energy use dropped by about 99.9%, and new ETH issuance fell a lot.

## 137: What is the Beacon Chain?

The Beacon Chain is Ethereum's proof of stake consensus layer. It manages validators, picks block proposers, collects votes and finalizes blocks. Since the Merge, every Ethereum node is two programs: an execution client (like Geth) and a consensus client (like Lighthouse or Prysm) following the Beacon Chain.

## 138: What are execution and consensus clients?

The execution client (Geth, Nethermind, Besu, Erigon, Reth) runs transactions in the EVM, keeps the state, and serves JSON-RPC. The consensus client (Prysm, Lighthouse, Teku, Nimbus, Lodestar, Grandine) handles proof of stake: following the Beacon Chain, proposer selection, attestations and finality. They talk to each other through the Engine API. Running a node means running one of each.

## 139: What is client diversity and why does it matter?

Client diversity means validators use many different client implementations instead of one. If one client has a bug and most of the network uses it, the bug could split the chain or even finalize a wrong block. If no client has more than a third of validators, a bug in one client can't break finality.

## 140: What is a slot and an epoch on Ethereum?

A slot is a 12-second window where one validator can propose a block. An epoch is 32 slots, about 6.4 minutes. Validators are split into committees per epoch to vote, and finality is reached at epoch boundaries, usually after two epochs.

## 141: What is the Bitcoin UTXO model?

UTXO stands for unspent transaction output. In Bitcoin, coins are not account balances; they are outputs of past transactions that haven't been spent yet. A new transaction consumes some UTXOs as inputs and creates new outputs, often one to the receiver and one back to yourself as change. Your "balance" is the sum of UTXOs your keys can spend.

## 142: What is the account model?

In the account model, used by Ethereum, the chain keeps a balance (and nonce, code and storage) for each address, like a bank account. A transfer just lowers one balance and raises another. It is simpler for smart contracts than the UTXO model, because contracts have their own persistent state.

## 143: What is Satoshi?

A satoshi (sat) is the smallest unit of Bitcoin: 1 BTC = 100,000,000 sats. Fees are usually shown in sats per virtual byte (sat/vB). The name honors Bitcoin's anonymous creator, Satoshi Nakamoto.

## 144: What is the Lightning Network?

The Lightning Network is a layer 2 on Bitcoin for fast, cheap payments. Two users open a payment channel by locking BTC in an on-chain transaction, then trade signed updates off-chain as often as they want. Payments can route through several channels. Only opening and closing the channel touch the main chain.

## 145: What is Solana?

Solana is a high-throughput layer 1 that aims for fast blocks (about 400 ms slots) and low fees. Programs are usually written in Rust, often with the Anchor framework, and it uses an account model where programs are stateless and data lives in separate accounts. It runs transactions in parallel because each transaction declares which accounts it touches.

## 146: What are some well-known EVM-compatible chains?

Besides Ethereum, popular EVM chains include BNB Chain, Polygon PoS, Avalanche C-Chain, and layer 2s like Arbitrum, Optimism, Base, Linea, Scroll and zkSync Era. The same Solidity code and tools (MetaMask, Foundry, ethers.js) work on all of them, usually with only a different RPC URL and chain ID.

## 147: What is a smart contract audit?

An audit is a security review of smart contract code by specialists before launch. Auditors look for bugs like reentrancy, access control mistakes, math errors and economic attacks, and write a report with findings. An audit lowers risk but does not guarantee the code is safe; many hacked protocols had been audited.

## 148: What is a rug pull?

A rug pull is a scam where the creators of a project suddenly take the funds, for example by draining the liquidity pool, minting a huge amount of tokens, or using an admin function to steal deposits. Signs include anonymous teams, unverified contracts, unlimited mint functions, and liquidity that isn't locked.

## 149: What is a phishing attack in crypto?

Crypto phishing tricks users into signing something harmful or giving away their seed phrase. Common forms are fake websites that look like real dApps, fake support accounts asking for the seed phrase, and signature requests that secretly approve a scammer to spend tokens. Always check the site URL and read what a wallet asks you to sign.

## 150: What are some real uses of blockchain besides cryptocurrency?

Common uses are stablecoins for cross-border payments, tokenized real-world assets like treasury bonds, supply chain tracking, digital identity and credentials, NFTs for tickets and game items, and DAOs for shared treasuries. A good question to ask is whether the use case really needs several parties who don't trust each other; if not, a normal database is usually better.

# Moderate Questions (151-300)

## 151: How does EIP-1559 change how transaction fees work?

EIP-1559 (London upgrade, 2021) split the fee into a base fee and a priority fee (tip). The base fee is set by the protocol for each block, rises when blocks are more than half full and falls when they are less, and it is burned. The tip goes to the block proposer. You set `maxFeePerGas` (the most you'll pay in total) and `maxPriorityFeePerGas` (the tip), and you pay `min(maxFee, baseFee + tip)` per gas.

## 152: How do you set gas fees for a transaction with ethers.js?

You can let the library fill them in, or read current values with `getFeeData()` and set them yourself. Set `maxFeePerGas` with headroom over the current base fee, since the base fee can rise up to 12.5% per block.

```js
const fee = await provider.getFeeData();
const tx = await signer.sendTransaction({
  to,
  value: parseEther("0.01"),
  maxPriorityFeePerGas: fee.maxPriorityFeePerGas,
  maxFeePerGas: fee.maxFeePerGas,
});
```

## 153: What is the gas limit of a transaction versus the block gas limit?

The transaction gas limit is the most gas you allow your transaction to use; if it runs out, it reverts and you still pay for the gas used. The block gas limit is the most gas all transactions in one block can use together. Validators vote the block gas limit up or down slowly; on Ethereum it was 30 million for years, was raised to 60 million during 2025, and core developers plan to keep raising it.

## 154: How do you estimate gas for a transaction?

Call `eth_estimateGas`, which simulates the transaction against the latest state and returns the gas it would use. Add a small buffer, because state can change before your transaction is mined. If estimation fails, the transaction would most likely revert, which is a useful early warning.

```js
const gas = await contract.mint.estimateGas(to, amount);
const tx = await contract.mint(to, amount, { gasLimit: (gas * 120n) / 100n });
```

## 155: What happens to the fee if a transaction reverts?

You still pay for all the gas used up to the point of the revert, because validators did the work. State changes are rolled back, but the nonce is still used and the fee is still taken. That's why front ends simulate transactions first to warn users.

## 156: How do you connect a web app to MetaMask?

Use the EIP-1193 provider that the wallet injects, ask for accounts, and wrap it in a library. In real apps, use EIP-6963 to discover all installed wallets instead of relying only on `window.ethereum`.

```js
import { BrowserProvider } from "ethers";

const provider = new BrowserProvider(window.ethereum);
const signer = await provider.getSigner(); // prompts the user to connect
console.log(await signer.getAddress());
```

## 157: What is EIP-1193?

EIP-1193 defines the standard JavaScript interface for Ethereum providers in the browser. It has one main method, `request({ method, params })`, and events like `accountsChanged`, `chainChanged`, `connect` and `disconnect`. All major wallets follow it, so libraries can work with any of them.

```js
const accounts = await window.ethereum.request({
  method: "eth_requestAccounts",
});
window.ethereum.on("chainChanged", () => window.location.reload());
```

## 158: What is EIP-6963 and what problem does it solve?

When several wallet extensions are installed, they fight over `window.ethereum` and only one wins. EIP-6963 lets each wallet announce itself through window events with its name, icon and provider, so the app can show a list and let the user pick. Libraries like wagmi and RainbowKit support it out of the box.

```js
window.addEventListener("eip6963:announceProvider", (event) => {
  const { info, provider } = event.detail;
  console.log(info.name, info.rdns);
});
window.dispatchEvent(new Event("eip6963:requestProvider"));
```

## 159: What is wagmi?

wagmi is a library of React hooks for Ethereum built on viem. It handles wallet connections, account and chain state, reading contracts, sending transactions and caching (through TanStack Query). Hooks like `useAccount`, `useReadContract` and `useWriteContract` save a lot of boilerplate.

```jsx
const { data: balance } = useReadContract({
  address: tokenAddress,
  abi: erc20Abi,
  functionName: "balanceOf",
  args: [account],
});
```

## 160: What is WalletConnect?

WalletConnect (now Reown) is a protocol that connects dApps to mobile wallets. The dApp shows a QR code or deep link, the wallet scans it, and they talk through an encrypted relay server. It lets users on desktop sites sign with their phone wallet.

## 161: How do you read data from a smart contract with ethers.js?

Create a `Contract` with the address, ABI and a provider, then call view functions like normal async functions. Reads use `eth_call` and cost no gas.

```js
import { Contract, JsonRpcProvider } from "ethers";

const provider = new JsonRpcProvider(process.env.RPC_URL);
const token = new Contract(
  tokenAddress,
  ["function totalSupply() view returns (uint256)"],
  provider,
);
console.log(await token.totalSupply());
```

## 162: How do you send a transaction to a contract with viem?

Use a wallet client with an account, call `writeContract`, and wait for the receipt with a public client. It's good practice to call `simulateContract` first to catch reverts.

```js
const { request } = await publicClient.simulateContract({
  account,
  address: tokenAddress,
  abi,
  functionName: "transfer",
  args: [to, 1000n],
});
const hash = await walletClient.writeContract(request);
const receipt = await publicClient.waitForTransactionReceipt({ hash });
```

## 163: How do you listen to contract events in JavaScript?

Use `contract.on` in ethers.js or `watchContractEvent` in viem. For reliable back ends, don't rely only on live listeners, because connections drop; also poll past logs from the last processed block.

```js
token.on("Transfer", (from, to, value, event) => {
  console.log(from, to, value, event.log.transactionHash);
});
```

## 164: How do you query past events?

Use `queryFilter` in ethers.js or `getLogs`/`getContractEvents` in viem with a block range. Most providers cap how many blocks or results you can request in one call, so query in chunks.

```js
const filter = token.filters.Transfer(null, myAddress);
const events = await token.queryFilter(filter, fromBlock, toBlock);
```

## 165: What are indexed event parameters?

Up to three event parameters can be marked `indexed`. They go into the log's topics instead of its data, so nodes can filter on them quickly. For example, you can find all `Transfer` events to one address. Indexed dynamic types like `string` are stored as their hash, so you can filter on them but can't read the original value from the topic.

## 166: What are the topics in an Ethereum log?

A log has up to four topics and a data field. For a normal event, topic 0 is the Keccak-256 hash of the event signature, like `Transfer(address,address,uint256)`. Topics 1-3 are the indexed parameters. Non-indexed parameters are ABI-encoded in the data field. Anonymous events skip topic 0.

## 167: What is a function selector?

The function selector is the first 4 bytes of the Keccak-256 hash of the function signature, like `transfer(address,uint256)`, which gives `0xa9059cbb`. It's the first 4 bytes of the call data, and the contract uses it to decide which function to run. The rest of the call data is the ABI-encoded arguments.

```js
import { id } from "ethers";
console.log(id("transfer(address,uint256)").slice(0, 10)); // 0xa9059cbb
```

## 168: How does ABI encoding work?

ABI encoding turns function arguments into bytes. Static types (like `uint256`, `address`, `bool`) take exactly 32 bytes each, padded. Dynamic types (like `string`, `bytes`, arrays) put an offset in the main part and the actual length and content at the end. Libraries handle this, but knowing it helps when you debug raw call data.

```js
import { AbiCoder } from "ethers";
const data = AbiCoder.defaultAbiCoder().encode(
  ["address", "uint256"],
  [to, 100n],
);
```

## 169: What is the difference between abi.encode and abi.encodePacked?

`abi.encode` pads every value to 32 bytes and follows the standard ABI layout, so it's unambiguous. `abi.encodePacked` uses the minimum bytes with no padding for static types, so it's shorter. Never hash `encodePacked` output that has two or more dynamic values next to each other: `("ab","c")` and `("a","bc")` give the same bytes, which can lead to signature collisions.

## 170: What are custom errors in Solidity?

Custom errors are named errors declared with `error`, used with `revert` or `require`. They are cheaper than string messages because only a 4-byte selector plus arguments is returned, and they can carry useful data. Front ends decode them with the ABI.

```solidity
error InsufficientBalance(uint256 available, uint256 required);

function withdraw(uint256 amount) external {
    uint256 bal = balances[msg.sender];
    if (bal < amount) revert InsufficientBalance(bal, amount);
    balances[msg.sender] = bal - amount;
}
```

## 171: What is the difference between require, revert and assert?

`require` checks a condition, usually inputs and permissions, and reverts if it fails. `revert` stops execution unconditionally, usually inside an `if`, and is handy with custom errors. `assert` is for things that should never be false (internal invariants); when it fails, it raises a `Panic` error. All three undo state changes and refund the unused gas since Solidity 0.8.

## 172: How does Solidity 0.8 handle integer overflow?

Since Solidity 0.8.0, arithmetic is checked by default: an overflow or underflow reverts with a `Panic(0x11)` error. Before that, numbers wrapped around silently, and people used the SafeMath library. You can skip the checks with an `unchecked { }` block to save gas when you're sure it can't overflow, like a loop counter.

```solidity
for (uint256 i = 0; i < n; ) {
    // ...
    unchecked { ++i; }
}
```

## 173: What are storage, memory and calldata in Solidity?

`storage` is the contract's permanent state on-chain and is expensive to write. `memory` is temporary data that lives during one function call. `calldata` is read-only input data of an external call and is the cheapest to use for parameters. Reference types like arrays, structs and strings in function parameters must declare one of these.

```solidity
function sum(uint256[] calldata nums) external pure returns (uint256 total) {
    for (uint256 i; i < nums.length; ++i) total += nums[i];
}
```

## 174: What are constant and immutable variables?

`constant` values are fixed at compile time; `immutable` values are set once in the constructor. Neither takes a storage slot: they are written into the bytecode, so reading them is very cheap. Use them for things like fee rates, token addresses or the owner if it never changes.

```solidity
uint256 public constant MAX_SUPPLY = 10_000;
address public immutable treasury;

constructor(address _treasury) {
    treasury = _treasury;
}
```

## 175: How does inheritance work in Solidity?

A contract can inherit from one or more contracts with `is`. Functions that are meant to be overridden are marked `virtual`, and the overriding function uses `override`. With multiple inheritance, Solidity uses C3 linearization, and you list parents from "most base" to "most derived". `super` calls the next contract in that order.

```solidity
contract Base {
    function name() public pure virtual returns (string memory) { return "Base"; }
}

contract Child is Base {
    function name() public pure override returns (string memory) { return "Child"; }
}
```

## 176: What is an interface in Solidity?

An interface declares functions without implementing them, like a TypeScript type. It has no state, no constructor, and all functions are `external`. You use interfaces to call other contracts in a typed way.

```solidity
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address to, uint256 amount) external returns (bool);
}

uint256 bal = IERC20(token).balanceOf(address(this));
```

## 177: What is an abstract contract?

An abstract contract is marked `abstract` and can have functions without a body. It can't be deployed directly; another contract must inherit it and implement the missing functions. Unlike an interface, it can have state, a constructor and implemented functions.

## 178: What is a library in Solidity?

A library is reusable code that is deployed once (or inlined) and has no state of its own. Internal library functions are copied into the calling contract at compile time. With `using LibName for Type`, you can call library functions as if they were methods on that type.

```solidity
library MathLib {
    function double(uint256 x) internal pure returns (uint256) { return x * 2; }
}

contract C {
    using MathLib for uint256;
    function f(uint256 a) external pure returns (uint256) { return a.double(); }
}
```

## 179: What are receive and fallback functions?

`receive()` runs when a contract gets plain ETH with empty call data. `fallback()` runs when no function matches the selector, or when ETH is sent with data and there's no `receive`. Both must be `external`, and they need `payable` to accept ETH. If neither exists, sending plain ETH to the contract reverts.

```solidity
receive() external payable {
    emit Received(msg.sender, msg.value);
}

fallback() external payable {
    revert("unknown function");
}
```

## 180: What are the ways to send ETH from a contract and which should you use?

`transfer` and `send` forward only 2,300 gas, which can fail when the receiver is a smart wallet, so they are discouraged now. The recommended way is a low-level `call` with a check on the result, combined with reentrancy protection.

```solidity
(bool ok, ) = payable(to).call{value: amount}("");
require(ok, "ETH transfer failed");
```

## 181: How does the Ownable pattern work?

`Ownable` stores an owner address and gives an `onlyOwner` modifier for admin functions. OpenZeppelin's version takes the initial owner in the constructor and has `transferOwnership` and `renounceOwnership`. `Ownable2Step` is safer because the new owner must accept, so you can't hand ownership to a typo address.

```solidity
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

contract Vault is Ownable {
    constructor() Ownable(msg.sender) {}

    function sweep() external onlyOwner { /* ... */ }
}
```

## 182: What is role-based access control in smart contracts?

Instead of one owner, you define roles (like `MINTER_ROLE` or `PAUSER_ROLE`) and give them to addresses. OpenZeppelin's `AccessControl` provides `grantRole`, `revokeRole` and the `onlyRole` modifier. It's better than `Ownable` when different people or contracts need different powers.

```solidity
bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

function mint(address to, uint256 amount) external onlyRole(MINTER_ROLE) {
    _mint(to, amount);
}
```

## 183: How do you pause a contract in an emergency?

Inherit OpenZeppelin's `Pausable`, add `whenNotPaused` to sensitive functions, and give a trusted role the power to call `_pause()` and `_unpause()`. This lets a team stop deposits or transfers while they investigate a bug. The downside is that it adds a central point of control.

## 184: How do you write a basic test with Foundry?

Tests are Solidity contracts that inherit `Test` from forge-std. Functions starting with `test` are run by `forge test`, and cheatcodes on `vm` let you change the caller, time and more.

```solidity
import {Test} from "forge-std/Test.sol";
import {Counter} from "../src/Counter.sol";

contract CounterTest is Test {
    Counter c;

    function setUp() public { c = new Counter(); }

    function test_Increment() public {
        c.increment();
        assertEq(c.count(), 1);
    }
}
```

## 185: What are Foundry cheatcodes?

Cheatcodes are special functions on the `vm` object that change the test environment. Common ones are `vm.prank(addr)` (next call comes from `addr`), `vm.deal(addr, amount)` (set ETH balance), `vm.warp(ts)` (set block time), `vm.roll(n)` (set block number) and `vm.expectRevert(...)` (assert the next call reverts).

```solidity
function test_OnlyOwnerCanPause() public {
    vm.prank(address(0xBEEF));
    vm.expectRevert();
    vault.pause();
}
```

## 186: What is fuzz testing in smart contracts?

Fuzz testing runs a test many times with random inputs to find edge cases you didn't think of. In Foundry, any test function with parameters is a fuzz test. You can limit inputs with `bound` or `vm.assume`.

```solidity
function testFuzz_Deposit(uint96 amount) public {
    vm.deal(address(this), amount);
    vault.deposit{value: amount}();
    assertEq(vault.balanceOf(address(this)), amount);
}
```

## 187: What is invariant testing?

Invariant (stateful fuzz) testing calls random sequences of functions on your contracts and checks after each call that certain rules always hold. For example, "the sum of all user balances equals the token's total supply" or "the vault always holds at least what it owes". It finds bugs that only show up after several steps.

## 188: What is mainnet forking in testing?

Forking runs a local node that copies the state of a real network at a given block. Your tests can then interact with real deployed contracts like Uniswap or Aave without spending real money. Foundry supports `forge test --fork-url` and Anvil and Hardhat can also fork.

```bash
anvil --fork-url $MAINNET_RPC_URL --fork-block-number 21000000
```

## 189: How do you deploy a contract with Foundry?

Write a script that inherits `Script`, wrap deployment calls with `vm.startBroadcast()` and `vm.stopBroadcast()`, and run it with `forge script`. Keep the private key out of the command history by using an encrypted keystore account.

```bash
forge script script/Deploy.s.sol --rpc-url $RPC_URL --account deployer --broadcast --verify
```

## 190: How do you deploy a contract with Hardhat Ignition?

Ignition uses declarative modules that describe which contracts to deploy and how they connect. It keeps track of what was already deployed, so a failed deploy can resume.

```js
import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("TokenModule", (m) => {
  const token = m.contract("MyToken", []);
  return { token };
});
```

```bash
npx hardhat ignition deploy ignition/modules/Token.js --network sepolia
```

## 191: How should you manage private keys in a development project?

Never commit keys or put them in front end code. Use environment variables loaded from an ignored `.env` file for testnets at most, and prefer encrypted keystores (`cast wallet import`), hardware wallets, or a key management service for anything with real value. For production deployments and admin actions, use a multisig rather than a single key.

## 192: How do you handle big numbers in JavaScript blockchain code?

Token amounts in wei don't fit in a JavaScript `number` without losing precision (it is only exact up to 2^53). Use native `BigInt` (with the `n` suffix) for all on-chain values, as ethers v6 and viem do. Convert to strings for display with `formatUnits`, and never do money math with floats.

```js
const amount = parseUnits("1.5", 6); // 1500000n for USDC
const fee = (amount * 30n) / 10000n; // 0.3%
```

## 193: What is the difference between a provider and a signer?

A provider is a read-only connection to the chain: you can read balances, blocks and call view functions. A signer has a private key (or a connected wallet) and can sign messages and send transactions. In viem the same idea is the public client and the wallet client.

## 194: How do you sign a message and verify it?

Use `personal_sign` (EIP-191), which prefixes the message so it can't be a valid transaction. On the server, recover the address from the signature and compare it with the expected one.

```js
import { verifyMessage } from "ethers";

const message = "Login nonce: 8f2a1c";
const signature = await signer.signMessage(message);
const recovered = verifyMessage(message, signature);
console.log(recovered === (await signer.getAddress()));
```

## 195: What is EIP-712 typed data signing?

EIP-712 lets users sign structured data instead of a raw string. The wallet shows the fields clearly (like "spender" and "amount"), and the signature includes a domain (name, version, chain ID, contract address) so it can't be reused on another app or chain. It's used for permits, gasless orders and meta-transactions.

```js
const domain = {
  name: "MyApp",
  version: "1",
  chainId: 1,
  verifyingContract: appAddress,
};
const types = {
  Order: [
    { name: "maker", type: "address" },
    { name: "amount", type: "uint256" },
  ],
};
const signature = await signer.signTypedData(domain, types, {
  maker,
  amount: 100n,
});
```

## 196: What is Sign-In with Ethereum (SIWE)?

SIWE (EIP-4361) is a standard login message a user signs with their wallet to prove they own an address. The message includes the domain, address, a server nonce, the chain ID and an issue time. The server checks the signature, domain and nonce, then creates a normal session. It replaces passwords for Web3 apps.

## 197: What is ERC-2612 permit?

`permit` lets a token holder approve a spender with an off-chain EIP-712 signature instead of a separate `approve` transaction. The spender (or anyone) submits the signature in the same transaction as the action, saving one transaction and allowing gasless approvals. Many newer tokens support it, but not all, like USDT on Ethereum.

## 198: What is Permit2?

Permit2 is a contract by Uniswap that brings signature-based approvals to any ERC-20, even ones without `permit`. Users approve Permit2 once, then give each app a signed permission with an amount and an expiry. It improves safety because allowances can expire, but a malicious Permit2 signature is now a common phishing method.

## 199: How do you switch the user's wallet to the right network?

Call `wallet_switchEthereumChain` with the chain ID in hex. If the wallet doesn't know the chain, it returns error 4902, and you call `wallet_addEthereumChain` with the chain details.

```js
try {
  await window.ethereum.request({
    method: "wallet_switchEthereumChain",
    params: [{ chainId: "0x2105" }], // Base
  });
} catch (err) {
  if (err.code === 4902) {
    // call wallet_addEthereumChain with name, rpcUrls, nativeCurrency, blockExplorerUrls
  }
}
```

## 200: How do you handle a user rejecting a transaction?

Wallets reject with EIP-1193 error code 4001. Catch it and show a calm message instead of an error page. In ethers v6 the error code is `ACTION_REJECTED`; in viem it's a `UserRejectedRequestError`.

```js
try {
  await contract.mint(1n);
} catch (err) {
  if (err.code === "ACTION_REJECTED") showToast("Transaction cancelled");
  else throw err;
}
```

## 201: How do you decode a revert reason in the front end?

Libraries decode it if you give them the contract ABI, including custom errors. In ethers v6, a `CALL_EXCEPTION` error has `reason`, `revert` (name and args) and raw `data`. In viem, the error has `cause.data.errorName` and `args`. Simulating the call first gives you the reason before the user pays gas.

```js
try {
  await vault.withdraw.staticCall(amount);
} catch (err) {
  console.log(err.revert?.name, err.revert?.args); // e.g. InsufficientBalance [10n, 50n]
}
```

## 202: How do you wait for a transaction and handle it being replaced?

Use `tx.wait()` in ethers or `waitForTransactionReceipt` in viem. If the user speeds up or cancels the transaction in their wallet, it gets replaced by one with the same nonce and a new hash. ethers throws a `TRANSACTION_REPLACED` error with the new receipt and a `cancelled` flag; viem's waiter has an `onReplaced` callback. Handle both cases so the UI doesn't hang.

## 203: How do you speed up or cancel a pending transaction?

Send a new transaction with the same nonce and a higher fee; nodes replace the old one if the new fees are at least about 10% higher. To speed up, resend the same transaction with higher fees. To cancel, send 0 ETH to yourself with that nonce. You can't cancel a transaction that's already mined.

## 204: What does a stuck transaction mean and how does it affect later ones?

A transaction is stuck when its fee is too low to be picked up. Because nonces must be used in order, every later transaction from that account also waits behind it. Fix it by replacing the stuck one with a higher fee. Back ends that send many transactions need to track nonces themselves for this reason.

## 205: How do you manage nonces when sending many transactions from a back end?

Fetch the pending nonce once, then increase it locally for each transaction instead of asking the node every time, since parallel requests can get the same value. Keep a queue per sending address, record which nonces are pending, and watch for drops or stuck ones. ethers has a `NonceManager` wrapper for simple cases.

```js
import { NonceManager } from "ethers";
const managed = new NonceManager(wallet);
await Promise.all(
  recipients.map((to) => managed.sendTransaction({ to, value: 1n })),
);
```

## 206: What are transaction types on Ethereum?

Ethereum uses typed transactions (EIP-2718). Type 0 is legacy, type 1 adds access lists (EIP-2930), type 2 is EIP-1559 fees, type 3 carries blobs (EIP-4844), and type 4 sets EOA code (EIP-7702). Most normal transactions today are type 2.

## 207: What is an access list transaction?

An access list (EIP-2930) is a list of addresses and storage slots a transaction will touch, declared up front. Those accesses are charged a lower "warm" price during execution in exchange for a small upfront cost. It can save a bit of gas in some cross-contract calls, but the savings are small and it's rarely used directly.

## 208: What is the difference between call, staticcall and delegatecall?

`call` runs another contract's code in that contract's context, with its own storage, and can send ETH. `staticcall` is the same but any state change reverts; it's used for `view` calls. `delegatecall` runs another contract's code in the caller's context: the caller's storage, balance, `msg.sender` and `msg.value` stay the same. Proxies and libraries use `delegatecall`.

## 209: How does the proxy pattern work?

Users call a proxy contract that holds the storage. The proxy's `fallback` uses `delegatecall` to run code from an implementation contract, so the logic runs on the proxy's storage. To upgrade, the admin points the proxy to a new implementation. The implementation address is kept in a special storage slot defined by EIP-1967 so it doesn't clash with normal variables.

## 210: What is the difference between a transparent proxy and a UUPS proxy?

In a transparent proxy, the upgrade logic lives in the proxy, and admin calls are handled separately from user calls (via a `ProxyAdmin` contract). In UUPS (ERC-1822 / EIP-1967), the upgrade function lives in the implementation, which makes the proxy cheaper. With UUPS, if you deploy an implementation without the upgrade function, the contract can never be upgraded again. OpenZeppelin recommends UUPS for most new projects.

## 211: Why can't upgradeable contracts use constructors?

The constructor runs when the implementation is deployed, so it sets values in the implementation's storage, not the proxy's. Instead you use an `initialize` function called once through the proxy, protected by the `initializer` modifier. You should also call `_disableInitializers()` in the implementation's constructor so nobody can initialize it directly.

```solidity
contract VaultV1 is Initializable, OwnableUpgradeable, UUPSUpgradeable {
    /// @custom:oz-upgrades-unsafe-allow constructor
    constructor() { _disableInitializers(); }

    function initialize(address owner) public initializer {
        __Ownable_init(owner);
    }

    function _authorizeUpgrade(address) internal override onlyOwner {}
}
```

## 212: What is a storage collision in upgradeable contracts?

A storage collision happens when a new implementation lays out state variables differently from the old one, so a variable reads data that belonged to another. Rules: never reorder, remove or change the type of existing variables; only add new ones at the end. Newer OpenZeppelin contracts use ERC-7201 namespaced storage to avoid these issues, and their upgrade plugins check layouts for you.

## 213: What is the beacon proxy pattern?

In a beacon proxy, many proxies ask a single beacon contract for the current implementation address. Upgrading the beacon upgrades all those proxies at once. It's useful when a factory creates many copies of the same contract, like one vault per user.

## 214: What is a minimal proxy (clone)?

A minimal proxy (EIP-1167) is a tiny contract, about 45 bytes, that delegates every call to a fixed implementation. It's very cheap to deploy, so factories use it to create many instances. Unlike upgradeable proxies, the implementation can't be changed. OpenZeppelin's `Clones` library creates them.

```solidity
address clone = Clones.clone(implementation);
IVault(clone).initialize(msg.sender);
```

## 215: How does CREATE2 work?

`CREATE2` deploys a contract to an address computed from the deployer address, a salt, and the hash of the creation code. Since the address doesn't depend on the nonce, you can know it before deploying and deploy the same contract to the same address on many chains. It's used for counterfactual wallets and cross-chain deployments.

```solidity
Vault v = new Vault{salt: keccak256(abi.encode(user))}(user);
```

## 216: How does an ERC-20 transfer work under the hood?

The token contract keeps a `mapping(address => uint256)` of balances. `transfer(to, amount)` checks the sender has enough, lowers the sender's balance, raises the receiver's, and emits `Transfer`. No tokens actually "move" between wallets; only numbers in the contract change. That's why wallets need to know the token address to show the balance.

## 217: Why do some ERC-20 tokens not return a boolean?

Some older tokens, notably USDT on Ethereum, don't return `bool` from `transfer` and `approve` even though the standard says they should. Calling them through a normal interface reverts when decoding the missing return value. OpenZeppelin's `SafeERC20` (`safeTransfer`, `safeTransferFrom`, `forceApprove`) handles both kinds.

```solidity
using SafeERC20 for IERC20;
token.safeTransferFrom(msg.sender, address(this), amount);
```

## 218: What is the approve front-running issue in ERC-20?

If Alice changes Bob's allowance from 100 to 50, Bob can see the transaction in the mempool, spend 100 first, and then spend the new 50 too. To avoid it, set the allowance to 0 first, or use increase and decrease patterns, or use signature-based approvals with exact amounts. Some tokens, like USDT, even require resetting to 0 before setting a new non-zero value.

## 219: What is safeTransferFrom in ERC-721?

`safeTransferFrom` checks that if the receiver is a contract, it implements `onERC721Received` and returns the right selector. This stops NFTs from being sent to contracts that can't handle them and would lock them forever. The catch is that it calls the receiver, which opens a reentrancy path.

## 220: How is NFT metadata stored?

The contract stores a `tokenURI` for each token, usually pointing to a JSON file with name, description, image and attributes. The JSON and images are usually on IPFS or Arweave, sometimes on a normal server. Some projects store everything on-chain as SVG and base64 JSON, which is more durable but more expensive.

```json
{
  "name": "Item #1",
  "description": "A sample item",
  "image": "ipfs://bafy.../1.png",
  "attributes": [{ "trait_type": "Color", "value": "Blue" }]
}
```

## 221: What is ERC-2981?

ERC-2981 is the NFT royalty standard. It adds `royaltyInfo(tokenId, salePrice)` which returns who should get a royalty and how much. Marketplaces can read it, but paying is voluntary because the standard can't force it on transfers.

## 222: What is ERC-4626?

ERC-4626 is a standard for tokenized vaults: you deposit an asset (an ERC-20) and get shares that represent your part of the vault. It defines `deposit`, `mint`, `withdraw`, `redeem` and the preview and conversion functions. Yield protocols use it so other apps can integrate any vault the same way.

## 223: What is ERC-165?

ERC-165 lets a contract say which interfaces it supports through `supportsInterface(bytes4 interfaceId)`. The interface ID is the XOR of all function selectors in the interface. Marketplaces use it to check if a contract is ERC-721 or ERC-1155, for example.

## 224: What is a merkle airdrop and why use it?

Instead of storing every eligible address on-chain, you build a Merkle tree of `(address, amount)` pairs off-chain and store only the root. Each user claims by submitting a proof, and the contract verifies it. It's cheap no matter how big the list is.

```solidity
function claim(uint256 amount, bytes32[] calldata proof) external {
    require(!claimed[msg.sender], "already claimed");
    bytes32 leaf = keccak256(bytes.concat(keccak256(abi.encode(msg.sender, amount))));
    require(MerkleProof.verify(proof, merkleRoot, leaf), "bad proof");
    claimed[msg.sender] = true;
    token.safeTransfer(msg.sender, amount);
}
```

## 225: What is a reentrancy attack?

Reentrancy happens when a contract calls an external address before updating its own state, and that address calls back into the contract while it's in a half-updated state. The classic case is a withdraw function that sends ETH before setting the balance to zero, letting the attacker withdraw again and again. The 2016 DAO hack drained millions of ETH this way.

```solidity
// Vulnerable
function withdraw() external {
    uint256 bal = balances[msg.sender];
    (bool ok, ) = msg.sender.call{value: bal}("");
    require(ok);
    balances[msg.sender] = 0; // too late
}
```

## 226: How do you prevent reentrancy?

Follow checks-effects-interactions: do all checks, then update state, and only then make external calls. Add a `nonReentrant` guard from OpenZeppelin (`ReentrancyGuard`, or `ReentrancyGuardTransient` which uses cheaper transient storage) on functions that move value. Be aware of cross-function and read-only reentrancy too, where the attacker re-enters a different function or a view.

```solidity
function withdraw() external nonReentrant {
    uint256 bal = balances[msg.sender];
    balances[msg.sender] = 0;
    (bool ok, ) = msg.sender.call{value: bal}("");
    require(ok, "send failed");
}
```

## 227: What is the checks-effects-interactions pattern?

It's an ordering rule for functions: first check conditions (`require`), then apply effects to your own state, then interact with other contracts or send ETH. If an external call re-enters, your state is already correct. It's the first defense against reentrancy and should be used even when you also have a guard.

## 228: What is front-running?

Front-running is when someone sees your pending transaction in the public mempool and gets theirs mined before yours, usually by paying a higher fee, to profit from yours. For example, buying a token right before your big buy and selling right after. Block builders and bots do this all the time on public chains.

## 229: What is MEV?

MEV (maximal extractable value) is the profit someone can make by choosing which transactions go in a block and in what order. It includes arbitrage between DEXs, liquidations, and sandwich attacks on users. On Ethereum, most blocks are built by specialized builders who compete for MEV and pay validators through MEV-Boost.

## 230: What is a sandwich attack?

A bot sees your swap in the mempool, buys the same token just before you (raising the price), lets your swap go through at the worse price, then sells right after. Your loss is their profit, limited by your slippage setting. To protect users, use tight slippage and send through private transaction routes like Flashbots Protect or MEV Blocker.

## 231: What is a private mempool or private RPC?

A private RPC sends your transaction straight to block builders instead of the public mempool, so bots can't see it before it's included. Examples are Flashbots Protect and MEV Blocker. Some also give back part of the MEV your transaction creates. The trade-off is that you trust the relay not to misuse your transaction.

## 232: What is a commit-reveal scheme?

Commit-reveal hides a value until it's safe to show. First, a user submits the hash of their value plus a secret salt (commit). Later, they submit the value and salt (reveal), and the contract checks the hash. It's used for sealed-bid auctions, voting and games so others can't copy or front-run the choice.

```solidity
function commit(bytes32 hash) external { commits[msg.sender] = hash; }

function reveal(uint256 value, bytes32 salt) external {
    require(keccak256(abi.encode(value, salt, msg.sender)) == commits[msg.sender], "mismatch");
    // use value
}
```

## 233: Why is block.timestamp not a good source of randomness?

Anything on-chain at execution time is known to validators and can be computed by other contracts in the same block. `block.timestamp` and `blockhash` can be predicted or slightly influenced by the block proposer. An attacker contract can check the "random" result and revert if it doesn't like it. Use a VRF service or commit-reveal instead.

## 234: What is Chainlink VRF?

Chainlink VRF (verifiable random function) gives contracts random numbers with a cryptographic proof that they weren't tampered with. Your contract requests randomness, and the VRF service calls back with the number and proof, which is checked on-chain. It's used for NFT mints, lotteries and games.

## 235: How do you get a price feed in a smart contract?

The common way is a Chainlink price feed: call `latestRoundData()` on the aggregator for a pair like ETH/USD. Always check that the price is positive and recent enough, and handle the feed's decimals.

```solidity
(, int256 answer, , uint256 updatedAt, ) = feed.latestRoundData();
require(answer > 0, "bad price");
require(block.timestamp - updatedAt < 1 hours, "stale price");
```

## 236: Why is using a DEX spot price as an oracle dangerous?

A DEX pool's current price can be moved a lot within one transaction, especially with a flash loan. An attacker can push the price, use your contract that reads it (for example to borrow too much), and then push it back, all in one transaction. Use decentralized oracle feeds or time-weighted average prices (TWAPs) instead.

## 237: What is a flash loan?

A flash loan lets you borrow any amount from a pool without collateral, as long as you pay it back (plus a fee) in the same transaction. If you don't, the whole transaction reverts as if nothing happened. It's used for arbitrage, liquidations and refinancing, but also to fund attacks on contracts with weak oracles or logic.

## 238: What is impermanent loss?

Impermanent loss is what a liquidity provider loses compared to just holding the two tokens, when their prices change relative to each other. The pool keeps rebalancing, so you end up with more of the token that went down. If prices return to where they started, the loss goes away, which is why it's called "impermanent". Trading fees may or may not make up for it.

## 239: How does lending work in DeFi protocols like Aave?

Lenders deposit tokens into a pool and earn interest. Borrowers deposit collateral worth more than what they borrow (over-collateralized) and pay interest, with rates set by how much of the pool is used. If the collateral value drops below a threshold, anyone can liquidate the position by repaying part of the debt and taking collateral at a discount.

## 240: What is a liquidation in DeFi?

A liquidation happens when a borrower's collateral is no longer enough to safely cover their debt. A liquidator repays some of the debt and receives part of the collateral plus a bonus. This keeps the protocol solvent. Liquidation bots compete fiercely, which is a big source of MEV.

## 241: What is a health factor in lending protocols?

The health factor sums up how safe a loan is: roughly the collateral value times its liquidation threshold, divided by the debt value. Above 1 the position is safe; below 1 it can be liquidated. Users watch it and add collateral or repay debt when it gets close to 1.

## 242: What is a time lock in smart contracts?

A timelock forces a delay between scheduling an admin action and running it, like 48 hours for an upgrade. Users can see what's coming and exit if they don't like it. OpenZeppelin's `TimelockController` is commonly used together with governance or a multisig.

## 243: How does on-chain governance usually work?

Token holders delegate voting power, someone creates a proposal with the exact calls to execute, voting runs for a set period, and if it passes and meets quorum, it goes into a timelock and then executes. OpenZeppelin's `Governor` plus `ERC20Votes` is a standard setup. Many DAOs use off-chain voting on Snapshot for signaling and execute through a multisig.

## 244: What is ERC20Votes and why use checkpoints?

`ERC20Votes` adds delegation and vote tracking to a token. It stores checkpoints of each account's voting power at past blocks or timestamps, so a proposal can count votes as of a snapshot in the past. This stops people from buying or borrowing tokens just to vote and then selling them.

## 245: How do you build a subgraph with The Graph?

A subgraph indexes contract events into a database you query with GraphQL. You define a schema, map events to entities with AssemblyScript handlers, and deploy it to The Graph's network or a hosted indexer. Front ends then query the subgraph instead of scanning logs themselves.

```graphql
type Transfer @entity(immutable: true) {
  id: Bytes!
  from: Bytes!
  to: Bytes!
  value: BigInt!
  blockNumber: BigInt!
}
```

## 246: Why do dApps need an indexer?

Nodes are good at answering "what is the state now" but bad at queries like "all trades by this user, sorted by date" or "top 10 holders". Scanning logs over millions of blocks from the front end is slow and hits rate limits. An indexer like The Graph, Ponder, Envio or your own service processes events into a normal database you can query fast.

## 247: How would you build your own event indexer in Node.js?

Keep a "last processed block" cursor in your database. In a loop, fetch logs in chunks from the cursor to a safe head (for example the finalized block), decode them, write them to the database in one transaction along with the new cursor, and repeat. Make writes idempotent using transaction hash plus log index as a key, so reprocessing is safe.

```js
const logs = await client.getContractEvents({
  address,
  abi,
  eventName: "Transfer",
  fromBlock,
  toBlock,
});
await db.tx(async (t) => {
  for (const log of logs)
    await t.upsertTransfer(`${log.transactionHash}-${log.logIndex}`, log.args);
  await t.setCursor(toBlock);
});
```

## 248: What is a chain reorganization (reorg) and how should apps handle it?

A reorg is when the chain's recent blocks are replaced by a different set, so transactions you saw may disappear or change order. Apps that act on events should wait for enough confirmations or for the finalized block, or be able to roll back data from orphaned blocks. Indexers store block hashes to notice when the parent hash no longer matches.

## 249: What are the "latest", "safe" and "finalized" block tags?

`latest` is the newest block the node knows, which can still be reorged. `safe` is a block that has enough votes that a reorg is very unlikely under normal conditions. `finalized` is a block that can't be reverted without burning a huge amount of stake. Use `latest` for showing quick UI updates and `finalized` for things like crediting deposits.

```js
const block = await provider.getBlock("finalized");
```

## 250: How do you call a read function at a past block?

Pass a block tag or number to the call. This needs an archive node (or a provider that offers archive data) if the block is older than what a full node keeps.

```js
const pastBalance = await token.balanceOf(user, { blockTag: 20_000_000 });
```

## 251: How do you make many contract reads in one request?

Use Multicall3, a contract deployed at the same address on most EVM chains, which runs many calls and returns all results. viem's `multicall` and wagmi's `useReadContracts` use it automatically. It cuts round trips and makes sure all values come from the same block.

```js
const results = await publicClient.multicall({
  contracts: [
    { address: usdc, abi: erc20Abi, functionName: "balanceOf", args: [user] },
    { address: weth, abi: erc20Abi, functionName: "balanceOf", args: [user] },
  ],
});
```

## 252: How do you handle RPC rate limits and failures?

Use a paid provider for production, batch and cache reads, and use multicall. Add retries with backoff for errors like 429 or timeouts, and set up fallback providers so one outage doesn't break the app. viem has a `fallback` transport and ethers has `FallbackProvider`.

```js
import { createPublicClient, fallback, http } from "viem";

const client = createPublicClient({
  chain: mainnet,
  transport: fallback([http(process.env.RPC_A), http(process.env.RPC_B)]),
});
```

## 253: Should you put your RPC API key in the front end?

Any key in front end code is public. For read-only keys, most providers let you limit them by domain and by allowed contract addresses, which is often enough. For anything sensitive or expensive, proxy RPC calls through your own back end and add rate limiting there.

## 254: What is a gas optimization you can make with storage?

Storage is the most expensive part of most contracts. Common tricks: pack several small variables into one 32-byte slot by declaring them next to each other, cache storage values in memory when used more than once, use `immutable` and `constant` where possible, and avoid writing a slot with the same value it already has.

```solidity
// One slot: 20 + 8 + 4 bytes = 32 bytes
address owner;
uint64 lastUpdate;
uint32 count;
```

## 255: Why is reading the same storage variable many times in a loop expensive?

Each `SLOAD` costs gas: 2,100 the first time in a transaction (cold) and 100 after that (warm). In a loop, even warm reads add up. Copy the value to a local variable before the loop, and write it back once at the end if you change it.

```solidity
uint256 total = totalStaked; // one SLOAD
for (uint256 i; i < amounts.length; ++i) total += amounts[i];
totalStaked = total; // one SSTORE
```

## 256: What is the cost of writing to storage?

Writing a non-zero value to a zero slot costs about 20,000 gas, plus 2,100 if the slot is cold. Changing a non-zero value to another non-zero value costs about 2,900 (plus the cold cost). Setting a slot back to zero gives a partial refund. These numbers are why designs try to avoid creating new storage slots.

## 257: Why should you avoid unbounded loops in smart contracts?

A loop over an array that grows with users can eventually cost more gas than the block limit, making the function impossible to call and possibly locking funds. Prefer designs where each user handles their own entry (pull payments), use pagination, or track running totals so you don't need to loop.

## 258: What is the pull over push payment pattern?

Instead of the contract sending funds to many users in one go (push), each user calls a function to withdraw what they're owed (pull). One failing receiver can't block everyone else, there's no unbounded loop, and reentrancy is easier to control.

## 259: What is a denial of service attack in smart contracts?

It's when an attacker makes a function unusable. Examples: a contract that refunds the previous highest bidder with `transfer`, where the bidder is a contract that always reverts, so no one else can bid; or filling an array until looping over it runs out of gas. Pull payments and bounded loops prevent most of these.

## 260: What is tx.origin and why shouldn't you use it for authorization?

`tx.origin` is the EOA that started the whole transaction, while `msg.sender` is the direct caller. If you check `tx.origin == owner`, a malicious contract the owner interacts with can call your contract and pass the check. Always use `msg.sender` for auth. Also, with smart wallets and EIP-7702, `tx.origin` checks to detect "humans" are unreliable.

## 261: What is signature replay and how do you prevent it?

A signature replay is when a valid signature is used more than once, or on another contract or chain. Prevent it by including a nonce that's marked as used, a deadline, the chain ID, and the contract address (EIP-712 domain) in the signed data. Also watch for signature malleability: use OpenZeppelin's `ECDSA` library, which rejects the second valid form.

## 262: How do you verify a signature in Solidity?

Rebuild the digest the user signed, recover the signer, and compare. OpenZeppelin's `ECDSA` and `EIP712` helpers do the hard parts. To also support smart contract wallets, use `SignatureChecker`, which falls back to ERC-1271.

```solidity
bytes32 digest = _hashTypedDataV4(keccak256(abi.encode(ORDER_TYPEHASH, maker, amount, nonce)));
address signer = ECDSA.recover(digest, signature);
require(signer == maker, "bad signature");
```

## 263: What is ERC-1271?

ERC-1271 lets smart contract wallets "sign" messages. A contract implements `isValidSignature(hash, signature)` and returns a magic value if the signature is valid by its own rules (for example, enough multisig owners signed). Apps that verify signatures should support it, otherwise Safe and other smart wallet users can't log in or sign orders.

## 264: What is account abstraction?

Account abstraction means letting accounts be controlled by custom code instead of only by one private key. This allows features like multisig, passkey login, social recovery, gas paid by someone else, session keys and batched actions. On Ethereum, it's done through ERC-4337 (smart accounts with a separate mempool) and EIP-7702 (EOAs that delegate to contract code).

## 265: How does ERC-4337 work?

Users send UserOperations (not normal transactions) to bundlers. A bundler groups many UserOperations into one transaction to the shared EntryPoint contract. The EntryPoint calls each smart account to validate (check signature, nonce and payment) and then execute. Paymasters can sponsor gas or accept tokens as payment. No protocol change was needed.

## 266: What is a paymaster?

A paymaster is a contract in ERC-4337 that agrees to pay gas for a UserOperation. Apps use it to give users gasless transactions, or to let users pay fees in USDC instead of ETH. The paymaster checks its own rules during validation, like an off-chain signature from the app's server, before agreeing to pay.

## 267: What is EIP-7702?

EIP-7702, part of the Pectra upgrade (May 2025), lets an EOA set a "delegation" to a contract's code with a new transaction type. After that, calls to the EOA run that code, so a normal account can batch calls, use sponsored gas, or add other smart wallet features while keeping its address. The private key still has full control, so delegating to a malicious contract can drain the account.

## 268: What are session keys?

A session key is a temporary key with limited permissions, like "can call this game contract for the next hour, spending up to 0.01 ETH". The smart account checks the limits before allowing the action. It lets apps run actions without a wallet popup each time while keeping risk small.

## 269: How do passkeys work with blockchain wallets?

Passkeys use the secp256r1 (P-256) curve and are stored in the device's secure hardware, unlocked with a fingerprint or face. Smart accounts can verify these signatures, and since Fusaka (EIP-7951) Ethereum has a precompile for P-256 verification, which makes it much cheaper. This lets users have a wallet without a seed phrase.

## 270: What is an optimistic rollup?

An optimistic rollup posts transaction batches to layer 1 and assumes they're valid unless someone proves otherwise. Anyone can submit a fraud proof during a challenge window (usually about 7 days) to show a wrong state. Because of the window, withdrawals to layer 1 take about a week through the official bridge. Arbitrum, Optimism and Base are optimistic rollups.

## 271: What is a ZK rollup?

A ZK rollup posts batches to layer 1 along with a validity proof, a cryptographic proof that the new state is correct. Layer 1 checks the proof, so there's no challenge window and withdrawals can finalize once the proof is verified. Generating proofs takes heavy computation. zkSync Era, Starknet, Scroll and Linea are ZK rollups.

## 272: What is the difference between optimistic and ZK rollups?

Optimistic rollups assume correctness and rely on fraud proofs, so they're simpler and fully EVM-equivalent, but withdrawals take about 7 days. ZK rollups prove correctness up front, so withdrawals are faster and security doesn't depend on someone watching, but proving is expensive and EVM support was historically harder. ZK proving costs have dropped a lot, and the line is getting thinner.

## 273: What is data availability?

Data availability means the data needed to rebuild a chain's state has actually been published and anyone can download it. For rollups, if the transaction data isn't available, users can't prove their balances or exit. That's why rollups post their data to Ethereum (as blobs) or to dedicated data availability layers like Celestia or EigenDA.

## 274: What are blobs (EIP-4844)?

Blobs, added in the Dencun upgrade (March 2024), are large chunks of data (about 128 KB each) attached to type 3 transactions. They're stored by consensus nodes for about 18 days, then deleted, and the EVM can't read their content, only a commitment to it. They have their own cheaper fee market, which cut rollup costs by a lot.

## 275: What did the Fusaka upgrade bring?

Fusaka went live on Ethereum mainnet in December 2025. Its main feature is PeerDAS (EIP-7594), which lets nodes check blob availability by sampling small parts instead of downloading every blob, so the number of blobs per block can grow over time. It also added a P-256 signature precompile, a per-transaction gas limit cap, and changes that make block size and blob fees behave better.

## 276: What was the Pectra upgrade?

Pectra went live in May 2025. Key changes: EIP-7702 (EOAs can delegate to contract code), EIP-7251 (validators can have up to 2,048 ETH effective balance), EIP-6110 (deposits processed faster on-chain), EIP-7002 (exits triggered from the execution layer), more blobs per block (EIP-7691), and a BLS12-381 precompile (EIP-2537).

## 277: What is the next planned Ethereum upgrade?

The next upgrade is Glamsterdam. Its main planned features are enshrined proposer-builder separation (ePBS, EIP-7732), which moves block building auctions into the protocol, and block-level access lists (EIP-7928), which let clients run transactions in parallel. It was running on testnets in fall 2026, with a mainnet date still to be set.

## 278: How do you bridge tokens between layer 1 and a rollup?

With the official (canonical) bridge, you deposit tokens into a bridge contract on layer 1, and the rollup mints them on layer 2 after a few minutes. To withdraw, you burn on layer 2, wait for the state to be proven (7 days for optimistic rollups), then claim on layer 1. Third-party bridges use liquidity providers to make withdrawals fast for a fee.

## 279: What is a cross-chain messaging protocol?

It's a system that sends arbitrary messages, not just tokens, between chains, so a contract on chain A can trigger an action on chain B. Examples are Chainlink CCIP, LayerZero, Wormhole, Hyperlane and Axelar. Each one has its own trust model: who verifies the message, and what happens if they lie.

## 280: What is the difference between a lock-and-mint bridge and a burn-and-mint bridge?

Lock-and-mint locks the original tokens on the source chain and mints wrapped tokens on the destination; the wrapped tokens are only as good as the bridge holding the locked funds. Burn-and-mint is used when the issuer controls the token on all chains, like Circle's CCTP for USDC: tokens are burned on one chain and minted natively on the other, with no wrapped version.

## 281: How do you deploy the same contract on multiple chains?

Use a deterministic deployer (a CREATE2 factory present on most chains) with the same bytecode and salt, so the contract gets the same address everywhere. Keep the compiler version and settings identical. Foundry scripts can loop over RPC URLs, and you should verify the contract on each chain's explorer.

## 282: What is a token vesting contract?

A vesting contract holds tokens for team members or investors and releases them over time, often with a cliff (nothing for the first year) and then linear unlocking. It shows the public that insiders can't dump everything at once. OpenZeppelin's `VestingWallet` is a simple base.

## 283: How do you implement an NFT allowlist mint?

Use a Merkle tree of allowed addresses and store only the root, or have a back end sign an EIP-712 voucher for each allowed address. The mint function checks the proof or signature, limits how many each address can mint, and takes payment.

```solidity
function allowlistMint(bytes32[] calldata proof) external payable {
    require(MerkleProof.verify(proof, root, keccak256(abi.encodePacked(msg.sender))), "not allowed");
    require(!minted[msg.sender], "already minted");
    require(msg.value == PRICE, "wrong price");
    minted[msg.sender] = true;
    _safeMint(msg.sender, nextId++);
}
```

## 284: What are soulbound tokens?

Soulbound tokens are NFTs that can't be transferred after they're issued. They are used for credentials, certificates, attendance badges, or reputation. You implement them by blocking transfers in the token's transfer hook, except for minting and maybe burning.

## 285: What is the difference between on-chain and off-chain data in a dApp?

On-chain data is stored in contracts or events and is trusted by all, but it's expensive and public. Off-chain data, like user profiles, images, search indexes or analytics, lives in normal databases or IPFS. A good design keeps only what needs trust and verification on-chain, and links to off-chain data with hashes or IDs.

## 286: How do you store and pin files on IPFS from Node.js?

You can run your own IPFS node or use a pinning service like Pinata or Filebase, which give HTTP APIs. You upload the file, get a CID back, and store that CID (as `ipfs://<cid>`) in your contract or metadata. Pinning makes sure the file stays available.

```js
const form = new FormData();
form.append("file", new Blob([buffer]), "image.png");
form.append("network", "public");
const res = await fetch("https://uploads.pinata.cloud/v3/files", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.PINATA_JWT}` },
  body: form,
});
const { data } = await res.json();
console.log(data.cid);
```

## 287: What is Arweave and how is it different from IPFS?

Arweave is a blockchain for permanent storage: you pay once up front, and the network is paid to keep the data forever. IPFS is just a protocol for sharing content by hash; it has no built-in guarantee that anyone keeps your file. Projects that want NFT media to last often use Arweave, or IPFS together with paid pinning or Filecoin.

## 288: How do you show token balances for a user in a dApp?

For the native coin, call `getBalance`. For tokens, call `balanceOf` on each token contract, ideally batched with multicall, and format with each token's `decimals`. To discover which tokens a user holds without a known list, use an indexer or an API like Alchemy's token balances endpoint.

## 289: How do you handle account and network changes in a dApp?

Listen to the wallet's `accountsChanged` and `chainChanged` events, then reload data or update state. With wagmi, `useAccount` and `useChainId` re-render automatically. Never cache data by assuming the account stays the same, and check that the user is on a supported chain before sending a transaction.

## 290: What is optimistic UI in a dApp?

Optimistic UI shows the expected result right after the user signs, before the transaction is confirmed, with a "pending" state. Once the receipt arrives, you confirm it; if it fails, you roll back and show an error. It makes slow blockchain actions feel faster, but you must clearly show what's still pending.

## 291: How do you show transaction status to users?

Show clear steps: waiting for wallet signature, submitted (with a link to the explorer using the hash), confirmed, or failed with a readable reason. Handle rejection, replacement and dropped transactions. Persist pending hashes in local storage so the status survives a page refresh.

## 292: How do you protect users from approving unlimited allowances?

Ask for the exact amount needed instead of the max `uint256`, or use Permit2 with an expiry. Show the spender and amount clearly in your UI. Point users to tools like revoke.cash to review old approvals. Unlimited approvals are convenient but mean a hacked contract can drain all of that token.

## 293: What is transaction simulation and why do wallets show it?

Simulation runs the transaction against current state without sending it, then shows the expected balance changes, like "you send 1 ETH, you receive 3,000 USDC". Wallets like Rabby and MetaMask do this to warn about scams. Developers can simulate with `eth_call`, Tenderly, or Foundry's `cast call --trace`.

## 294: How do you debug a failed transaction?

Look at the receipt and the explorer for the revert reason. Then get a full trace with `cast run <txhash>` (Foundry), Tenderly, or `debug_traceTransaction` on a node that supports it. The trace shows each call, its inputs and where it reverted. You can also fork the chain at that block and replay the transaction in a local test.

```bash
cast run 0xTX_HASH --rpc-url $RPC_URL
```

## 295: What is Etherscan's API useful for?

It gives you data that's hard to get from a plain node: contract ABIs and source of verified contracts, a list of an address's transactions, token transfers, gas price estimates, and contract verification. Its V2 API uses one key and a `chainid` parameter for many chains. It's handy for tooling, but production apps should not depend on it alone.

## 296: How do you write a Hardhat test in TypeScript?

Hardhat 3 uses Node's built-in test runner (or Mocha) with viem or ethers through the network connection. You deploy contracts, call them and assert results.

```ts
import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { network } from "hardhat";

describe("Counter", async () => {
  const { viem } = await network.connect();

  it("increments", async () => {
    const counter = await viem.deployContract("Counter");
    await counter.write.increment();
    assert.equal(await counter.read.count(), 1n);
  });
});
```

## 297: What is gas reporting and snapshotting?

Gas reports show how much gas each function uses in your tests, so you can track costs. Foundry has `forge test --gas-report` and `forge snapshot`, which saves gas per test to a file you can diff in CI. If a change makes a function much more expensive, you notice before deploying.

## 298: What is Slither?

Slither is a static analysis tool for Solidity from Trail of Bits. It reads your code and flags common problems like reentrancy, unchecked return values, shadowed variables and dangerous `delegatecall`. It runs in seconds and is easy to add to CI, though you'll need to triage false positives.

```bash
slither . --exclude-dependencies
```

## 299: What should a smart contract code review checklist include?

Check access control on every state-changing function, reentrancy and external call order, input validation, math and rounding direction, oracle usage, token quirks (fee-on-transfer, no return value, different decimals), upgrade safety, event emission, and behavior at edge values like zero and max. Also review deployment scripts and admin key setup, not just the contract code.

## 300: What are fee-on-transfer and rebasing tokens, and why do they cause bugs?

A fee-on-transfer token takes a cut on each transfer, so the receiver gets less than the amount sent. A rebasing token (like stETH) changes balances automatically over time. Contracts that assume "I received exactly `amount`" or that balances stay fixed will miscount. Measure the actual balance change before and after a transfer, or don't support these tokens.

```solidity
uint256 before = token.balanceOf(address(this));
token.safeTransferFrom(msg.sender, address(this), amount);
uint256 received = token.balanceOf(address(this)) - before;
```

# Advanced Questions (301-450)

## 301: What is the blockchain trilemma?

The trilemma says a blockchain struggles to be decentralized, secure and scalable all at once. Making blocks bigger or faster helps scale but raises hardware needs, so fewer people can run nodes. Ethereum's answer is to keep layer 1 easy to verify and move most activity to rollups, while making data cheaper for them with blobs and data availability sampling.

## 302: How does Ethereum's proof of stake reach consensus?

Time is split into 12-second slots and 32-slot epochs. In each slot, a randomly chosen validator proposes a block, and a committee of validators attests to it. LMD-GHOST, the fork choice rule, picks the chain head with the most recent attestation weight. Casper FFG works at the epoch level: when two-thirds of stake votes for a checkpoint link, the earlier checkpoint is finalized. Together this is called Gasper.

## 303: What is the difference between justification and finalization on Ethereum?

A checkpoint (the first block of an epoch) is justified when at least two-thirds of total staked ETH votes for it as a target. When a justified checkpoint is followed by another justified checkpoint right after it, the first one becomes finalized. Undoing a finalized block would need at least one-third of stake to sign conflicting votes, and that stake would be slashed.

## 304: What is an inactivity leak?

If the chain can't finalize for more than four epochs, for example because over a third of validators went offline, the inactivity leak starts. Offline validators slowly lose stake until the online ones are back above two-thirds of the total, and finality can resume. It lets the chain recover from big outages without manual intervention, at the cost of the offline validators.

## 305: How are block proposers chosen on Ethereum and why does it matter that the choice is unpredictable?

Proposers are chosen with RANDAO, a random value built by mixing in each proposer's BLS signature over the epoch number. The proposer schedule is known about one epoch ahead. Each proposer can only influence randomness by skipping their block (losing rewards), which gives one bit of bias. Proposer predictability is a reason people study single secret leader election, so proposers can't be targeted with DoS attacks before their slot.

## 306: What does PREVRANDAO give you in Solidity and how safe is it?

Since the Merge, `block.prevrandao` returns the beacon chain's RANDAO value from the previous slot (it replaced `block.difficulty`). It's better than a block hash, but the proposer can still choose to skip a block to bias it, and the value is known ahead of time within the same block. It's fine for low-stakes uses, but use a VRF for anything valuable.

## 307: How does Bitcoin's difficulty adjustment work?

Every 2,016 blocks (about two weeks), nodes compare how long those blocks took with the target of 20,160 minutes. The target is then scaled so blocks come every 10 minutes on average again, with the change capped at 4x in either direction per period. This keeps block time stable even as total hash power rises or falls.

## 308: What is the longest chain rule in Bitcoin, and why is "most work" more accurate?

Nodes follow the valid chain with the most total proof of work, not simply the most blocks. If difficulty were ignored, an attacker could build a longer chain of easy blocks. Counting cumulative work means an attacker needs real hash power to compete. This rule is how Bitcoin resolves forks.

## 309: What is a selfish mining attack?

A miner who finds a block keeps it secret and keeps mining on top of it. When the public chain catches up, they release their hidden blocks to orphan the honest miners' work. Research showed this can be profitable with less than half the hash power, depending on network conditions. It shows that PoW incentives aren't perfectly aligned with honest behavior.

## 310: What is a long range attack in proof of stake and how is it prevented?

An attacker gets old validator keys (for example, from validators who already withdrew and don't care anymore) and builds a fake chain from far in the past. A new node with no prior knowledge can't tell which chain is real just from the rules. Proof of stake handles this with weak subjectivity: new nodes start from a recent trusted checkpoint (checkpoint sync), and nodes never revert finalized blocks.

## 311: What is the nothing at stake problem?

In naive proof of stake, voting on several forks costs nothing, so validators might vote on all of them to be safe, which would stop the chain from converging. Ethereum fixes this with slashing: signing two conflicting blocks or votes for the same slot or epoch burns part of the stake. Validators therefore have a real cost for equivocating.

## 312: How do BFT-style consensus protocols differ from Nakamoto consensus?

BFT protocols like Tendermint (CometBFT) or HotStuff have a known validator set vote in rounds, and a block is final once two-thirds sign it, often in one block. They favor safety: with too many nodes offline, the chain stops. Nakamoto consensus (longest chain) always keeps producing blocks but only gives probabilistic finality. Ethereum mixes both: a longest-chain-like fork choice plus BFT-style finality on top.

## 313: What is the CAP theorem's relevance to blockchains?

During a network partition, a system must choose between staying available and staying consistent. Bitcoin chooses availability: both sides keep making blocks and one is later dropped. BFT chains choose consistency: they stop if they can't get two-thirds of votes. Ethereum's LMD-GHOST keeps the chain live while finality pauses if more than a third of stake is unreachable.

## 314: What is proposer-builder separation (PBS)?

PBS splits block production into two roles: builders, who assemble the most profitable block, and proposers (validators), who just pick the highest bid. Today it runs outside the protocol through MEV-Boost, with relays trusted by both sides. It lets ordinary validators earn MEV without being sophisticated. Enshrined PBS (ePBS) in Glamsterdam moves this auction into the protocol to remove trusted relays.

## 315: How does MEV-Boost work?

A validator runs MEV-Boost next to its consensus client. Builders send blocks to relays, which check them and pass only the header and bid to the validator. The validator signs the header with the best bid, and then the relay reveals the full block. The validator can't steal the block content because it never sees it before signing, and the builder can't get paid without delivering the block.

## 316: What are the centralization concerns with MEV?

A few builders build most Ethereum blocks, and a few relays carry most of them, because building well needs exclusive order flow and lots of data. These builders could censor certain transactions. Defenses being worked on include inclusion lists (FOCIL), which let validators force transactions into blocks, and ePBS to remove reliance on relays.

## 317: What is the Ethereum state and how is it stored?

The state is the current data of every account: balance, nonce, code hash and storage root. It's stored in a Merkle Patricia Trie, and the root hash goes in each block header. Each contract has its own storage trie. Clients store the trie in a key-value database and use flat snapshots to make reads fast.

## 318: What is a Merkle Patricia Trie?

It's a trie (prefix tree) where keys are paths of hex nibbles and each node is referenced by its hash, combining a Patricia trie with a Merkle tree. It has branch nodes (16 children), extension nodes (shared prefix), and leaf nodes. It lets you prove a key's value with a proof from root to leaf. Ethereum uses it for state, storage, transactions and receipts.

## 319: What are Verkle trees and why does Ethereum want them?

Verkle trees replace hashes in the tree with vector commitments, making proofs much smaller than Merkle Patricia proofs. Small proofs allow stateless clients, which can verify blocks without storing the full state, because each block comes with a proof of the state it touches. The roadmap has been debating Verkle versus a binary hash tree with zero-knowledge proofs (EIP-7864), which may be more friendly to quantum-safe and ZK systems.

## 320: What is state growth and why is it a problem?

Every new account and storage slot stays in the state forever, so the state keeps growing (well over 100 GB for Ethereum). Nodes need fast SSDs to keep up, which raises the bar to run a node. Ideas to manage it include statelessness, state expiry, and charging more for creating new state.

## 321: What is history expiry (EIP-4444)?

History expiry lets execution clients drop old block bodies and receipts instead of keeping everything since genesis. Old history is still available from archives, torrents and the Portal network. Ethereum clients started removing pre-Merge history in 2025. It cuts disk requirements a lot but means apps needing old data must use an archive or indexer.

## 322: How does the EVM work at a low level?

The EVM is a stack machine with a 1024-item stack of 256-bit words. It has byte-addressable memory that's cleared after each call, persistent storage (key to value, 256 bits each), transient storage, and read-only call data. It runs opcodes one by one, charging gas for each. A call creates a new frame with its own stack and memory.

## 323: What are warm and cold storage accesses (EIP-2929)?

The first time a transaction touches an address or storage slot, it's "cold" and costs more: 2,100 gas for an `SLOAD`, 2,600 for an account access. After that it's "warm" and costs 100. This was added in the Berlin upgrade to price disk reads more fairly and make DoS attacks harder. It affects gas estimates and the order you access things in.

## 324: What is transient storage and how is it used?

Transient storage (EIP-1153, Cancun) is key-value storage that's cleared at the end of each transaction. `TSTORE` and `TLOAD` cost about 100 gas, far cheaper than normal storage. It's great for reentrancy locks and for passing data between calls in one transaction, as Uniswap V4 does. Solidity supports `transient` state variables for value types since 0.8.28.

```solidity
bool transient locked;

modifier lock() {
    require(!locked, "reentrant");
    locked = true;
    _;
    locked = false;
}
```

## 325: What happened to SELFDESTRUCT?

Since Cancun (EIP-6780), `SELFDESTRUCT` only deletes a contract's code and storage if it's called in the same transaction that created the contract. Otherwise it just sends all ETH to the target and leaves the contract in place. Designs that relied on destroying and redeploying a contract at the same address (with CREATE2) no longer work. The opcode is deprecated.

## 326: How is memory expansion charged in the EVM?

Memory costs 3 gas per 32-byte word plus a quadratic term (words squared divided by 512). Small use is cheap, but large arrays in memory get expensive fast. This is why copying big arrays to memory or returning large data can blow up gas. Using `calldata` and processing in chunks helps.

## 327: What is the 63/64 rule for gas?

When a contract makes a call, it can forward at most 63/64 of its remaining gas (EIP-150). The caller keeps 1/64 to finish after the call returns. This limits call depth in practice and means a sub-call can run out of gas while the caller still has enough to continue. Attackers have used it to make a sub-call fail on purpose while the outer call succeeds, so check call results and required gas carefully.

## 328: What is the contract size limit?

Deployed contract code is limited to 24,576 bytes (EIP-170), and init code to twice that (EIP-3860). Big contracts hit this limit. Fixes: move logic into libraries or separate contracts, use the diamond pattern, turn on the optimizer with a lower runs value, and remove unused code and long revert strings.

## 329: What is the diamond pattern (EIP-2535)?

A diamond is a proxy that sends each function selector to a different implementation contract (a facet). It gets around the contract size limit and lets you upgrade single functions. The trade-off is complexity: shared storage must be managed carefully (usually with namespaced storage), and it's harder for users and auditors to see which code runs.

## 330: How does the Solidity optimizer "runs" setting work?

The `runs` value tells the optimizer how many times you expect each function to be called. A low value optimizes for smaller deployment cost; a high value optimizes for cheaper calls at the cost of bigger bytecode. Use a high value for contracts users call a lot, like a DEX router, and a low one for contracts near the size limit.

## 331: What is the via-IR pipeline?

`via-IR` compiles Solidity through Yul, an intermediate language, before producing bytecode. It can optimize across functions better and fixes many "stack too deep" errors. It's slower to compile and can change gas costs, so test with the same settings you deploy with. Many teams use it now for complex contracts.

## 332: What is the "stack too deep" error and how do you fix it?

The EVM can only reach the top 16 stack items, so a function with too many local variables, parameters and return values fails to compile. Fixes: group variables into a struct, split the function, use block scopes `{ }` to free variables early, or compile with `viaIR: true`.

## 333: What is inline assembly in Solidity and when should you use it?

Inline assembly lets you write Yul inside Solidity for low-level control, such as reading storage slots directly, custom memory layouts, or saving gas in hot paths. It skips Solidity's safety checks, so bugs are easy to make and hard to spot. Use it only when needed, keep it small, mark it `memory-safe` only if it truly is, and test it well.

```solidity
function getSlot(bytes32 slot) external view returns (bytes32 value) {
    assembly {
        value := sload(slot)
    }
}
```

## 334: How are dynamic arrays and mappings laid out in storage?

Each state variable gets a slot number in order. For a dynamic array at slot `p`, slot `p` holds the length, and the elements start at `keccak256(p)`. For a mapping at slot `p`, the value for key `k` is at `keccak256(abi.encode(k, p))`. Knowing this lets you read storage directly with `eth_getStorageAt` and helps when debugging upgrades.

```js
import { AbiCoder, keccak256 } from "ethers";
const slot = keccak256(
  AbiCoder.defaultAbiCoder().encode(["address", "uint256"], [user, 0]),
);
const raw = await provider.getStorage(tokenAddress, slot);
```

## 335: Can private variables be read by anyone?

Yes. `private` only stops other contracts from reading the variable through Solidity. Anyone can read any storage slot with `eth_getStorageAt` or see it in transaction inputs. Never store secrets like passwords or unrevealed answers on-chain, even as `private`; use hashes, commit-reveal, or encryption.

## 336: What is read-only reentrancy?

A view function returns wrong data while the contract is in the middle of a state change, and another protocol reads that value during a callback. For example, a pool sends ETH before updating its totals, and a lending protocol reads the pool's price in the receiver's fallback. The view isn't protected by `nonReentrant`. Fixes: update state before external calls and have views check the reentrancy lock.

## 337: What is cross-function and cross-contract reentrancy?

Cross-function reentrancy is when an attacker re-enters a different function that shares state with the one making the external call, like calling `transfer` while `withdraw` is mid-way. Cross-contract reentrancy is the same idea across contracts sharing state. A per-function guard doesn't help; you need a shared lock and correct ordering of effects before interactions.

## 338: What are ERC-777 and ERC-721 hooks, and why are they reentrancy risks?

ERC-777 tokens call `tokensReceived` and `tokensToSend` hooks on the receiver and sender, and ERC-721 and ERC-1155 call `onERC721Received` and `onERC1155Received` on safe transfers. These hooks hand control to an outside contract in the middle of your logic. Several DeFi hacks used ERC-777 hooks to re-enter lending protocols. Treat every token transfer as an external call.

## 339: What is a price manipulation attack, step by step?

The attacker takes a flash loan and makes a huge trade in a thin DEX pool, moving its price. Then they use a protocol that reads that pool's spot price, for example borrowing against collateral that now looks overvalued. They trade back to restore the price, repay the flash loan and keep the profit, all in one transaction. Defense: robust oracles, TWAPs over enough time, and limits on sudden price moves.

## 340: What is a TWAP oracle and its limits?

A TWAP (time-weighted average price) averages a pool's price over a period using cumulative price values stored on-chain, like Uniswap V3's observations. It's much harder to manipulate within one transaction. But it lags real prices, and over several blocks a well-funded attacker or a validator who controls consecutive blocks can still move it, especially for low-liquidity pools.

## 341: What is an ERC-4626 inflation (donation) attack?

When a vault is empty, the first depositor deposits 1 wei, then donates a large amount of the asset directly to the vault. Now one share is worth a lot, and the next depositor's shares round down to zero, so the attacker takes their deposit. OpenZeppelin's ERC-4626 uses virtual shares and an offset to make this unprofitable; other fixes are seeding the vault on deploy or a minimum first deposit.

## 342: How should you handle rounding in DeFi math?

Always round in the protocol's favor: round down what users receive (shares minted, assets withdrawn) and round up what they owe (shares burned, debt). Do multiplications before divisions to keep precision, and use `mulDiv` for full-precision `a * b / c` without overflow. Rounding errors that favor users can be repeated thousands of times to drain a protocol.

```solidity
uint256 shares = Math.mulDiv(assets, totalShares, totalAssets, Math.Rounding.Floor);
```

## 343: How does Uniswap V3 concentrated liquidity work?

Liquidity providers choose a price range for their liquidity instead of the full 0 to infinity curve. Within that range, their capital is used much more efficiently and earns more fees. Outside the range, it holds only one token and earns nothing. Positions are NFTs because each one is unique. Prices move in discrete "ticks", and the pool tracks liquidity changes at tick boundaries.

## 344: What are Uniswap V4 hooks and the singleton design?

Uniswap V4 keeps all pools in one `PoolManager` contract (singleton) and uses flash accounting with transient storage: within a transaction, only net balances are settled at the end, which makes multi-hop swaps cheaper. Hooks are external contracts that pools can call at points like before or after a swap, allowing custom fees, limit orders or oracles. Hooks add flexibility and new risks, since each pool trusts its hook.

## 345: How would you design a stablecoin and what are the main risks?

Options are fiat-backed (simple, but depends on a company and banks), over-collateralized crypto-backed (transparent, but capital-heavy and depends on liquidations working in a crash), or algorithmic (fragile; TerraUSD collapsed in 2022). Key parts: a reliable oracle, liquidation system, peg stability tools (minting and redemption at 1:1), and governance over risk settings. The biggest risks are oracle failures, bank runs and fast collateral crashes.

## 346: What is a governance attack and how can you defend against it?

An attacker gets enough votes, often by buying or borrowing tokens briefly, and passes a proposal that drains the treasury. Beanstalk lost about $180 million in 2022 this way using a flash loan. Defenses: voting power snapshots taken before the proposal, voting delays, quorums, timelocks before execution, and a guardian that can veto clearly malicious proposals.

## 347: How do you secure admin keys for a protocol?

Use a multisig (like a 4-of-7 Safe) with keys on hardware wallets held by different people in different places. Put a timelock in front of sensitive actions like upgrades and parameter changes. Split roles so a pauser can stop things quickly but only the timelocked governance can upgrade. Document the setup publicly and practice the emergency process.

## 348: What did the Bybit hack in 2025 teach about multisig security?

In February 2025, attackers stole about $1.5 billion in ETH from Bybit's cold wallet, a Safe multisig. They compromised the web interface the signers used, so the signers saw a normal transfer but actually signed a `delegatecall` that replaced the wallet's logic. The lesson: signers must verify the raw transaction data on an independent device, not trust the UI, and watch for unexpected `delegatecall` operations.

## 349: What is blind signing and how do you avoid it?

Blind signing is approving a transaction or message without being able to read what it does, for example when a hardware wallet only shows a hash. Many hacks start here. Use wallets that decode transactions and EIP-712 data in a readable way, simulate before signing, and on hardware wallets enable clear signing for known contracts. Teams should verify calldata independently before signing high-value transactions.

## 350: What is address poisoning?

An attacker sends a tiny or zero-value transfer to your history from an address that looks like one you use, with the same first and last characters. Later, you copy the address from your history and send funds to the attacker by mistake. Defenses: check the full address, use an address book or ENS, and make wallets hide zero-value transfers from unknown tokens.

## 351: What are common bridge vulnerabilities?

Most big bridge losses came from a few patterns: compromised validator or multisig keys (Ronin, about $600 million in 2022), bugs in message verification that let attackers forge deposits (Wormhole, Nomad), and bad initialization where a zero value was accepted as a valid root. Bridges are risky because one contract holds a lot of value and must trust a proof or signers about another chain.

## 352: How do ZK proofs work at a high level?

A zero-knowledge proof lets a prover convince a verifier that a statement is true, like "I know inputs that make this program output X", without revealing the inputs. The computation is turned into math constraints (a circuit), and the prover creates a short proof that all constraints are met. The verifier checks the proof much faster than redoing the work. Blockchains use this for privacy and for compressing computation in ZK rollups.

## 353: What is the difference between SNARKs and STARKs?

SNARKs (like Groth16 and PLONK) have very small proofs and cheap verification, but many need a trusted setup and rely on elliptic curves, which aren't quantum safe. STARKs need no trusted setup and use only hash functions, so they're considered quantum resistant, but proofs are larger. Many systems now prove with STARKs and then wrap the result in a SNARK to make on-chain verification cheap.

## 354: What is a trusted setup ceremony?

Some SNARK systems need secret random values to create public parameters. If anyone kept those secrets, they could forge proofs. A ceremony has many participants each add their own randomness; as long as one of them destroys their part, the setup is safe. Ethereum's KZG ceremony for blobs in 2023 had over 140,000 contributions.

## 355: What is a zkVM?

A zkVM proves the correct execution of normal programs, often written in Rust and compiled to RISC-V, instead of hand-written circuits. Examples are RISC Zero, SP1 and others. They make ZK much easier to use: coprocessors, rollups and even proving whole Ethereum blocks in real time are built on them. There's an active Ethereum research effort to let validators verify blocks with zkVM proofs instead of re-executing them.

## 356: What is a ZK coprocessor?

A ZK coprocessor runs heavy computation off-chain, like reading lots of historical chain data or doing math that would cost too much gas, and returns the result plus a proof. The contract verifies the proof and trusts the result. It extends what contracts can do without trusting an off-chain server.

## 357: What are KZG commitments and how are they used for blobs?

A KZG commitment is a short value (48 bytes) that commits to a polynomial. Each blob is treated as a polynomial, and its KZG commitment goes on-chain, while the blob itself stays in the consensus layer. Anyone can later prove the value at any point of the blob with a small proof, checked by the point evaluation precompile. This is also what makes data availability sampling with erasure coding work.

## 358: How does data availability sampling (PeerDAS) work?

Blob data is extended with erasure coding, so the original can be rebuilt from any half of the extended data. With PeerDAS, each node stores and serves only some columns of the extended data, and checks a few random samples from others. If enough samples are available, the whole data is almost certainly available. This lets the network handle many more blobs without each node downloading all of them.

## 359: How does an optimistic rollup's fraud proof actually work?

When a proposer posts a state root, a challenger who disagrees starts a dispute. Both sides bisect the execution step by step (interactive bisection) until they find one instruction they disagree on. That single step is run on layer 1, and whoever is wrong loses their bond. Arbitrum's BoLD and Optimism's Cannon fault proof system follow this idea, and both now let anyone challenge, not just whitelisted parties.

## 360: What are the "stages" of rollup decentralization?

L2BEAT rates rollups in stages. Stage 0: users rely on the operator; proofs may not be live. Stage 1: working fraud or validity proofs, and a security council can override only with a high threshold, with an exit window. Stage 2: proofs fully control the system and upgrades give users enough time to exit. It's a quick way to judge how much you trust the team behind a rollup.

## 361: What is a sequencer and what are the risks of a centralized one?

The sequencer orders rollup transactions and gives fast confirmations. Most rollups run one central sequencer, which can censor or reorder transactions and is a single point of failure for liveness. Users can usually force a transaction through layer 1 (force inclusion) after a delay, so funds aren't trapped. Shared and based sequencing aim to decentralize it.

## 362: What is a based rollup?

A based rollup lets the layer 1 validators sequence its transactions, instead of running its own sequencer. It inherits Ethereum's liveness and censorship resistance and makes composing with layer 1 easier. The trade-off is slower confirmation (tied to layer 1 slots) unless preconfirmations are added, and giving up sequencer revenue. Taiko is an example.

## 363: What are preconfirmations?

A preconfirmation is a signed promise from a sequencer or proposer that a transaction will be included, possibly in a set position, before the block is published. It gives users fast feedback. If the party breaks the promise, they can be slashed. They're important for based rollups and for making layer 1 feel faster.

## 364: How do layer 2 fees work?

A layer 2 fee has two parts: the execution cost on layer 2 (gas used times the layer 2 gas price) and the layer 1 data cost (the cost of posting the transaction's compressed data to Ethereum, now usually as blobs). After blobs, the data part became very small, so layer 2 transactions often cost less than a cent. During blob congestion, the data part can spike.

## 365: What is the difference between EVM equivalence and EVM compatibility?

EVM compatible means Solidity code generally runs, but some opcodes, precompiles, gas costs or addresses may behave differently. EVM equivalent means it matches Ethereum's behavior exactly, so all tools and bytecode work unchanged. Vitalik's classification of ZK-EVMs (types 1 to 4) describes how close each is, trading equivalence for faster proving.

## 366: How do you make an app work across several layer 2s safely?

Don't assume the same address means the same contract on every chain unless you deployed it deterministically. Check chain-specific details like block numbers (`block.number` on Arbitrum returns an approximate layer 1 block number), different gas pricing, missing opcodes or precompiles, and sequencer downtime. Use the chain's official addresses for tokens like USDC, since bridged versions differ from native ones.

## 367: What is a sequencer uptime feed and why do lending protocols use it?

If a layer 2's sequencer goes down, prices can move a lot while users can't add collateral. When it comes back, positions can be liquidated unfairly. Chainlink provides a sequencer uptime feed; protocols check it and pause liquidations or borrowing for a grace period after the sequencer restarts.

## 368: What are intents and solvers?

With intents, the user signs what they want ("swap 1 ETH for at least 3,000 USDC on any chain") instead of the exact steps. Solvers compete to fill the intent in the best way, using their own liquidity or routes, and are paid if they deliver. CoW Swap, UniswapX and cross-chain systems like Across use this. ERC-7683 is a standard for cross-chain intents.

## 369: How does a Bitcoin transaction get validated?

For each input, the node finds the referenced UTXO, checks it's unspent, and runs the input's unlocking data against the output's locking script (or witness program). If all scripts succeed, the sum of inputs is at least the sum of outputs (the difference is the fee), and other rules pass, the transaction is valid. The spent UTXOs are removed and the new outputs are added to the UTXO set.

## 370: What is Bitcoin Script?

Bitcoin Script is a simple stack-based language used to lock and unlock outputs. It's intentionally not Turing complete: no loops, so every script ends quickly. A typical lock says "provide a signature matching this public key hash". It supports multisig, time locks and hash locks, which are enough for things like the Lightning Network.

## 371: What were SegWit and Taproot?

SegWit (2017) moved signature data (the witness) out of the part used for the transaction ID, fixing transaction malleability and raising effective block capacity with a weight limit. Taproot (2021) added Schnorr signatures and MAST, so complex spending conditions look like normal single-signature payments when spent cooperatively, improving privacy and saving space.

## 372: What are Schnorr signatures and their advantages?

Schnorr signatures are simpler than ECDSA and have a useful property: signatures and keys can be combined. Several signers can produce one signature for one combined key (MuSig2), so a multisig looks like a single-signature on-chain. They also allow batch verification. Bitcoin uses them since Taproot.

## 373: What are Ordinals and inscriptions?

Ordinals is a convention for numbering individual satoshis and tracking them across transactions. Inscriptions attach data, like images or text, to a satoshi by putting it in a Taproot witness. This created NFTs and BRC-20 tokens on Bitcoin. It caused debate because it filled blocks with non-payment data and raised fees.

## 374: How do HTLCs and the Lightning Network route payments?

An HTLC (hash time-locked contract) pays out if the receiver reveals the secret that matches a hash before a deadline; otherwise the funds return after a timeout. Lightning chains HTLCs across several channels with the same hash, so either the whole route completes when the final receiver reveals the secret, or nothing moves. Intermediaries can't steal funds because they only get paid by passing the secret back.

## 375: What is the UTXO model's advantage for parallelism and privacy?

UTXOs are independent, so transactions spending different UTXOs can be validated in parallel without conflicts. Each payment can use a fresh address, making linking a bit harder than with one reused account. The downside is that complex smart contracts are harder, since there's no shared mutable state like an account's storage. Cardano's eUTXO model extends UTXOs with scripts and data to get some of both.

## 376: How does Solana achieve high throughput?

Solana uses Proof of History, a verifiable clock of sequential hashes, to order events without waiting for votes, plus Tower BFT for consensus. Transactions declare which accounts they read and write, so the Sealevel runtime can run non-conflicting ones in parallel. It streams blocks in pieces (Turbine), forwards transactions straight to upcoming leaders instead of using a mempool, and needs strong hardware. Firedancer, a second independent validator client, is being rolled out for better performance and client diversity.

## 377: How is writing a Solana program different from writing a Solidity contract?

On Solana, programs are stateless; all data is stored in separate accounts that are passed into each instruction. You must declare every account a transaction touches, and accounts must pay rent (or be rent-exempt with a deposit). Programs are usually written in Rust with the Anchor framework. Program Derived Addresses (PDAs) let a program "own" accounts without a private key, similar to CREATE2 addresses.

## 378: What is Move and how do Sui and Aptos use it?

Move is a smart contract language built around resources: assets are types that can't be copied or silently dropped, only moved, which prevents many token bugs by design. Aptos uses Move with a global storage model, while Sui uses an object model where each asset is an object with an owner, letting simple transfers skip full consensus. Both aim for parallel execution and high throughput.

## 379: What is Cosmos and the IBC protocol?

Cosmos is an ecosystem of app-specific blockchains built with the Cosmos SDK and CometBFT consensus. IBC (Inter-Blockchain Communication) lets these chains send tokens and messages to each other using light client verification instead of a trusted bridge committee. Each chain has its own validators, so security isn't shared unless the chain opts into something like Interchain Security.

## 380: What is restaking?

Restaking lets ETH stakers use the same stake to also secure other services, like oracles, bridges or data availability layers, in exchange for extra rewards. EigenLayer is the best-known protocol. The risk is that one stake can be slashed by multiple systems, and a big failure could spread across many services.

## 381: What is liquid staking and what are its risks?

Liquid staking protocols like Lido stake ETH for users and give them a token (stETH, rETH) that earns rewards and can be used in DeFi. Risks include smart contract bugs, depeg of the token from ETH during panics, slashing of the protocol's validators, and centralization if one protocol controls too much stake. Some people worry about any one protocol going above a third of all stake.

## 382: What is distributed validator technology (DVT)?

DVT splits one validator's key among several operators using threshold signatures, so the validator keeps working even if some operators go offline, and no single operator has the full key. Obol and SSV are DVT projects. It improves resilience and lets small groups run validators together.

## 383: What are BLS signatures and why does Ethereum's consensus use them?

BLS signatures can be aggregated: many signatures on the same message combine into one short signature that can be checked against a combined public key. Ethereum has a huge number of validators voting every epoch, and aggregation makes those votes small enough to put in blocks. Ethereum uses the BLS12-381 curve, which is also available as a precompile since Pectra.

## 384: What are precompiled contracts?

Precompiles are special addresses that run native code instead of EVM bytecode, for operations that would be too expensive in the EVM. Examples: `ecrecover` at address 0x01, SHA-256, RIPEMD-160, modular exponentiation, BN254 pairing (used for SNARK verification), the KZG point evaluation, BLS12-381 operations, and P-256 verification. They have fixed gas costs set by the protocol.

## 385: How does ecrecover work and what are its pitfalls?

`ecrecover(hash, v, r, s)` returns the address that signed `hash`. Pitfalls: it returns `address(0)` for invalid signatures instead of reverting, so you must reject zero; it accepts both "high s" and "low s" forms, so a signature can be changed into another valid one (malleability); and it only works for EOAs, not smart wallets. Use OpenZeppelin's `ECDSA` and `SignatureChecker` instead of calling it directly.

## 386: How do HD wallets (BIP-32 and BIP-44) derive keys?

BIP-32 defines a tree of keys from one seed: each child key is derived from a parent key, a chain code and an index using HMAC-SHA512. BIP-44 sets a path format, `m / purpose' / coin_type' / account' / change / address_index`, so Ethereum's first address is at `m/44'/60'/0'/0/0`. Hardened derivation (the `'`) stops a leaked child private key plus the parent public key from revealing siblings.

```js
import { HDNodeWallet } from "ethers";
const wallet = HDNodeWallet.fromPhrase(mnemonic, undefined, "m/44'/60'/0'/0/1");
console.log(wallet.address);
```

## 387: What is MPC wallet technology?

In an MPC (multi-party computation) wallet, the private key is never created in one place. Several parties each hold a key share and run a protocol to sign together. On-chain it looks like a normal single-key signature, so it works on any chain, unlike smart contract multisigs. Exchanges and custodians use MPC, and some consumer wallets split shares between the user's device and a server.

## 388: What is social recovery?

A smart wallet with social recovery lets a set of guardians (friends, other devices, or services) approve changing the wallet's signing key if the owner loses it. Usually a majority of guardians must agree, often with a time delay so the owner can cancel. It removes the single point of failure of a seed phrase.

## 389: How would you design a secure custodial deposit system for an exchange?

Give each user a unique deposit address, derived from an HD wallet or created as cheap CREATE2 forwarder contracts. Run your own nodes, watch for incoming transfers, and credit only after the block is finalized. Sweep funds to a hot wallet with limits and keep most in cold storage or MPC. Handle reorgs, token quirks and duplicate events, and reconcile on-chain balances with your ledger regularly.

## 390: How do you monitor smart contracts in production?

Watch events and state changes in real time with tools like Tenderly alerts, Hypernative, Forta, or your own indexer. Alert on large withdrawals, ownership or role changes, upgrades, unusual gas usage, and oracle price jumps. Have a runbook ready: who can pause, how to reach them, and how to communicate with users.

## 391: What should an incident response plan for a hacked protocol include?

Detect fast with monitoring, then pause affected contracts if possible. Contact security groups like SEAL 911, warn users to revoke approvals, and work with exchanges and stablecoin issuers to freeze stolen funds. Trace the attacker's funds, offer a bounty for return, post honest updates, and write a full post-mortem. Practice this before you need it.

## 392: What is formal verification for smart contracts?

Formal verification uses math tools to prove that code meets a specification for all possible inputs, not just tested ones. Tools include Certora, Halmos, the K framework and the Solidity SMTChecker. It's great for critical invariants like "total supply equals the sum of balances", but it's only as good as the spec, and writing good specs takes experience.

## 393: What is symbolic execution?

Symbolic execution runs code with symbolic variables instead of concrete values, exploring all paths and solving for inputs that reach each one. For smart contracts, it can find inputs that break an assertion or reach a revert you didn't expect. Halmos runs Foundry-style tests symbolically, and Mythril and hevm also use this approach.

## 394: What is differential fuzzing?

Differential fuzzing runs two implementations of the same thing with the same random inputs and checks that the outputs match. For example, an assembly-optimized math function versus a simple Solidity version, or your contract versus a reference model in Python. Any mismatch is a bug in one of them. Foundry can call external programs with `vm.ffi` for this.

## 395: How do you test upgrades safely?

Fork mainnet, deploy the new implementation, run the upgrade through the real proxy and admin path, and run your full test suite against the upgraded contract with real state. Check the storage layout with OpenZeppelin's upgrade tools or `forge inspect`. Verify that old data reads correctly, new initializers run once, and only the intended addresses can upgrade.

## 396: What is the risk of uninitialized implementation contracts?

If the implementation behind a proxy is never initialized, an attacker can call `initialize` on it directly and become its owner. With UUPS, that owner could upgrade the implementation itself to code that self-destructs, which used to break every proxy pointing to it (this was a real OpenZeppelin issue in 2021). Always call `_disableInitializers()` in the implementation constructor.

## 397: What is a function selector clash in proxies?

Two different function signatures can share the same 4-byte selector. In a proxy, if an admin function and an implementation function share a selector, calls can be routed wrongly. The transparent proxy pattern avoids this by handling admin calls only from the admin address. Tools check for clashes when you add functions to proxies or diamonds.

## 398: How would you design a gas-efficient NFT mint for 10,000 tokens?

Use ERC-721A-style batch minting, which records ownership once per batch instead of per token, or a simple counter-based ID with minimal storage writes. Avoid enumerable extensions that maintain extra arrays. Use Merkle proofs or signatures for allowlists, custom errors, and pack mint state into one slot. Keep metadata off-chain with a base URI.

## 399: What causes "nonce too low" and "replacement transaction underpriced" errors?

"Nonce too low" means a transaction with that nonce already got mined, often because two processes used the same key or your local nonce counter got out of sync. "Replacement transaction underpriced" means you sent a new transaction with a pending nonce, but its fees aren't high enough (about 10% more) to replace the old one. Both point to poor nonce management on the sender side.

## 400: How do you handle chain reorgs in a payment system?

Don't credit deposits on the first block. Wait for finality (on Ethereum, finalized blocks) or a safe number of confirmations based on the amount and chain. Store the block hash with each processed event; when a new block's parent hash doesn't match, roll back events from the dropped blocks and reprocess. Design your ledger so credits can be reversed until they're final.

## 401: How would you design a back end that sends many on-chain transactions reliably?

Use a job queue with one worker per sending address (or a few addresses to spread load). The worker assigns nonces locally, signs, broadcasts, and stores each transaction's state in a database. A separate watcher checks receipts, bumps fees on stuck transactions with the same nonce, and handles replacements and reorgs. Make jobs idempotent so retries never send the same payment twice.

## 402: How do you keep private keys safe on a server that signs transactions?

Don't keep raw keys in environment variables in production. Use a cloud KMS or HSM that supports secp256k1 (AWS KMS and Google Cloud KMS do), so the key never leaves the hardware and you sign through an API. Limit what each key can do with on-chain rules, like a smart account with spending limits, and keep hot wallet balances low.

## 403: How do you build a gasless transaction experience?

With ERC-4337, users sign a UserOperation and a paymaster sponsors the gas, often after your back end approves it. With EIP-7702, an EOA can delegate to a smart account implementation and get the same features. Older apps used meta-transactions (ERC-2771) with a trusted forwarder and a relayer. In all cases, protect the sponsor with rate limits and rules on what calls it pays for.

## 404: What is ERC-2771 and what are its risks?

ERC-2771 lets a trusted forwarder relay a user's signed request, appending the real sender's address to the call data. The contract reads `_msgSender()`, which returns that address when the call comes from the forwarder. A bug class appeared in 2023 when ERC-2771 was combined with `Multicall`: attackers could craft call data that spoofed `_msgSender()`. Use updated library versions and avoid mixing these patterns carelessly.

## 405: How do you build a token-gated website?

The user signs in with SIWE so you know they control an address. Your server then checks on-chain whether that address holds the required NFT or token balance (with a provider or indexer), and issues a session with the right permissions. Re-check holdings periodically since tokens can be sold. Never trust the front end to do the check.

## 406: How do you design a smart contract system for upgrades and long-term maintenance?

Decide early which parts must be upgradeable; keep core funds logic simple and immutable where you can. Put upgrades behind a timelock and a multisig or governance. Use namespaced storage, versioned initializers, and events for every admin action. Write migration tests and keep a public changelog. Some teams prefer immutable contracts and migrate users to new versions instead of upgrading.

## 407: When should you not use a blockchain?

If one trusted party runs the system anyway, if data must be private or deleted (GDPR), if you need high speed and low cost for simple records, or if users can't manage keys, a normal database is usually better. Blockchains are worth it when several parties who don't trust each other need a shared record, or when users need to own and move assets without permission.

## 408: How do you handle personal data and GDPR with blockchains?

Data on a public chain can't be deleted, which conflicts with the right to erasure. Keep personal data off-chain and store only hashes or references on-chain; delete the off-chain data and salt when needed so the hash becomes meaningless. Be careful that even addresses linked to people can count as personal data.

## 409: What are tokenized real-world assets (RWAs) and their technical challenges?

RWAs are tokens representing off-chain assets like treasury bills, real estate or invoices, such as BlackRock's BUIDL fund. Challenges: the token is only as good as the legal claim and the custodian, transfers often need allowlists for compliance, prices come from off-chain sources, and the issuer usually can freeze or force-transfer tokens. Standards like ERC-3643 add identity and transfer rules.

## 410: How do stablecoin issuers freeze funds and what does that mean for your contracts?

USDC and USDT have admin functions to blacklist addresses, after which those addresses can't send or receive. If your contract is blacklisted or holds funds for a blacklisted user, transfers to or from it will revert. Design with this in mind: don't let one blocked transfer stop everyone (use pull payments), and know that "decentralized" protocols holding these tokens still carry issuer risk.

## 411: How would you design a decentralized exchange order book on-chain?

A fully on-chain order book is expensive on Ethereum layer 1 because every order placement and cancel costs gas, so most designs keep orders off-chain as signed EIP-712 messages and settle matches on-chain (like 0x or CoW Swap). On fast chains or app-specific chains, on-chain order books are practical, as dYdX v4 and Hyperliquid show. Key concerns are front-running, fair matching and cancel latency.

## 412: How does Ethereum's EIP-1559 base fee formula work exactly?

Each block has a gas target (half the gas limit). The next base fee equals the current base fee times `1 + (gasUsed - gasTarget) / gasTarget / 8`. So a full block raises the base fee by 12.5% and an empty block lowers it by 12.5%. Blobs have a similar but separate mechanism based on blob gas used versus a blob target.

```js
function nextBaseFee(baseFee, gasUsed, gasTarget) {
  const delta = (baseFee * (gasUsed - gasTarget)) / gasTarget / 8n;
  return baseFee + delta;
}
```

## 413: What determines a validator's rewards on Ethereum?

Rewards come from consensus duties (attestations, proposing blocks, sync committee duties) and execution rewards (priority fees and MEV when proposing). Base rewards scale with the square root of total stake, so the per-validator yield drops as more ETH is staked. Missing duties costs small penalties; proposing a block is rare but can bring a large MEV payment.

## 414: How are ETH withdrawals and exits handled for validators?

Validators with execution-layer withdrawal credentials get balances above their effective balance swept automatically to their withdrawal address. To fully exit, the validator joins an exit queue, which has a limit per epoch to keep the validator set stable. Since Pectra, exits and partial withdrawals can also be triggered from the withdrawal address via a contract (EIP-7002), which helps staking pools.

## 415: What is the churn limit and why does it exist?

The churn limit caps how many validators (or how much ETH since Pectra) can enter or exit per epoch. It keeps the validator set from changing too quickly, which matters for the safety of finality and weak subjectivity: an attacker can't quickly withdraw slashable stake. During high demand, entry or exit queues can take days or weeks.

## 416: What is the difference between a light client in proof of work and in proof of stake?

In proof of work, a light client checks headers and their proof of work, and follows the chain with most work. In Ethereum's proof of stake, a light client follows a sync committee of 512 validators that changes about every 27 hours; it checks their aggregated BLS signatures on headers. This is very cheap and is used in wallets, bridges and ZK light client designs.

## 417: How do ZK light client bridges improve on multisig bridges?

A multisig bridge trusts a small group of signers to tell the truth about the other chain. A ZK light client bridge proves on-chain that the source chain's consensus (for example, the sync committee signatures and state) really produced a given block, so you trust only the source chain and the math. Proving consensus is expensive but costs have dropped with zkVMs.

## 418: What is the role of the Engine API?

The Engine API is the authenticated interface between Ethereum's consensus and execution clients. The consensus client sends new payloads to the execution client to validate and tells it which head to follow (`engine_newPayload`, `engine_forkchoiceUpdated`). When it's time to propose, it asks the execution client to build a payload (`engine_getPayload`). They authenticate with a shared JWT secret.

## 419: How do you run your own Ethereum node and when is it worth it?

Run an execution client (like Geth, Nethermind or Reth) plus a consensus client (like Lighthouse), using checkpoint sync, on a machine with a fast 2-4 TB NVMe SSD, 16-32 GB RAM and a solid connection. It's worth it when you need no rate limits, privacy for your queries, trace APIs, or independence from providers. For most apps, a reliable provider plus a fallback is cheaper to operate.

## 420: What are trace and debug APIs and when do you need them?

`debug_traceTransaction` and `trace_*` methods return the full internal execution of a transaction: every call, value transfer, and storage change. You need them for detecting internal ETH transfers (not visible in logs), analyzing hacks, and building explorers. They're heavy and often need archive nodes or premium plans.

```js
const trace = await provider.send("debug_traceTransaction", [
  txHash,
  { tracer: "callTracer" },
]);
```

## 421: How would you detect internal ETH transfers to a deposit address?

Contracts can send ETH to an address without emitting an event, so watching logs isn't enough. Use `callTracer` traces on every block (or provider webhooks that include internal transfers), or compare the address balance between blocks. A common alternative is to make deposit addresses contracts that emit an event in their `receive` function.

## 422: What is a reorg-safe way to build real-time notifications for users?

Send "pending" notifications from the mempool or latest block marked as unconfirmed, then send "confirmed" only after finality or enough confirmations. Store notifications with the block hash so you can retract or correct them if a reorg drops the transaction. Never trigger irreversible off-chain actions, like shipping goods, before finality.

## 423: What is EOF and what happened to it?

EOF (EVM Object Format) was a set of EIPs to restructure contract bytecode into sections for code and data, with validation at deploy time and new opcodes for jumps and calls. It was planned for Pectra, then for Fusaka, but was removed from Fusaka in 2025 after disagreement about its complexity and benefits. Contracts today still use the legacy bytecode format.

## 424: How would you reduce gas costs for a high-traffic contract?

Measure first with gas reports and traces. Then: pack storage, use transient storage for locks, cache storage reads, use `calldata`, custom errors and events instead of storage where possible, avoid unbounded loops, batch operations, and use clones for many instances. Consider moving the app to a layer 2, which often saves far more than micro-optimizations.

## 425: Why are gas refunds limited?

Clearing storage gives a refund, but since the London upgrade (EIP-3529) the refund is capped at one fifth of the transaction's gas used, and the `SELFDESTRUCT` refund was removed. Before this, "gas tokens" stored data when gas was cheap and cleared it when gas was expensive to get refunds, which bloated state and made blocks unpredictable.

## 426: How do you protect a DeFi protocol from oracle failure?

Use more than one source where you can (for example Chainlink plus a TWAP) and compare them. Check that data is fresh and within sane bounds, with circuit breakers that pause actions if prices jump too far. Handle the feed returning zero or reverting without bricking withdrawals. On layer 2s, also check the sequencer uptime feed.

## 427: What is economic security, and how do you estimate it for a protocol?

Economic security is the cost to attack something versus what an attacker can gain. For a proof of stake chain, it's roughly the stake that would be slashed in an attack. For an oracle or bridge, it's the cost to corrupt its signers. If an attacker can gain more than the attack costs (for example, a $10 million loan secured by an oracle that $1 million can manipulate), the design is broken.

## 428: How would you design an on-chain auction that resists front-running?

Use a sealed-bid commit-reveal auction with deposits, so bids are hidden until reveal and non-revealers lose part of their deposit. Alternatively use a Dutch auction, where the price falls over time and the first buyer wins, which makes front-running less useful. Batch auctions that clear all bids at one price (like CoW Swap) also remove ordering advantages.

## 429: How do you make a contract work with both EOAs and smart contract wallets?

Use `msg.sender` instead of `tx.origin`, verify signatures with `SignatureChecker` (supports ERC-1271), and don't use `extcodesize` to detect EOAs, since smart wallets and EIP-7702 accounts have code. Send ETH with `call` and enough gas, and support batched calls. Test with Safe and an ERC-4337 account.

## 430: Why is checking extcodesize to block contracts unreliable?

During a contract's constructor, its code size is still zero, so a contract can call you from its constructor and pass the check. Also, with EIP-7702, EOAs can have code, and smart wallets are legitimate users you probably don't want to block. If you need to stop bots, use other mechanisms like signatures from your back end or rate limits per address.

## 431: How do you design a token with a fixed supply that's safe from admin abuse?

Mint the full supply in the constructor, don't include a `mint` function, don't use upgradeable proxies, and don't add pause or blacklist powers. Renounce any ownership that isn't needed, or don't use `Ownable` at all. Verify the source so anyone can confirm. This makes the token trustworthy but means you can't fix bugs later.

## 432: What is a time-weighted voting or vote-escrow (veToken) model?

In a vote-escrow model, users lock tokens for a period (for example up to 4 years) and get voting power that grows with lock length and decays as the unlock date approaches. Curve's veCRV introduced it to reward long-term holders and direct rewards between pools. It reduces short-term vote buying but creates bribe markets where protocols pay locked holders for votes.

## 433: What is a sybil attack and how do apps resist it?

A sybil attack is one person creating many fake identities, like thousands of wallets to farm an airdrop or swing a vote. Since addresses are free, blockchains resist it through cost (fees, stake). Apps add sybil resistance with proof of personhood (World ID), on-chain history scoring, Gitcoin Passport-style stamps, or simply by weighting by tokens instead of by address.

## 434: How do privacy tools like mixers work and what are the legal concerns?

A mixer like Tornado Cash lets users deposit a fixed amount into a pool and later withdraw to a new address with a ZK proof that they made some deposit, without revealing which. This breaks the link between addresses. It was sanctioned by the US Treasury in 2022 for laundering use; a court later ruled the immutable contracts couldn't be sanctioned and the sanctions were lifted in 2025, but developer prosecutions show the legal risk is still real. Privacy Pools propose letting users prove they're not linked to known illicit deposits.

## 435: What are stealth addresses?

Stealth addresses let a sender create a fresh one-time address for a receiver from the receiver's public "meta-address", so payments to the same person can't be linked publicly. Only the receiver can find and spend them by scanning announcements with their viewing key. ERC-5564 standardizes this for Ethereum.

## 436: What is fully homomorphic encryption (FHE) in blockchains?

FHE lets you compute on encrypted data without decrypting it. Some projects, like Zama's fhEVM, use it to make smart contracts with encrypted balances and inputs, so state stays private while contracts still work. It's still slow and expensive compared to normal execution, and decryption needs a threshold network of key holders.

## 437: How might quantum computers threaten blockchains?

A large quantum computer could use Shor's algorithm to derive private keys from public keys, breaking ECDSA and BLS. Addresses whose public key was never revealed are safer for now, because only a hash is public. Hashes are only weakened, not broken. The defense is migrating to post-quantum signatures (like hash-based or lattice-based schemes), and both Bitcoin and Ethereum researchers have active proposals.

## 438: How does Ethereum's roadmap plan to scale layer 1 itself?

Plans include raising the gas limit steadily as clients get faster, parallel execution through block-level access lists (Glamsterdam), repricing operations to match real costs, statelessness so nodes don't need all state, and eventually verifying blocks with ZK proofs so validators don't re-execute. The goal is a much faster layer 1 while home validators can still keep up.

## 439: What would you check before integrating a third-party DeFi protocol?

Read its audits and bug bounty, check admin powers (who can upgrade, pause, or change parameters, and if there's a timelock), its oracle setup, past incidents, TVL and liquidity depth, and token quirks. Test the integration on a mainnet fork with edge cases like paused states and extreme prices. Cap how much of your funds depend on it.

## 440: Walk through what happens when a user clicks "Swap" on a DEX front end.

The front end gets a quote from a router or aggregator API and simulates the swap. If the token isn't approved, it asks for an approval or a Permit2 signature. Then the wallet shows the swap transaction with a minimum output (slippage) and deadline. The user signs, the wallet sends it to an RPC (ideally a private one), it lands in a block, the router pulls the input token, swaps through pools, checks the minimum output, and sends the result. The front end waits for the receipt and updates balances.

## 441: How would you debug "execution reverted" with no reason?

First simulate the call with `eth_call` and full ABI (including errors of called contracts) to decode any custom error. If there's no data, the revert likely came from a failed `require` without a message, a call to an address with no code, running out of gas in a sub-call, or a low-level `revert()`. Trace it with `cast run` or Tenderly to see the exact call and opcode, and check token quirks like a missing return value.

## 442: How do you test a contract that depends on time?

Use cheatcodes to move time: `vm.warp` sets `block.timestamp` and `vm.roll` sets the block number. Test boundaries exactly: one second before, at, and after deadlines. Remember that on mainnet, timestamps advance in 12-second steps, and on some layer 2s they behave differently, so avoid logic that assumes precise timing.

```solidity
function test_CannotClaimBeforeUnlock() public {
    vm.warp(unlockTime - 1);
    vm.expectRevert(Vesting.Locked.selector);
    vesting.claim();
}
```

## 443: How do you write an invariant test in Foundry?

Create a handler contract with functions that call your system in valid ways, register it as the target, and write `invariant_` functions that assert properties. Foundry calls handler functions in random order with random inputs, then checks the invariants after each call.

```solidity
contract VaultInvariants is Test {
    Vault vault;
    Handler handler;

    function setUp() public {
        vault = new Vault();
        handler = new Handler(vault);
        targetContract(address(handler));
    }

    function invariant_SolventVault() public view {
        assertGe(address(vault).balance, vault.totalDeposits());
    }
}
```

## 444: What makes a good bug bounty program for a protocol?

Clear scope (which contracts and which networks), rewards that scale with funds at risk (often 10% of the amount at risk up to a cap) so whitehats prefer reporting over exploiting, a fast and honest triage process, and a safe harbor statement. Immunefi and Cantina host many programs. It should run alongside audits, not replace them.

## 445: How would you migrate users from an old contract to a new one?

If the contract isn't upgradeable, deploy the new version, then either let users move their positions themselves with a helper contract that withdraws from the old and deposits into the new in one transaction, or take a snapshot and airdrop new balances. Pause new deposits in the old contract but always keep withdrawals open. Communicate clearly and give plenty of time.

## 446: How do you design an NFT marketplace's order matching securely?

Sellers sign EIP-712 orders off-chain with price, token, expiry, nonce and fees. On purchase, the contract checks the signature (with ERC-1271 support), that the order isn't cancelled or filled, the expiry, and that the seller still owns and approved the token, then transfers payment and the NFT atomically. Let users cancel all orders at once by bumping a counter. Seaport is a well-known design to learn from.

## 447: What are the trade-offs between app-specific chains and deploying on a general-purpose chain?

An app chain (Cosmos SDK chain, OP Stack or Arbitrum Orbit rollup) gives you control over block space, fees, ordering and upgrades, and can capture MEV and fees for your own token. But you must bootstrap security and liquidity, run infrastructure, and you lose easy composability with other apps. Deploying on a shared chain gives you users, liquidity and composability, but you compete for block space.

## 448: How do you choose which chain to build on?

Look at where your users and the liquidity you need already are, transaction cost and speed requirements, the security model (layer 1, rollup stage, or sidechain), tooling and language (EVM versus Solana or Move), wallet support, and the ecosystem of oracles, indexers and bridges. For many web apps, an established Ethereum layer 2 is a sensible default.

## 449: How would you design a cross-chain token?

Pick one canonical issuance model: either a burn-and-mint setup controlled by the issuer across chains (using a standard like ERC-7802 or a messaging layer such as CCIP or LayerZero's OFT), or a hub chain with lock-and-mint to others. Add rate limits on minting per bridge, so one compromised bridge can't mint unlimited tokens. Keep total supply tracking clear and avoid several competing wrapped versions.

## 450: What's a sensible end-to-end architecture for a production dApp?

Smart contracts with tests, fuzzing, audits, a multisig and timelock for admin, and monitoring. A front end with wagmi/viem, EIP-6963 wallet discovery, simulation before signing, clear transaction states and chain checks. A back end with an indexer writing events to a database, an API for the front end, a reliable transaction sender if needed, and keys in a KMS. Infrastructure with multiple RPC providers, alerts, and an incident runbook. Keep on-chain only what needs trust, and everything else off-chain.
