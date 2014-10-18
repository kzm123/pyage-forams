# coding=utf-8
from functools import partial

import Pyro4
from pyage.core import address

from pyage.core.stop_condition import StepLimitStopCondition
from pyage_forams.solutions.distributed.neighbour_matcher import Neighbour2dMatcher, Neighbour3dMatcher
from pyage_forams.solutions.agent.remote_aggegate import create_remote_agent
from pyage_forams.solutions.distributed.request import create_dispatcher
from pyage_forams.solutions.environment import environment_factory, Environment3d
from pyage_forams.solutions.foram import create_forams
from pyage_forams.solutions.genom import GenomFactory
from pyage_forams.solutions.insolation_meter import StaticInsolation
from pyage_forams.solutions.statistics import PlottingStatistics, SimpleStatistics


factory = GenomFactory(chambers_limit=2)
genom_factory = lambda: factory.generate
forams = create_forams(5, initial_energy=5)
agents = partial(create_remote_agent, "lowerrightback")
insolation_meter = StaticInsolation
size = lambda: 5

environment = environment_factory(regeneration_factor=0.1, clazz=Environment3d)
neighbour_matcher = Neighbour3dMatcher

request_dispatcher = create_dispatcher()

stop_condition = lambda: StepLimitStopCondition(90)

reproduction_minimum = lambda: 20
movement_energy = lambda: 0.00025
growth_minimum = lambda: 10
energy_need = lambda: 0.03
algae_limit = lambda: 2
newborn_limit = lambda: 3
reproduction_probability = lambda: 0.00008
growth_probability = lambda: 0.08
growth_cost_factor = lambda: 0.5
capacity_factor = lambda: 1.1
initial_algae_probability = lambda: 0.3

address_provider = address.SequenceAddressProvider
stats = SimpleStatistics

ns_hostname = lambda: "127.0.0.1"
pyro_daemon = Pyro4.Daemon()
daemon = lambda: pyro_daemon

neighbours = lambda: {"left": "lowerleftback", "upper": "upperrightback", "front": "lowerrightfront"}