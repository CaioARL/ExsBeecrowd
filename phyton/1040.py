valor1 = input().split(" ")
N1,N2,N3,N4 = valor1

media = ((float(N1) * 2) + (float(N2) * 3) + (float(N3) * 4) + (float(N4) * 1))/10
print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")

if media < 5.0:
    print("Aluno reprovado.")

if media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    n_ex = float(input())
    media_ex = (float(media) + float(n_ex))/2
    print("Nota do exame: %.1f" %n_ex)

    if media_ex >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" %media_ex)

    if media_ex < 5.0:
        print("Media final: %.1f" %media_ex)

