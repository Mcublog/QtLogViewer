#!/usr/bin/env python

from lviewer.application import Application
from lviewer.ui.qt.viewer import QtApplicationView


def main():
    viewer = QtApplicationView()
    app = Application(viewer)
    app.run()


if __name__ == "__main__":
    main()
