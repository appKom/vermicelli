"""
TODO:
- [Gjort] Lage funksjon som deler opp fra en komités slot 
- Sette opp begrensningene fra modelleringen
- Flikke litt på modelleringen.
- Finn ut hvordan man kan preprosessere dataen for å få ned kjøretiden (f. eks ved å lage lister av personer for hver komité.)
"""

from __future__ import annotations
from mip_matching.TimeInterval import TimeInterval
from mip_matching.Applicant import Applicant
from mip_matching.Committee import Committee

import sys
print(sys.path)


# personer_og_tidsslots = {"Jørgen": {TimeInterval(1, 4)},
#                          "Sindre": {TimeInterval(2, 3), TimeInterval(4, 6)},
#                          "Julian": {TimeInterval(3, 4), TimeInterval(1, 2), TimeInterval(5, 6)},
#                          "Fritz": {TimeInterval(1, 2), TimeInterval(4, 5)}}
# komiteer_og_tidsslots = {"Appkom": {TimeInterval(1, 2), TimeInterval(2, 3), TimeInterval(3, 4), TimeInterval(4, 5)},
#                          "OIL": {TimeInterval(4, 5), TimeInterval(5, 6)},
#                          "Prokom": {TimeInterval(1, 3), TimeInterval(4, 6)}}

# komite_kapasiteter = {"Appkom": {TimeInterval(1, 2): 1,
#                                  TimeInterval(2, 3): 1,
#                                  TimeInterval(3, 4): 1,
#                                  TimeInterval(4, 5): 1},
#                       "OIL": {TimeInterval(4, 5): 1,
#                               TimeInterval(5, 6): 1},
#                       "Prokom": {TimeInterval(1, 3): 1,
#                                  TimeInterval(4, 6): 1}}


# personer = personer_og_tidsslots.keys()
# komiteer = komiteer_og_tidsslots.keys()

# intervjulengder = {"Appkom": 1,
#                    "Prokom": 2,
#                    "OIL": 1}

# komiteer_per_person = {"Jørgen": {"Appkom", "Prokom"},
#                        "Sindre": {"Appkom", "OIL"},
#                        "Julian": {"Appkom", "Prokom", "OIL"},
#                        "Fritz": {"OIL"}}


"""
Tror det følgende er gammel kode som ble brukt for CSP.
"""

# # Variables
# variables = set()
# for person in komiteer_per_person:
#     for komite in komiteer_per_person[person]:
#         variables.add((person, komite))
# # Domains
# domains = {var: personer_og_tidsslots[var[0]].intersection(
#     komiteer_og_tidsslots[var[1]]) for var in variables}

# constraints = {var: set() for var in variables}
# for var, annen in itertools.permutations(variables, 2):
#     if annen[0] == var[0]:
#         constraints[var].add(annen)
#     if annen[1] == var[1]:
#         constraints[var].add(annen)
