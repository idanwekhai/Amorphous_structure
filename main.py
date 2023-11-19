import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
# from PIL import Image

from geometries.bent_120_degrees import bent_120_degrees
from geometries.bent_150_degrees import bent_150_degrees
from geometries.body_centered_cubic import body_centered_cubic
from geometries.hexagonal_bipyramidal import hexagonal_bipyramidal
from geometries.hexagonal_planar import hexagonal_planar
from geometries.hexagonal_pyramidal import hexagonal_pyramidal
from geometries.l_shaped import l_shaped
from geometries.linear import linear
from geometries.octahedral import octahedral
from geometries.pentagonal_bipyramidal import pentagonal_bipyramidal
from geometries.pentagonal_planar import pentagonal_planar
from geometries.pentagonal_pyramidal import pentagonal_pyramidal
from geometries.rectangular_see_saw_like import rectangular_see_saw_like
from geometries.see_saw_like import see_saw_like
from geometries.sgl_bd import sgl_bd
from geometries.square_co_planar import square_co_planar
from geometries.square_pyramidal import square_pyramidal
from geometries.t_shaped import t_shaped
from geometries.tetrahedral import tetrahedral
from geometries.trigonal_bipyramidal import trigonal_bipyramidal
from geometries.trigonal_non_coplanar import trigonal_non_coplanar
from geometries.trigonal_planar import trigonal_planar
from geometries.trigonal_pyramidal import trigonal_pyramidal
from geometries.water_like import water_like


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # img = Image.open(
        #     get_file_path(
        #         "rascore_logo.png",
        #         dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
        #     ),
        # )

        # st.set_page_config(page_title="rascore", page_icon=img, layout="wide")
        st.set_page_config(page_title="Energy predict", layout="wide")

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.selectbox(
            "Select Geometry", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()


app = MultiApp()

app.add_app('SGL_BD', sgl_bd)
app.add_app('L-SHAPED', l_shaped)
app.add_app('WATER-LIKE', water_like)
app.add_app('BENT 120 DEGREES', bent_120_degrees)
app.add_app('BENT 150 DEGREES', bent_150_degrees)
app.add_app('LINEAR', linear)
app.add_app('TRIGONAL PLANAR', trigonal_planar)
app.add_app('TRIGONAL NON-COPLANAR', trigonal_non_coplanar)
app.add_app('T-SHAPED', t_shaped)
app.add_app('SQUARE CO-PLANAR', square_co_planar)
app.add_app('TETRAHEDRAL', tetrahedral)
app.add_app('RECTANGULAR SEE-SAW-LIKE', rectangular_see_saw_like)
app.add_app('SEE-SAW-LIKE', see_saw_like)
app.add_app('TRIGONAL PYRAMIDAL', trigonal_pyramidal)
app.add_app('PENTAGONAL PLANAR', pentagonal_planar)
app.add_app('SQUARE PYRAMIDAL', square_pyramidal)
app.add_app('TRIGONAL BIPYRAMIDAL', trigonal_bipyramidal)
app.add_app('OCTAHEDRAL', octahedral)
app.add_app('PENTAGONAL PYRAMIDAL', pentagonal_pyramidal)
app.add_app('HEXAGONAL PLANAR', hexagonal_planar)
app.add_app('HEXAGONAL PYRAMIDAL', hexagonal_pyramidal)
app.add_app('PENTAGONAL BIPYRAMIDAL', pentagonal_bipyramidal)
app.add_app('BODY-CENTERED CUBIC', body_centered_cubic)
app.add_app('HEXAGONAL BIPYRAMIDAL', hexagonal_bipyramidal)

app.run()