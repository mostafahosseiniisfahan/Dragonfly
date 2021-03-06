# Dragonfly: A Plugin for Climate Modeling (GPL) started by Chris Mackey <chris@ladybug.tools> 
# This file is part of Dragonfly.
#
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Use this component to generate parameters that describe the pavement of the urban area, which can be plugged into the "DF uwg City" component.
-
Provided by Dragonfly 0.0.03
    
    Args:
        _albedo_: A number between 0 and 1 that represents the surface albedo (or reflectivity) of the pavement.  The default is set to 0.1, which is typical of fresh asphalt.
        _thickness_: A number that represents the thickness of the pavement material in meters (m).  The default is set to 0.5 meters.
        _conductivity_:  A number representing the conductivity of the pavement material in W/m-K.  This is the heat flow in Watts across one meter thick of the material when the temperature difference on either side is 1 Kelvin. The default is set to 1 W/m-K, which is typical of asphalt.
        _vol_heat_cap_:  A number representing the volumetric heat capacity of the pavement material in J/m3-K.  This is the number of joules needed to raise one cubic meter of the material by 1 degree Kelvin.  The default is set to 1,600,000 J/m3-K, which is typical of asphalt.
    Returns:
        pavement_par: Pavement parameters that can be plugged into the "DF uwg City" component.

"""

ghenv.Component.Name = "DF Pavement Parameters"
ghenv.Component.NickName = 'PavementPar'
ghenv.Component.Message = 'VER 0.0.03\nJUL_08_2018'
ghenv.Component.Category = "Dragonfly"
ghenv.Component.SubCategory = "1 | Urban Weather"
#compatibleDFVersion = VER 0.0.02\nMAY_20_2018
ghenv.Component.AdditionalHelpFromDocStrings = "5"


import scriptcontext as sc
import Grasshopper.Kernel as gh

#Dragonfly check.
init_check = True
if not sc.sticky.has_key('dragonfly_release') == True:
    init_check = False
    print "You should first let Drafgonfly fly..."
    ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, "You should first let Drafgonfly fly...")
else:
    if not sc.sticky['dragonfly_release'].isCompatible(ghenv.Component): init_check = False
    if sc.sticky['dragonfly_release'].isInputMissing(ghenv.Component): init_check = False
    df_PavementPar = sc.sticky["dragonfly_PavementPar"]

if init_check == True:
    pavement_par = df_PavementPar(_albedo_, _thickness_, _conductivity_, 
        _vol_heat_cap_)