def notas(*num, sit=False):
    """
        -> Função que analisa notas e situção do aluno.
        :param num: uma ou mais notas do aluno
        :param sit: valor opcional, mostrar situação ou não (True or False)
        :return: dicíonario com dados de QTD de notas (total),maior, menor e media de notas e a situação do aluno
    """
    resp = {}
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['media'] = sum(num)/len(num)
    if sit:
        if resp['media'] >= 7:
            resp['situação'] = 'Boa'
        elif resp['media'] >= 5:
            resp['situação'] = 'Razoavel'
        else:
            resp['situação'] = 'Ruim'
    return resp
print(notas(7,5,8,7,10, sit = True))
