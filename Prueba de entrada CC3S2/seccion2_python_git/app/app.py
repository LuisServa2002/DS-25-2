# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    try:
        numbers = [float(x) for x in nums]
    except Exception:
        raise ValueError("Todos los elementos deben ser numéricos")

    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return {"count": count, "sum": total, "avg": avg}


def main():
    import sys
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    items = [p.strip() for p in raw.split(",") if p.strip()]
    result = summarize(items)
    print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")


if __name__ == "__main__":
    main()
