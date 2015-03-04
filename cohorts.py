import numpy as np

def initial(self):
    self.Init_Wet_NPG = np.sum(self.ATTM_Wet_NPG)
    self.Init_Wet_LCP = np.sum(self.ATTM_Wet_LCP)
    self.Init_Wet_CLC = np.sum(self.ATTM_Wet_CLC)
    self.Init_Wet_FCP = np.sum(self.ATTM_Wet_FCP)
    self.Init_Wet_HCP = np.sum(self.ATTM_Wet_HCP)
    self.Init_Ponds   = np.sum(self.ATTM_Ponds)
    self.Init_Lakes   = np.sum(self.ATTM_Lakes)

def final(self):
    self.Final_Wet_NPG = np.sum(self.ATTM_Wet_NPG)
    self.Final_Wet_LCP = np.sum(self.ATTM_Wet_LCP)
    self.Final_Wet_CLC = np.sum(self.ATTM_Wet_CLC)
    self.Final_Wet_FCP = np.sum(self.ATTM_Wet_FCP)
    self.Final_Wet_HCP = np.sum(self.ATTM_Wet_HCP)
    self.Final_Ponds   = np.sum(self.ATTM_Ponds)
    self.Final_Lakes   = np.sum(self.ATTM_Lakes)
