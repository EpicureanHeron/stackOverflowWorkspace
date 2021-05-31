x = price= [[{'adjusted_mark_price': '0.400000', 'ask_price': '0.430000', 'ask_size': 49, 'bid_price': '0.370000', 'bid_size': 37, 'break_even_price': '260.400000', 'high_price': '0.710000', 'instrument': 'https://api.robinhood.com/options/instruments/70b3f0a9-3747-4cde-817e-07850f2d1a16/', 'instrument_id': '70b3f0a9-3747-4cde-817e-07850f2d1a16', 'last_trade_price': '0.390000', 'last_trade_size': 1, 'low_price': '0.380000', 'mark_price': '0.400000', 'open_interest': 2409, 'previous_close_date': '2021-05-27', 'previous_close_price': '0.470000', 'volume': 747, 'symbol': 'MSFT', 'occ_symbol': 'MSFT  210611C00260000', 'chance_of_profit_long': '0.092005', 'chance_of_profit_short': '0.907995', 'delta': '0.105930', 'gamma': '0.022910', 'implied_volatility': '0.177756', 'rho': '0.008438', 'theta': '-0.061925', 'vega': '0.082234', 'high_fill_rate_buy_price': '0.420000', 'high_fill_rate_sell_price': '0.370000', 'low_fill_rate_buy_price': '0.390000', 'low_fill_rate_sell_price': '0.400000'}]]

print(x)

print(x[0])

print(x[0][0]['ask_size'])