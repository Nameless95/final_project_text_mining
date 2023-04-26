import matplotlib.pyplot as plt

#our ceiling values for a 3-splitted range for each NEO classification
nscore_range=[-.7951,0.91093,3.27393]
escore_range=[-1.37639,0.63779,3.27393]
oscore_range=[-1.27553,0.44585,2.90161]
ascore_range=[-1.47955,0.59042,3.46436]
cscore_range=[-1.38502,0.41594,3.46436]

#gender legend
# 0 is male, 1 is female

#age ranges
eighteen_24=-.95197
twentyfive_34=-.07854
thirtyfive_44=.49788
fortyfive_54=1.09449
fiftyfive_64=1.82213
sixtyfive_andup=2.59171


# variables for each usage level. final graph will have 2 choices: 
# moderation levels(cl0-cl6) OR patient stats (age & gender)

class PatientDatabase(object):
        def __init__(self,S,k,N,usage = "",a=None):
            self.age=k  #wordcode
            self.gender=N #documentfrequency
            self.id = S  #globalfrequency
            self.CL = usage
            self.attribute = []
            if a is None:
                a={}


class UserDrugSearch:
        def __init__(self, a=None):       
            self.age=[]       #wordcode
            self.gender= []         #frequency
            self.usage = []
            self.neo_level = []
            self.tracker = {}
            if a is None:
                a={}

        def changetousable(self,emotion, stats):
            empty = True
            uniqstuff = []
            if(stats == '2'):
                uniqstuff = set(self.age)
                uniqstuff = list(uniqstuff)
                listiteator = self.age
            else:
                uniqstuff = set(self.usage)
                uniqstuff = list(uniqstuff)
                listiteator = self.usage

            


            #our ceiling values for a 3-splitted range for each NEO classification
            # emotion = neo frr 1-5
            for x, y in zip(self.neo_level,listiteator):
                valuevalueincoming = float(x)
                
                if emotion == 1:
                   if empty:
                        for j in uniqstuff:
                            self.tracker[str("low ") + j] = 0
                            self.tracker[str("medium ") +j] = 0
                            self.tracker[str("high ") +j ] = 0
                        empty = False
                   if nscore_range[0] > valuevalueincoming:
                       self.tracker[str("low ") + y] += 1
                   if nscore_range[0] > valuevalueincoming:
                      self.tracker[str("medium ") + y] += 1
                   else:
                      self.tracker[str("high ") + y] += 1
                elif emotion == 2:
                   if empty:
                        for j in uniqstuff:
                            self.tracker[str("low ") + j] = 0
                            self.tracker[str("medium ") +j] = 0
                            self.tracker[str("high ") +j ] = 0
                        empty = False
                   if escore_range[0] > valuevalueincoming:
                        self.tracker[str("low ") + y] += 1
                   if escore_range[0] > valuevalueincoming:
                       self.tracker[str("medium ") + y] += 1
                   else:
                      self.tracker[str("high ") + y] += 1
                elif emotion == 3:
                   if empty:
                        for j in uniqstuff:
                            self.tracker[str("low ") + j] = 0
                            self.tracker[str("medium ") +j] = 0
                            self.tracker[str("high ") +j ] = 0
                        empty = False
                   if oscore_range[0] > valuevalueincoming:
                       self.tracker[str("low ") + y] += 1
                   if oscore_range[0] > valuevalueincoming:
                      self.tracker[str("medium ") + y] += 1
                   else:
                      self.tracker[str("high ") + y] += 1
                elif emotion == 4:
                   if empty:
                        for j in uniqstuff:
                            self.tracker[str("low ") + j] = 0
                            self.tracker[str("medium ") +j] = 0
                            self.tracker[str("high ") +j ] = 0
                        empty = False
                   if ascore_range[0] > valuevalueincoming:
                       self.tracker[str("low ") + y] += 1
                   if ascore_range[0] > valuevalueincoming:
                      self.tracker[str("medium ") + y] += 1
                   else:
                      self.tracker[str("high ") + y] += 1
                else:
                   if empty:
                        for j in uniqstuff:
                            self.tracker[str("low ") + j] = 0
                            self.tracker[str("medium ") +j] = 0
                            self.tracker[str("high ") +j ] = 0
                        empty = False
                   if cscore_range[0] > valuevalueincoming:
                       self.tracker[str("low ") + y] += 1
                   if cscore_range[0] > valuevalueincoming:
                      self.tracker[str("medium ") + y] += 1
                   else:
                      self.tracker[str("high ") + y] += 1



def DrugFileCreation():

    # 13 unigrams per drug in selected study
    
    Dtable ={"alcohol": [],"amphetamines": [],"amyl nitrite": [],
             "benzodiazepine": [],"cannabis": [],"chocolate": [],
            "cocaine": [],"caffeine": [],"crack": [],
             "ecstasy": [],"heroin": [],"ketamine": [],
             "legal highs": [],"LSD": [],"methadone": [],
             "mushrooms": [],"nicotine": [],"Semeron": []} 


    #Iteration through chunks
    with open("drug_consumption.data") as wiki_line:
        #Original Raw Data
        for x in wiki_line:


            #List-ify input by ',' delim
            searching = x.split(",")
            counter = 13                    #i think this grabs 31, double check later

            # index[0]= PID, [1]=age, [2]=gender,[8]-[12]=NEO-FFI, [13]-[30]= relative frequency to Dtable
            for y in Dtable:
                temp = PatientDatabase(searching[0],searching[1],searching[2],searching[counter])
                for neo in range(6,11):
                    temp.attribute.append(searching[neo])
                Dtable[y].append(temp)
                counter += 1

#Creating drug files, keeping info we want from patients
    for x in Dtable:
       file1 = open(x + ".txt", "w+")
       for y in Dtable[x]:
        temp2 = ' '.join([str(z) for z in y.attribute])
        file1.write(y.id + " "+ y.gender + " " + y.age + " " +   y.CL + " " + temp2 +"\n")
       file1.close()

    

def control():
    Dtable = ["alcohol","amphetamines","amyl nitrite",
             "benzodiazepine","cannabis","chocolate",
            "cocaine","caffeine","crack",
             "ecstasy","heroin","ketamine",
             "legal highs","LSD","methadone",
             "mushrooms","nicotine","Semeron"]

    fivevalues = ["neuroticism", "extraversion", "openness" , "agreeableness","conscientiousness"]
    
    exist = True
    while(exist):
        tempdrug = UserDrugSearch()
        print (str(Dtable) + "\n")


        userinput1 = input("enter a drug you would like to search from this list\n")

        file1 = open(userinput1 + ".txt")

    #grabbing one neo score
        userinput2 = input("select the value you would like to plot, choose from: %s" % fivevalues)

        indexvalue = fivevalues.index(userinput2) + 4

    #grabbing cl index OR age,gender indices
        userinput3= "1"
        



        #after putting age
        for x in file1:
            x = x.split()
            # if statement for moderation levels
            if userinput3 == 1:
                tempdrug.usage.append(x[3])
            else:
                if float(x[1]) < 0:
                    tempdrug.gender.append('0')
                else:
                    tempdrug.gender.append('1')
                currentage = float(x[2])
                if eighteen_24 >= currentage:
                    tempdrug.age.append("18-24")
                elif float(twentyfive_34) >= currentage:
                   tempdrug.age.append("25-34")
                elif float(thirtyfive_44) >= currentage:
                   tempdrug.age.append("35-44")
                elif float(fortyfive_54) >= currentage:
                 tempdrug.age.append("45-54")
                elif float(fiftyfive_64) >= currentage:
                 tempdrug.age.append("55-64")
                else: 
                 tempdrug.age.append("65+")
            tempdrug.neo_level.append(x[indexvalue])
            tempdrug.usage.append(x[3])
        counter = 0

   
        tempdrug.changetousable( indexvalue - 3, 1)
        # print("print graph")

        myList = list(tempdrug.tracker.keys())      #'low cl6' , 'medium cl6
        myList2 = list(tempdrug.tracker.values())   #amount of people

        dictionstuf = {"CL0" : "Never " , "CL1": "over a Decade Ago",
        "CL2": " in Last Decade" ,"CL3" :" in Last Year", "CL4" : "in Last Month ", "CL5": "in Last Week", 
        "CL6": " in Last Day"}

        #myList = Use Level _ Use Frequency
        counter2 = 0
        for x in myList:
            temp = x.split()
            temp[1] = dictionstuf[temp[1]] 
            myList[counter2] = str(temp)
            counter2 += 1
        
        fir_level=myList[:3]
        sec_level=myList[3:6]
        thir_level=myList[6:9]
        four_level=myList[9:12]
        fif_level=myList[12:15]
        six_level=myList[15:18]
        sev_level=myList[18:]


        people_fir_level=myList2[:3]
        people_sec_level=myList2[3:6]
        people_thir_level=myList2[6:9]
        people_four_level=myList2[9:12]
        people_fif_level=myList2[12:15]
        people_six_level=myList2[15:18]
        people_sev_level=myList2[18:]



        plt.bar(fir_level,people_fir_level,color='r',edgecolor="black", label="Type 1")
        plt.bar(sec_level,people_sec_level,color='b',edgecolor="black", label="Type 2")
        plt.bar(thir_level,people_thir_level,color='g',edgecolor="black", label="Type 3")
        plt.bar(four_level,people_four_level,color='y',edgecolor="black", label="Type 4")
        plt.bar(fif_level,people_fif_level,color='w',edgecolor="black", label="Type 5")
        plt.bar(six_level,people_six_level,color='k',edgecolor="black", label="Type 6")
        plt.bar(sev_level,people_sev_level,color='m',edgecolor="black", label="Type 7")

        plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees
        plt.xticks(fontsize=10)
        plt.ylabel("Patients")
        plt.xlabel("Usage Levels")
        plt.title("Selected Comparison: " + userinput2 +"," + userinput1)
        plt.legend()
        plt.show()



def main():

    #read given data
    DrugFileCreation()

    #perform
    control()


if __name__=='__main__':
    main()