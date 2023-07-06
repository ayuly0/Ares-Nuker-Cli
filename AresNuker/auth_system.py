from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>2mQdsnwD4jZ/s0+YaN0dRccbWiYkCnukTR/JSebZMmfiILYd6szdXkq6ouEAfZxJv3FGDJSkyxVtOD/sWKVE+mHPE6sTgMvsPhr72SDIY1uCEDBsY38Gi2/330GIGYJRohaCphdRLyDg3JGXob3ttzojFOSkw0Q3Vb0d41fDmlZTQWup5qzcH1t9JkGhDhem+6F/MBjFt0JU4PWZvKghnVa08EBNUMK+C1oyBd7Hc5I/mOKnl7McbuMsy3Bm66clcKotMYH+CbcGQ/DqUV1Bx4Hvts3U8Zdleh8pBwD2autOFiiffM9YdIGsBJfp6jtnvvUnWA8O3nLrEwTqVe7rYQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI1MzU5NjE2NiIsIloyazdzeEdQRXEwbjNIQnVBUVhURmgxRmEzNjFDNVVVeFVrRTA1SnIiXQ=="

def auth_system(key):

	result = Key.activate(token=auth,\
					rsa_pub_key=RSAPubKey,\
					product_id=20809, \
					key=key,\
					machine_code=Helpers.GetMachineCode(v=2))

	if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
		return False
	else:
		# print("The license is valid!")
		# license_key = result[0]
		# print("Feature 1: " + str(license_key.f1))
		# print("License expires: " + str(license_key.expires))
		return True