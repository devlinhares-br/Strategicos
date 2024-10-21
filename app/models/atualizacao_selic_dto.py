class AtualizacaoSelicDTO():
    def __init__(self, **kw) -> None:
        self.id = kw.get('id')
        self.entity_type_id = kw.get('entityTypeId')

        valor = kw.get('ufCrm23_1717491352', '0')
        if isinstance(valor, str):
            valor = valor.split('|')[0]
        
        try:
            self.atualizacao = float(valor)
        except ValueError:
            self.atualizacao = 0

        self.tipo_id = kw.get('ufCrm23_1717491363')

        if str(self.tipo_id) == '2057':
            self.tipo = 's1'
        elif str(self.tipo_id) == '2019':
            self.tipo = 's2'
        elif str(self.tipo_id) == '2021':
            self.tipo = 's3'
        elif str(self.tipo_id) == '2023':
            self.tipo = 's4'
        elif str(self.tipo_id) == '2629':
            self.tipo = 's5'
        else:
            self.tipo == None