# Communication with Viessmann heating via Optolink interface


![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

Python package to communicate with Viessmann heatings via the optolink serial interface.
Replacement for vcontrold when using a python environment.

Python package zur Kommunikation mit Viessmann-Heizungen über die Optolink serielle Schnittstelle.
Geeignet um vcontrold zu ersetzen wenn ohnehin mit Python gearbeitet wird.

Neuentwicklung basierend  auf 
-  [SmartHomeNG plugin (Python)][SHNGpyPlugin]
-  [vcontrold][vcontrold]

Motivation:
- Python-Modul um direkt auf die Viessmann-Heizung zugreifen zu können (ohne Umweg über vcontrold)

Einschränkungen/known issues/ToDos:
 - Tests not up2date after refactorings
 - Some code was added while drunk
 - Data types need work and should be externalized (maybe?)
 - Only Vitocal 200-A implemented, however should be easily exchangable
 - API documentation (Swagger)

Usage:
 - Set up optolink device and API parameters in `config/viConfig.json`
 - In root directory run `pip install .` to install package
    - If you use centrally managed python libraries it's best to use virtual environments (`venv`)
    - If you plan on adding/developing, best to use `pip install -e .`. Makes the package editable without reinstalling after each change.
  - In the test directory, use `python testViessmann.py` to test all commands in shell
  - Run `python viAPI.py` to run a bootleg `flask` REST API
    - API endpoint docs to follow



[vcontrold]: https://github.com/openv (vcontrold)
[SHNGpyPlugin]: https://github.com/sisamiwe/myplugins/tree/master/viessmann (SmartHomeNG python Plugin)
[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
