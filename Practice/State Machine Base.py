class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        s, o = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs, verbose = False):
        self.start()
        
        if verbose:
            print 'Start state: ', self.state
            outputs = []
            nextState = []
            for i in range(len(inputs)):
                inp = inputs[i]
                out = self.step(inp)
                outputs.append(out)
                nextState.append(self.state)
                print 'In:', inp, ' Out:', out, ' Next State:', self.state     
            return outputs
        
        return [self.step(inp) for inp in inputs]

    def run(self, n = 10):
        return self.transduce([None]*n)


class Delay(SM):
    def __init__(self, s0):
        self.startState = s0
    def getNextValues(self, state, inp):
            return (inp, state)

class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.startState = (sm1.startState, sm2.startState)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))

class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = splitValues(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))

    def splitValues(inp):
        if inp == 'undefined':
            return ('undefined', 'undefined')
        else:
            return inp

class ParallelAdd(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), o1 + o2)
    
        
class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.startState = self.m.startState

    def getNextValues(self, state, inp):
        (ignore, o) = self.m.getNextValues(state, 'undefined')
        (newS, ignore) = self.m.getNextValues(state, o)
        return (newS, o)

class Increment(SM):
    startState = 0
    def __init__(self, incr):
        self.incr = incr
    def getNextValues(self, state, inp):
        return (state, inp + self.incr)
    
sm = sm.Feedback(sm.R(0))
