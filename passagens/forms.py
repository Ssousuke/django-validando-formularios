from django import forms
from .validation import *
from tempus_dominus.widgets import DatePicker


class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_retorno = forms.DateField(label='Volta', widget=DatePicker())

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_retorno = self.cleaned_data.get('data_retorno')

        lista_de_erros = {}

        verifica_se_inputs_contem_numeros(origem, 'origem', lista_de_erros)
        verifica_se_inputs_contem_numeros(destino, 'destino', lista_de_erros)
        verifica_se_origem_e_igual_ao_destino(origem, destino, lista_de_erros)
        verifica_data_ida_maior_data_volta(data_ida, data_retorno, lista_de_erros)
        verifica_data_ida_nao_pode_ser_maior_que_data_de_hoje(data_ida, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem = lista_de_erros[erro]
                self.add_error(erro, mensagem)
        return self.cleaned_data
