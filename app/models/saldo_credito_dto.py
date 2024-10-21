
from dataclasses import dataclass, field

class SaldoCreditoDTO():
    def __init__(self, **kw) -> None:
        self.id = kw.get('id')
        self.entity_type_id = kw.get('entityTypeId')

        self.s1_valor_transmissao = self.parse_valor(kw.get('ufCrm15_1708970676', '0|BRL'))
        self.s1_atualizacao = self.parse_valor(kw.get('ufCrm15_1717762449', '0|BRL'))
        self.s1_valor_restante = self.parse_valor(kw.get('ufCrm15_1709310661', '0|BRL'))

        self.s2_valor_transmissao = self.parse_valor(kw.get('ufCrm15_1708975765', '0|BRL'))
        self.s2_atualizacao = self.parse_valor(kw.get('ufCrm15_1713271434212', '0|BRL'))
        self.s2_valor_restante = self.parse_valor(kw.get('ufCrm15_1709316195', '0|BRL'))

        self.s3_valor_transmissao = self.parse_valor(kw.get('ufCrm15_1708975848', '0|BRL'))
        self.s3_atualizacao = self.parse_valor(kw.get('ufCrm15_1713271403922', '0|BRL'))
        self.s3_valor_restante = self.parse_valor(kw.get('ufCrm15_1709316209', '0|BRL'))

        self.s4_valor_transmissao = self.parse_valor(kw.get('ufCrm15_1708975994', '0|BRL'))
        self.s4_atualizacao = self.parse_valor(kw.get('ufCrm15_1713271280413', '0|BRL'))
        self.s4_valor_restante = self.parse_valor(kw.get('ufCrm15_1709316217', '0|BRL'))

        self.s5_valor_transmissao = self.parse_valor(kw.get('ufCrm15_1722370065', '0|BRL'))
        self.s5_atualizacao = self.parse_valor(kw.get('ufCrm15_1722370124', '0|BRL'))
        self.s5_valor_restante = self.parse_valor(kw.get('ufCrm15_1722370106', '0|BRL'))
    
    def parse_valor(self, valor):
        if isinstance(valor, str) and '|' in valor:
            valor_num = valor.split('|')[0].strip()
            try:
                return float(valor_num)
            except ValueError:
                return 0
        return 0

@dataclass
class FieldsSaldoCreditoS1:
    valor_transmissao: str = 'ufCrm15_1708970676'
    atualizacao: str = 'ufCrm15_1717762449'
    valor_restante: str = 'ufCrm15_1709310661'

@dataclass
class FieldsSaldoCreditoS2:
    valor_transmissao: str = 'ufCrm15_1708975765'
    atualizacao: str = 'ufCrm15_1713271434212'
    valor_restante: str = 'ufCrm15_1709316195'

@dataclass
class FieldsSaldoCreditoS3:
    valor_transmissao: str = 'ufCrm15_1708975848'
    atualizacao: str = 'ufCrm15_1713271403922'
    valor_restante: str = 'ufCrm15_1709316209'

@dataclass
class FieldsSaldoCreditoS4:
    valor_transmissao: str = 'ufCrm15_1708975994'
    atualizacao: str = 'ufCrm15_1713271280413'
    valor_restante: str = 'ufCrm15_1709316217'

@dataclass
class FieldsSaldoCreditoS5:
    valor_transmissao: str = 'ufCrm15_1722370065'
    atualizacao: str = 'ufCrm15_1722370124'
    valor_restante: str = 'ufCrm15_1722370106'

@dataclass
class FieldsSaldoCredito:
    id: str = 'id'
    s1: FieldsSaldoCreditoS1 = field(default_factory=FieldsSaldoCreditoS1)
    s2: FieldsSaldoCreditoS2 = field(default_factory=FieldsSaldoCreditoS2)
    s3: FieldsSaldoCreditoS3 = field(default_factory=FieldsSaldoCreditoS3)
    s4: FieldsSaldoCreditoS4 = field(default_factory=FieldsSaldoCreditoS4)
    s5: FieldsSaldoCreditoS5 = field(default_factory=FieldsSaldoCreditoS5)