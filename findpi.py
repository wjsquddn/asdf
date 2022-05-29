def findone(numlist, a):
    arr = []
    for i in range(a):
        arr.append([])
    for i in range(len(numlist)):
        arr[numlist[i].count('1')].append(numlist[i])
    return arr

def makecheck(arr):
    check = []
    for i in range(len(arr)):
        check.append([])
        if len(arr[i]) == 0:
            continue
        for j in range(len(arr[i])):
            check[i].append("0")
    return check

def findpi(numlist, a):
    answer = []
    b = a+1
    while 1:
        arr = findone(numlist, b)
        numlist = []
        b -= 1
        #체크 배열 만들기
        check = makecheck(arr)
        for i in range(len(arr) - 1):
            if len(arr[i]) == 0:
                continue
            if len(arr[i+1]) == 0:
                continue
            for j in range(len(arr[i])):
                for k in range(len(arr[i+1])):
                    cnt = ""#합쳐지는 것 문자열
                    cnt1 = 0#하나만 다른지 확인하는 방법
                    for l in range(a):
                        if arr[i][j][l] != arr[i + 1][k][l]:
                            cnt += "2"
                            cnt1 += 1
                        if arr[i][j][l] == arr[i + 1][k][l] and arr[i][j][l] == "0":
                            cnt += "0"
                        if arr[i][j][l] == arr[i + 1][k][l] and arr[i][j][l] == "2":
                            cnt += "2"
                        if arr[i][j][l] == arr[i + 1][k][l] and arr[i][j][l] == "1":
                            cnt += "1"

                    if cnt1 == 1:
                        if cnt not in numlist:
                            numlist.append(cnt)
                        check[i][j] = "1"
                        check[i + 1][k] = "1"

        checkcnt = 0
        for i in range(len(check)):
            if len(check[i]) == 0:
                continue
            for j in range(len(arr[i])):
                if check[i][j] == "0":
                    answer.append(arr[i][j])
                else:
                    checkcnt += 1
        if checkcnt == 0:
            break
    return answer


def findepi(answer, xlist, n,a):
    epi = []
    for i in range(len(answer)+1):
        epi.append([])
        for j in range(n+1):
            epi[i].append("-")
    for i in range(1,n+1):
        epi[0][i] = xlist[i-1]
    for j in range(1,len(answer)+1):
        epi[j][0] = answer[j-1]
    for i in range(1,len(answer)+1):
        checkinglist = []
        checkinglist.append(epi[i][0])
        checkinglist = checking(checkinglist,a)

        for j in range(1,n+1):
            if epi[0][j] in checkinglist:
                epi[i][j] = "1"

    realepi = []
    for j in range(1,n+1):
        count = []
        for i in range(1,len(answer)+1):
            if epi[i][j] == "1":
                count.append(epi[i][0])
        if len(count) == 1 and count[0] not in realepi:
            realepi.append(count[0])
    return realepi

def checking(checkinglist,a):
    checkinglist1 = []
    for i in range(len(checkinglist)):
        for j in range(a):
            if checkinglist[i][j] == '-':
                checkinglist1.append(checkinglist[i][:j]+"0"+checkinglist[i][j+1:a])
                checkinglist1.append(checkinglist[i][:j] + "1" + checkinglist[i][j + 1:a])

                break
    checkinglist = checkinglist1
    #재귀 끝내는 것
    checkbreak = 0
    for i in range(len(checkinglist)):
        for j in range(a):
            if checkinglist[i][j] == '-':
                checkbreak += 1
    if checkbreak == 0:
        return checkinglist
    return checking(checkinglist,a)

def reducedlist(epii, a, answer, xlist):
    reducedxlist = checking(epii,a)
    result = []
    for i in xlist:
        if i not in reducedxlist:
            result.append(i)
    xlist = result
    # print("---------")
    # print(answer)
    #print(epii)
    if len(epii)!=0:
        answer.remove(epii[0])

    print(answer)

    #reducedlist 만들기
    relist = []
    n = len(xlist)
    for i in range(len(answer) + 1):
        relist.append([])
        for j in range(n + 1):
            relist[i].append("-")
    for i in range(1, n + 1):
        relist[0][i] = xlist[i - 1]
    for j in range(1, len(answer) + 1):
        relist[j][0] = answer[j - 1]
    for i in range(1, len(answer) + 1):
        checkinglist = []
        checkinglist.append(relist[i][0])
        checkinglist = checking(checkinglist, a)

        for j in range(1, n + 1):
            if relist[0][j] in checkinglist:
                relist[i][j] = "1"
    return relist
def inlist(rest_list,rest_list1):
    answer = 1
    for i in rest_list1:
        if i not in rest_list:
            answer = 0
    return answer
def rowdominance(relist):
    row = []
    row_number = []
    changed = 0
    for i in range(len(relist)):
        print(relist[i])
    for i in range(1, len(relist)):
        rest_list = list(filter(lambda x: relist[i][x] == '1', range(1, len(relist[i]))))
        for j in range(1, len(relist)):
            if j == i:
               continue
            rest_list1 = list(filter(lambda x: relist[j][x] == '1', range(1, len(relist[j]))))
            if inlist(rest_list, rest_list1):
                row.append(relist[j][0])
                row_number.append(j)
    row_number = list(set(row_number))
    row = list(set(row))
    row_number.sort(reverse=True)
    print(row)
    for i in row_number:
        del relist[i]
        changed = 1
    return relist,row, changed

    #print(relist)
    #for i in range(1,len(relist)-1):
    #    if relist[i][-1] !=1:

def columndominance(relist):
    column = []
    column_number = []
    changed = 0
    for i in range(1, len(relist[0])):
        rest_list = list(filter(lambda x: relist[x][i] == '1', range(1, len(relist))))
        for j in range(1, len(relist[0])):
            if j == i:
                continue
            rest_list1 = list(filter(lambda x: relist[x][j] == '1', range(1, len(relist))))
            if inlist(rest_list, rest_list1):
                column.append(relist[0][i])
                column_number.append(i)
    column = list(set(column))
    column_number = list(set(column_number))
    column_number.sort(reverse=True)

    for i in column_number:
        for j in range(len(relist)):
            del relist[j][i]
            changed = 1

    for i in range(1,len(relist)):
        cnt1 = 0
        for j in range(1,len(relist[0])):
            if relist[i][j]=='1':
                cnt1+=1
        if cnt1==0:
            del relist[i]
    return relist, column, changed

def secondaryepi(relist):

    # for i in range(1,len(relist)-1):
    #     cnt22 = 0
    #     for j in range(1,len(relist[0])):
    #         if relist[i][j]=='1':
    #             cnt22+=1
    #     if cnt22 == 0:
    #         del relist[i]
    # for i in range(len(relist)):
    #     print(relist[i])
    secondaryepi = []
    idx = []
    for j in range(1,len(relist[0])):
        count = []
        idxcount = []
        for i in range(1,len(relist)):
            if relist[i][j] == "1":
                count.append(relist[i][0])
                idxcount.append(i)
        if len(count) == 1:
            secondaryepi.append(count[0])
            idx.append(idxcount[0])
    idx.sort(reverse=True)
    # print("--------------")
    # print(idx)
    for i in range(len(relist)):
        print(relist[i])
    for i in idx:
        del relist[i]
    # for i in range(1,len(relist)):
    #     for j in secondaryepi:
    #         if relist[i][0] in secondaryepi:
    #             del relist[i]
    # print(secondaryepi)
    # for i in range(len(relist)):
    #     print(relist[i])
    # print("\n")
    return secondaryepi,relist

def interchangable(relist):
    for i in range(1,len(relist)-1):
        cnt22 = 0
        for j in range(1,len(relist[0])):
            if relist[i][j]=='1':
                cnt22+=1
        if cnt22==0:
            del relist[i]

    while(1):
        checklist=[]
        changed = 0
        for i in range(1,len(relist)):
            checklist = []
            isdelete = 0
            for j in range(i+1,len(relist)):
                if relist[i][1:-1]==relist[j][1:-1]:
                    checklist.append(j)
                    changed = 1
            checklist.sort(reverse=True)
            for k in checklist:
                del relist[k]
                isdelete = 1
            if isdelete == 1:
                break
        if changed == 0:
            break

    return relist
def patric(relist):
    patric = []
    for i in range(1,len(relist[0])):
        patric_row = []
        for j in range(1,len(relist)):
            if relist[j][i] == '1':
                patric_row.append(j)
        patric.append(patric_row)
    # 가능한 조합 리스트 만들기
    print(patric)
    list1 = []
    notselect = []
    for i in range(len(patric)):
        insert = []
        covercount = []
        for j in range(len(patric[0])):
            if (patric[i][j] in list1):
                covercount.append(patric[i][j])
            if (patric[i][j] not in list1) and (patric[i][j] not in notselect):
                insert.append(patric[i][j])
        if len(insert) == 1 and len(covercount)==1:
            notselect.append(insert[0])
            continue
        if len(insert)==1:
            list1.append(insert[0])
        if len(insert)==2:
            list1.append(insert[0])
            notselect.append(insert[1])

    list1.sort(reverse=True)
    # print("list1----------------------")
    # print(list1)
    # for i in range(len(relist)-1,0,-1):
    #     if i not in list1:
    #         del relist[i]
    # print("relist without list1------------------")
    # for i in range(len(relist)):
    #     print(relist[i])
    patricanswer = []
    for i in list1:
        patricanswer.append(relist[i][0])
    return patricanswer
def solution(minterm):
    a = minterm[0]
    n = minterm[1]
    numlist = []
    for i in range(n):
        x = minterm[i + 2]
        bin_num = bin(x)[2:].zfill(a)

        numlist.append(bin_num)
    xlist = numlist
    answer = findpi(numlist, a)
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    for i in range(len(answer)):
        answer[i] = answer[i].replace('2','-')

    epii=findepi(answer, xlist, n,a)

    relist = reducedlist(epii, a, answer, xlist)
    for i in range(len(relist)):
        print(relist[i])

    # relist = interchangable(relist)

    for i in range(1,len(relist)-1):
        cnt22 = 0
        for j in range(1,len(relist[0])):
            if relist[i][j]=='1':
                cnt22+=1
        if cnt22==0:
            del relist[i]
    # for i in range(len(relist)):
    #     print(relist[i])

    nothingchange = 0
    secondepi = []
    while(1):
        if len(relist)==1:
            print("finished and second epi : ")
            print(secondepi)
            break
        relist, row, changed2 = rowdominance(relist)
        for i in range(len(relist)):
            print(relist[i])
        print("row : ")
        print(row)

        relist, column, changed1 = columndominance(relist)
        print("after columndominance")
        for i in range(len(relist)):
            print(relist[i])
        print(column)
        if (changed1==1) or (changed2==1):
            second,relist= secondaryepi(relist)
            secondepi = secondepi+second
            print("secondepi : ")
            print(secondepi)
            print("relist : ")
            print(relist)
        elif (changed1!=1) and (changed2!=1):
            nothingchange = 1
            break
    if nothingchange==1:
        print("---------------")
        # for i in range(len(relist)):
        #     print(relist[i])
        print("petrick : ")
        print(patric(relist))
        # print("---------------")
        # for i in range(len(relist)):
        #     print(relist[i])

    # for i in range(len(relist)):
    #     print(relist[i])
    # relist, row,changed2 = rowdominance(relist)
    # print(changed2)
    #print(row)
    # for i in range(len(relist)):
    #     print(relist[i])

    # relist,second = secondaryepi(relist)
    # print(second)
    # print(relist)
    answer.append("EPI")
    answer = answer+epii
    return answer

# print(solution([4,11,0,2,5,6,7,8,10,12,13,14,15]))
print(solution([3,6,0,1,2,5,6,7]))
# print(solution([4,8,0,4,8,10,11,12,13,15]))
