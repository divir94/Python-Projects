fd = open("Google - 10 days.txt")
    
class transaction:
    def __init__(self, price, amount, upperPer, lowerPer):
        self.price = price
        self.amount = amount
        self.quantity = amount/price
        self.balance = -amount
        self.upperPer = upperPer
        self.lowerPer = lowerPer
        self.upperVal = upperPer
        self.lowerVal = lowerPer
        self.numTrans = 0
        self.minBalance = self.balance
        self.updateUpperLower()
        return

    def comparePrice(self):
        if self.price > self.upperVal:
            return 'upperBound'
        elif self.price < self.lowerVal:
            return 'lowerBound'
        return 'inRange'

    def updateBalanceQuantity(self, compare):
        if compare == 'inRange': return 0
        if compare == 'upperBound':
            self.amount = 1000 
        else:
            self.amount = 2*self.amount
        self.balance += self.price * self.quantity - self.amount
        self.quantity = self.amount/self.price
        self.numTrans += 1
        self.printInfo(compare)
        return 1
            
    def updateUpperLower(self):
        self.upperVal = self.price * (1 + self.upperPer/100.0)
        self.lowerVal = self.price * (1 - self.lowerPer/100.0)
        return

    def getMinBalance(self):
        return self.minBalance

    def getBalance(self):
        return self.balance
    
    def getNumTrans(self):
        return self.numTrans

    def finish(self):
        self.balance += self.price * self.quantity
        self.quantity = 0
        self.printInfo('none')
        return

    def run(self, price):
        self.price = price
        compare = self.comparePrice()
        res = self.updateBalanceQuantity(compare)
        if res:
            self.updateUpperLower()
            self.minBalance = self.minBalance if self.balance > self.minBalance else self.balance
        return

    def printInfo(self, compare):
        print 'price = ', self.price, ' balance = ', self.balance, \
              ' quantity = ', self.quantity, compare
        #' upper bound = ', self.upperVal, ' lower bound = ', self.lowerVal
        return


##T = transaction(100, 1000, 10, 10)
##T.run(50)
##T.run(51)
##T.run(70)
##T.finish()
   

minBound = 1.0
maxBound = 1.0

data = []
for line in fd:
    data.append(float(line))

#print 'min ', 'max ', 'balance ', 'minBalance'

T = transaction(data[0], 1000, minBound, maxBound)
for i in range(len(data) - 1):
    T.run(data[i+1])
T.finish()
print minBound, maxBound, T.getBalance(), T.getMinBalance(), T.getNumTrans()  


