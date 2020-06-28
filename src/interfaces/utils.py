
def slot_config(config: dict):
    def wrapper(f):
        setattr(f, 'slots', config)

        return f

    return wrapper