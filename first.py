# If the numbers to are written out in words: one, two, three, four, five,
#  then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
 
 





units=['one','two','three','four','five','six','seven','eight','nine']
teens=['eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# teen=['eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
hundred='hundred'
thousand='thousand'
def number_to_words(n):
    if 1<=n <=9:
        return units[n-1]
    elif 11<=n<=19:
        return teens[n-11]
    elif 10<=n<=99:
        if n%10 == 0:
            return tens[n//10-1]
        else:
            return tens[n//10-1]+units[n%10-1]
    elif 100<=n<=999:
        if n%100 == 0:
            return units[n//100-1]+hundred
        else:
            return units[n//100-1]+hundred+'and'+ number_to_words(n%100)
    elif n==1000:
        return 'one'+ thousand
    
    total_letters=0
    for i in range(1,1001):
        words=number_to_words(i)
        total_letters =total_letters+len(words)
    print("total leters are :",total_letters)