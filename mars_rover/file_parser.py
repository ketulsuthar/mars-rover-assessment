
class FileParser:
    def __int__(self, filrname):
        self.file = filrname
        self.plateau = {}
        self.rovers = []

    def parsers(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
            if len(lines) > 1:
                p = lines[0].split(':')[1].split()
                self.plateau['x'] = int(p[0])
                self.plateau['y'] = int(p[0])
                for line in lines[1:]:
                    r = {}
                    if 'landing' in line:
                        name = line.split()[0]
                        l = line.split(':')[1].split()
                        r['name'] = name
                        r['x'] = int(l[0])
                        r['y'] = int(l[1])
                        r['head'] = l[2]
                    else:
                        r['command'] = line.split(':')[1]
                        self.rovers.append(r)








