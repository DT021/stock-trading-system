import pandas as pd
import finnhub


# Setup client
client = finnhub.Client(api_key="bsqlqj748v6p29vi65q0")

# Stock candles
res = client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

# Convert to Pandas Dataframe
print(pd.DataFrame(res))

# Aggregate Indicators
print(client.aggregate_indicator('AAPL', 'D'))

# Basic financials
print(client.company_basic_financials('AAPL', 'margin'))

# Earnings surprises
print(client.company_earnings('TSLA', limit=5))

# EPS estimates
print(client.company_eps_estimates('AMZN', freq='quarterly'))

# Company Executives
print(client.company_executive('AAPL'))

# Company News
# Need to use _from instead of from to avoid conflict
print(client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))

# Company Peers
print(client.company_peers('AAPL'))

# Company Profile
print(client.company_profile(symbol='AAPL'))
print(client.company_profile(isin='US0378331005'))
print(client.company_profile(cusip='037833100'))

# Company Profile 2
print(client.company_profile2(symbol='AAPL'))

# Revenue Estimates
print(client.company_revenue_estimates('TSLA', freq='quarterly'))

# List country
print(client.country())

# Crypto Exchange
print(client.crypto_exchanges())

# Crypto symbols
print(client.crypto_symbols('BINANCE'))

# Economic data
print(client.economic_data('MA-USA-656880'))

# Filings
print(client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11"))

# Financials
print(client.financials('AAPL', 'bs', 'annual'))

# Financials as reported
print(client.financials_reported(symbol='AAPL', freq='annual'))

# Forex exchanges
print(client.forex_exchanges())

# Forex all pairs
print(client.forex_rates(base='USD'))

# Forex symbols
print(client.forex_symbols('OANDA'))

# Fund Ownership
print(client.fund_ownership('AMZN', limit=5))

# General news
print(client.general_news('forex', min_id=0))

# Investors ownership
print(client.investors_ownership('AAPL', limit=5))

# IPO calendar
print(client.ipo_calendar(_from="2020-05-01", to="2020-06-01"))

# Major developments
print(client.major_developments(
    'AAPL', _from="2020-01-01", to="2020-12-31"))

# News sentiment
print(client.news_sentiment('AAPL'))

# Pattern recognition
print(client.pattern_recognition('AAPL', 'D'))

# Price target
print(client.price_target('AAPL'))

# Quote
print(client.quote('AAPL'))

# Recommendation trends
print(client.recommendation_trends('AAPL'))

# Stock dividends
print(client.stock_dividends('KO', _from='2019-01-01', to='2020-01-01'))

# Stock symbols
print(client.stock_symbols('US')[0:5])

# Transcripts
print(client.transcripts('AAPL_162777'))

# Transcripts list
print(client.transcripts_list('AAPL'))

# Earnings Calendar
print(client.earnings_calendar(_from="2020-06-10",
                               to="2020-06-30", symbol="", international=False))

# Covid-19
print(client.covid19())

# Upgrade downgrade
print(client.upgrade_downgrade(
    symbol='AAPL', _from='2020-01-01', to='2020-06-30'))

# Economic code
print(client.economic_code()[0:5])

# Support resistance
print(client.support_resistance('AAPL', 'D'))

# Technical Indicator
print(client.technical_indicator(symbol="AAPL", resolution='D',
                                 _from=1583098857, to=1584308457, indicator='rsi', indicator_fields={"timeperiod": 3}))

# Stock splits
print(client.stock_splits('AAPL', _from='2000-01-01', to='2020-01-01'))

# Forex candles
print(client.forex_candles('OANDA:EUR_USD', 'D', 1590988249, 1591852249))

# Crypto Candles
print(client.crypto_candles(
    'BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))

# Tick Data
print(client.stock_tick('AAPL', '2020-03-25', 500, 0))


# Indices Constituents
print(client.indices_const(symbol="^GSPC"))

# Indices Historical Constituents
print(client.indices_hist_const(symbol="^GSPC"))

# ETFs Profile
print(client.etfs_profile('SPY'))

# ETFs Holdings
print(client.etfs_holdings('SPY'))

# ETFs Industry Exposure
print(client.etfs_ind_exp('SPY'))

# ETFs Country Exposure
print(client.etfs_country_exp('SPY'))
