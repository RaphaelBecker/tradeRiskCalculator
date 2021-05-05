
def calc_trade(availalbe_balance, initial_bet, start_price, leverage):
    # Use a breakpoint in the code line below to debug your script.
    i = 0
    persent = leverage / 100
    correction_account = availalbe_balance - initial_bet
    bet = initial_bet
    liq_price = start_price + (persent - persent * 0.025) * start_price
    print(' ')
    print(f'Available Balance: {correction_account}')
    print('Initial trade:', initial_bet, 'Entry price: ', '%0.2f' % start_price, 'Liquidation price: ', '%0.2f' % liq_price)
    print(' ')
    while (bet <= correction_account):
        correction_account = correction_account - bet
        trade_vol = bet * 2
        print('Corr-Nr: ',i + 1, ' Trade vol:', trade_vol , ' Correction: ', bet, ' Avai balance:', correction_account)
        bet = bet * 2
        i += 1
        start_price = start_price + 0.5 * (liq_price - start_price)
        liq_price = start_price + (persent - persent * 0.025) * start_price
        print('New entry price: ', '%0.2f' % start_price, '  Liquidation price:', '%0.2f' % liq_price)
        print(' ')
    print(f'Corrections possible: {i}')  # Press ⌘F8 to toggle the breakpoint.
    start_price = start_price + (availalbe_balance / (trade_vol + availalbe_balance)) * (liq_price - start_price)
    liq_price = start_price + (persent - persent * 0.025) * start_price
    print('Last liquidation price: ', liq_price)

def add(num1, num2):
    return num1 + num2