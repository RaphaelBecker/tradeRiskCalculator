
def calc_trade(availalbe_balance, einsatz, startPreis, leverage):
    # Use a breakpoint in the code line below to debug your script.
    i = 0
    persent = leverage / 100
    korrekturKonto = availalbe_balance - einsatz
    einsatzcalc = einsatz
    liqPreis = startPreis + (persent - persent * 0.025) * startPreis
    print(' ')
    print(f'Available Balance: {korrekturKonto}')
    print('Initial trade:', einsatz, 'Entry price: ', '%0.2f' % startPreis, 'Liquidation price: ', '%0.2f' % liqPreis)
    print(' ')
    while (einsatzcalc <= korrekturKonto):
        korrekturKonto = korrekturKonto - einsatzcalc
        trade_vol = einsatzcalc * 2
        print('Corr-Nr: ',i + 1, ' Trade vol:', trade_vol , ' Correction: ', einsatzcalc, ' Avai balance:', korrekturKonto)
        einsatzcalc = einsatzcalc * 2
        i += 1
        startPreis = startPreis + 0.5 * (liqPreis - startPreis)
        liqPreis = startPreis + (persent - persent * 0.025) * startPreis
        print('New entry price: ', '%0.2f' % startPreis, '  Liquidation price:', '%0.2f' % liqPreis)
        print(' ')
    print(f'Corrections possible: {i}')  # Press ⌘F8 to toggle the breakpoint.
    startPreis = startPreis + (availalbe_balance / (trade_vol + availalbe_balance)) * (liqPreis - startPreis)
    liqPreis = startPreis + (persent - persent * 0.025) * startPreis
    print('Last liquidation price: ', liqPreis)

def add(num1, num2):
    return num1 + num2