import re 
class CleanText():
    def CleaningText(self,Data):
        List = []
        for data in Data: 
            test1 = str(data).replace('\n','')
            test1 = str(test1).replace('Ver toda la actividad', '')
            test1 = re.sub(r'Información de(.*)aquí', ' ', test1, flags=re.IGNORECASE)
            test1 = re.sub(r'\dValidada por', '',test1, flags=re.IGNORECASE)
            test1 = re.sub(r'Contacto de \der grado\der', '', test1, flags= re.IGNORECASE)
            test1 = re.sub(r'Ver todas las aptitudes', '', test1, flags=re.IGNORECASE)
            test1 = re.sub(r'Intereses(.*)', '',test1, flags= re.IGNORECASE)
            test1 = re.sub(r'actualidad', 'currently', test1)
            test1 = re.sub(r'comentario', '', test1, flags=re.IGNORECASE)
            test1 = re.sub(r'Publicado', '', test1)
            test1 = re.sub(r'año', 'year', test1)
            test1 = re.sub(r'años', 'years', test1)
            test1 = re.sub(r'\d min de lectura', '', test1)
            test1 = re.sub(r'meses', 'months', test1)
            test1 = re.sub(r'mes', 'month', test1)
            List.append(test1) 
        return List