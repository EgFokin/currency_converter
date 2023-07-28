import requests 


def get_exchange_rates():
    access_key = "YOUR_FIXER_IO_ACCESS_KEY"  # Replace this with your own Fixer.io access key
    url = f"http://data.fixer.io/api/latest?access_key={access_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error while fetching exchange rates.")
        return None
    
    data = response.json()
    return data["rates"]


def currency_converter():
    exchange_rates = get_exchange_rates


    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency from which you want to convert: ") # USD/EUR/RUB etc
    to_currency = input("Enter the currency to which you want to convert: ") #USD/EUR/RUB etc

    if from_currency not in exchange_rates() or to_currency not in exchange_rates():
        print("Error: Invalid currencies specified.")
        return
    
    converted_money = amount * exchange_rates()[to_currency] / exchange_rates()[from_currency]

    result = f"Conversion result: {amount:.2f} {from_currency} = {converted_money:.2f} {to_currency}"
    print(result)

currency_converter() # call func
    
