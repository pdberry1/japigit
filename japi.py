import sys
from alpha_vantage.timeseries import TimeSeries 


API_KEY = 'ZK80GPZ5T9QV0RPM'

def getStockdata(symbol):

    try:

        print("Gathering info....")

        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:

        return "not found"

def main():

    outFile = open('japi.out', 'w')

    while 1:

        userInput = input("Hello! Please enter a stock symbol or enter EXIT to leave the program: ").upper()

        if userInput != "EXIT":

            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))

            print(serverData)

            outFile.write(serverData)

        else:

            sys.exit("\nThank you, Goodbye!\n")

main()