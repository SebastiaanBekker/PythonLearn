# Een bedrag gepast betalen met zo min mogelijk euromunten

bedrag = input ( 'Geef bedrag tussen 0 en 500 eurocent: ' )

totaal = 0

for munt in 200, 100, 50, 20, 10, 5, 2, 1 :
    aantal = 0

    while bedrag >= munt :
      aantal = aantal + 1
      totaal = totaal + 1
      bedrag = bedrag - munt
    
    if aantal > 0 :
        print aantal, 'x', munt


print 'aantal munten', totaal