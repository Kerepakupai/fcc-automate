# Informacion de ligas de Futbol

https://football-data.co.uk/data.php

# Leer tabla desde un PDF

## Dependencias
```bash
apt install ghostscript python3-tk  # ubuntu
brew install ghostscript tcl-tk     # macos
```
### Validar instalacion
```python
from ctypes.util import find_library
find_library("gs")  # "libgs.so.9"
```
### Instalar paquetes
```
pip install tk
pip install ghostscript
pip install "camelot-py[base]"
```

