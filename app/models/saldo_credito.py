from app.models.saldo_credito_dto import SaldoCreditoDTO
from app.models.atualizacao_selic_dto import AtualizacaoSelicDTO
from app.models.compensacao_dto import CompensacaoDTO
from app.models.ressarcimento_dto import RessarcimentoDTO

class SaldoCredito():
    def __init__(self, saldo_credito:dict, atualizacao_selic:list, compensacao:list, ressarcimentos:list) -> None:
        self.saldo_credito = SaldoCreditoDTO(**saldo_credito)
        
        self.atualizacao_selic = [AtualizacaoSelicDTO(**att) for att in atualizacao_selic]
        self.compensacoes = [CompensacaoDTO(**comp) for comp in compensacao]
        self.ressarcimentos = [RessarcimentoDTO(**ress) for ress in ressarcimentos]
    
    def soma_selic(self):
        self.selic = self._soma_por_tipo(self.atualizacao_selic, 'atualizacao')
        return self.selic
    
    def soma_compensacao(self):
        return self._soma_por_tipo(self.compensacoes, 'compensacao')
    
    def soma_ressarcimento(self):
        return self._soma_por_tipo(self.ressarcimentos, 'valor_ressarcido')
    
    def _soma_por_tipo(self, lista, attr):
        resultado = {'s1': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0}
        for item in lista:
            tipo = getattr(item, 'tipo', None)
            try:
                valor = float(getattr(item, attr, 0))
            except (TypeError, ValueError):
                valor = 0

            if tipo in resultado:
                resultado[tipo] += valor
        return resultado
    
    def soma_total(self):
        selic = self.soma_selic()
        compensacao = self.soma_compensacao()
        ressarcimento = self.soma_ressarcimento()
        total = {
            's1': round(selic['s1'] - compensacao['s1'] - ressarcimento['s1'], 2),
            's2': round(selic['s2'] - compensacao['s2'] - ressarcimento['s2'], 2),
            's3': round(selic['s3'] - compensacao['s3'] - ressarcimento['s3'], 2),
            's4': round(selic['s4'] - compensacao['s4'] - ressarcimento['s4'], 2),
            's5': round(selic['s5'] - compensacao['s5'] - ressarcimento['s5'], 2),
        }

        return total