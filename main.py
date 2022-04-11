
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import hf_gs_l0_decode_header as hf_hdr
    
#----------------------------------------------------------
# open ccsds file
#----------------------------------------------------------
fin = open("C:/share/Linux/juice_test/20210908_radio_full_2D_matrix/HF_20210908-1832.ccs","rb")


while True:

    #----------------------------------------------------------
    # get one HF pachet
    #----------------------------------------------------------
    st_hdr_pri, \
    st_hdr_sec, \
    st_hdr_rpw, \
    st_aux,     \
    st_hdr_hf,  \
    st_cnt,     \
    hf_buff,    \
    hf_sz = hf_hdr.get_one_packet(fin)


    # Detect End-of-file
    if st_cnt.eof:
        break

    print('process ID      ',format(st_hdr_pri.pid, '02x'))
    print('packet category ',format(st_hdr_pri.pcat, '02x'))
    print('packet length   ',hf_sz)

    #----------------------------------------------------------
    # Convert L0 to L1
    #----------------------------------------------------------



#----------------------------------------------------------
# close ccsds file
#----------------------------------------------------------
print("End of file")
fin.close()

