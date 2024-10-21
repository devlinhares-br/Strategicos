class RessarcimentoDTO():
    def __init__(self, **kw) -> None:
        self.id = kw.get('id')
        self.entity_type_id = kw.get('entityTypeId')

        valor = kw.get('ufCrm21_1715176027', '0|BRL')

        if isinstance(valor, str):
            valor = valor.split('|')[0]
        
        try:
            self.valor_ressarcido = float(valor)
        except ValueError:
            self.valor_ressarcido = 0

        self.tipo_id = kw.get('ufCrm21_1715176035')

        if str(self.tipo_id) == '1377':
            self.tipo = 's1'
        elif str(self.tipo_id) == '1379':
            self.tipo = 's2'
        elif str(self.tipo_id) == '1381':
            self.tipo = 's3'
        elif str(self.tipo_id) == '1383':
            self.tipo = 's4'
        elif str(self.tipo_id) == '2631':
            self.tipo = 's5'
        else:
            self.tipo = None