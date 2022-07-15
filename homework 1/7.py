secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
#secret_message[0][3], secret_message[1][9:12], secret_message[2][5:14, 1], secret_message[3][-19:-14]
word = []
word1 = []
word1.extend(secret_message[0][3])
word1.extend(secret_message[1][9:13])
word1.extend(secret_message[2][5:15:2])
word1.extend(reversed(secret_message[3][7:13]))
word1.extend(reversed(secret_message[4][16:21]))
word = secret_message[2][5:15:1]
print(word)
print(word1)