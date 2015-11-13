import numpy as np

def initial_barrow(self):
    self.Init_Wet_NPG = np.sum(self.ATTM_Wet_NPG)
    self.Init_Wet_LCP = np.sum(self.ATTM_Wet_LCP)
    self.Init_Wet_CLC = np.sum(self.ATTM_Wet_CLC)
    self.Init_Wet_FCP = np.sum(self.ATTM_Wet_FCP)
    self.Init_Wet_HCP = np.sum(self.ATTM_Wet_HCP)
    self.Init_Ponds   = np.sum(self.ATTM_Ponds)
    self.Init_Lakes   = np.sum(self.ATTM_Lakes)

def initial_tanana(self):
    self.Init_TF_OB     = np.sum(self.ATTM_TF_OB)
    self.Init_TF_YB     = np.sum(self.ATTM_TF_YB)
    self.Init_TF_OF     = np.sum(self.ATTM_TF_OF)
    self.Init_TF_YF     = np.sum(self.ATTM_TF_YF)
    self.Init_TF_Dec_PP = np.sum(self.ATTM_TF_Dec_PP)
    self.Init_TF_Con_PP = np.sum(self.ATTM_TF_Con_PP)
    self.Init_TF_TL     = np.sum(self.ATTM_TF_TL)

def final_barrow(self):
    self.Final_Wet_NPG = np.sum(self.ATTM_Wet_NPG)
    self.Final_Wet_LCP = np.sum(self.ATTM_Wet_LCP)
    self.Final_Wet_CLC = np.sum(self.ATTM_Wet_CLC)
    self.Final_Wet_FCP = np.sum(self.ATTM_Wet_FCP)
    self.Final_Wet_HCP = np.sum(self.ATTM_Wet_HCP)
    self.Final_Ponds   = np.sum(self.ATTM_Ponds)
    self.Final_Lakes   = np.sum(self.ATTM_Lakes)


def final_tanana(self):
    self.Final_TF_OB     = np.sum(self.ATTM_TF_OB)
    self.Final_TF_YB     = np.sum(self.ATTM_TF_YB)
    self.Final_TF_OF     = np.sum(self.ATTM_TF_OF)
    self.Final_TF_YF     = np.sum(self.ATTM_TF_YF)
    self.Final_TF_Dec_PP = np.sum(self.ATTM_TF_Dec_PP)
    self.Final_TF_Con_PP = np.sum(self.ATTM_TF_Con_PP)
    self.Final_TF_TL     = np.sum(self.ATTM_TF_TL)
