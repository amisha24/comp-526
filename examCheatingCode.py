# Compute the honking protocol for the exam cheaters

def compute_and_send_code(exam):
    code = [0] * 10
    # Dont change anything above this line
    # ==========================

    # five groupings of three and the rest filled
    for i in range(len(code)):

            # stop when we reach the 5 groups of three
        if 3*i+2 > 14:
            break

            # to iterate it would be 3i, 3i+1, 3i+2
            # -- if the count is greater than 1 then the dominate 
            #    feature is 1 and not 0.
        count = exam[3*i] + exam[3*i+1] + exam[3*i+2]
        if count > 1:
            code[i] = 1
        else:
            code[i] = 0

        # 5 one-to-one mappings
    for i in range(5, 10):
        code[i] = exam[i+10]

        


    # ==========================
    # Dont change anything below this line
    return code


def enter_solution_based_on_code(code):
    answer = [0] * 20

    # Dont change anything above this line
    # ==========================

      # decode in sets of three
    for i in range(len(code)):

            # ensure the five groupings is not exceeded
        if 3*i+2 > 14:
            break
            
        answer[3*i]     = code[i]
        answer[3*i+1]   = code[i]
        answer[3*i+2]   = code[i]

        # 5 one-to-one mappings
    for i in range(5, 10):
        answer[i+10] = code[i]



    # ==========================
    # Dont change anything below this line
    return answer
