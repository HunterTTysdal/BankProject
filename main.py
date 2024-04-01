# Fantastic 4
from Login import *
from HomePage import *


choice = 0
if "logged in" in st.session_state:
    homePage()
else:
    login()


