

#Variant 8: Crypto Portfolio Holding

class CryptoHolding:
    def __init__(self, token_name,usd_price,coin_amount):
        self.token_name =token_name
        self.usd_price =usd_price
        self.coin_amount =coin_amount

    def __str__(self):
        return f"{self.token_name}: {self.coin_amount} coin(s) at ${self.usd_price}"

    def __repr__(self):
        return f"CryptoHolding('{self.token_name}', {self.usd_price}, {self.coin_amount})"

    def __add__(self, other):
        if isinstance(other, CryptoHolding):
            if self.token_name ==other.token_name:
                return CryptoHolding(
                    self.token_name,
                    self.usd_price,
                    self.coin_amount +other.coin_amount
                )
            else:
                return NotImplemented

        elif isinstance(other, int):
            return CryptoHolding(
                self.token_name,
                self.usd_price,
                self.coin_amount +other
            )

        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, CryptoHolding):
            return self.token_name == other.token_name and self.usd_price == other.usd_price
        return NotImplemented

    def __bool__(self):
        return self.coin_amount > 0


holding1 = CryptoHolding("Bitcoin",65000.0, 2)
holding2 = CryptoHolding("Bitcoin", 65000.0, 1)
holding3 = CryptoHolding("Ethereum",3500.0, 0)

print(str(holding1))
print(repr(holding1))
print(holding1 + holding2)
print(holding1 + 4)
print(holding1 == holding2)
print(bool(holding1))
print(bool(holding3))