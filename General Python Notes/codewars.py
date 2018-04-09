import re
def change_case(identifier, targetCase):
    def CaseFinder(string=identifier):
        
        Camel = (identifier.lower != identifier,"Camel")
        Kebab =  (identifier.find("-") != -1,"Kebab")
        Snake = (identifier.find("_") != -1,"Snake")

        filtered = list(filter(lambda x : x[0],[Snake,Kebab,Camel]))
        
        if len(filtered) > 1:
            return "invalid"
        else:
            
            return filtered[0][0]
    print(CaseFinder())
    def CaseMake(case = CaseFinder(identifier),target = targetCase):
        if case == "Camel":
            if target == "Camel":
                return identifier
            if  target == "Snake":
                return separator(identifier,"_")
            if target == "Kebab":
                return separator(identifier,"-")

        if case == "Snake":
            if target == "Camel":


                
    def separator(string, sep):
        strToReturn = ""
        for x in string:
                    if x.isupper():
                        strToReturn += sep + x.lower()
                    else:
                        strToReturn += x
        return strToReturn


