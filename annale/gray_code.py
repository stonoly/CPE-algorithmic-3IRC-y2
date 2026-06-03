def gray_code_generator(n: int) -> [string]:
    if n <= 1:
        return ['0', '1']

    else:
        tab_jedi = gray_code_generator(n - 1)
        tab_sith = tab_jedi[::-1] 
        
        for j, jedi in enumerate(tab_jedi):
            tab_jedi[j] = '0' + jedi

        
        for s, sith in enumerate(tab_sith):
            tab_sith[s] = '1' + sith

        concatenate = tab_jedi + tab_sith
        return concatenate

if __name__ == "__main__":
    tab = gray_code_generator(3)
    print(tab)
    