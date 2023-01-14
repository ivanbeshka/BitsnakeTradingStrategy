from tradingview_ta import TA_Handler, Interval

def choose_sma():
    SMA = TA_Handler(
            symbol="BTCUSDT",
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_1_DAY
        )
    return SMA.get_analysis().moving_averages['COMPUTE']['SMA100']

def choose_position(taimfraim):
    BTC = TA_Handler(
        symbol="BTCUSDT",
        screener="crypto",
        exchange="BINANCE",
        interval=taimfraim
    )
    return BTC.get_analysis().oscillators['COMPUTE']['RSI']

def make_purchase():
    # функция выставления ордера на покупку
    print("покупаем")

def complete_sale():
    # функция выставления ордера на продажу
    print("продаём")

def getting_value(taimfraims):
    values = []
    for taimfraim in taimfraims:
        values.append(choose_position(taimfraim))
    values.append(choose_sma())
    if all(values):
        if values[0] == 'BUY':
            make_purchase()
        elif values[0] == 'SELL':
            complete_sale()



taimfraims = (Interval.INTERVAL_1_MINUTE, Interval.INTERVAL_30_MINUTES, Interval.INTERVAL_4_HOURS)
getting_value(taimfraims)

