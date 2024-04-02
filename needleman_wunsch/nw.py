class NeedlemanWunsch():
    def __init__(self, s1, s2, match_reward = 1, gap_penalty = -1, mismatch_penalty= -1):
        self.s1 = s1
        self.s2 = s2
        self.match_reward = match_reward
        self.gap_penalty = gap_penalty
        self.mismatch_penalty = mismatch_penalty
        self.scoring_matrix = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        self.traceback_matrix = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        for i in range(len(self.scoring_matrix)):
            for j in range(len(self.scoring_matrix[0])):
                self.scoring_matrix[0][j] = 0 - j
            self.scoring_matrix[i][0] = 0 - i
        self.fillMatrices()
        self.alignment1, self.alignment2 = self.traceback()
        self.alignment_score = self.scoring_matrix[-1][-1]

    def fillMatrices(self):
        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):
                if self.s1[i-1] == self.s2[j-1]:
                    diag = self.scoring_matrix[i-1][j-1] + self.match_reward
                else:
                    diag = self.scoring_matrix[i-1][j-1] + self.mismatch_penalty
                up = self.scoring_matrix[i-1][j] + self.gap_penalty
                back = self.scoring_matrix[i][j-1] + self.gap_penalty
                self.scoring_matrix[i][j] = max(diag, up, back)

                if self.scoring_matrix[i][j] == diag:
                    self.traceback_matrix[i][j] = 'd'
                elif self.scoring_matrix[i][j] == up:
                    self.traceback_matrix[i][j] = 'u'
                else:
                    self.traceback_matrix[i][j] = 'b'
    
    def traceback(self):
        a1 = ""
        a2 = ""
        a1_ptr = len(self.s1)
        a2_ptr = len(self.s2)
        while a1_ptr > 0 or a2_ptr > 0:
            curr_pos = self.traceback_matrix[a1_ptr][a2_ptr]
            if curr_pos == 'd':
                a1 = self.s1[a1_ptr - 1] + a1
                a2 = self.s1[a2_ptr - 1] + a2
                a1_ptr -= 1
                a2_ptr -= 1
            elif curr_pos == 'u':
                a1 = self.s1[a1_ptr-1] + a1
                a2= '-' + a2
                a1_ptr -= 1
            else:
                a1 = self.s2[a2_ptr-1] + a2
                a1= '-' + a1
                a2_ptr -= 1
        return a1, a2
    
    def displayAlignment(self):
        print(self.alignment1)
        print(self.alignment2)
