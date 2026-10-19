"""x402 Bazaar Agent-to-Agent Payment Protocol."""
def generate_payment_required_header(resource_id: str, amount_usd: float) -> dict:
    return {
        "status": 402,
        "x402-resource": resource_id,
        "x402-price-usd": str(amount_usd),
        "x402-bazaar-version": "2.0"
    }
