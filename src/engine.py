"""Pure-Python baseline utilities; NO blockchain integration or cryptographic guarantees."""
import hashlib

def conway_step(live_cells):
    counts = {}
    for x, y in live_cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    point = (x + dx, y + dy)
                    counts[point] = counts.get(point, 0) + 1
    return {p for p, n in counts.items() if n == 3 or (n == 2 and p in live_cells)}

def state_hash(live_cells):
    serialized = ";".join(f"{x},{y}" for x, y in sorted(live_cells))
    return hashlib.sha256(serialized.encode()).hexdigest()

def emission_limit(supply, annual_rate_bps, requested):
    for value in (supply, annual_rate_bps, requested):
        if type(value) is not int or value < 0:
            raise ValueError("Values must be non-negative integers")
    if annual_rate_bps > 10000:
        raise ValueError("annual_rate_bps exceeds 100%")
    return min(requested, supply * annual_rate_bps // 10000)
