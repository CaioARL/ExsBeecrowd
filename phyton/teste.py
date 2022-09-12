aluno = [
    { id:1, "n1": 10, "n2": 5, "n3": 6,"n4": 7,"media": 0,"situacao":''},
    { id:2, "n1": 3, "n2": 5, "n3": 6,"n4": 7,"media": 0,"situacao":''},
    { id:3, "n1": 8, "n2": 8, "n3": 8,"n4": 7,"media": 0,"situacao":''}
    ]

for x in aluno:
    media  = (x["n1"] + x["n2"] + x["n3"] + x["n4"])/4
    x["media"] = media
    if media >= 7:
        x["situacao"] = "Aprovado"
    else:    
        x["situacao"] = "Reprovado"

for x in aluno:
    print(x)