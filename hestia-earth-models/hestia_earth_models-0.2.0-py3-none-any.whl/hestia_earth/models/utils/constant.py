from enum import Enum
from hestia_earth.utils.tools import list_sum


class Units(Enum):
    KG = 'kg'
    KG_CA = 'kg Ca'
    KG_CACO3 = 'kg CaCO3'
    KG_CAO = 'kg CaO'
    KG_CH4 = 'kg CH4'
    KG_CO2 = 'kg CO2'
    KG_K = 'kg K'
    KG_K2O = 'kg K2O'
    KG_MGCO3 = 'kg MgCO3'
    KG_N = 'kg N'
    KG_N2O = 'kg N2O'
    KG_NH3 = 'kg NH3'
    KG_NH4 = 'kg NH4'
    KG_NO2 = 'kg NO2'
    KG_NO3 = 'kg NO3'
    KG_NOX = 'kg NOx'
    KG_P = 'kg P'
    KG_P2O5 = 'kg P2O5'
    KG_PO43 = 'kg PO43'
    TO_C = '-C'
    TO_N = '-N'


ATOMIC_WEIGHT_CONVERSIONS = {
    Units.KG_P.value: {
        Units.KG_P2O5.value: (30.974*2+15.999*5)/(30.974*2),  # Conv_Mol_P_P2O5
        Units.KG_PO43.value: (30.974+15.999*4)/30.974  # Conv_Mol_P_PO43-
    },
    Units.KG_PO43.value: {
        Units.KG_P2O5.value: (30.974*2+15.999*5)/((30.974+15.999*4)*2)  # Conv_Mol_PO43-_P2O5
    },
    Units.KG_K.value: {
        Units.KG_K2O.value: (39.098*2+15.999)/(39.098*2)  # Conv_Mol_K_K2O
    },
    Units.KG_CA.value: {
        Units.KG_CAO.value: (40.078+15.999)/40.078  # Conv_Mol_Ca_CaO
    },
    Units.KG_CAO.value: {
        Units.KG_CACO3.value: (40.078+12.012+15.999*3)/(40.078+15.999)  # Conv_Mol_CaO_CaCO3
    },
    Units.KG_CACO3.value: {
        Units.KG_CO2.value: 0.12
    },
    Units.KG_MGCO3.value: {
        Units.KG_CO2.value: 0.13
    },
    Units.KG_CH4.value: {
        Units.TO_C.value: (12.012+1.008*4)/12.012  # Conv_Mol_CH4C_CH4
    },
    Units.KG_CO2.value: {
        Units.TO_C.value: (12.012+15.999*2)/12.012  # Conv_Mol_CO2C_CO2
    },
    Units.KG_NOX.value: {
        Units.TO_N.value: (14.007+15.999)/14.007  # Conv_Mol_NON_NO
    },
    Units.KG_N2O.value: {
        Units.TO_N.value: (14.007*2+15.999)/(14.007*2)  # Conv_Mol_N2ON_N2O
    },
    Units.KG_NO2.value: {
        Units.TO_N.value: (14.007+15.999*2)/14.007  # Conv_Mol_NO2N_NO2
    },
    Units.KG_NO3.value: {
        Units.TO_N.value: (14.007+15.999*3)/14.007  # Conv_Mol_NO3N_NO3
    },
    Units.KG_NH3.value: {
        Units.TO_N.value: (14.007+1.008*3)/14.007  # Conv_Mol_NH3N_NH3
    },
    Units.KG_NH4.value: {
        Units.TO_N.value: (14.007+1.008*4)/14.007  # Conv_Mol_NH4N_NH4
    }
}


def get_atomic_conversion(src_unit: Units, dest_unit: Units):
    src_key = src_unit if isinstance(src_unit, str) else src_unit.value
    dest_key = dest_unit if isinstance(dest_unit, str) else dest_unit.value
    return ATOMIC_WEIGHT_CONVERSIONS.get(src_key, {}).get(dest_key, 1)


def convert_to_unit(node: dict, dest_unit: Units):
    return list_sum(node.get('value', [])) * get_atomic_conversion(node.get('term', {}).get('units'), dest_unit)
