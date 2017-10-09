import os

### GLOBALS ###
# NoteToSelf: try to fix this in later assignments.


### FUNCTIONS ###

def get_quote(ticker):
    import pandas_datareader as pdr
    '''
    Using Yahoo market data feed, and not Bloomberg
    Using Pandas, instead of using BS4.
    There is a strong reason for doing this. Instead of scraping the page, and trying to cast
    the traded value as float, I think if we use a native pandas data-type, which returns values
    as float, then we are in a better position.
    Personally speaking, I would go for a typed return value, than parsing and praying for results to be accurate.
    
    The return value of the fx, can be used in operations.
    e.g. val = get_quote('MSFT')
    val = val+1
    val is of the type float64
    
    I believe, this is a much safer approach when dealing with stock quotes.
    '''
    quote = pdr.get_quote_yahoo(ticker)
    traded_value = quote['last']
    return traded_value 

def stock_buy(ticker,qty):
    quote = get_quote(ticker)
    print("BUYING:: %s shares of %s, at PRICE: $%s" %(qty, ticker, quote))
            
def stock_sell(ticker,qty):
    print("SELLING:: %s, shares of %s." %(qty, ticker))
    
# based on Intro to Python - http://introtopython.org/terminal_apps.html
def display_title_bar():
    print("\t**********************************************")
    print("\t***  CONSOLE TRADER !!  ***")
    print("\t**********************************************")
    
def display_menu():
    # Clears the terminal screen, and displays a title bar.
    choice = ''
    while choice != 'q':    
        display_title_bar()
        
        # Let users know what they can do.
        print("\n[1] Trade.")
        print("[2] Show Blotter.")
        print("[3] Show P/L.")
        print("[q] Quit.")
        
        choice = input("What would you like to do? ")
        
        # Respond to the user's choice.
        if choice == '1':
            print("\n")
            print("You are in the **TRADING MENU**. Please enter your trade separated by a single space.")
            print("The first word should be a trade-typre (BUY/SELL). Second word should be the ticker, followed by quantity.")
            print("E.g. BUY AAAPL 100")
            print("\n")
            user_input = input()
            parsed_text = user_input.split()
            trade = parsed_text[0]
            stock = parsed_text[1]
            qty = int(parsed_text[2])
            
            
            print("Please confirm, that you want to %s, %s shares of, %s." %(trade,qty,stock))
            print("")
            
            if trade== 'BUY':
                stock_buy(stock,qty)
            if trade== 'SELL':
                stock_sell(stock,qty)
                 
        elif choice == '2':
            print("\n")
            print("Current Blotter status")
            
        elif choice == '3':
            print("\n")
            print("Current P/L status")
            
        elif choice == 'q':
            print("\n")
            print("Thanks for trading with us. Goodbye.")
        
        else:
            print("\n")
            print("That option is not available. Please try again")

