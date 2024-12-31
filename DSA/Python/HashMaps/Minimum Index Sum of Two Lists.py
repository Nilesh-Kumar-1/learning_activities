def findRestaurant( list1: list[str], list2: list[str]) -> list[str]:
        Map={}
        mini = 2000
        res=[]
        for i in range(len(list1)):
            Map[list1[i]] = i
        print(Map)
        for j in range(len(list2)):
            if list2[j] in Map:
                sum = j + Map[list2[j]]
                print(mini , sum)
                if sum < mini:
                    mini = sum
                    res = []
                    res.append(list2[j])
                elif sum == mini:
                    res.append(list2[j])
        return res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]



print(findRestaurant(list1, list2))