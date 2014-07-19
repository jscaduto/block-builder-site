from copy import copy
from math import factorial

SOLUTION_TYPES = ['ALL', 'FIRST']


class BlockSolver:
    # block_faces is a hashmap of the faces of the blocks (inversion of block)
    block_face_sets = {}

    def __init__(self, block_sets):
        self._create_block_faces_hashes(block_sets)

    def __call__(self, block_set_name, phrase, solution_type='FIRST', get_difficulty=False):
        self.block_set_name = block_set_name
        self.phrase = phrase.upper()
        self.solution_type = solution_type.upper() if solution_type.upper() in SOLUTION_TYPES else 'FIRST'
        self.solution = []
        self.solutions = []

        self.find_solutions()

        if len(self.solutions) == 1 and self.solution_type != 'ALL':
            return self.solutions[0]
        return self.solutions

    def _create_block_faces_hashes(self, block_sets):
        for block_set_name, blocks in block_sets.items():
            self.block_face_sets[block_set_name] = {}
            for block_num, faces in enumerate(blocks, start=1):
                for face in faces:
                    if face not in self.block_face_sets[block_set_name]:
                        self.block_face_sets[block_set_name][face] = []
                    # added this check because molly's blocks have a block with 2 Gs
                    if block_num not in self.block_face_sets[block_set_name][face]:
                        self.block_face_sets[block_set_name][face].append(block_num)

    def find_solutions(self, index=0):
        if len(self.solutions) == 1 and self.solution_type != 'ALL':
            return
        block_faces = self.block_face_sets[self.block_set_name]
        if index == len(self.phrase):
            self.solutions.append(copy(self.solution))
            return
        letter = self.phrase[index]
        if letter == ' ':
            self.find_solutions(index + 1)
        elif block_faces[letter]:
            for block_num in block_faces[letter]:
                if block_num not in self.solution:
                    self.solution.append(block_num)
                    self.find_solutions(index + 1)
                    self.solution.pop()

    def _nCr(self, n, r):
        """
        equation for permutations of a order dependent and non-returning set
        """
        f = factorial
        return float(f(n) / f(n - r))

    def get_difficulty(self):
        """
        the chance you will pick up the blocks in order
        """
        if not len(self.solutions):
            return None
        nCr = self._nCr(len(self.blocks), len(self.phrase.replace(" ", "")))
        return 1 / (len(self.solutions) / nCr)

    def print_solutions(self):
        if len(self.solutions):
            print 'Phrase:         ' + self.phrase
            print '# of Solutions: ' + str(len(self.solutions))
            # print a solution
            # pprint(solutions[0])
            print 'Difficulty: ' + str(self.get_difficulty())
        else:
            print 'Not Possible'
