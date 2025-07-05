def get_label(command: str):
    """
    Map an internal command string to a (label, BGR‑color) tuple
    """
    mapping = {
        "MOVE"        : ("Move Mode",        (255, 255,   0)),  # cyan
        "LEFT"        : ("Left Click",       (  0, 255,   0)),  # green
        "RIGHT"       : ("Right Click",      (  0,   0, 255)),  # red
        "SCROLL"      : ("Scroll Up",         (255,   0, 255)),  # magenta
        "SCROLL_DOWN" : ("Scroll Down",         (255,   0, 255)),
        "ALT_TAB"     : ("Alt+Tab",        (  0, 255, 255)),  # yellow
        None          : ("",                 (0, 0, 0))
    }
    return mapping.get(command, ("", (0, 0, 0)))
