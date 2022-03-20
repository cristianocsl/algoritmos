def my_sort(word):
    array = list(word.lower())
    for index in range(len(array)):
        current_value = array[index]
        current_position = index
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and
            array[current_position - 1] > current_value
        ):
            # move as posições para a direita
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
            # colocamos o elemento em sua nova posição
        array[current_position] = current_value
    return array
    # return "".join(array)


# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html#:~:text=Se%20for%20poss%C3%ADvel%20%E2%80%9Cmarcar%E2%80%9D%20cada,segunda%20string%20em%20uma%20lista.
def is_anagram(first_string, second_string):
    if not (first_string and second_string):
        return False

    array_1 = my_sort(first_string)
    array_2 = my_sort(second_string)

    position = 0
    same = True

    while position < len(array_1) and same:
        if array_1[position] == array_2[position]:
            position += 1
        else:
            same = False
    return same
