import pandas as pd 
import re 
import numpy as np 
class GeneralProfiles():  
  def GeneralProfileSFEN(self,ProfileContent):
    ProfileList = []
    time1 = 0 
    time2 = 0 
    total = 0 
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
            Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", str(i) , flags= re.MULTILINE)
            try:
              Experience = Experience[0]
              exp = re.findall('Software engineer.{135,150}|Software Development Engineer.{135,150}|Software developer.{135,150}|Web developer.{135,150}|Java developer.{135,150}', Experience, flags = re.IGNORECASE)
              exp = ''.join(exp)
              months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
              months = ''.join(months)
              months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
              years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
              years = ''.join(years)
              years = re.findall('\d',years)
              for year in years:
                  yearsD = int(year)
                  if yearsD == 1:
                      yearsD = 12
                  if yearsD == 2:
                      yearsD = 24
                  time2 += int(yearsD)
              for time in months:
                  time1 += int(time)
              total = time1 + time2 
            except: 
              total = np.nan
            if total != np.nan:
                experience = 1
            else: 
                experience = 0
            #Note it still needs adjustment when we have various categories
            EducationProfile = re.findall('Computer and Information Systems|Computer Science|Information Science|Telecommunications| Mechatronics Engineering|Electrical and Electronics|Software Engineering', str(i), flags= re.MULTILINE|re.IGNORECASE)
            EducationProfile = list(set(EducationProfile))
            if EducationProfile != []:
              EducationProfile = 1
            else:
              EducationProfile = 0 
            English = 1
            Languages = re.findall('Afrikaans|Albanian|Arabic|Armenian|Azerbaijani|Belarusian|Bengali|Bosnian|Bulgarian|Chinese|Croatian|Czech|Danish|Dutch|Estonian|Fijian|Finnish|French|Scottish|Georgian|German|Greek|Hebrew|Hindi|Hungarian|Icelandic|Indonesian|Irish|Italian|Japanese|Kazakh|Korea|Kurdish|Lao|Latvian|Lithuanian|Macedonian|Malay|Moldavian|Mongolian|Ndonga|Nepali|Norwegian|Persian|Polish|Portuguese|Romanian|Russian|Serbian|Slovak|Slovenian|Somali|Spanish|Swahili|Swati|Swedish|Turkish|Turkmen|Ukrainian|Urdu|Uzbek|Vietnamese|Welsh|Zulu', str(i), flags= re.MULTILINE)
            Languages = list(set(Languages))
            if len(Languages) < 1:
              SecondLanguage = 0
              ThirdLanguage = 0
            elif len(Languages) == 1:
              SecondLanguage = 1
              ThirdLanguage = 0
            else:
              SecondLanguage = 1
              ThirdLanguage = 1
            PHD = re.findall('PHD', str(i), flags= re.IGNORECASE|re.MULTILINE)
            Masters = re.findall('Masters', str(i), flags=re.IGNORECASE|re.MULTILINE)
            Bachelors = re.findall('Bachelor', str(i), flags=re.IGNORECASE)
            EducationLevel = list(set(PHD+ Masters+ Bachelors))
            if PHD != []:
              EducationLevel = 3
            elif Masters != []:
              EducationLevel = 2
            elif Bachelors != []:
              EducationLevel = 1
            else:
              EducationLevel = 0
            #Nota falta agregar C++
            GeneralPurposeProgrammingSkills = re.findall('HTML|Python|Java| C |C#|JavaScript|Java|Ruby|PHP|Swift|Go|Kotlin|Rust|Scala|Dart|Perl|MatLab| R ', str(i), flags=re.MULTILINE)
            GeneralPurposeProgrammingSkills = list(set(GeneralPurposeProgrammingSkills))
            if GeneralPurposeProgrammingSkills != []:
              GeneralPurposeProgrammingSkills = 1
            else:
              GeneralPurposeProgrammingSkills = 0
            BackendSkills = re.findall('database|Oracle|PHP|backend|REST|MySQL|MongoDB|SQLServer|Apache|Django|Larval|Linux|API', str(i), flags=re.MULTILINE)
            BackendSkills = list(set(BackendSkills))
            if BackendSkills != []:
              BackendSkills = 1
            else:
              BackendSkills = 0
            FrontendSkills = re.findall('CSS+|HTML|JavaScript|JQuery|Angular|React|TypeScript|Git|Spring|DOM|Node', str(i), flags=re.MULTILINE)
            FrontendSkills = list(set(FrontendSkills))
            if FrontendSkills != []:
              FrontendSkills = 1
            else:
              FrontendSkills = 0
            VersionControl = re.findall('Git|GitHub', str(i), flags=re.MULTILINE|re.IGNORECASE) 
            VersionControl = list(set(VersionControl))
            if VersionControl != []:
              VersionControl = 1
            else:
              VersionControl = 0
            SoftwareDevelopment = re.findall('DevOps|Software deveolpment|Apps', str(i), flags=re.MULTILINE|re.IGNORECASE)
            SoftwareDevelopment = list(set(SoftwareDevelopment))
            if SoftwareDevelopment != []:
              SoftwareDevelopment = 1 
            else:
              SoftwareDevelopment = 0 
            GoodPractices = re.findall('Scrum|agile|Debugging|good practices', str(i), flags=re.MULTILINE| re.IGNORECASE)
            GoodPractices = list(set(GoodPractices))
            if GoodPractices != []:
              GoodPractices = 1
            else:
              GoodPractices = 0 
            MicrosoftOffice = re.findall('Excel|Microsoft Office|Office|PowerPoint', str(i), flags=re.MULTILINE)
            if MicrosoftOffice != []:
              MicrosoftOffice = 1 
            else:
              MicrosoftOffice = 0
            IoT = re.findall('IoT|Raspberry', str(i), flags=re.MULTILINE)
            if IoT != []:
              IoT = 1 
            else:
              IoT = 0 
            NetworkManagement = re.findall('network|cisco|firewall|security', str(i), flags=re.MULTILINE)
            if NetworkManagement != []:
              NetworkManagement = 1
            else:
              NetworkManagement = 0
            DataModelling = re.findall('data modelling', str(i), flags=re.MULTILINE)
            if DataModelling != []:
              DataModelling = 1
            else:
              DataModelling = 0
            DatabaseDesign = re.findall('database design', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DatabaseDesign != []:
              DatabaseDesign = 1
            else:
              DatabaseDesign = 0
            EmbeddedSystems = re.findall('embedeed systems|arduino|embedded', str(i), flags=re.MULTILINE)
            if EmbeddedSystems != []:
              EmbeddedSystems = 1
            else:
              EmbeddedSystems = 0
            APIsDevelopment = re.findall('API', str(i), flags=re.MULTILINE)
            if APIsDevelopment != []:
              APIsDevelopment = 1
            else:
              APIsDevelopment = 0
            BugManagement= re.findall('bug|Bug management|debugging', str(i), flags=re.IGNORECASE|re.MULTILINE)
            if BugManagement != []:
              BugManagement = 1
            else:
              BugManagement = 0
            ProcessAutomation = re.findall('automation', str(i), flags=re.MULTILINE)
            if ProcessAutomation != []:
              ProcessAutomation = 1
            else:
              ProcessAutomation = 0
            SolutionRefining = re.findall('solution refining|refinig|refine|adjusting',str(i), flags=re.MULTILINE)
            if SolutionRefining != []:
              SolutionRefining = 1
            else:
              SolutionRefining = 0
            GeneralProfile = {'Category': Category, 'Job': job,'Experience': experience,'Time experience': total,'Education Level': EducationLevel, 'Education profile': EducationProfile,'English': English,'Second Language': SecondLanguage,'Third Language': ThirdLanguage,'General Purpose Programming Skills': GeneralPurposeProgrammingSkills, 'Backend Skills': BackendSkills, 'Frontend Skills': FrontendSkills, 'Version Control': VersionControl, 'Software Development': SoftwareDevelopment, 'Good Practices': GoodPractices, 'Microsoft Office': MicrosoftOffice, 'IoT': IoT, 'Network management': NetworkManagement, 'Data Modelling': DataModelling, 'Database design': DatabaseDesign, 'Embedded system': EmbeddedSystems, 'APIs development': APIsDevelopment, 'Bug management': BugManagement, 'Process automation': ProcessAutomation, 'Solution refining': SolutionRefining}
            ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList) 
    #This the final data 
    return Data
  def GeneralProfileMLE(self,ProfileContent):
    ProfileList = []
    time1 = 0
    time2 = 0
    total = 0
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
            Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", str(i) , flags= re.MULTILINE)
            try:
              Experience = Experience[0]
              exp = re.findall('Machine Learning Engineer.{135,150}|Data Scientist.{135,150}|Data Engineer.{135,150}|AI Engineer.{135,150}', Experience, flags = re.IGNORECASE)
              exp = ''.join(exp)
              months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
              months = ''.join(months)
              months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
              years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
              years = ''.join(years)
              years = re.findall('\d',years)
              for year in years:
                  yearsD = int(year)
                  if yearsD == 1:
                      yearsD = 12
                  if yearsD == 2:
                      yearsD = 24
                  time2 += int(yearsD)
              for time in months:
                  time1 += int(time)
              total = time1 + time2 
            except: 
              total = np.nan
            if total != np.nan:
                experience = 1
            else: 
                experience = 0
            EducationProfile = re.findall('Software Engineering|Data Science|Mathematics degree|Statistics degree|Computer Science|Information and Technology', str(i), flags= re.MULTILINE|re.IGNORECASE)
            EducationProfile = list(set(EducationProfile))
            if EducationProfile != []:
              EducationProfile = 1
            else:
              EducationProfile = 0 
            English = 1
            Languages = re.findall('Afrikaans|Albanian|Arabic|Armenian|Azerbaijani|Belarusian|Bengali|Bosnian|Bulgarian|Chinese|Croatian|Czech|Danish|Dutch|Estonian|Fijian|Finnish|French|Scottish|Georgian|German|Greek|Hebrew|Hindi|Hungarian|Icelandic|Indonesian|Irish|Italian|Japanese|Kazakh|Korea|Kurdish|Lao|Latvian|Lithuanian|Macedonian|Malay|Moldavian|Mongolian|Ndonga|Nepali|Norwegian|Persian|Polish|Portuguese|Romanian|Russian|Serbian|Slovak|Slovenian|Somali|Spanish|Swahili|Swati|Swedish|Turkish|Turkmen|Ukrainian|Urdu|Uzbek|Vietnamese|Welsh|Zulu', str(i), flags= re.MULTILINE)
            Languages = list(set(Languages))
            if len(Languages) < 1:
              SecondLanguage = 0
              ThirdLanguage = 0
            elif len(Languages) == 1:
              SecondLanguage = 1
              ThirdLanguage = 0
            else:
              SecondLanguage = 1
              ThirdLanguage = 1
            #Still needs adjustment 
            EducationLevel = re.findall('Bachelor|Masters|PhD|PHD', str(i), flags= re.MULTILINE)
            if 'PhD' or 'PHD' in EducationLevel:
                EducationLevel = 3
            elif 'Masters' in EducationLevel:
                EducationLevel = 2 
            elif 'Bachelor' in EducationLevel:
                EducationLevel = 1
            else:
                EducationLevel = 0
            #Nota falta agregar C++
            GeneralPurposeProgrammingSkills = re.findall('HTML|Python|Java| C |C#|JavaScript|Java|Ruby|PHP|Swift|Go|Kotlin|Rust|Scala|Dart|Perl|MatLab| R ', str(i), flags=re.MULTILINE)
            GeneralPurposeProgrammingSkills = list(set(GeneralPurposeProgrammingSkills))
            if GeneralPurposeProgrammingSkills != []:
              GeneralPurposeProgrammingSkills = 1
            else:
              GeneralPurposeProgrammingSkills = 0
            MachineLearningProgramming = re.findall('pipeplines|Pyspark|Apache Spark|Apache Sqoop|Hadoop|Flask|IBM Watson|ONNX|Apache|Django|Larval|Linux|API', str(i), flags=re.MULTILINE)
            MachineLearningProgramming = list(set(MachineLearningProgramming))
            if MachineLearningProgramming != []:
              MachineLearningProgramming = 1
            else:
              MachineLearningProgramming = 0
            SoftwareLibrariesforML = re.findall('pandas|keras|sklearn|tensorflow|seaborn|numpy|sympy|armadillo|fann|matplotlib|mlpack|nltk|opennn|pytorch|scipy|shogun|theano|caffe|torch', str(i), flags=re.MULTILINE|re.IGNORECASE)
            SoftwareLibrariesforML = list(set(SoftwareLibrariesforML))
            if SoftwareLibrariesforML != []:
              SoftwareLibrariesforML = 1
            else:
              SoftwareLibrariesforML = 0
            LaTex = re.findall('latex', str(i), flags=re.MULTILINE|re.IGNORECASE) 
            LaTex = list(set(LaTex))
            if LaTex != []:
              LaTex = 1
            else:
              LaTex = 0
            SoftwareDevelopment = re.findall('DevOps|Software deveolpment|Apps', str(i), flags=re.MULTILINE|re.IGNORECASE)
            SoftwareDevelopment = list(set(SoftwareDevelopment))
            if SoftwareDevelopment != []:
              SoftwareDevelopment = 1 
            else:
              SoftwareDevelopment = 0 
            OperatingSystems = re.findall('Windows|Linux|Operating System', str(i), flags=re.MULTILINE| re.IGNORECASE)
            OperatingSystems = list(set(OperatingSystems))
            if OperatingSystems != []:
              OperatingSystems = 1
            else:
              OperatingSystems = 0 
            MicrosoftOffice = re.findall('Excel|Microsoft Office|Office|PowerPoint', str(i), flags=re.MULTILINE)
            if MicrosoftOffice != []:
              MicrosoftOffice = 1 
            else:
              MicrosoftOffice = 0
            IoT = re.findall('IoT|Raspberry', str(i), flags=re.MULTILINE)
            if IoT != []:
              IoT = 1 
            else:
              IoT = 0 
            DataAnalysis = re.findall('data analysis|analysis data', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DataAnalysis != []:
              DataAnalysis = 1
            else:
              DataAnalysis = 0
            DataStructures = re.findall('data structures|list|tuple|stack|set|map|queue|tree|heap|array|matrix', str(i), flags=re.MULTILINE)
            if DataStructures != []:
              DataStructures = 1
            else:
              DataStructures = 0
            DatabaseManagement = re.findall('database management|MongoDB|Oracle|SQL|MariaDB|Salesforce|PhP', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DatabaseManagement != []:
              DatabaseManagement = 1
            else:
              DatabaseManagement = 0
            EmbeddedSystems = re.findall('embedeed systems|arduino|embedded', str(i), flags=re.MULTILINE)
            if EmbeddedSystems != []:
              EmbeddedSystems = 1
            else:
              EmbeddedSystems = 0
            DataVisualization = re.findall('data visualization|matplotlib|seaborn|Tableau|ChartBlocks|Datawrapper|Power BI', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DataVisualization != []:
              DataVisualization = 1
            else:
              DataVisualization = 0
            SoftwareContainerManager = re.findall('kubernetes|docker|aws|Azure kubernetes', str(i), flags=re.IGNORECASE|re.MULTILINE)
            if SoftwareContainerManager != []:
              SoftwareContainerManager = 1
            else:
              SoftwareContainerManager = 0
            DeepLearningFrameworks = re.findall('Keras|TensorFlow|Torch|Deeplearning4j|CNTK|keras|onnx|mxnet|sonnet', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DeepLearningFrameworks != []:
              DeepLearningFrameworks = 1
            else:
              DeepLearningFrameworks = 0
            Hardware = re.findall('Raspberry|hardware|NVIDIA',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Hardware != []:
              Hardware = 1
            else:
              Hardware = 0
            Cloud = re.findall('Azure|AWS|Google Cloud',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Cloud != []:
              Cloud = 1
            else:
              Cloud = 0
            MachineLearningPlatforms = re.findall('PyTorch|Cuda|noxx|TensorFlow|IBM Watson',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if MachineLearningPlatforms != []:
              MachineLearningPlatforms = 1
            else:
              MachineLearningPlatforms = 0
            NaturalLanguageProcessing = re.findall('NLTK|Word2Vec|Natural language processing|SpaCy|Aylien|MonkeyLearn|NLP|TextBlob|GenSim',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if NaturalLanguageProcessing != []:
              NaturalLanguageProcessing = 1
            else:
              NaturalLanguageProcessing = 0
            ComputerVision = re.findall('OpenCV|VisionAI|Matlab|TensorFlow|Cuda|Theano|Keras|GPUImage|BoofCV|YOLO|scikit-image|SciPy|Pillow|Mahotas|pgmagick|Pycairo',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if ComputerVision != []:
              ComputerVision = 1
            else:
              ComputerVision = 0
            HPC = re.findall('High computing performance|Cuda|NVIDIA',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if HPC != []:
              HPC = 1
            else:
              HPC = 0
            CAD = re.findall('cad|computer aided design',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if CAD != []:
              CAD = 1
            else:
              CAD = 0
            Maintenance = re.findall('maintenance',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Maintenance != []:
              Maintenance = 1
            else:
              Maintenance = 0
            VersionControl = re.findall('Git|GitHub',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if VersionControl != []:
              VersionControl = 1
            else:
              VersionControl = 0
            Mathematics = re.findall('linear algebra|statistics|differential equations|math|calculus',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Mathematics != []:
              Mathematics = 1
            else:
              Mathematics = 0
            LaboratorySkills = re.findall('laboratory skills',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if LaboratorySkills != []:
              LaboratorySkills = 1
            else:
              LaboratorySkills = 0
            Research = re.findall('Research',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Research != []:
              Research = 1
            else:
              Research = 0
            GraphicDesign = re.findall('Corel|graphic design|illustrator',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if GraphicDesign != []:
              GraphicDesign = 1
            else:
              GraphicDesign = 0
            SocialNetworks = re.findall('social networks',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if SocialNetworks != []:
              SocialNetworks = 1
            else:
              SocialNetworks = 0
            ResourceManagement = re.findall('resource management',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if ResourceManagement != []:
              ResourceManagement = 1
            else:
              ResourceManagement = 0
            #Terminar de cambiae el diccionario para guardar las variables correctas 
            GeneralProfile = {'Category': Category, 'Job': job,'Experience': experience,'Time experience': total,'Education Level': EducationLevel,'Education Profile': EducationProfile,'English': English,'Second Language': SecondLanguage,'Third Language': ThirdLanguage,'General Purpose Programming Skills': GeneralPurposeProgrammingSkills, 'Machine Learning programming skills': MachineLearningProgramming, 'Software libraries for programming languages': SoftwareLibrariesforML,'Microsoft Office': MicrosoftOffice, 'LaTex': LaTex, 'Database management': DatabaseManagement,'Data analysis': DataAnalysis,'Data structures': DataStructures,'Data visualization': DataVisualization,'Software development': SoftwareDevelopment,'Software container manager': SoftwareContainerManager,'Deep Learning Frameworks': DeepLearningFrameworks,'Hardware': Hardware,'Cloud': Cloud,'Machine Learning Platforms': MachineLearningPlatforms,'Processing Natural Language': NaturalLanguageProcessing,'Computer vision': ComputerVision,'High Perfomance Computing': HPC,'Computer aided design': CAD,'Maintenance': Maintenance,'Embedded systems': EmbeddedSystems,'IoT':IoT,'Laboratory Skills': LaboratorySkills,'Research': Research,'Resource management':ResourceManagement,'Graphic design': GraphicDesign}
            ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def GeneralProfileCSE(self,ProfileContent):
    ProfileList = []
    time1 = 0
    time2 = 0
    total = 0
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
            Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", str(i) , flags= re.MULTILINE)
            try:
              Experience = Experience[0]
              exp = re.findall('Malware Engineer.{135,150}|Threat Hunter.{135,150}|Digital Forensic Analyst.{135,150}|Malware analyst.{135,150}|Security Engineer.{135,150}', Experience, flags = re.IGNORECASE)
              exp = ''.join(exp)
              months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
              months = ''.join(months)
              months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
              years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
              years = ''.join(years)
              years = re.findall('\d',years)
              for year in years:
                  yearsD = int(year)
                  if yearsD == 1:
                      yearsD = 12
                  if yearsD == 2:
                      yearsD = 24
                  time2 += int(yearsD)
              for time in months:
                  time1 += int(time)
              total = time1 + time2 
            except: 
              total = np.nan
            if total != np.nan:
                experience = 1
            else: 
                experience = 0
            EducationProfile = re.findall('Software Engineering|Mathematics degree|Computer Science|Information and Technology|Network Engineering', str(i), flags= re.MULTILINE|re.IGNORECASE)
            EducationProfile = list(set(EducationProfile))
            if EducationProfile != []:
              EducationProfile = 1
            else:
              EducationProfile = 0 
            English = 1
            Languages = re.findall('Afrikaans|Albanian|Arabic|Armenian|Azerbaijani|Belarusian|Bengali|Bosnian|Bulgarian|Chinese|Croatian|Czech|Danish|Dutch|Estonian|Fijian|Finnish|French|Scottish|Georgian|German|Greek|Hebrew|Hindi|Hungarian|Icelandic|Indonesian|Irish|Italian|Japanese|Kazakh|Korea|Kurdish|Lao|Latvian|Lithuanian|Macedonian|Malay|Moldavian|Mongolian|Ndonga|Nepali|Norwegian|Persian|Polish|Portuguese|Romanian|Russian|Serbian|Slovak|Slovenian|Somali|Spanish|Swahili|Swati|Swedish|Turkish|Turkmen|Ukrainian|Urdu|Uzbek|Vietnamese|Welsh|Zulu', str(i), flags= re.MULTILINE)
            Languages = list(set(Languages))
            if len(Languages) < 1:
              SecondLanguage = 0
              ThirdLanguage = 0
            elif len(Languages) == 1:
              SecondLanguage = 1
              ThirdLanguage = 0
            else:
              SecondLanguage = 1
              ThirdLanguage = 1
            #Still needs adjustment 
            EducationLevel = re.findall('Bachelor|Masters|PhD|PHD', str(i), flags= re.MULTILINE)
            if 'PhD' or 'PHD' in EducationLevel:
                EducationLevel = 3
            elif 'Masters' in EducationLevel:
                EducationLevel = 2 
            elif 'Bachelor' in EducationLevel:
                EducationLevel = 1
            else:
                EducationLevel = 0
            #Nota falta agregar C++
            GeneralPurposeProgrammingSkills = re.findall('HTML|Python|Java| C |C#|JavaScript|Java|Ruby|PHP|Swift|Go|Kotlin|Rust|Scala|Dart|Perl|MatLab| R ', str(i), flags=re.MULTILINE)
            GeneralPurposeProgrammingSkills = list(set(GeneralPurposeProgrammingSkills))
            if GeneralPurposeProgrammingSkills != []:
              GeneralPurposeProgrammingSkills = 1
            else:
              GeneralPurposeProgrammingSkills = 0
            CybersecurityProgramming = re.findall('Jira|PowerShell|Deduplication|Shell|Penetration testing|Assembly|Virtual Machines|VPN|Security incident|Audit|Intelligence|Intrusion detection', str(i), flags=re.MULTILINE|re.IGNORECASE)
            CybersecurityProgramming = list(set(CybersecurityProgramming))
            if CybersecurityProgramming != []:
              CybersecurityProgramming = 1
            else:
              CybersecurityProgramming = 0
            SoftwareLibrariesforProgrammingLanguages = re.findall('selenium|node.js|nmap|faker|cryptography|twisted|scapy|sql', str(i), flags=re.MULTILINE|re.IGNORECASE)
            SoftwareLibrariesforProgrammingLanguages = list(set(SoftwareLibrariesforProgrammingLanguages))
            if SoftwareLibrariesforProgrammingLanguages != []:
              SoftwareLibrariesforProgrammingLanguages = 1
            else:
              SoftwareLibrariesforProgrammingLanguages = 0
            LaTex = re.findall('latex', str(i), flags=re.MULTILINE|re.IGNORECASE) 
            LaTex = list(set(LaTex))
            if LaTex != []:
              LaTex = 1
            else:
              LaTex = 0
            ActiveDirectory = re.findall('active directory', str(i), flags=re.MULTILINE|re.IGNORECASE)
            ActiveDirectory = list(set(ActiveDirectory))
            if ActiveDirectory != []:
              ActiveDirectory = 1 
            else:
              ActiveDirectory = 0 
            OperatingSystems = re.findall('Windows|Linux|Operating System', str(i), flags=re.MULTILINE| re.IGNORECASE)
            OperatingSystems = list(set(OperatingSystems))
            if OperatingSystems != []:
              OperatingSystems = 1
            else:
              OperatingSystems = 0 
            ConsoleInterface = re.findall('Console interface|powershell|bash|command line', str(i), flags=re.MULTILINE| re.IGNORECASE)
            ConsoleInterface = list(set(ConsoleInterface))
            if ConsoleInterface != []:
              ConsoleInterface = 1
            else:
              ConsoleInterface = 0 
            MicrosoftOffice = re.findall('Excel|Microsoft Office|Office|PowerPoint', str(i), flags=re.MULTILINE)
            if MicrosoftOffice != []:
              MicrosoftOffice = 1 
            else:
              MicrosoftOffice = 0
            WordPress = re.findall('WordPress', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if WordPress != []:
              WordPress = 1 
            else:
              WordPress = 0 
            Jira = re.findall('Jira', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Jira != []:
               Jira = 1
            else:
              Jira = 0
            DataStructures = re.findall('data structures|list|tuple|stack|set|map|queue|tree|heap|array|matrix', str(i), flags=re.MULTILINE)
            if DataStructures != []:
              DataStructures = 1
            else:
              DataStructures = 0
            DatabaseManagement = re.findall('database management|MongoDB|Oracle|SQL|MariaDB|Salesforce|PhP', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DatabaseManagement != []:
              DatabaseManagement = 1
            else:
              DatabaseManagement = 0
            SharePoint = re.findall('SharePoint', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if SharePoint != []:
              SharePoint = 1
            else:
              SharePoint = 0
            DataVisualization = re.findall('data visualization|matplotlib|seaborn|Tableau|ChartBlocks|Datawrapper|Power BI', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DataVisualization != []:
              DataVisualization = 1
            else:
              DataVisualization = 0
            Virtualisation = re.findall('Virtualisation', str(i), flags=re.IGNORECASE|re.MULTILINE)
            if Virtualisation != []:
              Virtualisation = 1
            else:
              Virtualisation = 0
            Firewalls = re.findall('ESET endpoint security|cisco|GlassWire|Cloudbric|Privatise|Mcafee|Forcepoint', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Firewalls != []:
              Firewalls = 1
            else:
              Firewalls = 0
            NetworkSecurity = re.findall('network security',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if NetworkSecurity != []:
              NetworkSecurity = 1
            else:
              NetworkSecurity = 0
            Cloud = re.findall('Azure|AWS|Google Cloud|Cloud|Server',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Cloud != []:
              Cloud = 1
            else:
              Cloud = 0
            NetworkAdministration = re.findall('Network management|WireShark|Traceroute|Supervision|Ping|Nmap|Cisco|SolarWindws Network Performance|Cisco|Network administration',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if NetworkAdministration != []:
              NetworkAdministration = 1
            else:
              NetworkAdministration = 0
            NetworkEndPointProtection = re.findall('end point|Mcafee',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if NetworkEndPointProtection != []:
              NetworkEndPointProtection = 1
            else:
              NetworkEndPointProtection = 0
            NetworkTroubleshooting = re.findall('network troubleshooting',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if NetworkTroubleshooting != []:
              NetworkTroubleshooting = 1
            else:
              NetworkTroubleshooting = 0
            Cyberdefense = re.findall('cyber defense|kali linux|metasploit|tcpdump|nikto|nexpose',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Cyberdefense != []:
              Cyberdefense = 1
            else:
              Cyberdefense = 0
            ThreatIntelligence = re.findall('threat intelligence|kaspersky|ETP|DeCYFIR|ThreatFusion|XVigil|Flashpoint|Mcafee|Argos',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if ThreatIntelligence != []:
              ThreatIntelligence = 1
            else:
              ThreatIntelligence = 0
            Ethicalhacking = re.findall('Ethical hacking',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Ethicalhacking != []:
              Ethicalhacking = 1
            else:
              Ethicalhacking = 0
            VersionControl = re.findall('Git|GitHub',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if VersionControl != []:
              VersionControl = 1
            else:
              VersionControl = 0
            AdobePhotoshop = re.findall('photoshop',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if AdobePhotoshop != []:
              AdobePhotoshop = 1
            else:
              AdobePhotoshop = 0
            ReverseEngineering = re.findall('reverse engineering',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if ReverseEngineering != []:
              ReverseEngineering = 1
            else:
              ReverseEngineering = 0
            Research = re.findall('Research',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Research != []:
              Research = 1
            else:
              Research = 0
            Blockchain = re.findall('Blockchain',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Blockchain != []:
              Blockchain = 1
            else:
              Blockchain = 0
            Cryptography = re.findall('cryptography',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Cryptography != []:
              Cryptography = 1
            else:
              Cryptography = 0
            GeneralProfile = {'Category': Category, 'Job': job,'Experience': experience,'Time experience': total,'Education Level': EducationLevel,'Education Profile': EducationProfile,'English': English,'Second Language': SecondLanguage,'Third Language': ThirdLanguage,'General Purpose Programming Skills': GeneralPurposeProgrammingSkills, 'Cybersecurity programming skills': CybersecurityProgramming, 'Software libraries for programming languages': SoftwareLibrariesforProgrammingLanguages, 'Acitve directory': ActiveDirectory, 'Operating system': OperatingSystems , 'Console interface': ConsoleInterface ,'WordPress': WordPress,'Jira': Jira,'SharePoint': SharePoint,'Microsoft Office': MicrosoftOffice,'LaTeX': LaTex,'Data visualization': DataVisualization,'Databases management': DatabaseManagement,'Data Structure': DataStructures,'Cloud': Cloud,'Virtualisation': Virtualisation,'Firewalls': Firewalls,'Network Security': NetworkSecurity,'Network Security': NetworkSecurity,'Network administration': NetworkAdministration,'Network Endpoint protection': NetworkEndPointProtection,'Network Troubleshooting': NetworkTroubleshooting ,'Cyber defense': Cyberdefense,'Threat intelligence': ThreatIntelligence,'Ethical hacking': Ethicalhacking,'Version Control': VersionControl,'Adobe Photoshop': AdobePhotoshop,'Reverse Engineering': ReverseEngineering, 'Blockchain': Blockchain, 'Crpythography': Cryptography, 'Research skills': Research}          
            ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def GeneralProfileDSC(self,ProfileContent):
    ProfileList = []
    time1 = 0
    time2 = 0 
    total = 0
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
            if job != []:
                job = 1 
            else:
                job = 0
            Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", str(i) , flags= re.MULTILINE)
            try:
              Experience = Experience[0]
              exp = re.findall('Data Scientist.{135,150}|AI engineer.{135,150}|Data analyst.{135,150}|Machine Learning Engineer.{135,150}', Experience, flags = re.IGNORECASE)
              exp = ''.join(exp)
              months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
              months = ''.join(months)
              months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
              years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
              years = ''.join(years)
              years = re.findall('\d',years)
              for year in years:
                  yearsD = int(year)
                  if yearsD == 1:
                      yearsD = 12
                  if yearsD == 2:
                      yearsD = 24
                  time2 += int(yearsD)
              for time in months:
                time1 += int(time)
              total = time1 + time2 
            except: 
              total = np.nan
            if total != np.nan:
                experience = 1
            else: 
                experience = 0
            EducationProfile = re.findall('Software Engineering|Mathematics degree|Computer Science|Information and Technology|Statistics|Data Science degree', str(i), flags= re.MULTILINE|re.IGNORECASE)
            EducationProfile = list(set(EducationProfile))
            if EducationProfile != []:
              EducationProfile = 1
            else:
              EducationProfile = 0 
            English = 1
            Languages = re.findall('Afrikaans|Albanian|Arabic|Armenian|Azerbaijani|Belarusian|Bengali|Bosnian|Bulgarian|Chinese|Croatian|Czech|Danish|Dutch|Estonian|Fijian|Finnish|French|Scottish|Georgian|German|Greek|Hebrew|Hindi|Hungarian|Icelandic|Indonesian|Irish|Italian|Japanese|Kazakh|Korea|Kurdish|Lao|Latvian|Lithuanian|Macedonian|Malay|Moldavian|Mongolian|Ndonga|Nepali|Norwegian|Persian|Polish|Portuguese|Romanian|Russian|Serbian|Slovak|Slovenian|Somali|Spanish|Swahili|Swati|Swedish|Turkish|Turkmen|Ukrainian|Urdu|Uzbek|Vietnamese|Welsh|Zulu', str(i), flags= re.MULTILINE)
            Languages = list(set(Languages))
            if len(Languages) < 1:
              SecondLanguage = 0
              ThirdLanguage = 0
            elif len(Languages) == 1:
              SecondLanguage = 1
              ThirdLanguage = 0
            else:
              SecondLanguage = 1
              ThirdLanguage = 1
            #Still needs adjustment 
            EducationLevel = re.findall('Bachelor|Masters|PhD|PHD', str(i), flags= re.MULTILINE)
            if 'PhD' or 'PHD' in EducationLevel:
                EducationLevel = 3
            elif 'Masters' in EducationLevel:
                EducationLevel = 2 
            elif 'Bachelor' in EducationLevel:
                EducationLevel = 1
            else:
                EducationLevel = 0
            #Nota falta agregar C++
            MicrosoftOffice = re.findall('Excel|Microsoft Office|Office|PowerPoint', str(i), flags=re.MULTILINE)
            if MicrosoftOffice != []:
              MicrosoftOffice = 1 
            else:
              MicrosoftOffice = 0
            GeneralPurposeProgrammingSkills = re.findall('HTML|Python|Java| C |C#|JavaScript|Java|Ruby|PHP|Swift|Go|Kotlin|Rust|Scala|Dart|Perl|MatLab| R ', str(i), flags=re.MULTILINE)
            GeneralPurposeProgrammingSkills = list(set(GeneralPurposeProgrammingSkills))
            if GeneralPurposeProgrammingSkills != []:
              GeneralPurposeProgrammingSkills = 1
            else:
              GeneralPurposeProgrammingSkills = 0
            DatabaseManagement = re.findall('database management|MongoDB|Oracle|SQL|MariaDB|Salesforce|PhP', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DatabaseManagement != []:
              DatabaseManagement = 1
            else:
              DatabaseManagement = 0
            BackendSkills = re.findall('database|Oracle|PHP|backend|REST|MySQL|MongoDB|SQLServer|Apache|Django|Larval|Linux|API', str(i), flags=re.MULTILINE)
            BackendSkills = list(set(BackendSkills))
            if BackendSkills != []:
              BackendSkills = 1
            else:
              BackendSkills = 0
            DataVisualization = re.findall('data visualization|matplotlib|seaborn|Tableau|ChartBlocks|Datawrapper|Power BI', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DataVisualization != []:
              DataVisualization = 1
            else:
              DataVisualization = 0
            Cloud = re.findall('Azure|AWS|Google Cloud|Cloud|Server',str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Cloud != []:
              Cloud = 1
            else:
              Cloud = 0
            SoftwareLibrariesforML = re.findall('pandas|keras|sklearn|tensorflow|seaborn|numpy|sympy|armadillo|fann|matplotlib|mlpack|nltk|opennn|pytorch|scipy|shogun|theano|caffe|torch', str(i), flags=re.MULTILINE|re.IGNORECASE)
            SoftwareLibrariesforML = list(set(SoftwareLibrariesforML))
            if SoftwareLibrariesforML != []:
              SoftwareLibrariesforML = 1
            else:
              SoftwareLibrariesforML = 0
            VersionControl = re.findall('Git|GitHub', str(i), flags=re.MULTILINE|re.IGNORECASE) 
            VersionControl = list(set(VersionControl))
            if VersionControl != []:
              VersionControl = 1
            else:
              VersionControl = 0
            DeepLearningFrameworks = re.findall('Keras|TensorFlow|Torch|Deeplearning4j|CNTK|keras|onnx|mxnet|sonnet', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DeepLearningFrameworks != []:
              DeepLearningFrameworks = 1
            else:
              DeepLearningFrameworks = 0
            GeograficInformationSystems = re.findall('geographic information systems', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if GeograficInformationSystems != []:
              GeograficInformationSystems = 1
            else:
              GeograficInformationSystems = 0
            DataCollection = re.findall('web scraping|API|BeautifulSoup|Data mining|selenium', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if DataCollection != []:
              DataCollection = 1
            else:
              DataCollection = 0
            Transformingdata = re.findall('transforming data|data scalling|normalization|pandas|data transformation', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Transformingdata != []:
              Transformingdata = 1
            else:
              Transformingdata = 0
            Statistics = re.findall('statistics', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if Statistics != []:
              Statistics = 1
            else:
              Statistics = 0
            SolutionArchitecture = re.findall('solution architecture', str(i), flags=re.MULTILINE|re.IGNORECASE)
            if SolutionArchitecture != []:
              SolutionArchitecture = 1
            else:
              SolutionArchitecture = 0
            GeneralProfile = {'Category': Category, 'Job': job,'Experience': experience,'Time experience': total,'Education Level': EducationLevel,'Education Profile': EducationProfile,'English': English,'Second Language': SecondLanguage,'Third Language': ThirdLanguage,'Microsoft Office': MicrosoftOffice,'General Purpose Programming Skills': GeneralPurposeProgrammingSkills, 'Database management': DatabaseManagement, 'Backend skills': BackendSkills, 'Data visualization tools': DataVisualization, 'Cloud platforms': Cloud, 'Machine Learning tools': SoftwareLibrariesforML, 'Version control':VersionControl, 'Deep Learning tools': DeepLearningFrameworks, 'Geografic information systems': GeograficInformationSystems, 'Data collection': DataCollection, 'Transforming data': Transformingdata,'Statistics': Statistics, 'Solution Architecture': SolutionArchitecture}
            ProfileList.append(GeneralProfile)
    Data = pd.DataFrame(ProfileList)
    #This the final data
    return Data
  def JoinDataFrame(self,Profile,Previous): #Función diseñada para unir datos anteriores a datos nuevos con solo el nombre del archivo 
    Previous = pd.read_csv(f"ProfileITforRegresion{Previous}.csv")
    data = pd.merge(Profile,Previous)
    return data
