from random import choice

class roulette:
     # money
     balance         = 10000
     last_bet        = 10
     # outcome
     last_outcome    = 1
     loss_streak     = 0

     # variables
     max_loss_streak = 4
     bet_amount      = 10
     multiplier      = 2     

     def __init__(self, iterations):
          self.iterations = iterations

     def get_bet_amount(self):
          if self.loss_streak <= self.max_loss_streak and self.last_outcome == 0:
               return self.last_bet * self.multiplier
          return self.bet_amount

     def place_bet(self):
          self.last_bet = self.get_bet_amount()
          self.balance -= self.last_bet

     def spin(self):
          outcome = choice([0,1])
          self.last_outcome = outcome
          if outcome:
               self.balance += 2 * self.last_bet
               self.loss_streak = 0
          else:
               self.loss_streak += 1
          

     def print_spin_result(self):
          print "%3d:   Bet: %5s,    Outcome: %d,   Balance: %7s" \
                % (self.i, '$'+str(self.last_bet), self.last_outcome, '$'+str(self.balance))

     def run(self):
          for i in range(self.iterations):
               self.i = i+1
               self.place_bet()
               self.spin()
               #self.print_spin_result()
          print "Final balance: $%d" % self.balance
          print "Percentage profit: %.1f%%\n" % ( (self.balance-10000) /100)
          return self.balance

balance = 0
for i in range(10):
     game = roulette(1000000)
     balance += game.run() - 10000
print balance
     
          
     
