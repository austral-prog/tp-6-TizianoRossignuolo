# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    nueva_lista = list_to_remove_elements[:]

    if len(nueva_lista) > 5:
        del nueva_lista[5]
    if len(nueva_lista) > 4:
        del nueva_lista[4]
    if len(nueva_lista) > 0:
        del nueva_lista[0]

    return nueva_lista


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")

    return list_to_add_elements


def is_empty(list_to_check):
    if len(list_to_check)==0:
        return True
    else: 
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return True
        else:
            return False



def list_of_lists(list_of_lists_to_modify):
    lista1 = list_of_lists_to_modify[0]
    lista2 = list_of_lists_to_modify[1]
    lista3 = list_of_lists_to_modify[2]

    nueva1 = lista1[:2]
    nueva2 = lista2[1:4]
    nueva3 = lista3[-2:]

    return [nueva1, nueva2, nueva3]

