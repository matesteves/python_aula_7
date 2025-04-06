def produtos_nao_entregues(lista: list[dict]) -> list:
    """
    Returns non delivered items
    """
    entregues = []
    for i in lista:
        if i.get("delivered") == "False":
            entregues.append(i)
    return entregues

def total_revenue(lista: list[dict]) -> float:
    """
    Returns the total value for all sales
    """
    total: float = 0
    for i in lista:
        total += float(i.get("price"))
    return total