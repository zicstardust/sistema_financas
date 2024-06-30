from utils import (
    register_tag,
    register_transaction,
    total_balance
)


tag_receitas = register_tag("Receitas")
tag_viagens = register_tag("Viagens")
tag_contas = register_tag("Contas")


register_transaction(
    description="Salario",
    value=40000.0,
    tag=tag_receitas
)

register_transaction(
    description="Buenos Aires",
    value=-10000.0,
    tag=tag_viagens
)


register_transaction(
    description="Evento",
    value=-500.0,
    tag=tag_contas
)


total = total_balance()

print (total)