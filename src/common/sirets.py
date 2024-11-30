import random


def generate_siren():
    """
    Generate a valid 9-digit SIREN number with correct Luhn algorithm check digit.

    Returns:
        str: A valid 9-digit SIREN number
    """
    # Generate first 8 digits
    base_digits = [random.randint(0, 9) for _ in range(8)]

    # Build Luhn
    total = 0
    for i, digit in enumerate(base_digits):
        if i % 2 == 0:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit

    check_digit = (10 - (total % 10)) % 10

    # Combine base digits with check digit
    siren = base_digits + [check_digit]
    return "".join(map(str, siren))


def generate_nic():
    """
    Generate a 5-digit NIC (Numéro Interne de Classement).

    Returns:
        str: A 5-digit NIC
    """
    return "".join(str(random.randint(0, 9)) for _ in range(5))


def generate_siret():
    """
    Generate a valid 14-digit French SIRET number.

    Returns:
        str: A valid 14-digit SIRET number
    """
    siren = generate_siren()
    nic = generate_nic()
    return siren + nic


def validate_siret(siret):
    """
    Validate a SIRET number using Luhn algorithm.

    Args:
        siret (str): 14-digit SIRET number to validate

    Returns:
        bool: True if SIRET is valid, False otherwise
    """
    siret = siret.replace(" ", "")

    if len(siret) != 14:
        return False

    digits = [int(d) for d in siret]

    # check Luhn
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit

    return total % 10 == 0
