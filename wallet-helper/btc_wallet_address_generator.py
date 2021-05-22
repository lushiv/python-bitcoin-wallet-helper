from bitcoinaddress import Wallet

def get_mainnet_wallet_address():
    try:
        wallet_address_info = Wallet()
        wallet_address_data = {
            'private_key_hex' : wallet_address_info.key.hex,
            "private_key_wif" : wallet_address_info.key.mainnet.wif,
            "private_key_wic" : wallet_address_info.key.mainnet.wifc,
            "publick_key" : wallet_address_info.address.pubkey,
            "publick_key_compressed" : wallet_address_info.address.pubkeyc,
            "publick_address_1" : wallet_address_info.address.mainnet.pubaddr1,
            "publick_address_1_compressed" : wallet_address_info.address.mainnet.pubaddr1c,
            "publick_address_3" : wallet_address_info.address.mainnet.pubaddr3,
            "publick_address_bc1_p2wpkh" : wallet_address_info.address.mainnet.pubaddrbc1_P2WPKH,
            "publick_address_bc1_p2wsh" : wallet_address_info.address.mainnet.pubaddrbc1_P2WSH
        }

        print(wallet_address_data)
        return wallet_address_data

    except Exception as e:
        print(e.message)


def get_testnet_wallet_address():
    try:
        wallet_address_info = Wallet(testnet=True)
        wallet_address_data = {
            'private_key_hex' : wallet_address_info.key.hex,
            "private_key_wif" : wallet_address_info.key.mainnet.wif,
            "private_key_wic" : wallet_address_info.key.mainnet.wifc,
            "publick_key" : wallet_address_info.address.pubkey,
            "publick_key_compressed" : wallet_address_info.address.pubkeyc,
            "publick_address_1" : wallet_address_info.address.mainnet.pubaddr1,
            "publick_address_1_compressed" : wallet_address_info.address.mainnet.pubaddr1c,
            "publick_address_3" : wallet_address_info.address.mainnet.pubaddr3,
            "publick_address_bc1_p2wpkh" : wallet_address_info.address.mainnet.pubaddrbc1_P2WPKH,
            "publick_address_bc1_p2wsh" : wallet_address_info.address.mainnet.pubaddrbc1_P2WSH
        }

        return wallet_address_data

    except Exception as e:
        print(e.message)
