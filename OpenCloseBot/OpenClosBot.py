import MetaTrader5 as mt5
from mt5_trade_utils import send_market_order, close_position, close_all_positions
from time import sleep

if __name__ == "__main__":

    mt5.initialize()

   
    login = mt5_credentials['login']
    password = mt5_credentials['password']
    server = mt5_credentials['server']

    mt5.login(login, password, server)
   


    sleep(5)
    symbol = 'XAUUSD'
    volume = 1.0
    order_type = 'sell'
    send_market_order(symbol, volume, order_type)
    sleep(5)
    close_all_positions('all')