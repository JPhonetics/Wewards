def normalize_email(email):
    if not email:
        return email

    return email.strip().casefold()


def normalize_name(name):
    if not name:
        return name

    name = name.strip()

    return name[:1].upper() + name[1:]