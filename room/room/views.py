from django.shortcuts import render
import random,os,json

def ShuffleRoom():
    r1 = ['Navid Manshuri', 'Bilal', 'khalil', 'Muneer', 'Bhavnesh', 'Kumar Nayak', 'Raju','Rohit Roy']
    r6 = ['Deepak Sharma', 'Deepak patel', 'S.Vivak', 'Paranthaman', 'Chandan Sahoo', 'Ramesh', 'Sanjay', 'Shabid Khan','Amarpal','Riyaz Khan']
    r7 = ['Sonu', 'Rahit Roy', 'Bhaskar', 'Prabhakar', 'biju', 'Shubham', 'Teja', 'Rahul']
    r8 = ['Tarique', 'Kaushal Sahoo', 'Abhishek', 'Himanshu', 'Mohit', 'Aakash']
    r9 = ['pralhad', 'Ajay']
    r10 = ['Kirithiv', 'Bijendra', 'Umesh', 'Peter', 'Tapas']
    r11 = ['Yousaf', 'Viresh', 'Prince', 'Rakesh', 'Rohit']
    r12 = ['Somesh', 'Aman Kumar', 'Ankur ', 'Vishal kumar', 'Vishal', 'Akhilesh']

    bed = []
    FinalBedDict = {1:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

    allRooms = [r1, r6, r7, r8, r9, r10, r11, r12]

    roomAndBed = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36],
        [37, 38, 39, 40, 41, 42, 43, 44],
        [45, 47, 48, 49, 50],
        [51, 52, 53, 54, 55, 56, 57, 58, 59]
    ]
    NameList = []
    BedNoList = []
    RoomNoList = []
    LineList = []
    FinalList = {}
    i = 0
    while (i < len(allRooms)):
        for j in allRooms[i]:

            while True:
                first = random.choice(roomAndBed)
                BedNO = random.choice(first)

                if (BedNO not in bed) and roomAndBed.index(first) != i:
                    FinalList['Name'] = j
                    FinalList['Bed'] = BedNO
                    if int(BedNO) % 2 == 0:
                        FinalList['Position']='Upper Side Bed '
                    else:
                        FinalList['Position'] ='Down Side Bed'
                    BedNoList.append(BedNO)
                    NameList.append(j)
                    bed.append(BedNO)
                    LineList.append("|")
                    if BedNO < 9:
                        RoomNo = 1
                    elif BedNO < 19:
                        RoomNo = 6
                    elif BedNO < 27:
                        RoomNo = 7
                    elif BedNO < 33:
                        RoomNo = 8
                    elif BedNO < 37:
                        RoomNo = 9
                    elif BedNO < 45:
                        RoomNo = 10
                    elif BedNO < 51:
                        RoomNo = 11
                    else:
                        RoomNo = 12
                    RoomNoList.append(RoomNo)
                    first.pop(first.index(BedNO))
                    FinalBedDict[RoomNo] += [FinalList]
                    if 'Count' not in FinalBedDict[RoomNo][0]:
                        FinalBedDict[RoomNo][0]['Count']=0
                    FinalBedDict[RoomNo][0]['Count']+=1

                    FinalList = {}

                    if first == []:
                        roomAndBed.pop(roomAndBed.index(first))
                    break
        i += 1
    return FinalBedDict
def home(request):
    if os.path.exists('RoomData.json')==False:
        FinalBedDict = ShuffleRoom()
        File = open('RoomData.json','w')
        json.dump(FinalBedDict,File,indent=4)
        File.close()
    file = open('RoomData.json','r')
    file=  json.load(file)


    for i in file:
        j = 0
        while (j < len(file[i]) - 1):
            if file[i][j]['Bed'] > file[i][j + 1]['Bed']:
                file[i][j], file[i][j + 1] = file[i][j + 1], file[i][j]
                if 'Count' in file[i][j+1]:
                    file[i][j]['Count']=file[i][j+1]['Count']
                j = 0
            else:
                j += 1

    return render(request,'home.html',{'file':file })
