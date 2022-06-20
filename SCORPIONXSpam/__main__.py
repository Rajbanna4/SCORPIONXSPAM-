#SCORPIONXSpam

import glob
import logging
from pathlib import Path
from . import SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9, SP10
from SORPIOMXSpam.utils import load_plugins

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "SCORPIONXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("SCORPIOM Spam Bot Successfully deployed 😎🤘🏻 ===|")

if __name__ == "__main__":
    SP1.run_until_disconnected()
    
if __name__ == "__main__":
    SP2.run_until_disconnected()

if __name__ == "__main__":
    SP3.run_until_disconnected()
    
if __name__ == "__main__":
    SP4.run_until_disconnected()

if __name__ == "__main__":
    SP5.run_until_disconnected()
    
if __name__ == "__main__":
    SP6.run_until_disconnected()
    
if __name__ == "__main__":
    SP7.run_until_disconnected()

if __name__ == "__main__":
    SP8.run_until_disconnected()
    
if __name__ == "__main__":
    SP9.run_until_disconnected()

if __name__ == "__main__":
    SP10.run_until_disconnected()    
