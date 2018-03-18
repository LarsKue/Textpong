# utils.py
# Scripted by: Philipp Koehler, Lars Kuehmichel
# subclass of Pong.py
# common utilities and functions


# checking dimensions of an image (e.g. the player's model)
def get_image_size(path):
    import get_image_size
    try:
        width, height = get_image_size.get_image_size(path)
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1

    return width, height
