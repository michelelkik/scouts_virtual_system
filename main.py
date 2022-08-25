import sys
import streamlit
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "webapp.py"]
    sys.exit(stcli.main())
