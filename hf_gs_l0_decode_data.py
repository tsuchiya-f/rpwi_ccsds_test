# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:24:55 2022

@author: tsuch
"""


# -----------------------------------------------------------------------------
# decode HF raw data (survey) 
# -----------------------------------------------------------------------------
def unpack_science_data_raw(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# radio-full mode (survey)
# -----------------------------------------------------------------------------
def unpack_science_data_full(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# radio-burst mode (survey)
# -----------------------------------------------------------------------------
def  unpack_science_data_burst_surv(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# radio-burst mode (rich)
# -----------------------------------------------------------------------------
def unpack_science_data_burst_rich(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR1 mode (survey)
# -----------------------------------------------------------------------------
def unpack_science_data_pssr1_surv(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR1 mode (rich)
# -----------------------------------------------------------------------------
def unpack_science_data_pssr1_rich(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR2 mode (survey)
# -----------------------------------------------------------------------------
def unpack_science_data_pssr2_surv(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR2 mode (rich)
# -----------------------------------------------------------------------------
def unpack_science_data_pssr2_rich(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR3 mode (survey)
# -----------------------------------------------------------------------------
def unpack_science_data_pssr3_surv(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# PSSR3 mode (rich)
# -----------------------------------------------------------------------------
def unpack_science_data_seer3_rich(st_aux, st_hdr_hf, hf_buff, hf_sz):
    # to be added
    ls_dsd = 0
    return ls_dsd

# -----------------------------------------------------------------------------
# decode HF data 
# -----------------------------------------------------------------------------

def unpack_science_data(
        sid,
        sw_ver,
        st_aux,
        st_hdr_hf,
        hf_buff,
        hf_sz
        ):

    if sid == 0x42:
        # HF raw data
        ls_dsd = unpack_science_data_raw(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x43:
        # radio-full mode
        ls_dsd = unpack_science_data_full(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x44:
        # radio-burst mode (survey)
        ls_dsd = unpack_science_data_burst_surv(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x74:
        # radio-burst mode (rich)
        ls_dsd = unpack_science_data_burst_surv(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x45:
        # PSSR1 mode (survey)
        ls_dsd = unpack_science_data_pssr1_surv(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x75:
        # PSSR1 mode (rich)
        ls_dsd = unpack_science_data_pssr1_rich(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x46:
        # PSSR2 mode (survey)
        ls_dsd = unpack_science_data_pssr2_surv(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x76:
        # PSSR2 mode (rich)
        ls_dsd = unpack_science_data_pssr2_rich(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x47:
        # PSSR3 mode (survey)
        ls_dsd = unpack_science_data_pssr3_surv(st_aux, st_hdr_hf, hf_buff, hf_sz)

    elif sid == 0x77:
        # PSSR3 mode (rich)
        ls_dsd = unpack_science_data_seer3_rich(st_aux, st_hdr_hf, hf_buff, hf_sz)

    return ls_dsd
