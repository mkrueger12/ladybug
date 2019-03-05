# coding=utf-8
"""Generic data type."""
from __future__ import division

from .base import DataTypeBase


class GenericType(DataTypeBase):
    """Type for any data type that is not currently implemented."""
    def __init__(self, name, unit, min=float('-inf'), max=float('+inf'),
                 abbreviation=None, unit_descr='', point_in_time=True,
                 cumulative=False, min_epw=float('-inf'), max_epw=float('+inf'),
                 missing_epw=None):
        """Initalize Generic Type.

        Args:
            name: A name for the data type as a string.
            unit: A unit for the data type as a string.
            min: Optional lower limit for the data type, values below which should be
                physically or mathematically impossible. (Default: -inf)
            max: Optional upper limit for the data type, values above which should be
                physically or mathematically impossible. (Default: +inf)
            abbreviation: An optional abbreviation for the data type as text.
            unit_descr: An optional description of the units if numerical values
                of these units relate to specific categories.
            point_in_time: Boolean to note whether the data type represents conditions
                at a single instant in time (True) as opposed to being an average or
                accumulation over time (False) when it is found in hourly lists of data.
                (Default: True)
            cumulative: Boolean to tell whether the data type can be cumulative when it
                is represented over time (True) or it can only be averaged over time
                to be meaningful (False). Note that cumulative cannot be True
                when point_in_time is also True. (Default: False)
            min_epw: Lower limit for the data type when it occurs in EPW files.
                (Default: -inf)
            max_epw: Upper limit for the data type when it occurs in EPW files.
                (Default: +inf)
            missing_epw: Missing value for the data type when it occurs in EPW files.
                (Default: None)
        """
        assert isinstance(name, str), 'name must be a string. Got {}.'.format(type(name))
        assert isinstance(unit, str), 'unit must be a string. Got {}.'.format(type(unit))
        assert isinstance(min, (float, int)), 'min must be a number. ' \
            'Got {}.'.format(type(min))
        assert isinstance(max, (float, int)), 'max must be a number. ' \
            'Got {}.'.format(type(max))
        if abbreviation is not None:
            assert isinstance(abbreviation, str), 'abbreviation must be a ' \
                'string. Got {}.'.format(type(abbreviation))
        assert isinstance(unit_descr, str), 'unit_descr must be a ' \
            'string. Got {}.'.format(type(unit_descr))
        assert isinstance(point_in_time, bool), 'point_in_time must be a ' \
            'boolean. Got {}.'.format(type(point_in_time))
        assert isinstance(cumulative, bool), 'cumulative must be a ' \
            'boolean. Got {}.'.format(type(cumulative))
        if point_in_time is True:
            assert cumulative is False, 'cumulative cannot be True when ' \
                'point_in_time is also True.'
        assert isinstance(min_epw, (float, int)), 'min_epw must be a number. ' \
            'Got {}.'.format(type(min_epw))
        assert isinstance(max_epw, (float, int)), 'max_epw must be a number. ' \
            'Got {}.'.format(type(max_epw))
        if missing_epw is not None:
            assert isinstance(missing_epw, (float, int)), 'missing_epw must be' \
                'a number .Got {}.'.format(type(missing_epw))

        self._name = name
        self._units = [unit]
        self._min = min
        self._max = max
        self._abbreviation = abbreviation if abbreviation is not None else name
        self._unit_descr = unit_descr
        self._point_in_time = point_in_time
        self._cumulative = cumulative
        self._min_epw = min_epw
        self._max_epw = max_epw
        self._missing_epw = missing_epw

    def to_ip(self, values, from_unit):
        """Return values in IP and the units to which the values have been converted."""
        return values, from_unit

    def to_si(self, values, from_unit):
        """Return values in SI and the units to which the values have been converted."""
        return values, from_unit