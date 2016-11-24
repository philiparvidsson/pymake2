#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake2                 import report
from pymake2.core.exceptions import NoSuchTargetError
from pymake2.core.target     import Target

#---------------------------------------
# CLASSES
#---------------------------------------

class Maker(object):
    #---------------------------------------
    # STATIC ATTRIBUTES
    #---------------------------------------

    _inst = None

    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self):
        self.def_target = None # Default target.
        self.targets    = []   # List with known targets.

    #---------------------------------------
    # METHODS
    #---------------------------------------

    def check_target(self, name, checked=None, depends=()):
        if checked is None:
            checked = []

        if name in depends:
            report.error("circular dependency found in target: {}", name)
            return

        if name in checked:
            return

        checked.append(name)

        depends += name,

        target = self.get_target(name, False)

        if not target:
            report.error("target does not exist: {}", name)
            return

        if not target.func:
            report.warn("unbound target: {}", name)

        for depend in target.depends:
            self.check_target(depend, checked, depends)

    def check_targets(self):
        checked = []

        for target in self.targets:
            self.check_target(target.name, checked)

    def get_target(self, name, create=True):
        for target in self.targets:
            if target.name == name:
                return target

        if not create:
            return None

        target = Target(name)

        self.targets.append(target)

        return target

    def make(self, name, conf, completed=None):
        if completed is None:
            completed = []

        if name in completed:
            return

        target = self.get_target(name, False) if name else self.def_target

        if not target:
            raise NoSuchTargetError(name)

        for depend in target.depends:
            self.make(depend, conf, completed)

        target.make(conf)
        completed.append(name)

    @staticmethod
    def inst():
        if not Maker._inst:
            Maker._inst = Maker()

        return Maker._inst