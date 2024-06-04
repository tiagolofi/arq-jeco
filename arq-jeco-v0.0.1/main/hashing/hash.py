
from random import sample

ALFNUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

class Hash:

    TOKEN_L4 = ''.join(sample(ALFNUM, 4))
    TOKEN_L8 = ''.join(sample(ALFNUM, 8))
    TOKEN_L12 = ''.join(sample(ALFNUM, 12))
