# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:34:59 2022

@author: tsuch
"""

class struct:
    pass

# -----------------------------------------------------------------------------
# decode packet primary header
# -----------------------------------------------------------------------------
def get_hdr_pri(bdata):
    ret = struct()
    ret.ccsds_ver =  (bdata[0] & 0xe0) >> 5
    ret.pkt_type  =  (bdata[0] & 0x10) >> 4
    ret.dat_flg   =  (bdata[0] & 0x08) >> 3
    ret.pid       = ((bdata[0] & 0x07) << 4) | ((bdata[1] & 0xf0) >> 4)
    ret.pcat      =   bdata[1] & 0x0f
    ret.seq_flg   =  (bdata[2] & 0xc0) >> 6
    ret.seq_cnt   = ((bdata[2] & 0x3f) << 8) | bdata[3]  
    ret.pkt_len   =  (bdata[4] << 8) | bdata[5]  
    
    return ret
# -----------------------------------------------------------------------------
# decode data field header (packet secondary header)
# -----------------------------------------------------------------------------
def get_hdr_sec(bdata):
    ret = struct()
    ret.psu_ver   = (bdata[0] & 0x70) >> 4
    ret.ser_type  =  bdata[1]
    ret.ser_stype =  bdata[2]
    ret.dst_id    =  bdata[3]
    ret.time      =  bdata[4] << 40 + bdata[5] << 32 + bdata[6] << 24 + bdata[7] << 16 + bdata[8] << 8 + bdata[9]
    
    return ret
# -----------------------------------------------------------------------------
# decode RPWI header
# -----------------------------------------------------------------------------
def get_hdr_rpw(bdata):
    ret = struct()
    ret.sid       =  bdata[0]
    ret.rpwi_time =  bdata[1] << 24 + bdata[2] << 16 + bdata[3] << 8 + bdata[4]
    ret.seq_cnt   =  bdata[5] << 8 + bdata[6]
    ret.aux_len   =  bdata[7]
    
    # HF software version
    if ret.aux_len == 4:
        ret.sw_ver = 1
    elif ret.aux_len == 16:
        ret.sw_ver = 2
    else:
        ret.sw_ver = -1        
    
    return ret
# -----------------------------------------------------------------------------
# decode AUX field
# -----------------------------------------------------------------------------
def get_aux(bdata, sid, ver):
    ret = struct()

    if ver == 1:
        ret.hf_hdr_len = 24
    else:
        ret.hf_hdr_len = ((bdata[0] & 0xf0) >> 4) * 4
    
    if sid == 0x42:
        # HF raw data
        # to be added
        pass
    elif sid == 0x43:
        # radio-full mode
        # to be added
        pass
    elif sid == 0x44:
        # radio-burst mode (survey)
        # to be added
        pass
    elif sid == 0x74:
        # radio-burst mode (rich)
        # to be added
        pass
    elif sid == 0x45:
        # PSSR1 mode (survey)
        # to be added
        pass
    elif sid == 0x75:
        # PSSR1 mode (rich)
        # to be added
        pass
    elif sid == 0x46:
        # PSSR2 mode (survey)
        # to be added
        pass
    elif sid == 0x76:
        # PSSR2 mode (rich)
        # to be added
        pass
    elif sid == 0x47:
        # PSSR3 mode (survey)
        # to be added
        pass
    elif sid == 0x77:
        # PSSR3 mode (rich)
        # to be added
        pass
    
    return ret
# -----------------------------------------------------------------------------
# decode HF header
# -----------------------------------------------------------------------------
def get_hdr_hf(bdata, ver):
    ret = struct()

    # to be added
    
    return ret
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# get one HF packet
# -----------------------------------------------------------------------------
def get_one_packet(fin):
    
    ret = struct()
    ret.eof = 0
    
    # initialize data buffer
    hf_buff = []
    hf_sz = 0

    
    while True:
        
        #----------------------------------------------------------
        # raed primary header
        #----------------------------------------------------------
        buff = fin.read(6)
        if not buff:
            ret.eof = 1
            break
        st_hdr_pri = get_hdr_pri(buff)

        #print(format(st_hdr_pri.pid, '02x'),format(st_hdr_pri.pcat, '02x'))

        #----------------------------------------------------------
        # read data field header
        #----------------------------------------------------------
        buff = fin.read(10)
        if not buff:
            ret.eof = 1
            break
        st_hdr_sec = get_hdr_sec(buff)

        # check HF science data or not
        if (st_hdr_pri.pid != 0x4d) or (st_hdr_sec.ser_type != 0xcc):
            # skip remaining data
            sz = st_hdr_pri.pkt_len + 1 - 10;
            buff = fin.read(sz)
            if not buff:
                ret.eof = 1
                break
            continue

        #----------------------------------------------------------
        # read RPWI header
        #----------------------------------------------------------
        buff = fin.read(8)
        if not buff:
            ret.eof = 1
            break
        st_hdr_rpw = get_hdr_rpw(buff)
        
        # size of HF tlm
        # (20Byte = sec header(10Byte) + rpwi header(8Byte) + crc(2Byte))
        sz = st_hdr_pri.pkt_len + 1 - 20;

        #print(st_hdr_pri.seq_flg, st_hdr_pri.seq_cnt)

        #----------------------------------------------------------
        # read AUX field and HF header if first & single packet 
        # sequence flag (0: conitnue, 1: first, 2: last, 3: single)
        #----------------------------------------------------------
        if st_hdr_pri.seq_flg == 1 or st_hdr_pri.seq_flg == 3:
            #------------------------------------------------------
            # read AUX field
            #------------------------------------------------------
            buff = fin.read(st_hdr_rpw.aux_len)
            if not buff:
                ret.eof = 1
                break
            st_aux = get_aux(buff, st_hdr_rpw.sid, st_hdr_rpw.sw_ver)

            #------------------------------------------------------
            # read HF header
            #------------------------------------------------------
            buff = fin.read(st_aux.hf_hdr_len)
            if not buff:
                ret.eof = 1
                break
            st_hdr_hf = get_hdr_hf(buff, st_hdr_rpw.sw_ver)

            # update size of HF tlm
            sz = sz - st_hdr_rpw.aux_len - st_aux.hf_hdr_len;
            
        # read science data
        buff = fin.read(sz)
        hf_buff.extend(buff)
        hf_sz += sz

        # read CRC
        fin.read(2)

        if st_hdr_pri.seq_flg == 2 or st_hdr_pri.seq_flg == 3:
            #print(hf_sz)
            break


    if ((ret.eof == 1) and (hf_sz == 0)):
        return 0, 0, 0, 0, 0, ret, 0, 0
    else:
        return st_hdr_pri, st_hdr_sec, st_hdr_rpw, st_aux, st_hdr_hf, ret, hf_buff, hf_sz
