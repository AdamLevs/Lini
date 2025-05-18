list1 = [2, 3, 4, 8, 5, 1, 0]
list2 = [4, 5, 6, 7, 8, 9]

# section 1
find_common_elements = list(set(list1) & set(list2))
print(f"common list: {find_common_elements}")

# section 2
merged_unique = list(set(list1 + list2))
print(f"merge without duplicates: {merged_unique}")

# section 3
elements_only_in_first = list(set(list1) - set(list2))
print(f"only in first: {elements_only_in_first}")

# section 4
# making a functions to store the summary
save_list_summary = {
    'length_list1': len(list1),
    'length_list2': len(list2),
    'avg_list1': sum(list1) / len(list1),
    'avg_list2': sum(list2) / len(list2),
    'common_elements_count': len(find_common_elements)
}
# here we are creating a summary of the lists
# using the \n to create a new line
summary = ""
summary = summary + f"first list len: {save_list_summary['length_list1']}\n"
summary = summary + f"second list len: {save_list_summary['length_list2']}\n"
summary = summary + f"average first list: {save_list_summary['avg_list1']}\n"
summary = summary + f"average second list: {save_list_summary['avg_list2']}\n"
summary = summary + f"sum of the common nums: {save_list_summary['common_elements_count']}"

file = open('lists_summary.txt', 'w', encoding='utf-8')
file.write(summary)
file.close()
