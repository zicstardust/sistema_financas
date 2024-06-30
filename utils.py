from classes.tag import Tag
from classes.transactions import Transaction

TAG_LIST = []
TRANSACTION_LIST = []


def register_tag(name):
    new_tag = Tag(name=name)
    TAG_LIST.append(new_tag)
    return new_tag


def register_transaction(description, value, tag):
    new_transaction = Transaction(
        description=description,
        value=value,
        tag=tag
    )
    TRANSACTION_LIST.append(new_transaction)
    return new_transaction


def total_balance():
    total = 0
    
    for t in TRANSACTION_LIST:
        total += t.value

    return total