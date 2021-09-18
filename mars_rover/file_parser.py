class FileParser:
    def __init__(self, filename):
        self.filename = filename
        self.plateau = {}
        self.rovers = []

    def parsers(self):
        '''
        It will parse the input file.
        :return: None
        '''
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            r = {}
            if len(lines) > 1:
                p = lines[0].strip('\n').split(':')[1].split()
                self.plateau['x'] = int(p[0])
                self.plateau['y'] = int(p[0])
                for line in lines[1:]:

                    line = line.strip('\n')
                    if 'landing' in line.lower():
                        name = line.split()[0]
                        l = line.strip('\n').split(':')[1].split()
                        r['name'] = name
                        r['x'] = int(l[0])
                        r['y'] = int(l[1])
                        r['head'] = l[2]
                    else:
                        r['command'] = line.split(':')[1]
                        self.rovers.append(r)
                        r = {}