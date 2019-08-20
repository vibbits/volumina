"""
Wraps stdlib abc module to provide convenience classes for defining QObject interfaces
"""
from abc import ABCMeta, ABC, abstractproperty, abstractclassmethod, abstractmethod

from PyQt5.QtCore import QObject

__all__ = [
    "ABCMeta",
    "QABCMeta",
    "ABC",
    "ABCMeta",
    "abstractproperty",
    "abstractclassmethod",
    "abstractmethod",
    "abstractsignal",
]


class abstractsignal:
    """
    Should be used in place of pyqtSignal
    NOTE: This class doesn't implement any typechecks as abc decorators also don't provide this capability
    """

    __isabstractmethod__ = True

    def __init__(self, *args):
        pass


class QABCMeta(type(QObject), type(ABC)):
    pass


class QABC(metaclass=QABCMeta):
    pass
