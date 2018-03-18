"""
utils.py
Subclass of Pong.py
Scripted by: Philipp Koehler, Lars Kuehmichel
Description: Common utilities and functions
"""


# checking dimensions of an image (e.g. the player's model)
def get_image_size(path):
    import get_image_size
    try:
        width, height = get_image_size.get_image_size(path)
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1

    return width, height
