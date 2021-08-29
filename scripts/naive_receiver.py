#!/usr/bin/python3

from brownie import  FlashLoanReceiver, NaiveReceiverLenderPool as LenderPool, accounts

def main():
    NaiveReceiver().main()

class NaiveReceiver():


    """class to run pass/fail check on challenge exploit: naive_receiver"""


    def __init__(self):
        self.deployer = accounts[0]
        self.user = accounts[1]
        self.some_user = accounts[2]
        self.other_accounts = accounts[3:]
        self.ETHER_IN_POOL = self.ether(1000)
        self.ETHER_IN_RECEIVER = self.ether(10)
        self.pool = LenderPool.deploy({'from': self.deployer})
        self.receiver = FlashLoanReceiver.deploy(self.pool.address, {"from": self.user})

    def main(self):
        """runs setup, exploit and test_exploit, results are logged by respective classes"""
        self.setup()
        self.test_contract_pre_exploit()
        self.exploit()
        self.test_contract_post_exploit_outcome_1()
        self.test_contract_post_exploit_outcome_2()

    def setup(self):
        """performs required deployments and token transfers prior to running the exploit"""
        self.deployer.transfer(self.pool.address, self.ETHER_IN_POOL)
        print(f"Setup Check 1 passed: {self.pool.balance() == self.ETHER_IN_POOL}\n")
        print(f"Setup Check 2 passed: {self.pool.fixedFee() == self.ether(1)}\n")
        self.user.transfer(self.receiver.address, self.ETHER_IN_RECEIVER)
        print(f"Setup Check 3 passed: {self.receiver.balance() == self.ETHER_IN_RECEIVER}\n")

    def test_contract_pre_exploit(self):
        """print anything here that helps understand the contracts process"""
        print("PRE EXPLOIT TEST RUNNING...")
        return
        
    def exploit(self):
        """WRITE EXPLOIT HERE"""
        print("RUNNING EXPLOIT...")
        return

    def exploit_outcome_1(self):
        """returns True if exploit outcome 1 is as expected"""
        return self.receiver.balance() == 0
    
    def exploit_outcome_2(self):
        """returns True if exploit outcome 2 is as expected"""
        return self.pool.balance() == self.ETHER_IN_POOL + self.ETHER_IN_RECEIVER

    def test_contract_post_exploit_outcome_1(self):
        """test"""
        print("POST EXPLOIT TEST RUNNING...")
        try:
            assert(self.exploit_outcome_1())
        except:
            print("Exploit outcome 1 did not pass: \u274E \n Expected receiver balance to be 0")
            return
        print("Passed outcome 1: \u2705")
    
    def test_contract_post_exploit_outcome_2(self):
        """test"""
        print("POST EXPLOIT TEST RUNNING...")
        try:
            assert(self.exploit_outcome_2())
        except:
            print("Exploit outcome 2 did not pass: \u274E \n Expected pool balance to have increased")
            return
        print("Passed outcome 2: \u2705")
        print("Passed all outcomes: \u2705")
    
    def ether(self, amount):
        """receives number and converts to wei"""
        return amount*10**18
