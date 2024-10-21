class CompensacaoDTO():
    def __init__(self, **kw) -> None:
        self.id = kw.get('id')
        self.entity_type_id = kw.get('entityTypeId')

        valor = kw.get('ufCrm17_1708977331', '0|BRL')
        if isinstance(valor, str):
            valor = valor.split('|')[0]
        
        try:
            self.compensacao = float(valor)
        except ValueError:
            self.compensacao = 0

        self.tipo_id = kw.get('ufCrm17_1708977227')

        if str(self.tipo_id) == '777':
            self.tipo = 's1'
        elif str(self.tipo_id) == '779':
            self.tipo = 's2'
        elif str(self.tipo_id) == '781':
            self.tipo = 's3'
        elif str(self.tipo_id) == '783':
            self.tipo = 's4'
        elif str(self.tipo_id) == '2633':
            self.tipo = 's5'
        else:
            self.tipo = None