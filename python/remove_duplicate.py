# def Remove(duplicate):
#     final_list=[]
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list


duplicate = [2,3,4,5,2,4,3,4,6,7,8,8,9,0]
# print(Remove(duplicate))

print(list(set(duplicate)))