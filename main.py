import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '2009246251:AAHQBEn4MWFPmKSiMxNipIwPv103zs2Gq5w'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('TUTORIAIS', 'Tutoriais', 'tutoriais'):
            return f'''Escolha uma das opções abaixo:\n{os.linesep}1 - TUDO SOBRE CONSULTAVEIS{os.linesep}2 - TUDO SOBRE FULL {os.linesep}3 - VIRAR SALDO PAGBANK\n4 - VIRAR SALDO PICPAY\n5 - ABRINDO LARAS\n6 - REMOVENDO ANJO\n7 - REMOVENDO PREVENTIVO\n8 - + DE 30 SITES APROVANDO NA HORAS\n9 - VALORES\n\n'''
        if mensagem == '1':
            
           return f'''O QUE SÃO CONSULTAVEIS?\n\nConsultaveis são nada mais do que info full com\nacesso ao aplicativo para consulta saldo e fatura,\nobrigatoriamente consultaveis deve vim no seguinte formado\n\nNUMERO/VALIDADE/CVV/SENHA DO CARTÃO E PUXADA COMPLETA\n\nAs mesma tbm devem vim sem anjo\n(aviso de sms no telefone do bico)\ne sem Preventivo\n(Sem Bloqueio pra compras online)\nresumindo consultavel nao e nada mais\nque uma info com acesso a futura que te posibilida fazer a virada de saldo entre outras coisas''' 

        elif mensagem == '2':
            return f'''Full são info cc (Informaçao de Cartão de Credito)\n\nbasicamente o NUMERO VALIDADE CVV E NOME DE UM CARTÃO\nno qual nao se sabe o limite então os vendendores\npodem garanti geralmente somente\ a info esta live (funcionado)
            '''
        elif mensagem == '3':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''

        elif mensagem == '4':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''

        elif mensagem == '5':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''

        elif mensagem == '6':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''

        elif mensagem == '7':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''
       
        elif mensagem == '8':
            return f'''CONTEÚDO VIP DIGITE\n\nDigite VALORES e veja como aquirir'''
       
        elif mensagem == '9':
            return f'''Para ter acesso completo ao bot de tutoriais\nentre em contato com @Kevin71\n\nValor R$: 90,00\n\nRemovendo Anjo\nRemovendo Preventivo\nVirando Saldo\n(em diversas plataformas)\nLista de sites aprovando na hora\n\nAcesso ao grupo vip de\nclientes com cosulta full'''
       
              
                      
        else:
            return '👾 Seja bem vindo a o bot REVOADA TUTORIAIS 👾 \n \n Aqui você ira aprender com alguns tutoriais Grátis e \n compra tutoriais privados \n Atualizados diaramente \n Metodos 100% Funcionais \n \n ADM e Criador: @Kevin71\n\n DIGITE TUTORIAIS E VEJA OS DISPONIVEIS'

            

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()