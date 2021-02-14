# Build a Logic Gate class that permits us to run a digital circuit's simulation.
#
# Build representation for Logic Gates.

class LogicGate:
    def __init__(self,n):       # General characteristics;
        self.label = n
        self.output = None
    
    def getLabel(self):         
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None 
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getName() + "--> ")
        else:
                return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getName() + "--> ")
        else:
            return self.pinB.getFrom().getOutput()

class AndGate(BinaryGate):
    def __init__(self,n): 
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        return 0 if (a == 0) and (b == 0) else 1

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None
    
    def getPin(self):
        return int(input('Enter Pin input for gate ' + self.getLabel() + '--> ')) 

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    
    def performGateLogic(self):

        pin = self.getPin()

        return 1 if pin == 0 else 0


class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate
    
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate
    
    def setNextPin(self, source):
        if self.pinA == None
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


g1 = AndGate("AND")
print(g1.getOutput())

g2 = OrGate("OR")
print(g2.getOutput())

g3 = NotGate("NOT")
print(g3.getOutput())
