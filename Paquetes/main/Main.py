# Los módulos que se utilizarán como principal deberían siempre utilizar imports absolutos
from sound.effects import echo
import Comunicator
Comunicator.do_comunicator()
echo.do_echo()
