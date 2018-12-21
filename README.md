# finance-ner
Named Entity Recogniser for Finance.

Take this delighful (highly illegal) exchange between 2 Deutsche bank traders: 

```
Trader 1: We have, eh, we have 20 yards of a 6 month fixing. [ . . . ] A lot in in March. So, basically, um, basically, uh, we need high 6 month.
Trader 2: You need high 6 month, ok.
Trader 1: High 6 month, yes.
Trader 2: Sure, we will get high 6 month, no worries.
Trader 1: High.
Trader 2: We will get high 6 month.
Trader 1: Es . . . especially on the IMM, on the 19th I have 7 yards.
```

That's barely understandle to a human that doesn't know finance. A machine without specific training has no chance to understand this. So we built a Named Entity Recognizer just for finance, so people can make sense of it all. 

FYI: 1 Yard = 1 Billion Dollars of notional. Someone once told me this is you don't get a 'Billion' confussed with 'A Million' when yelling across the trading floor, which Investopedia confirms. I guess that was an expensive mistake once upon a time. 
