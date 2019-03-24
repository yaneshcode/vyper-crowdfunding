## crowdfunding contract 
## converted crowdfunding solidity contract posted Tuesday

# events must be at the top
NewContribution: event({_who: indexed(address), _amount: wei_value, _timestamp: timestamp})
RefundIssued: event({_who: indexed(address), _amount: wei_value, _timestamp: timestamp})
BeneficiaryPaid: event({_beneficiary: indexed(address), _amount: wei_value, _timestamp: timestamp})

# variable declarations
beneficiary: public(address)
goal: public(wei_value)
startTime: public(timestamp)
deadline: public(timestamp)
contributions: public({value: wei_value}[address])


# constructor
@public
def __init__(_beneficiary: address, _goal: wei_value, _deadline: timedelta):
    self.beneficiary = _beneficiary
    self.goal = _goal
    self.startTime = block.timestamp    #for debugging, can remove later
    self.deadline = block.timestamp + (_deadline * 3600)
    

# contribute function- must be payable
@public
@payable
def contribute():
    assert block.timestamp < self.deadline
    
    self.contributions[msg.sender].value += msg.value
    
    log.NewContribution(msg.sender, msg.value, block.timestamp)
    
# refund function
@public
def refund():
    assert block.timestamp > self.deadline and self.balance < self.goal
    amount: wei_value
    amount = self.contributions[msg.sender].value
    
    send(msg.sender, amount)

    log.RefundIssued(msg.sender, amount, block.timestamp)

# paying out to the beneficiary
@public    
def payBeneficary():
    assert block.timestamp > self.deadline and self.balance >= self.goal
    
    send(self.beneficiary, self.balance)

    log.BeneficiaryPaid(self.beneficiary, self.balance, block.timestamp)

