
import MetaTrader5 as mt5
import pandas as pd
from time import sleep
from datetime import datetime

from mt5_trade_utils import send_market_order, close_all_positions, get_positions
from config import mt5_credentials


if __name__ == '__main__':
    
    mt5.initialize(mt5_credentials['exe_path'])

   
    login = mt5_credentials['login']
    password = mt5_credentials['password']
    server = mt5_credentials['server']

    mt5.login(login, password, server)

    
    symbol = 'EURUSD'
    time_frame = mt5.TIMEFRAME_M1
    period = 20
    magic = 1

    volume = 0.1

    
    sleep(5)

    
    trading_allowed = True
    while trading_allowed:

        
        rates = mt5.copy_rates_from_pos(symbol, time_frame, 1, 20)
        rates_df = pd.DataFrame(rates)

        sma = rates_df['close'].mean()

       
        last_close = rates_df.iloc[-1]['close']

        print('time', datetime.now(), '|', 'sma', sma, '|', 'last_close', last_close)

        
        positions = get_positions(magic=magic)

       
        num_buy_positions = positions[positions['type'] == mt5.ORDER_TYPE_BUY].shape[0]
        num_sell_positions = positions[positions['type'] == mt5.ORDER_TYPE_SELL].shape[0]

        if last_close > sma:
            
            if num_sell_positions > 0:
               
                close_all_positions('sell', magic=magic)

            
            if num_buy_positions == 0:
               
                send_market_order(symbol, volume, 'buy', magic=magic)

        elif last_close < sma:
            
            if num_buy_positions > 0:
                
                close_all_positions('buy', magic=magic)
               

           
            if num_sell_positions == 0:
                
                send_market_order(symbol, volume, 'sell', magic=magic)

        sleep(1)
