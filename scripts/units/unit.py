# ###################################################
# Copyright (C) 2008 The OpenAnnoTeam
# team@openanno.org
# This file is part of OpenAnno.
#
# OpenAnno is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################
import common, fife

class Unit(fife.InstanceActionListener):
    def __init__(self, model, unit_name, layer, uniqInMap=True):
        """@var model: fife.Model: engine model beeing used.
        @var unit_name: str containing the units name.
        @var layer: fife.Layer on which the unit is present.
        @var uniqInMap: bool if the unit is unique.
        """
        fife.InstanceActionListener.__init__(self)
        self.model = model
        self.unit_name = unit_name
        self.layer = layer
        if uniqInMap:
            self.unit = layer.getInstances('name', unit_name)[0]
            self.unit.addActionListener(self)

    def onInstanceActionFinished(self, instance, action):
        raise ProgrammingError('No OnActionFinished defined for Unit.')

    def start(self):
        raise ProgrammingError('No start defined for Unit.')
	

def create_anon_units(model, object_name, layer, UnitClass):
    """Creates all units off a certain class.
    @var model: fife.Model: engine model beeing used.
    @var object_name: str containing the opject's name.
    @var layer: fife.Layer on which the unit is present.
    @var UnitClass: Class representing the unit.
    """
    untis = []
    instances = [a for a in layer.getInstances() if a.getObject().Id() == object_name]
    i = 0
    for a in instances:
        unit_name = '%s:i:%d' % (objectName, i)
        i += 1
        unit = UnitClass(model, unit_name, layer, False)
        unit.unit = a
        a.addActionListener(unit)
        units.append(unit)
    return units
