__all__ = ['gmrt_raw_toguppi']
class GUPPIINJ:
    def __init__(self, guppifile) -> None:
        self.header = self.header_dict()
        self.guppifile = guppifile
        
    # def bbinj(self,d):# samples_per_frame=960, pktsize=1024,npol=2, nchan=4):
    #     hdr = {k: self.header[k] for k in self.header if self.header[k]}
    #     if 'TBIN' in hdr.keys():
    #         fg = guppi.open(self.guppifile,'ws',tbin=hdr['TBIN'],
    #                         #samples_per_frame=samples_per_frame, pktsize=pktsize,
    #                         #npol=npol, nchan=nchan,
    #                         **hdr )
    #         fg.write(d)
    #         fg.close()
    #     else:
    #         raise Exception(f'Required: please specify TBIN')
    #     return fg.header0
    # def wraw(self , braw):
    #     fraw = guppi.open(self.guppifile, 'ws', tbin=self.header.TBIN)
    #     fraw.fh_raw = braw
    #     fraw.close()

    @classmethod
    def header_dict(cls, par=None):
        cls._header = Header()
        _dict = cls._header.__dict__
        att = AttrDict()
        att.update(_dict)
        if par in _dict:
            return _dict[par]
        if par is None :
            return att
        elif par == '*':
            return _dict
        elif par == 'v':
            return _dict.values()
        elif par == 'k':
            return _dict.keys()
        else:
            return "'{}' is not a valid header parameter. please choose one from {} or use any of '*' 'v' 'k' ".format(par, _dict.keys())

class Header(GUPPIINJ):
    def __init__(self) -> None:
        self.__dict__ = {
            'BACKEND' : 'GUPPI   ',
            'TELESCOP':'',
            'OBSERVER':'',
            'PROJID'  :'',
            'FRONTEND':'',
            'NRCVR'   :'',
            'FD_POLN' :'',
            'BMAJ'    :'',
            'BMIN'    :'',
            'SRC_NAME':'',
            'TRK_MODE':'',
            'RA_STR'  :'',
            'RA'      :'',
            'DEC_STR' :'',
            'DEC'     :'',
            'LST'     :'',
            'AZ'      :'',
            'ZA'      :'',
            'DAQCTRL' :'',
            'DAQPULSE':'',
            'DAQSTATE':'',
            'NBITS'   :'',
            'OFFSET0' :'',
            'OFFSET1' :'',
            'OFFSET2' :'',
            'OFFSET3' :'',
            'BANKNAM' :'',
            'TFOLD'   :'',
            'DS_FREQ' :'',
            'DS_TIME' :'',
            'FFTLEN'  :'',
            'CHAN_BW' :'',
            'BANDNUM' :'',
            'NBIN'    :'',
            'OBSNCHAN':'',
            'SCALE0'  :'',
            'SCALE1'  :'',
            'DATAHOST':'',
            'SCALE3'  :'',
            'NPOL'    :'',
            'POL_TYPE':'',
            'BANKNUM' :'',
            'DATAPORT':'',
            'ONLY_I'  :'',
            'CAL_DCYC':'',
            'DIRECTIO':'',
            'BLOCSIZE':'',
            'ACC_LEN' :'',
            'CAL_MODE':'',
            'OVERLAP' :'',
            'OBS_MODE':'',
            'CAL_FREQ':'',
            'DATADIR' :'',
            'OBSFREQ' :'',
            'PFB_OVER':'',
            'SCANLEN' :'',
            'PARFILE' :'',
            'OBSBW'   :'',
            'SCALE2'  :'',
            'BINDHOST':'',
            'PKTFMT'  :'',
            'TBIN'    :'',
            'BASE_BW' :'',
            'CHAN_DM' :'',
            'SCAN'    :'',
            'STT_SMJD':'',
            'STT_IMJD':'',
            'STTVALID':'',
            'NETSTAT' :'',
            'DISKSTAT':'',
            'PKTIDX'  :'',
            'DROPAVG' :'',
            'DROPTOT' :'',
            'DROPBLK' :'',
            'PKTSTOP' :'',
            'NETBUFST':'',
            'STT_OFFS':'',
            'SCANREM' :'',
            'PKTSIZE' :'',
            'NPKT'    :'',
            'NDROP'   :''
        }
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        
