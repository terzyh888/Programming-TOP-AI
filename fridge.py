import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """Добавляет партию продукта в словарь items."""
    if title not in items:
        items[title] = []

    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, DATE_FORMAT
        ).date()

    items[title].append({
        'amount': amount,
        'expiration_date': expiration_date,
    })


def add_by_note(items, note):
    """Парсит строку вида '<название> <количество> [срок годности]'
    и добавляет продукт через add()."""
    parts = note.split()

    # Проверяем, является ли последняя часть датой
    try:
        expiration_date = datetime.datetime.strptime(
            parts[-1], DATE_FORMAT
        ).date()
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    except ValueError:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    """Возвращает список названий продуктов, содержащих подстроку needle
    (без учёта регистра)."""
    result = []
    for title in items:
        if needle.lower() in title.lower():
            result.append(title)
    return result


def get_amount(items, needle):
    """Возвращает общее количество продуктов с подстрокой needle
    в названии (тип Decimal)."""
    product_amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    """Возвращает список кортежей (название, количество) продуктов,
    срок годности которых истёк или истечёт в течение in_advance_days."""
    result = []
    today = datetime.date.today()
    expiration_limit = today + datetime.timedelta(days=in_advance_days)

    for title, parts in items.items():
        amount = Decimal('0')
        for part in parts:
            expiration_date = part['expiration_date']
            if (expiration_date is not None
                    and expiration_date <= expiration_limit):
                amount += part['amount']
        if amount > 0:
            result.append((title, amount))

    return result