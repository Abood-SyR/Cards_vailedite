def individual_serial(card) -> dict:
    return {
        "id": str(card["_id"]),
        "have_access": card["have_access"],
        "count": card["count"]
        
    }


def list_serial(cards) -> list:
    return [individual_serial(card) for card in cards] 