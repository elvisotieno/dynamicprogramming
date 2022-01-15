#A)You should first identify algorithms you want to execute as concrete strategies in the primary class.
#B)Define the context (primary class) and add a reference to the strategy, a method to
#set the strategy, and another method to execute the strategy.
#You may also define a default strategy to switch between strategies only if they do not like the default one.

#First, we define the strategy field for storing a reference to a strategy object, and two methods, setStrategy and executeStrategy
#The setStrategy sets the strategy selected if a user selects an option, or else the default one.

#C) Define the Strategy Interface, which is common to all the concrete strategies.
# The Strategy interface has an abstract method that you can alter in concrete strategies.

#D)Define the concrete strategies which should implement the Strategy interface.
#These concrete strategies must have a common method that overrides the execute method of the Strategy interface.

#E)Now, users can select the strategy they want at the runtime.
# Create an object of context and pass a concrete strategy.

from abc import ABC, abstractmethod
## context - the primary class
class Context:
    strategy: Strategy  ## the strategy interface

    def setStrategy(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def executeStrategy(self) -> str:
        print(self.strategy.execute())


## Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass


class ConcreteStrategyA(Strategy):
    def execute(self) -> str:
        return "ConcreteStrategy A"

class ConcreteStrategyB(Strategy):
    def execute(self) -> str:
        return "ConcreteStrategy B"

class Default(Strategy):
    def execute(self) -> str:
        return "Default"


## Example application
appA = Context()
appB = Context()
appC = Context()

## selecting stratigies
appA.setStrategy(ConcreteStrategyA())
appB.setStrategy(ConcreteStrategyB())
appC.setStrategy()    ## sets to default strategy

## each object below execute different strategy with same method
appA.executeStrategy()
appB.executeStrategy()
appC.executeStrategy()

