N1,N2,N3,N4 = input().split()

N1,N2,N3,N4 = float(N1),float(N2),float(N3),float(N4)

media = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')  
    exame = float(input()  )
    print('Nota do exame: {:.1f}'.format(exame))
    media_final = (media + exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno reprovado.')    
        print('Media final: {:.1f}'.format(media_final))
else: 
    print('Aluno reprovado.')    




