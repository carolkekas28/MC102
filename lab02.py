idade = int(input(""))
 
if(idade < 0):
    print("*Que página de meme do Instagram você é?*")
    print("Qual a sua idade?")
    print(idade)
    print("Erro: entrada inválida")
 
elif(idade < 25) and (idade >= 0):
    segundos = int(input("")) 
    if(idade < 0):
        print("*Que página de meme do Instagram você é?*") 
        print("Qual a sua idade?") 
        print(idade) 
        print("Erro: entrada inválida") 
    else:
        if(segundos <= 5) and (segundos > 0):
            print("*Que página de meme do Instagram você é?*")
            print("Qual a sua idade?") 
            print(idade) 
            print("Quantos segundos são necessários para saber se um vídeo é bom?")
            print(segundos)
            print("RESULTADO")
            print("Você deveria estar no TikTok")
        elif(segundos > 5):
            print("*Que página de meme do Instagram você é?*") 
            print("Qual a sua idade?") 
            print(idade) 
            print("Quantos segundos são necessários para saber se um vídeo é bom?")
            print(segundos)
            print("RESULTADO")
            print("Sua página de memes é: @meltmemes")
        elif(segundos <= 0): 
            print("*Que página de meme do Instagram você é?*") 
            print("Qual a sua idade?") 
            print(idade) 
            print("Quantos segundos são necessários para saber se um vídeo é bom?") 
            print(segundos) 
            print("Erro: entrada inválida") 
 
elif(idade >= 25) and (idade <= 40):
    banda = str(input("")) 
    if(banda == 'A') or (banda == 'B'):
        print("*Que página de meme do Instagram você é?*") 
        print("Qual a sua idade?") 
        print(idade) 
        print("Qual banda você gosta mais?")
        if(banda == 'A'):
            print("A) Matanza")
        elif(banda == 'B'):
            print("B) Iron Maiden")
        print("RESULTADO")
        print("Sua página de memes é: @badrockistamemes")
    elif(banda == 'C') or (banda == 'D'):
        resposta_capivaras = str(input(""))
        print("*Que página de meme do Instagram você é?*") 
        print("Qual a sua idade?") 
        print(idade) 
        print("Qual banda você gosta mais?")
        if(banda == 'C'):
            print("C) Imagine Dragons")
        elif(banda== 'D'):
            print("D) BlackPink")
        print("São as capivaras os melhores animais da Terra?")
        if(resposta_capivaras == 'Sim'):
            print("Sim")
            print("RESULTADO")
            print("Sua página de memes é: @genteboamemes")
        elif(resposta_capivaras == 'Não'):
            print("Não")
            print("RESULTADO")
            print("Sua página de memes é: @wrongchoicememes")
        else: 
            print(resposta_capivaras)
            print("Erro: entrada inválida")
    else:
        print("Erro: entrada inválida")
 
elif(idade > 40) and (idade <= 125):
    imagem_grupo = str(input("")) 
    print("*Que página de meme do Instagram você é?*") 
    print("Qual a sua idade?") 
    print(idade) 
    print("Que imagem de bom dia você manda no grupo da família?")
    if(imagem_grupo == 'A'):
        print("A) Bebê em roupa de flor")
        print("RESULTADO")
        print("Sua página de memes é: @bomdiabebe")
    elif(imagem_grupo == 'B'):
        print("B) Gato")
        print("RESULTADO")
        print("Sua página de memes é: @kittykatmsgs")
    elif(imagem_grupo == 'C'):
        print("C) Coração e rosas")
        print("RESULTADO")
        print("Sua página de memes é: @bomdiaflordodia")
    else:
        print(imagem_grupo)
        print("Erro: entrada inválida")
 
elif(idade > 125):
    print("*Que página de meme do Instagram você é?*") 
    print("Qual a sua idade?") 
    print(idade) 
    print("Erro: entrada inválida") 
