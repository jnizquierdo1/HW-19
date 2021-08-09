{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
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
    "load_dotenv(\"/users/juanizquierdo/documents/wallet/mnemonic.env\")\n",
    "mnemonic = os.getenv(\"mnemonic\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "JSONDecodeError",
     "evalue": "Expecting value: line 2 column 1 (char 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-40681ca5bb2b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;31m# Create a dictionary object called coins to store the output from `derive_wallets`.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m coins = {\n\u001b[0;32m---> 14\u001b[0;31m     \u001b[0mETH\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mderive_wallets\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mETH\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m     \u001b[0mBTCTEST\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mderive_wallets\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBTCTEST\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-8-40681ca5bb2b>\u001b[0m in \u001b[0;36mderive_wallets\u001b[0;34m(coin)\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0moutput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommunicate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0mp_status\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwait\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m     \u001b[0mjson\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mjson\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutput\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/pyvizenv/lib/python3.7/json/__init__.py\u001b[0m in \u001b[0;36mloads\u001b[0;34m(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[1;32m    346\u001b[0m             \u001b[0mparse_int\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mparse_float\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    347\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[0;32m--> 348\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    349\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    350\u001b[0m         \u001b[0mcls\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mJSONDecoder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/pyvizenv/lib/python3.7/json/decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[0;34m(self, s, _w)\u001b[0m\n\u001b[1;32m    335\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    336\u001b[0m         \"\"\"\n\u001b[0;32m--> 337\u001b[0;31m         \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    339\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/pyvizenv/lib/python3.7/json/decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[0;34m(self, s, idx)\u001b[0m\n\u001b[1;32m    353\u001b[0m             \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscan_once\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0midx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    354\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 355\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Expecting value\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    356\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mend\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mJSONDecodeError\u001b[0m: Expecting value: line 2 column 1 (char 1)"
     ]
    }
   ],
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
   "execution_count": 11,
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
   "execution_count": 12,
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
   "execution_count": 13,
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
   "execution_count": 14,
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pyvizenv] *",
   "language": "python",
   "name": "conda-env-pyvizenv-py"
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
