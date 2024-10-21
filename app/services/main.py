from app.models.bitrix import Bitrix24
from app.models.saldo_credito import SaldoCredito
from app.models.saldo_credito_dto import FieldsSaldoCreditoS1, FieldsSaldoCreditoS2, FieldsSaldoCreditoS3, FieldsSaldoCreditoS4, FieldsSaldoCreditoS5
from time import sleep


class Main():
    def __init__(self) -> None:
        self.b24 = Bitrix24()

    def main(self):
        last_id = count = 0

        while True:
            data = {'>id': f'{last_id}'}
            lista_saldos = self._get_items(data, 153)
            if lista_saldos == []:
                break

            for saldo in lista_saldos:
                parent_id = saldo.get('id')

                att = self.fetch_all_items(parent_id, 1032)
                comp = self.fetch_all_items(parent_id, 189)
                ressar = self.fetch_all_items(parent_id, 142)

                item = SaldoCredito(saldo, att, comp, ressar)

                total = item.soma_total()

                data = {
                    FieldsSaldoCreditoS1.valor_restante: f"{item.saldo_credito.s1_valor_transmissao + total.get('s1', 0)}|BRL",
                    FieldsSaldoCreditoS1.atualizacao: f"{item.selic.get('s1')}|BRL",

                    FieldsSaldoCreditoS2.valor_restante: f"{item.saldo_credito.s2_valor_transmissao + total.get('s2', 0)}|BRL",
                    FieldsSaldoCreditoS2.atualizacao: f"{item.selic.get('s2')}|BRL",

                    FieldsSaldoCreditoS3.valor_restante: f"{item.saldo_credito.s3_valor_transmissao + total.get('s3', 0)}|BRL",
                    FieldsSaldoCreditoS3.atualizacao: f"{item.selic.get('s3')}|BRL",

                    FieldsSaldoCreditoS4.valor_restante: f"{item.saldo_credito.s4_valor_transmissao + total.get('s4', 0)}|BRL",
                    FieldsSaldoCreditoS4.atualizacao: f"{item.selic.get('s4')}|BRL",

                    FieldsSaldoCreditoS5.valor_restante: f"{item.saldo_credito.s5_valor_transmissao + total.get('s5', 0)}|BRL",
                    FieldsSaldoCreditoS5.atualizacao: f"{item.selic.get('s5')}|BRL",

                }

                self.b24.update(data, 153, item.saldo_credito.id)
                last_id = item.saldo_credito.id
                print(last_id)
                count += 1
                if count == 10:
                    sleep(5)
                    count = 0
        print('Fim da execução')

    def _get_items(self, data, entity_id) -> list:
        response = self.b24.list(data, entity_id)
        return response.json().get('result', {}).get('items', [])

    def fetch_all_items(self, parent_id, entity_id):
        items = []
        last_id = 0
        data = {'>id': last_id, 'parentId153': parent_id}

        while True:
            aux = self._get_items(data, entity_id)
            if not aux:
                break
            items.extend(aux)
            last_id = aux[-1].get('id', 0)
            data['>id'] = last_id
            sleep(0.3)

        return items
