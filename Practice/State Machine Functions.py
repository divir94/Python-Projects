import lib601.sm as sm
import lib601.sig as sig

class Increment(sm.SM):
    startState = 0
    def __init__(self, incr):
        self.incr = incr
    def getNextValues(self, state, inp):
        return (state, sm.safeAdd(inp, self.incr))

class Adder(sm.SM):
    def getNextState(self, state, inp):
        (i1, i2) = sm.splitValue(inp)
        return sm.safeAdd(i1, i2)

class Multiplier(sm.SM):
    def getNextState(self, state, inp):
        (i1, i2) = sm.splitValue(inp)
        return sm.safeMul(i1, i2)

class Accumulator(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (state + inp, state + inp)

def dotProd(a, b):
    if len(a) == 0 or len(b) == 0: return 0
    if len(a) != len(b):
           print 'dotProd mismatch error ' + str(len(a)) + '  !=  ' + str(len(b))
    return sum([ai*bi for (ai,bi) in zip(a,b)])

def samplesInRange(sig, lo, hi):
    return [sig.sample(i) for i in range(lo,hi)]

class LTISM(sm.SM):
    def __init__(self, dCoeffs, cCoeffs,
                 previousInputs = [], previousOutputs = []):
        self.cCoeffs = cCoeffs
        self.dCoeffs = dCoeffs
        self.startState = (previousInputs, previousOutputs)

    def getNextValues(self, state, inp):
        (inputs, outputs) = state
        myInputs = [inp] + inputs
        myInputs = myInputs[:len(self.dCoeffs)]
        myOutputs = outputs
        myOutputs = myOutputs[:len(self.cCoeffs)]
        output = dotProd(myInputs, self.dCoeffs) + dotProd(myOutputs, self.cCoeffs)
        return ((myInputs, [output]+outputs), output)

class TransducedSignal(sig.Signal):
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def sample(self, n):
        if n < 0:
            return 0
        else:
            t = self.m.transduce(samplesInRange(self.s, 0, n+1))
            return t[n]

class Triangle(sig.Signal):
    def __init__(self, h):
        self.h = h
    def sample(self, n):
        if -self.h < n and n < self.h:
            return self.h - abs(n)
        else:
            return 0

s = Triangle(4)
a = sig.ScaledSignal(Triangle(2), -1)
c = sig.Rn(a + s, 4)

trapezoid = sig.Rn(Triangle(4) + sig.ScaledSignal(Triangle(2), -1), 4)

        
