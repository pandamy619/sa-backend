from typing import Dict, List


def sorting_descending_sales(data: Dict[str, List]) -> Dict[str, List]:
    """"Sorts dictionary descending sales"""
    sorted_keys = sorted(data, key=data.get, reverse=True)
    return {key: data[key] for key in sorted_keys}


def category(share: float) -> str:
    """Assigns categories A/B/C"""
    if share <= 80.0:
        return 'A'
    elif 80.0 < share <= 95.0:
        return 'B'
    return 'C'


def amount(data: Dict[str, List]) -> float:
    """Determines the total sales amount"""
    return sum([float(sale[0]) for sale in data.values()])


def abc(data: Dict[str, List]) -> Dict[str, List]:
    """Implements ABC sales analysis"""
    sorted_data = sorting_descending_sales(data)
    sales_amount = amount(sorted_data)
    accrued_share = 0
    for key in sorted_data:
        sorted_data[key].append(round(sorted_data[key][0] / sales_amount * 100, 2))
        sorted_data[key].append(round(accrued_share + sorted_data[key][1], 2))
        accrued_share = sorted_data[key][2]
        sorted_data[key].append(category(accrued_share))
    return sorted_data