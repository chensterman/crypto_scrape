# CryptoScrape

## Description
Simple app built for a friend to scrape cryptocurrency data.

## Usage
1. Have Python 3.11 installed.
2. Clone this repo and `cd` into the directory.
3. Run `pip install -r requirements.txt` to install the necessary dependencies.
3. Obtain a [Google Serper](https://serper.dev/) (free $50 credit on sign-up, I believe) and [CoinMarketCap](https://coinmarketcap.com/api/) (use the basic/free plan) API key
4. Create a `.env` file and populate with both API keys
	- SERP_API_KEY=[INSERT KEY HERE]
	- CMC_PRO_API_KEY=[INSERT KEY HERE]
5. Run `python scrape.py` to start the script.
6. Enter the token name (e.g. "bitcoin", "uniswap", etc.) and blockchain name (e.g. "ethereum") to begin scraping.

## Sample Result
For `uniswap` as token name and `ethereum` as blockchain name:
```json
{
	'website': {
		'link': 'https://uniswap.org/',
		'snippet': 'Build Defi apps and tools on the largest crypto project on Ethereum. Get started with quick start guides, protocol documentation, a Javascript SDK, and fully ...',
	},
	'twitter': {
		'link': 'https://twitter.com/uniswap?lang=en',
		'snippet': '@Uniswap. The largest onchain marketplace. Buy and sell crypto on Ethereum and 7+ other chains. Software Company Ethereum app.uniswap.org Joined April 2018.',
	},
	'discord': {
		'link': 'https://discord.com/invite/uniswap',
		'snippet': 'Uniswap is a decentralized exchange built on the Ethereum blockchain. | 45889 members.',
	},
	'dextools': {
		'link': 'https://www.dextools.io/app/en/ether/pair-explorer/0x3470447f3cecffac709d3e783a307790b0208d60?t=1711575005565',
		'snippet': 'Uniswap latest price, buy, sell and trade UNI, check airdrops, bots, whales on Bscscan, trending/listing at Pancakeswap V2.',
	},
	'cmc': {
		'market_data': {
			'USD': {
				'price': 12.917140502025433,
				'volume_24h': 160680953.22939783,
				'volume_change_24h': 32.3963,
				'percent_change_1h': -0.27395388,
				'percent_change_24h': 2.29409609,
				'percent_change_7d': 7.54920277,
				'percent_change_30d': 11.56733713,
				'percent_change_60d': 115.88573455,
				'percent_change_90d': 71.11356211,
				'market_cap': 7733958840.2744,
				'market_cap_dominance': 0.2873,
				'fully_diluted_market_cap': 12917140502.03,
				'tvl': 6042716731.51146,
				'last_updated': '2024-03-31T22:37:00.000Z',
			},
		},
		'link': 'https://coinmarketcap.com/currencies/uniswap',
	},
	'address_results': [
		{'link': 'https://docs.uniswap.org/contracts/v3/reference/deployments', 'snippet': 'Every Uniswap pool is a unique instance of the UniswapV3Pool contract and is deployed at its own unique address. The contract source code of the pool will be ...'},
		{'link': 'https://etherscan.io/address/0x7a250d5630b4cf539739df2c5dacb4c659f2488d', 'snippet': 'A contract address hosts a smart contract, which is a set of code stored on the blockchain that runs when predetermined conditions are met. Learn more about ...'},
		{'link': 'https://uniswap.org/', 'snippet': 'Swap, earn, and build on the leading decentralized crypto trading protocol.'},
	],
	'address_versbose_results': [
		{'link': 'https://docs.uniswap.org/contracts/v3/reference/deployments', 'snippet': 'Every Uniswap pool is a unique instance of the UniswapV3Pool contract and is deployed at its own unique address. The contract source code of the pool will be ...'},
		{'link': 'https://etherscan.io/address/0x7a250d5630b4cf539739df2c5dacb4c659f2488d', 'snippet': 'Uniswap V2: Router 2. 0.0009065455 ETH, (Pending) ... Uniswap V2: Router 2. 0.002 ETH ... Understand, Copy Address. Back to Top. Ethereum Logo Powered by Ethereum.'},
		{'link': 'https://uniswap.org/', 'snippet': 'Build Defi apps and tools on the largest crypto project on Ethereum. Get started with quick start guides, protocol documentation, a Javascript SDK, and ...'},
	],
	'google_results': [
		{'link': 'https://uniswap.org/', 'snippet': 'UNISWAP PROTOCOL. Swap, earn, and build on the leading decentralized crypto trading protocol. Launch App. $1.8T+. Trade Volume. 224M+. All Time Trades.'},
		{'link': 'https://www.coinbase.com/price/uniswap', 'snippet': 'Uniswap (UNI) is the largest decentralized exchange (or DEX) operating on the Ethereum blockchain. It allows users anywhere in the world to trade crypto without ...'},
		{'link': 'https://coinmarketcap.com/currencies/uniswap/', 'snippet': 'The live Uniswap price today is $13.04 USD with a 24-hour trading volume of $159,806,867 USD. We update our UNI to USD price in real-time. Uniswap is up 1.80% ...'},
		{'link': 'https://www.coindesk.com/price/uniswap/', 'snippet': 'Uniswap USD price, real-time (live) charts, UNI crypto and videos, Learn about UNI value, Uniswap news, crypto trading and more.'},
		{'link': 'https://crypto.com/price/uniswap', 'snippet': "Uniswap's price today is US$12.77, with a 24-hour trading volume of $174.57 M. UNI is +0.48% in the last 24 hours. It is currently -0.90% from its 7-day all- ..."},
	],
}
```