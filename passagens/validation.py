from django.utils.datetime_safe import datetime


def verifica_se_origem_e_igual_ao_destino(origem, destino, lista_de_erros):
    """
    Verifica se input de origem é igual ao input de destino
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem não pode ser igual ao destino!'


def verifica_se_inputs_contem_numeros(valor_do_campo, nome_do_campo, lista_de_erros):
    """
    Verifica se existe caracteres númericos no input
    """
    if any(char.isdigit() for char in valor_do_campo):
        lista_de_erros[nome_do_campo] = 'Origem inválida! Não pode conter números!'


def verifica_data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """
    Verifica se a data de ida é maior que a data de volta
    """
    if data_ida > data_volta:
        lista_de_erros['data_ida'] = 'A data de ida não pode ser maior que a data de retorno!'


def verifica_data_ida_nao_pode_ser_maior_que_data_de_hoje(data_ida, lista_de_erros):
    """
    Verifica se a data de ida é menor que a data de hoje
    """
    data_hoje = datetime.date(datetime.now())
    if data_ida < data_hoje:
        lista_de_erros['data_ida'] = 'A data de ida não pode ser menor que a data de hoje!'
