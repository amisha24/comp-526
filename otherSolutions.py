class encoding:
    #grouping of two
    def sets_of_two(self, code, exam):
        
        for i in range(len(code)):
            count = exam[2*i] + exam[2*i+1]
            if count > 0:
                code[i] = 1
            else:
                code[i] = 0

        return code
    
    # groupings of three
    def sets_of_three(self, code, exam):
        
        for i in range(len(code)):

            
            if 3*i+2 > 19:
                break


            count = exam[3*i] + exam[3*i+1] + exam[3*i+2]
            if count > 1:
                code[i] = 1
            else:
                code[i] = 0

        return code
    
    # groupings of five
    def sets_of_five(self, code, exam):

        for i in range(len(code)):

            
            if 5*i+4 > 19:
                break
            count = exam[5*i] + exam[5*i+1] + exam[5*i+2] + exam[5*i+3] + exam[5*i+4]
            if count > 2:
                code[i] = 1
            else:
                code[i] = 0

        return code
    
    # two groupings of five, one of three and the rest filled
    def sets_of_2fives_1three_fill(self, code, exam):
        
        for i in range(len(code)):

            
            if 5*i+4 > 9:
                break
            count = exam[5*i] + exam[5*i+1] + exam[5*i+2] + exam[5*i+3] + exam[5*i+4]
            if count > 2:
                code[i] = 1
            else:
                code[i] = 0
        
        # 1 group of three
        for i in range(2, 3):
            count = exam[10] + exam[11] + exam[12]

            if count > 1:
                code[i] = 1
            else:
                code[i] = 0

        # 7 one-to-one mappings
        for i in range(3, 10):
            code[i] = exam[i+10]

        return code
class Decoding:

    # groupings of two
    def sets_of_two(self, answer, code):
        
        # decode in sets of three
        for i in range(len(code)):

            answer[2*i]     = code[i]
            answer[2*i+1]   = code[i]

        return answer
    
    # groupings of three
    def sets_of_three(self, answer, code):
        
        # decode in sets of three
        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 3*i+2 > 19:
                break

            answer[3*i]     = code[i]
            answer[3*i+1]   = code[i]
            answer[3*i+2]   = code[i]

        return answer

    #groupings of five
    def sets_of_five(self, answer, code):

        # decode into 4 groups of five
        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 5*i+4 > 19:
                break

            answer[5*i]     = code[i]
            answer[5*i+1]   = code[i]
            answer[5*i+2]   = code[i]
            answer[5*i+3]   = code[i]
            answer[5*i+4]   = code[i]

        return answer
    
    # two groupings of five, one of three and the rest filled
    def sets_of_2fives_1three_fill(self, answer, code):

        # decode 2 groups of five
        for i in range(len(code)):

            # stop after the two decodings
            if 5*i+4 > 9:
                break

            answer[5*i]     = code[i]
            answer[5*i+1]   = code[i]
            answer[5*i+2]   = code[i]
            answer[5*i+3]   = code[i]
            answer[5*i+4]   = code[i]

        # decode 1 group of three
        answer[10]   = code[i]
        answer[11]   = code[i]
        answer[12]   = code[i]

        # 7 one-to-one mappings
        for i in range(3, 10):

            answer[i+10] = code[i]

        return answer


