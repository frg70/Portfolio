import pandas as pd 
import re 
import numpy as np 
class SoftSkill():
  def SFENSoftSkills(self,ProfileContent):
    ProfileList = []
    for i in ProfileContent:
      SfEngineer = re.findall('software engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
      MLEngineer = re.findall('machine learning engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
      CSExpert = re.findall('security expert', str(i), flags=re.IGNORECASE|re.MULTILINE)
      DataScientist = re.findall('data scientist', str(i), flags=re.IGNORECASE)
      Category = list(set(SfEngineer + MLEngineer + CSExpert + DataScientist))
      if ('Machine Learning Engineer' or 'machine learning engineer') in Category:
          Category = 2 
      elif ('Security Expert' or 'security expert') in Category:
          Category = 3
      elif ('Data Scientist' or 'data scientist') in Category:
          Category = 4
      elif ('Software Engineer' or 'software engineer') in Category:
          Category = 1
      else:
          Category = np.NaN
      if Category != 1:
          pass 
      else:
        job =  re.findall("actualidad", str(i) , flags= re.MULTILINE)
        if "actualidad" in job:
            job = 1 
        else:
            job = 0
        sales = re.findall('Sale+|Customer service', str(i), flags=re.MULTILINE)
        if sales != []:
          sales = 1
        else:
          sales = 0
        Teamwork = re.findall('team+|collaboration', str(i), flags= re.MULTILINE)
        if Teamwork != []:
          Teamwork = 1
        else:
          Teamwork = 0
        Adaptation = re.findall('adaptation+', str(i), flags=re.MULTILINE|re.IGNORECASE)
        if Adaptation != []:
          Adaptation = 1
        else: 
          Adaptation = 0
        Responsability = re.findall('responsible|diligent|formal', str(i), flags= re.MULTILINE)
        if Responsability != []:
          Responsability = 1
        else:
          Responsability = 0
        Proactive = re.findall('proactive', str(i), flags= re.MULTILINE|re.IGNORECASE)
        if Proactive != []:
          Proactive = 1
        else:
          Proactive = 0
        Effort = re.findall('effort+|hustle', str(i), flags= re.MULTILINE|re.IGNORECASE)
        if Effort != []:
          Effort = 1
        else:
          Effort = 0
        Creative = re.findall('creative|creativity', str(i), flags= re.MULTILINE|re.IGNORECASE)
        if Creative != []:
          Creative = 1
        else:
          Creative = 0
        Leadership = re.findall('leadership|leader', str(i), flags= re.MULTILINE|re.IGNORECASE)
        if Leadership != []:
          Leadership = 1
        else:
          Leadership = 0
        ProjectManagement = re.findall('project management', str(i), flags= re.MULTILINE)
        if ProjectManagement != []:
          ProjectManagement = 1
        else:
          ProjectManagement = 0
        Passionate = re.findall('passionate|passion', str(i), flags= re.MULTILINE|re.IGNORECASE)
        if Passionate != []:
          Passionate = 1
        else:
          Passionate = 0
        ProblemSolving = re.findall('solve|solving|problem solving|resolution', str(i), flags=re.MULTILINE)
        if ProblemSolving != []:
          ProblemSolving = 1
        else:
          ProblemSolving = 0
        LearningAbilities = re.findall('learning abilities|willing to learn|fast learner', str(i), flags=re.MULTILINE)
        if LearningAbilities != []:
          LearningAbilities = 1
        else: 
          LearningAbilities = 0
        Curious = re.findall('to learn|curious|seeking for challenges|learning oriented', str(i), flags= re.MULTILINE)
        if Curious != []:
          Curious = 1
        else:
          Curious = 0
        Formality = re.findall("formality|serious", str(i), flags= re.IGNORECASE)
        if Formality != []:
          Formality = 1
        else:
          Formality = 0 
        #Recordar hacer matiz si oral o escrita, cuando se trabaje con red 
        CommunicationSkills = re.findall('communication|presentation skills', str(i), flags=re.MULTILINE)
        if CommunicationSkills != []:
          CommunicationSkills = 1
        else:
          CommunicationSkills = 0
        Innovation = re.findall('innovation|innovate', str(i), flags=re.MULTILINE)
        if Innovation != []:
          Innovation = 1
        else:
          Innovation = 0
        GeneralProfile = {'Sales': sales, 'Teamwork': Teamwork,'Adaptation': Adaptation,'Responsability': Responsability,'Proactive': Proactive,'Effort': Effort,'Creative': Creative,'Leadership': Leadership,'Project Management': ProjectManagement,'Passionate': Passionate,'Problem Solving': ProblemSolving,'Curious': Curious,'Formality': Formality,'Communication skills': CommunicationSkills, 'Innovation': Innovation, 'Job': job}
        ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def MLESoftSkills(self,ProfileContent):
    ProfileList = []
    for i in ProfileContent:
      SfEngineer = re.findall('software engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
      MLEngineer = re.findall('machine learning engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
      CSExpert = re.findall('security expert', str(i), flags=re.IGNORECASE|re.MULTILINE)
      DataScientist = re.findall('data scientist', str(i), flags=re.IGNORECASE)
      Category = list(set(SfEngineer + MLEngineer + CSExpert + DataScientist))
      if ('Machine Learning Engineer' or 'machine learning engineer') in Category:
          Category = 2 
      elif ('Security Expert' or 'security expert') in Category:
          Category = 3
      elif ('Data Scientist' or 'data scientist') in Category:
          Category = 4
      elif ('Software Engineer' or 'software engineer') in Category:
          Category = 1
      else:
          Category = np.NaN
      if Category != 2:
          pass 
      else:
          job =  re.findall("actualidad", str(i) , flags= re.MULTILINE)
          if "actualidad" in job:
              job = 1 
          else:
              job = 0
          AnalythicalSkills = re.findall('analythical thinking', str(i), flags=re.MULTILINE)
          if AnalythicalSkills != []:
            AnalythicalSkills = 1
          else:
            AnalythicalSkills = 0
          PublicSpeaking = re.findall('public speaking|presenting|presentation', str(i), flags=re.MULTILINE)
          if PublicSpeaking != []:
            PublicSpeaking = 1
          else:
            PublicSpeaking = 0
          Teamwork = re.findall('team+|collaboration', str(i), flags= re.MULTILINE)
          if Teamwork != []:
            Teamwork = 1
          else:
            Teamwork = 0
          CommunicationSkills = re.findall('communication|presentation skills', str(i), flags=re.MULTILINE)
          if CommunicationSkills != []:
            CommunicationSkills = 1
          else:
            CommunicationSkills = 0
          PossitiveAttitude = re.findall('possitive attitude', str(i), flags=re.MULTILINE)
          if PossitiveAttitude != []:
            PossitiveAttitude = 1
          else:
            PossitiveAttitude = 0
          Leadership = re.findall('leadership|leader', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Leadership != []:
            Leadership = 1
          else:
            Leadership = 0
          ProblemSolving = re.findall('solve|solving|problem solving|resolution', str(i), flags=re.MULTILINE)
          if ProblemSolving != []:
            ProblemSolving = 1
          else:
            ProblemSolving = 0
          Enthusiasm = re.findall('enthusiasm', str(i), flags=re.MULTILINE)
          if Enthusiasm != []:
            Enthusiasm = 1
          else: 
            Enthusiasm = 0
          LearningAbilities = re.findall('learning abilities|willing to learn|fast learner', str(i), flags=re.MULTILINE)
          if LearningAbilities != []:
            LearningAbilities = 1
          else: 
            LearningAbilities = 0
          Curious = re.findall('curious|courius', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Curious != []:
            Curious = 1
          else:
            Curious = 0
          Creative = re.findall('creative|creativity', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Creative != []:
            Creative = 1
          else:
            Creative = 0
          Persevering = re.findall('persevering|hustle|persevere', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Persevering != []:
            Persevering = 1
          else:
            Persevering = 0
          Initiative = re.findall('initiative|propose', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Initiative != []:
            Initiative = 1
          else:
            Initiative = 0
          Proactivity = re.findall('proactive|proactivity', str(i), flags=re.MULTILINE|re.IGNORECASE)
          if Proactivity != []:
            Proactivity = 1
          else: 
            Proactivity = 0
          Negotiation = re.findall('negotiate|negotiation', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Negotiation != []:
            Negotiation = 1
          else:
            Negotiation = 0
          Responsability = re.findall('responsible|diligent|formal', str(i), flags= re.MULTILINE)
          ProjectManagement = re.findall('project management', str(i), flags= re.MULTILINE)
          if ProjectManagement != []:
            ProjectManagement = 1
          else:
            ProjectManagement = 0
          GeneralProfile = {'Analythical Skills': AnalythicalSkills,'Public presentations': PublicSpeaking, 'Teamwork': Teamwork,'Communication skills': CommunicationSkills,'Possitive attitude': PossitiveAttitude,'Leadership': Leadership,'Problem solving': ProblemSolving,'Enthusiasm': Enthusiasm,'Learning abilities': LearningAbilities,'Curious': Curious,'Creative': Creative,'Persevering': Persevering,'Initiative': Initiative,'Proactivity': Proactivity,'Negotiation': Negotiation,'Project Management': ProjectManagement}
          ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def CSESoftSkills(self,ProfileContent):
    ProfileList = []
    for i in ProfileContent:
        SfEngineer = re.findall('software engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
        MLEngineer = re.findall('machine learning engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
        CSExpert = re.findall('security expert', str(i), flags=re.IGNORECASE|re.MULTILINE)
        DataScientist = re.findall('data scientist', str(i), flags=re.IGNORECASE)
        Category = list(set(SfEngineer + MLEngineer + CSExpert + DataScientist))
        if ('Machine Learning Engineer' or 'machine learning engineer') in Category:
          Category = 2 
        elif ('Security Expert' or 'security expert') in Category:
          Category = 3
        elif ('Data Scientist' or 'data scientist') in Category:
          Category = 4
        elif ('Software Engineer' or 'software engineer') in Category:
          Category = 1
        else:
          Category = np.NaN
        if Category != 3:
          pass 
        else:
          job =  re.findall("actualidad", str(i) , flags= re.MULTILINE)
          if "actualidad" in job:
              job = 1 
          else:
              job = 0
          ProjectManagement = re.findall('project management', str(i), flags= re.MULTILINE)
          if ProjectManagement != []:
            ProjectManagement = 1
          else:
            ProjectManagement = 0
          CustomerService = re.findall('IT support|Customer service', str(i), flags=re.MULTILINE)
          if CustomerService != []:
            CustomerService = 1
          else:
            CustomerService = 0
          sales = re.findall('Sale+|Customer service', str(i), flags=re.MULTILINE)
          if sales != []:
            sales = 1
          else:
            sales = 0
          Teamwork = re.findall('team+|collaboration', str(i), flags= re.MULTILINE)
          if Teamwork != []:
            Teamwork = 1
          else:
            Teamwork = 0
          PublicSpeaking = re.findall('public speaking|presenting|presentation', str(i), flags=re.MULTILINE)
          if PublicSpeaking != []:
            PublicSpeaking = 1
          else:
            PublicSpeaking = 0
          CommunicationSkills = re.findall('communication|presentation skills', str(i), flags=re.MULTILINE)
          if CommunicationSkills != []:
            CommunicationSkills = 1
          else:
            CommunicationSkills = 0
          InterpersonalSkills = re.findall('sociable|outgoing|interpersonal skills', str(i), flags=re.MULTILINE)
          if InterpersonalSkills != []:
            InterpersonalSkills = 1
          else:
            InterpersonalSkills = 0
          AnalythicalSkills = re.findall('analythical thinking', str(i), flags=re.MULTILINE)
          if AnalythicalSkills != []:
            AnalythicalSkills = 1
          else:
            AnalythicalSkills = 0
          Leadership = re.findall('leadership|leader', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Leadership != []:
            Leadership = 1
          else:
            Leadership = 0
          Responsability = re.findall('responsible|diligent|formal', str(i), flags= re.MULTILINE)
          if Responsability != []:
            Responsability = 1
          else:
            Responsability = 0
          Dedication = re.findall('responsible|diligent|dedicate|dedication', str(i), flags= re.MULTILINE)
          if Dedication != []:
            Dedication = 1
          else:
            Dedication = 0
          ProblemSolving = re.findall('solve|solving|problem solving|resolution', str(i), flags=re.MULTILINE)
          if ProblemSolving != []:
            ProblemSolving = 1
          else:
            ProblemSolving = 0
          LearningAbilities = re.findall('learning abilities|willing to learn|fast learner', str(i), flags=re.MULTILINE)
          if LearningAbilities != []:
            LearningAbilities = 1
          else: 
            LearningAbilities = 0
          Negotiation = re.findall('negotiate|negotiation', str(i), flags=re.MULTILINE)
          if Negotiation != []:
            Negotiation = 1
          else: 
            Negotiation = 0
          GeneralProfile = {'Project management': ProjectManagement, 'Customer service': CustomerService,'Sales': sales,'Teamwork': Teamwork,'Public speaking': PublicSpeaking,'Communication skills': CommunicationSkills,'Interpersonal skills': InterpersonalSkills,'Analythcisl skills|analytical thinking': AnalythicalSkills, 'Leadership': Leadership, 'Responsability': Responsability, 'Dedication': Dedication,'Problem Solving': ProblemSolving,'Learning abilites': LearningAbilities,'Negotiation': Negotiation, 'Job': job}
          ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def DSCSoftSkills(self,ProfileContent):
    ProfileList = []
    for i in ProfileContent:
        SfEngineer = re.findall('software engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
        MLEngineer = re.findall('machine learning engineer', str(i), flags= re.MULTILINE|re.IGNORECASE)
        CSExpert = re.findall('security expert', str(i), flags=re.IGNORECASE|re.MULTILINE)
        DataScientist = re.findall('data scientist', str(i), flags=re.IGNORECASE)
        Category = list(set(SfEngineer + MLEngineer + CSExpert + DataScientist))
        if ('Machine Learning Engineer' or 'machine learning engineer') in Category:
          Category = 2 
        elif ('Security Expert' or 'security expert') in Category:
          Category = 3
        elif ('Data Scientist' or 'data scientist') in Category:
          Category = 4
        elif ('Software Engineer' or 'software engineer') in Category:
          Category = 1
        else:
          Category = np.NaN
        if Category != 4:
          pass 
        else:
          job =  re.findall("actualidad", str(i) , flags= re.MULTILINE)
          if "actualidad" in job:
              job = 1 
          else:
              job = 0
          Openminded = re.findall('open minded', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Openminded != []:
            Openminded = 1
          else:
            Openminded = 0
          Transparent= re.findall('transparent', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Transparent != []:
            Transparent = 1
          else:
            Transparent = 0
          CommunicationSkills = re.findall('communication|presentation skills', str(i), flags=re.MULTILINE)
          if CommunicationSkills != []:
            CommunicationSkills = 1
          else:
            CommunicationSkills = 0
          Leadership = re.findall('leadership|leader', str(i), flags= re.MULTILINE|re.IGNORECASE)
          if Leadership != []:
            Leadership = 1
          else:
            Leadership = 0
          ProjectManagement = re.findall('project management', str(i), flags= re.MULTILINE)
          if ProjectManagement != []:
            ProjectManagement = 1
          else:
            ProjectManagement = 0
          Adaptation = re.findall('adaptation|open to change', str(i), flags=re.MULTILINE)
          if Adaptation != []:
            Adaptation = 1
          else:
            Adaptation = 0
          Meticulousness = re.findall('Meticulousness', str(i), flags=re.MULTILINE)
          if Meticulousness != []:
            Meticulousness = 1
          else:
            Meticulousness = 0
          Teamwork = re.findall('team+|collaboration', str(i), flags= re.MULTILINE)
          if Teamwork != []:
            Teamwork = 1
          else:
            Teamwork = 0
          ProblemSolving = re.findall('solve|solving|problem solving|resolution', str(i), flags=re.MULTILINE)
          if ProblemSolving != []:
            ProblemSolving = 1
          else:
            ProblemSolving = 0
          LearningAbilities = re.findall('learning abilities|willing to learn|fast learner', str(i), flags=re.MULTILINE)
          if LearningAbilities != []:
            LearningAbilities = 1
          else: 
            LearningAbilities = 0
          CustomerService = re.findall('IT support|Customer service', str(i), flags=re.MULTILINE)
          if CustomerService != []:
            CustomerService = 1
          else:
            CustomerService = 0
          DecisionMaking = re.findall('decision making', str(i), flags=re.MULTILINE)
          if DecisionMaking != []:
            DecisionMaking = 1
          else:
            DecisionMaking = 0
          GeneralProfile = {'Open minded': Openminded, 'Transparent': Transparent,'Communicative skills': CommunicationSkills,'Leadership': Leadership,'Teamwork': Teamwork,'Project management': ProjectManagement,'Adaptation': Adaptation,'Meticulousness': Meticulousness,'Team work': Teamwork,'Problem Solving': ProblemSolving,'Learning abilites': LearningAbilities,'Customer Service': CustomerService,'Decision Making': DecisionMaking, 'Job': job}
          ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data