text_file = open("input", "r")
diag = text_file.readlines()
diag = map(lambda s: s.strip(), diag)
text_file.close()
def filter_list(input_diag,position,high):
    counter=0
    for values in input_diag:
        digits=list(values)
        counter=counter+int(digits[position])
    if high:
        filter_value="0"
        if float(counter)>=float(len(input_diag))/2:
            filter_value="1"
    else:
        filter_value="1"
        if float(counter)>=float(len(input_diag))/2:
            filter_value="0"
    short_list=[x for x in input_diag if x[position]==filter_value]
    if (position<len(input_diag[1])+1 and len(short_list)>1):
        filtered_list=filter_list(short_list,position+1,high)
    else:
        filtered_list=short_list
    return(filtered_list)
oxygen=int("".join(filter_list(diag,0,True)),2)
co2=int("".join(filter_list(diag,0,False)),2)
print oxygen,co2,oxygen*co2
