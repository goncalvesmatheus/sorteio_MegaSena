import random

def sorteio(repeticao):
    try:
        repeticao = int(repeticao)
        jogo = []
        i = 0
        while i < repeticao:
            while len(jogo) < 6:
                num = random.randrange(1,60)
                if num in jogo:
                    continue
                else:
                    jogo.append(num)
            print(sorted(jogo))
            i += 1
            jogo = []
    except:
        print ('Informação inválida.')

repeticao = input('Quantos jogos deseja fazer? ')

sorteio(repeticao)