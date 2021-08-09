{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import dependencies\n",
    "import os\n",
    "import subprocess\n",
    "import json\n",
    "from dotenv import load_dotenv\n",
    "from pathlib import Path\n",
    "from pprint import pprint\n",
    "from constants import *\n",
    "\n",
    "\n",
    "# Load and set environment variables\n",
    "load_dotenv(\"/users/juanizquierdo/documents//API_KEYS.env\")\n",
    "mnemonic = os.getenv(\"mnemonic\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function called `derive_wallets`\n",
    "def derive_wallets(coin):\n",
    "    command = f\"./derive -g --mnemonic='{mnemonic}' --cols=path,address,privkey,pubkey --format=json --coin='{coin}' --numderive= 2\"\n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "    output, err = p.communicate()\n",
    "    p_status = p.wait()\n",
    "    json.loads(output) \n",
    "    return json.loads(output) \n",
    "\n",
    "# print(json.dumps(data, indent=4))\n",
    "\n",
    "# Create a dictionary object called coins to store the output from `derive_wallets`.\n",
    "coins = {\n",
    "    ETH: derive_wallets(ETH),\n",
    "    BTCTEST: derive_wallets(BTCTEST)\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary functions from bit and web3\n",
    "# YOUR CODE HERE\n",
    "from bit import PrivateKeyTestnet\n",
    "from bit.network import NetworkAPI\n",
    "from bit import wif_to_key\n",
    "\n",
    "from web3 import Web3\n",
    "from web3.middleware import geth_poa_middleware\n",
    "from eth_account import Account\n",
    "\n",
    "from getpass import getpass\n",
    "\n",
    "w3 = Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545\"))\n",
    "\n",
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function called `priv_key_to_account` that converts privkey strings to account objects.\n",
    "def priv_key_to_account(coin, priv_key):\n",
    "    if coin == ETH:\n",
    "        return Account.privateKeyToAccount(priv_key)\n",
    "    elif coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(priv_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.\n",
    "def create_tx(coin, account, to, amount):\n",
    "    if coin == ETH:\n",
    "        gasEstimate = w3.eth.estimateGas(\n",
    "            {\"from\": account.address, \"to\": to, \"value\": amount}\n",
    "        )\n",
    "        return {\n",
    "            \"from\": account.address,\n",
    "            \"to\": to,\n",
    "            \"value\": amount,\n",
    "            \"gasPrice\": w3.eth.gasPrice,\n",
    "            \"gas\": gasEstimate,\n",
    "            \"nonce\": w3.eth.getTransactionCount(account.address),\n",
    "            \n",
    "        }\n",
    "    elif coin == BTCTEST:\n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.\n",
    "def send_tx(coin, account, to, amount):\n",
    "    tx = create_tx(coin, account, to, amount)\n",
    "    signed_tx = account.sign_transaction(tx)\n",
    "    if coin == ETH:\n",
    "        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)\n",
    "\n",
    "    elif coin == BTCTEST:\n",
    "        return NetworkAPI.broadcast_tx_testnet(signed_tx)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
