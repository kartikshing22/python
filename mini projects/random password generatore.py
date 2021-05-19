import random
chars=['a','b','c','d','e','f','g','h','i','j','k']
nums=['132','3452','783','566854','4565','5636','798r','3448','96745','56610']
syms=['1@#*(*&*R$#%','$^&*#$$#$&^','(,)_#$###%#','-@@$@@!$#','=#%%$<>?$#%']
passw=random.choice(chars)+random.choice(nums)+random.choice(syms)
print(passw)