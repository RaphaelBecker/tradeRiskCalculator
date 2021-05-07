def calc_short_trade(availalbe_balance, initial_bet, start_price, leverage):
    return_string = '-------------------------------------------------------------\n'
    return_string += 'DISCLAIMER: ALWAYS DOUBLE CHECK THE CALCULATIONS \n - NO GUARANTEE OF ACCURACY!\n \nSHORT trade ' \
                    'calculation:\n '
    i = 0
    percent = 1/leverage
    correction_account = availalbe_balance - initial_bet
    bet = initial_bet
    liq_price = start_price + (percent - percent * 0.026) * start_price
    return_string += str(f'\nAvailable Balance: {correction_account} ')
    return_string += str(f' Initial trade: {initial_bet} ')
    return_string += str(f'\nEntry price: {start_price:.2f} ')
    return_string += str(f'Liquidation price: {liq_price:.2f}\n')
    while bet <= correction_account:
        correction_account = correction_account - bet
        trade_vol = bet * 2
        return_string += str(f'\nCorr-Nr: {i + 1} ')
        return_string += str(f'\nTrade vol: {trade_vol} ')
        return_string += str(f'Correction: {bet} ')
        return_string += str(f'Remaining balance: {correction_account:.2f} ')
        bet = bet * 2
        i += 1
        start_price = start_price + 0.5 * (liq_price - start_price)
        liq_price = start_price + (percent - percent * 0.026) * start_price
        return_string += str(f'\nNew entry price: {start_price:.2f} ')
        return_string += str(f'Liquidation price: {liq_price:.2f} ')
        return_string += '\n'
    return_string += '\n**********************************\n'
    return_string += str(f'Corrections possible: {i} ')
    start_price = start_price + (availalbe_balance / (trade_vol + availalbe_balance)) * (liq_price - start_price)
    liq_price = start_price + (percent - percent * 0.026) * start_price
    return_string += str(f'\nFinal liquidation price: {liq_price:.2f} \n \n \n')
    return return_string


def calc_long_trade(availalbe_balance, initial_bet, start_price, leverage):
    return_string = '-------------------------------------------------------------\n'
    return_string += 'DISCLAIMER: ALWAYS DOUBLE CHECK THE CALCULATIONS \n - NO GUARANTEE OF ACCURACY!\n \nLONG trade ' \
                    'calculation:\n '
    i = 0
    percent = 1/leverage
    correction_account = availalbe_balance - initial_bet
    bet = initial_bet
    liq_price = start_price - (percent - percent * 0.026) * start_price  # + long!
    return_string += str(f'\nAvailable Balance: {correction_account} ')
    return_string += str(f' Initial trade: {initial_bet} ')
    return_string += str(f'\nEntry price: {start_price:.2f} ')
    return_string += str(f'Liquidation price: {liq_price:.2f}\n')
    while bet <= correction_account:
        correction_account = correction_account - bet
        trade_vol = bet * 2
        return_string += str(f'\nCorr-Nr: {i + 1} ')
        return_string += str(f'\nTrade vol: {trade_vol} ')
        return_string += str(f'Correction: {bet} ')
        return_string += str(f'Remaining balance: {correction_account:.2f} ')
        bet = bet * 2
        i += 1
        start_price = start_price - 0.5 * (start_price - liq_price)  # switched +- long!
        liq_price = start_price - (percent - percent * 0.026) * start_price  # + long!
        return_string += str(f'\nNew entry price: {start_price:.2f} ')
        return_string += str(f'Liquidation price: {liq_price:.2f} ')
        return_string += '\n'
    return_string += '\n**********************************\n'
    return_string += str(f'Corrections possible: {i} ')
    start_price = start_price - (correction_account / (trade_vol + correction_account)) * (start_price - liq_price) # switched liq_price and start_price
    liq_price = start_price - (percent - percent * 0.026) * start_price
    return_string += str(f'\nFinal liquidation price: {liq_price:.2f} \n \n \n')
    return return_string


def add(num1, num2):
    return num1 + num2
