from aqt import mw
from aqt.qt import *


def hide_menubar() -> None:
    mw.menuBar().setVisible(False)


def show_menubar() -> None:
    mw.menuBar().setVisible(True)


def toggle_menubar() -> None:
    is_hidden = not mw.menuBar().isVisible()
    if is_hidden:
        show_menubar()
    else:
        hide_menubar()


def setup_shortcut() -> None:
    config = mw.addonManager.getConfig(__name__)
    shortcut_config = config.get("ui", {})
    shortcut_str = shortcut_config.get("hide_menu_bar_shortcut", "")
    if shortcut_str:
        shortcut = QShortcut(QKeySequence(shortcut_str), mw)
        shortcut.activated.connect(toggle_menubar)


def on_main_window_did_init() -> None:
    config = mw.addonManager.getConfig(__name__)
    if config.get("main", {}).get("hide_menu_bar", False):
        hide_menubar()
    else:
        show_menubar()


setup_shortcut()
