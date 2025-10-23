def add_vat(prices,vat_price):
    return prices*(100+vat_price)/100;

price=[10,20,40];
vat_rated=0;
result=0;
for prices in price:
    vat_rated+=add_vat(prices,10);

print(f"Each VAT Rated price is {vat_rated}")