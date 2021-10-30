## -*- coding: utf-8 -*-
#
# «plg_mcp_remote» - Mythbuntu Control Panel tab to configure MCP Remote
#
# Copyright (C) 2021, Ted L (MythTV Forum member heyted)
#
# This is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this application. If not, see <http://www.gnu.org/licenses/>.
##################################################################################

from MythbuntuControlPanel.plugin import MCPPlugin
import os
import configparser, time

class MCPRemotePlugin(MCPPlugin):
    """A plugin for MCP remote settings"""

    def __init__(self):
        #Initialize parent class
        information = {}
        information["name"] = "MCP Remote"
        information["icon"] = "gtk-go-forward-ltr"
        information["ui"] = "tab_mcp_remote"
        MCPPlugin.__init__(self,information)

    def captureState(self):
        """Determines the state of the items managed by this plugin"""
        uhomepath = os.environ['HOME']
        if os.path.exists(uhomepath + '/.mythbuntu/mcp_remote.cfg'):
            config = configparser.RawConfigParser()
            config.read(uhomepath + '/.mythbuntu/mcp_remote.cfg')
            self.be_ip = config.get('mcp_remote_settings', 'be_ip')
            self.key_back = config.get('mcp_remote_settings', 'key_back')
            self.key_prev_ch = config.get('mcp_remote_settings', 'key_prev_ch')
            self.key_info = config.get('mcp_remote_settings', 'key_info')
            self.key_guide = config.get('mcp_remote_settings', 'key_guide')
            self.key_del = config.get('mcp_remote_settings', 'key_del')
            self.key_menu = config.get('mcp_remote_settings', 'key_menu')
            self.key_rewind = config.get('mcp_remote_settings', 'key_rewind')
            self.key_play_pau = config.get('mcp_remote_settings', 'key_play_pau')
            self.key_fst_fwd = config.get('mcp_remote_settings', 'key_fst_fwd')
            self.key_jump_bk = config.get('mcp_remote_settings', 'key_jump_bk')
            self.key_record = config.get('mcp_remote_settings', 'key_record')
            self.key_jump_ahd = config.get('mcp_remote_settings', 'key_jump_ahd')
            self.key_vol_dn = config.get('mcp_remote_settings', 'key_vol_dn')
            self.key_mute = config.get('mcp_remote_settings', 'key_mute')
            self.key_vol_up = config.get('mcp_remote_settings', 'key_vol_up')
        else:
            self.be_ip = ''
            self.key_back = 'ESCAPE'
            self.key_prev_ch = 'H'
            self.key_info = 'I'
            self.key_guide = 'S'
            self.key_del = 'D'
            self.key_menu = 'M'
            self.key_rewind = '<'
            self.key_play_pau = 'P'
            self.key_fst_fwd = '>'
            self.key_jump_bk = 'PAGEUP'
            self.key_record = 'R'
            self.key_jump_ahd = 'PAGEDOWN'
            self.key_vol_dn = '{'
            self.key_mute = '|'
            self.key_vol_up = '}'

    def applyStateToGUI(self):
        """Takes the current state information and sets the GUI
           for this plugin"""
        if os.path.exists(os.environ['HOME'] + '/.mythbuntu/mcp_remote.cfg'):
            self.ent_be_ip.set_text(self.be_ip)
            self.ent_back.set_text(self.key_back)
            self.ent_prev_ch.set_text(self.key_prev_ch)
            self.ent_info.set_text(self.key_info)
            self.ent_guide.set_text(self.key_guide)
            self.ent_del.set_text(self.key_del)
            self.ent_menu.set_text(self.key_menu)
            self.ent_rewind.set_text(self.key_rewind)
            self.ent_play_pau.set_text(self.key_play_pau)
            self.ent_fst_fwd.set_text(self.key_fst_fwd)
            self.ent_jump_bk.set_text(self.key_jump_bk)
            self.ent_record.set_text(self.key_record)
            self.ent_jump_ahd.set_text(self.key_jump_ahd)
            self.ent_vol_dn.set_text(self.key_vol_dn)
            self.ent_mute.set_text(self.key_mute)
            self.ent_vol_up.set_text(self.key_vol_up)

    def compareState(self):
        """Determines what items have been modified on this plugin"""
        #Prepare for state capturing
        MCPPlugin.clearParentState(self)
        save = False
        if self.be_ip != self.ent_be_ip.get_text():
            save =  True
        if self.key_back != self.ent_back.get_text():
            save =  True
        if self.key_prev_ch != self.ent_prev_ch.get_text():
            save =  True
        if self.key_info != self.ent_info.get_text():
            save =  True
        if self.key_guide != self.ent_guide.get_text():
            save =  True
        if self.key_del != self.ent_del.get_text():
            save =  True
        if self.key_menu != self.ent_menu.get_text():
            save =  True
        if self.key_rewind != self.ent_rewind.get_text():
            save =  True
        if self.key_play_pau != self.ent_play_pau.get_text():
            save =  True
        if self.key_fst_fwd != self.ent_fst_fwd.get_text():
            save =  True
        if self.key_jump_bk != self.ent_jump_bk.get_text():
            save =  True
        if self.key_record != self.ent_record.get_text():
            save =  True
        if self.key_jump_ahd != self.ent_jump_ahd.get_text():
            save =  True
        if self.key_vol_dn != self.ent_vol_dn.get_text():
            save =  True
        if self.key_mute != self.ent_mute.get_text():
            save =  True
        if self.key_vol_up != self.ent_vol_up.get_text():
            save =  True
        if save:
            settings = (self.ent_be_ip.get_text(), self.ent_back.get_text(),
            self.ent_prev_ch.get_text(), self.ent_info.get_text(), self.ent_guide.get_text(),
            self.ent_del.get_text(), self.ent_menu.get_text(), self.ent_rewind.get_text(),
            self.ent_play_pau.get_text(), self.ent_fst_fwd.get_text(), self.ent_jump_bk.get_text(),
            self.ent_record.get_text(), self.ent_jump_ahd.get_text(), self.ent_vol_dn.get_text(),
            self.ent_mute.get_text(), self.ent_vol_up.get_text())
            self._markReconfigureUser("save_settings", settings)

    def user_scripted_changes(self,reconfigure):
        """Local changes that can be performed by the user account.
           This function will be ran by the frontend"""
        for item in reconfigure:
            if item == 'save_settings':
                be_ip_okay = False
                pieces = reconfigure[item][0].split('.')
                if len(pieces) == 4:
                    be_ip_okay = True
                try:
                    if not all(0<=int(p)<256 for p in pieces):
                        be_ip_okay = False
                except ValueError:
                    be_ip_okay = False
                USERHOME = os.path.expanduser("~")
                if not os.path.isdir(USERHOME+"/.mythbuntu") and be_ip_okay:
                    os.mkdir(USERHOME+"/.mythbuntu")
                if be_ip_okay:
                    self.emit_progress("Saving settings", 50)
                    time.sleep(1)
                    config = configparser.RawConfigParser()
                    config.add_section('mcp_remote_settings')
                    config.set('mcp_remote_settings', 'be_ip', reconfigure[item][0])
                    config.set('mcp_remote_settings', 'key_back', reconfigure[item][1])
                    config.set('mcp_remote_settings', 'key_prev_ch', reconfigure[item][2])
                    config.set('mcp_remote_settings', 'key_info', reconfigure[item][3])
                    config.set('mcp_remote_settings', 'key_guide', reconfigure[item][4])
                    config.set('mcp_remote_settings', 'key_del', reconfigure[item][5])
                    config.set('mcp_remote_settings', 'key_menu', reconfigure[item][6])
                    config.set('mcp_remote_settings', 'key_rewind', reconfigure[item][7])
                    config.set('mcp_remote_settings', 'key_play_pau', reconfigure[item][8])
                    config.set('mcp_remote_settings', 'key_fst_fwd', reconfigure[item][9])
                    config.set('mcp_remote_settings', 'key_jump_bk', reconfigure[item][10])
                    config.set('mcp_remote_settings', 'key_record', reconfigure[item][11])
                    config.set('mcp_remote_settings', 'key_jump_ahd', reconfigure[item][12])
                    config.set('mcp_remote_settings', 'key_vol_dn', reconfigure[item][13])
                    config.set('mcp_remote_settings', 'key_mute', reconfigure[item][14])
                    config.set('mcp_remote_settings', 'key_vol_up', reconfigure[item][15])
                    config.set('mcp_remote_settings', 'last_used_fe', '')
                    with open(USERHOME + '/.mythbuntu/mcp_remote.cfg', 'w') as configfile:
                        config.write(configfile)
                else:
                    self.emit_progress("Invalid IP address", 0)
                    time.sleep(2)
