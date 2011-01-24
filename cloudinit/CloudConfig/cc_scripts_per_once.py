# vi: ts=4 expandtab
#
#    Copyright (C) 2011 Canonical Ltd.
#
#    Author: Scott Moser <scott.moser@canonical.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3, as
#    published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import cloudinit.util as util
from cloudinit.CloudConfig import per_once, per_always, per_instance
from cloudinit import get_cpath, get_ipath_cur

frequency = per_once
runparts_path = "%s/%s" % (get_cpath(), "scripts/per-once")

def handle(name,cfg,cloud,log,args):
    try:
        util.runparts(runparts_path)
    except:
        log.warn("failed to run-parts in %s" % runparts_path)
        raise
