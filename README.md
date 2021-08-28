# Damn Vulnerable Defi - Python Brownie Port 

The purpose of this repo is to allow python users to participate in the brilliant [Damn Vulnerable Defi](https://www.damnvulnerabledefi.xyz/) Crypto CTF written by [@tinchoabbate](https://twitter.com/tinchoabbate). I will utilise brownie to allow interaction with the smart contracts for each challenge. **work in progress**

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Install dependencies

    ```bash
    npm install
    ```

## Basic Use

To begin, choose one of the challenge folders in contracts. Get familiar with the contract then open the same named script
in scripts directory. Notice the Exploit method, this is where your exploit will be coded. Once the exploit is done run the below in the console in your root folder:

```bash
brownie console
```

or alternatively if you prefer hardhat over ganache:

```bash
brownie console --network hardhat
```

then in the brownie console run:

```bash
>>> run("script_name")
```

## Resources

To get started with Brownie:

* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).


Any questions? Join our [Gitter](https://gitter.im/eth-brownie/community) channel to chat and share with others in the community.

## License

This project is licensed under the [MIT license](LICENSE).
