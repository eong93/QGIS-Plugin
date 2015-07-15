# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HelloWorld2
                                 A QGIS plugin
 says hello world
                             -------------------
        begin                : 2015-06-26
        copyright            : (C) 2015 by Eric Ong
        email                : eric.ong@digitalglobe.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HelloWorld2 class from file HelloWorld2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hello_world import HelloWorld2
    return HelloWorld2(iface)
