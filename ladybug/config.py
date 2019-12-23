"""Ladybug configurations.

Import this into every module where access configurations are needed.

Usage:
    from ladybug.config import folders
    print(folders.default_epw_folder)
    folders.default_epw_folder = "C:/epw_data"
"""
import os
import sys
import json


class Folders(object):
    """Ladybug folders.

    Args:
        config_file: The path to the config.json file from which folders are loaded.
            If None, the config.json module included in this package will be used.
            Default: None.
        mute: If False, the paths to the various folders will be printed as they
            are found. If True, no printing will occur upon initialization of this
            class. Default: True.

    Properties:
        * default_epw_folder
        * config_file
        * mute
    """

    def __init__(self, config_file=None, mute=True):
        # set the mute value
        self.mute = bool(mute)

        # load paths from the config JSON file 
        self.config_file  = config_file

    @property
    def default_epw_folder(self):
        """Get or set the path to the default folder where EPW files are stored."""
        return self._default_epw_folder
    
    @default_epw_folder.setter
    def default_epw_folder(self, path):
        if not path:  # check the default location for epw files
            path = self._find_default_epw_folder()

        self._default_epw_folder = path

        if not self.mute and self._default_epw_folder:
            print('Path to the default epw folder is set to: '
                  '{}'.format(self._default_epw_folder))
    
    @property 
    def config_file(self):
        """Get or set the path to the config.json file from which folders are loaded.
        
        Setting this to None will result in using the config.json module included
        in this package.
        """
        return self._config_file

    @config_file.setter
    def config_file(self, cfg):
        if cfg is None:
            cfg = os.path.join(os.path.dirname(__file__), 'config.json')
        self._load_from_file(cfg)
        self._config_file = cfg

    def _load_from_file(self, file_path):
        """Set all of the the properties of this object from a config JSON file.
        
        Args:
            file_path: Path to a JSON file containing the file paths. A sample of this
                JSON is the config.json file within this package.
        """
        # check the default file path
        assert os.path.isfile(file_path), \
            ValueError('No file found at {}'.format(file_path))

        # set the default paths to be all blank
        default_path = {
            "default_epw_folder": r''
        }

        with open(file_path, 'r') as cfg:
            try:
                paths = json.load(cfg)
            except Exception as e:
                print('Failed to load paths from {}.\nThey will be set to defaults '
                      'instead\n{}'.format(file_path, e))
            else:
                for key, p in paths.items():
                    if not key.startswith('__') and p.strip():
                        default_path[key] = p.strip()

        # set paths for the default_epw_folder
        self.default_epw_folder = default_path["default_epw_folder"]

    @staticmethod
    def _find_default_epw_folder():
        """Find the the default EPW folder in its usual location.
        
        An attempt will be made to create the directory if it does not already exist.
        """
        try:  # windows
            sim_folder = os.path.join(os.environ['USERPROFILE'], 'ladybug')
        except KeyError:  # mac and linux
            sim_folder = os.path.join(os.environ['HOME'], 'ladybug')
        if not os.path.isdir(sim_folder):
            try:
                os.makedirs(sim_folder)
            except Exception as e:
                raise OSError('Failed to create default epw '
                              'folder: %s\n%s' % (sim_folder, e))
        return sim_folder


"""Object possesing all key folders within the configuration."""
folders = Folders()